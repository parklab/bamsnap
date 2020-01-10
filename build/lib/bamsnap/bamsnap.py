import os
import time
from PIL import Image, ImageDraw, ImageColor, ImageOps
from . import __init__
from . import _options
from pyfasta import Fasta
from .drawreadset import DrawReadSet
from .util import get_url, getTemplatePath, fileOpen, fileSave, check_dir
from .conf import COLOR


class BamSnap():
    has_opt_error = False
    bamlist = []
    refseq = {}
    outfnamelist = []

    def __init__(self, opt):
        self.opt = opt

    def load_bamlist(self):
        ks = self.opt.keys()
        if 'bamlist' in ks and self.opt['bamlist'] is not None:
            for line in open(self.opt['bamlist']):
                line = line.strip()
                if len(line) > 0 and line[0] != '#':
                    self.bamlist.append(line)
        elif 'bam' in ks and len(self.opt['bam']) > 0:
            for bam in self.opt['bam']:
                self.bamlist.append(bam)

    def set_refseq(self, pos1):
        self.refseq = {}
        if self.opt['ref'] == "":
            self.set_refseq_from_ucsc(pos1)
        else:
            self.set_refseq_from_localfasta(pos1)

    # def set_refseq_from_ncbiapi(self):
    #     url = "http://www.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nucleotide&id=NC_000001&seq_start=97533596&seq_stop=97533606&rettype=fasta&retmode=text"
    #     cont = get_url(url)
    #     seq = ""
    #     for line in cont.strip().split('\n'):
    #         if line[0] != '>':
    #             seq += line.strip()
    #     print ('seq:',seq)
    #     i = 0
    #     for gpos in range(self.opt['g_spos']-1000,self.opt['g_epos']+1000+1):
    #         self.refseq[gpos] = seq[i]
    #         i += 1

    def set_refseq_from_ucsc(self, pos1):
        spos = pos1['g_spos']-self.opt['margin'] - 500
        epos = pos1['g_epos']+self.opt['margin']+1 + 500
        url = "http://genome.ucsc.edu/cgi-bin/das/hg19/dna?segment=chr"+pos1['chrom']+":"+str(spos+1)+","+str(epos+1)
        cont = get_url(url)
        seq = ""
        for line in cont.strip().split('\n'):
            if line[0] != '<':
                seq += line.strip().upper()
        i = 0
        for gpos in range(spos, epos):
            self.refseq[gpos] = seq[i]
            i += 1

    def set_refseq_from_localfasta(self, pos1):
        spos = pos1['g_spos']-self.opt['margin'] - 500
        epos = pos1['g_epos']+self.opt['margin']+1 + 500
        seq = self.get_refseq(self.opt['ref'], pos1['chrom'], spos, epos)
        i = 0
        for gpos in range(spos, epos):
            self.refseq[gpos] = seq[i]
            i += 1

    def get_refseq(self, ref, chrom, spos, epos):
        f = Fasta(ref)
        fastachrommap = {}
        for c1 in list(f.keys()):
            arr = c1.split(' ')
            tchrom = arr[0]
            fastachrommap[tchrom] = c1
        # fasta_chrom = chrom + ' dna:chromosome chromosome:GRCh37:'+chrom+':1:'+str(CHROM_LEN['b37d5'][chrom])+':1'
        refseq = f[fastachrommap[chrom]][spos:epos+1]
        return refseq

    def save_image(self, ia, bam, pos1):
        outfname = os.path.join(self.opt['out'], 'snapfiles', 'snap_' + bam.split('/')[-1] +
                                '_' + pos1['chrom'] + '_' + str(pos1['t_spos']) + '-' + str(pos1['t_epos']))
        check_dir(outfname)

        if self.opt['out_type'] == 'png':
            outfname += '.png'
            ia.save(outfname, "PNG", quality=1, optimize=True)
        elif self.opt['out_type'] == "jpg":
            outfname += '.jpg'
            ia.save(outfname, "JPEG", quality=1, optimize=True)

        self.opt['log'].info('Saved ' + outfname)
        self.outfnamelist.append({'t': bam.split('/')[-1] + ': ' + pos1['chrom'] + '_' + str(pos1['t_spos']) + '-' +
                                  str(pos1['t_epos']), 'img': outfname.split('/')[-1]})

    def save_html(self):
        cont = fileOpen(getTemplatePath('template.html'))
        out = os.path.join(self.opt['out'], 'bamsnap_index.html')
        cont_bamsnapimages = ""
        for imgfile in self.outfnamelist:
            imgpath = os.path.join("snapfiles", imgfile['img'])
            # print (imgpath)
            cont_bamsnapimages += imgfile['t'] + "<br>"
            cont_bamsnapimages += "<img src='"+imgpath+"'><br>"
        cont = cont.replace('##BAMSNAPIMAGES##', cont_bamsnapimages)
        fileSave(out, cont, 'w')
        self.opt['log'].info('Saved '+out)

    def run(self):
        t0 = time.time()
        timemap = {'set_refseq': 0}
        self.load_bamlist()
        if not self.has_opt_error:
            image_w = self.opt['width']
            for pos1 in self.opt['poslist']:
                self.opt['log'].info("Processing position "+pos1['chrom']+':' +
                                     str(pos1['t_spos'])+'-'+str(pos1['t_epos']))

                t11 = time.time()
                self.set_refseq(pos1)
                # print (self.refseq)
                t12 = time.time()
                self.opt['log'].debug('Running time for getting reference sequence (set_refseq): ' +
                                      str(round(t12-t11, 5))+' sec')
                timemap['set_refseq'] += t12-t11

                if self.opt['merged_image']:
                    ia = Image.new('RGBA', (image_w, 0), (255, 255, 255, 255))

                image_h = 0
                offset_top = 0
                for bam in self.bamlist:
                    self.opt['log'].info("Processing.. "+bam)

                    rset = DrawReadSet(bam, pos1['chrom'], pos1['g_spos'], pos1['g_epos'], self.refseq)
                    rset.read_gap_w = self.opt['read_gap_w']
                    rset.read_gap_h = self.opt['read_gap_h']
                    rset.read_thickness = self.opt['read_thickness']
                    rset.coverage_vaf = self.opt['coverage_vaf']
                    rset.calculate_readmap()

                    delta_h = 0
                    for plot1 in self.opt['draw'].split(','):
                        if plot1 == "heatmap":
                            delta_h += self.opt['heatmap_height']
                        if plot1 == "coverage":
                            delta_h += self.opt['coverage_height']
                        if plot1 == "read":
                            delta_h += rset.max_cov * (rset.read_thickness + rset.read_gap_h) + rset.read_thickness

                    if not self.opt['merged_image']:
                        image_h = 0
                        offset_top = 0
                        ia = Image.new('RGBA', (image_w, 0), (255, 255, 255, 255))

                    ia = ImageOps.expand(ia, (0, 0, 0, delta_h+5), fill=(255, 255, 255, 255))
                    drawA = ImageDraw.Draw(ia)
                    image_h += delta_h

                    offset_top0 = offset_top

                    for plot1 in self.opt['draw'].split(','):
                        if plot1 == "heatmap":
                            rset.draw_coverage_heatmap(
                                drawA, [(0, offset_top), (image_w, offset_top+self.opt['heatmap_height'])])
                            self.scale_x = rset.scale_x
                            offset_top += self.opt['heatmap_height']

                        if plot1 == "coverage":
                            rset.draw_coverage(
                                drawA, [(0, offset_top), (image_w, offset_top+self.opt['coverage_height'])])
                            self.scale_x = rset.scale_x
                            offset_top += self.opt['coverage_height']

                        if plot1 == "read":
                            h = rset.max_cov * (rset.read_thickness + rset.read_gap_h) + rset.read_thickness
                            rset.draw_read(drawA, [(0, offset_top), (image_w, offset_top + h)])
                            self.scale_x = rset.scale_x
                            offset_top += h

                    # TODO: add label
                    # if self.opt['addlabel']:
                    #     # fnt = ImageFont.truetype(conf.MUTBOXPATH + 'static/fonts/VeraMono.ttf', 10)
                    #     # drawA.text((1,offset_top0), bam.title, font=fnt,fill=(0,0,0,150))
                    #     drawA.text((1,offset_top0), bam.title,fill=(0,0,0,150))

                    if self.opt['center_line']:
                        x1 = ((self.opt['g_epos']-self.opt['g_spos'])/2)*self.scale_x
                        for h1 in range(0, image_h, 7):
                            drawA.line([(x1, h1), (x1, h1+2)], fill=COLOR['CENTER_LINE'], width=1)

                    if not self.opt['no_target_line']:
                        x1 = (pos1['t_spos']-pos1['g_spos'])*self.scale_x-2
                        x2 = (pos1['t_epos']-pos1['g_spos'])*self.scale_x
                        for h1 in range(0, image_h, 7):
                            drawA.line([(x1, h1), (x1, h1+2)], fill=COLOR['CENTER_LINE'], width=1)
                            drawA.line([(x2, h1), (x2, h1+2)], fill=COLOR['CENTER_LINE'], width=1)

                    # TODO: highlight line
                    if 'highlight' in self.opt.keys():
                        for h1 in self.opt['highlight'].split(','):
                            arr = h1.split(':')
                            arr2 = arr[1].split('-')
                            t_spos = int(arr2[0])
                            t_epos = int(arr2[1])
                            x1 = (t_spos-self.opt['g_spos'])*self.scale_x - 4
                            x2 = (t_epos-self.opt['g_spos'])*self.scale_x - 2
                            for h1 in range(0, image_h, 7):
                                drawA.line([(x1, h1), (x1, h1+2)], fill=COLOR['CENTER_LINE'], width=1)
                                drawA.line([(x2, h1), (x2, h1+2)], fill=COLOR['CENTER_LINE'], width=1)
                    del drawA
                    del rset
                    if not self.opt['merged_image']:
                        self.save_image(ia, bam, pos1)
                if self.opt['merged_image']:
                    self.save_image(ia, bam, pos1)
                t13 = time.time()
                self.opt['log'].debug('Running time for processing position '+pos1['chrom']+':' +
                                      str(pos1['t_spos'])+'-'+str(pos1['t_epos']) + ": " + str(round(t13-t11, 5)) +
                                      ' sec')
        t2 = time.time()
        self.save_html()

        self.opt['log'].debug('Total running time for getting reference sequence (set_refseq): ' +
                              str(round(timemap['set_refseq'], 3))+' sec')
        self.opt['log'].info('Total running time: ' + str(round(t2-t0, 1))+' sec')
