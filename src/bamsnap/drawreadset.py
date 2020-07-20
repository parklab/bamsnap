import pysam
from PIL import Image, ImageColor, ImageDraw
from .drawread import DrawRead
from .conf import COLOR
from .util import getrgb, get_scale, add_dict_value, init_dict



class CoveragePlot():
    def __init__(self, readset, xscale, coverage_vaf=0.2):
        self.readset = readset
        self.font = None
        self.font_size = 12
        self.im = None
        self.coverage_vaf = coverage_vaf
        self.xscale = xscale
        self.coverage_color = "C8C8C8"
        self.axis_color = "000000"

    def get_image(self, w, h, bgcolor="FFFFFF"):
        if self.im is None:
            if self.font is None:
                self.set_font()
            self.im = Image.new('RGBA', (w, h), getrgb(bgcolor))
            dr = ImageDraw.Draw(self.im)
            self.draw_coverage(dr, w, h)
        return self.im

    def get_vaf(self, base_composition, dp, posi, refseq):
        aflist = []
        for b1 in base_composition.keys():
            if refseq[posi+1] != b1:
                aflist.append(base_composition[b1]/dp)
        return max(aflist)

    def draw_coverage(self, dr, w, h):
        try:
            covmap = self.readset.covmap['all']
            max_cov = self.readset.max_cov['all']
        except KeyError:
            covmap = {}
            max_cov = {}
        g_spos = self.readset.g_spos
        g_epos = self.readset.g_epos
        refseq = self.readset.refseq
        is_OK = self.readset.is_OK

        alt_pos_list = []
        for posi in sorted(covmap.keys()):
            cov = covmap[posi][0]
            base_composition = covmap[posi][1]
            # x = int((posi - g_spos) * self.scale_x) + int(self.base_width/2)
            # x = int((posi - g_spos) * self.scale_x)

            if max_cov > 0:
                y1 = h
                y2 = round(h - (cov / max_cov * h), 0)
                x1 = self.xscale.xmap[posi+1]['spos']
                x2 = self.xscale.xmap[posi+1]['epos']
                dr.rectangle([(x1, y1), (x2, y2)], fill=getrgb(self.coverage_color), outline=getrgb(self.coverage_color, 15), width=1)
                if len(base_composition.keys()) > 1:
                    if is_OK(base_composition, refseq[posi+1]):
                        alt_pos_list.append((cov, posi))

        for (cov, posi) in alt_pos_list:
            cov = covmap[posi][0]
            base_composition = covmap[posi][1]
            # x = int((posi - g_spos) * self.scale_x) + int(self.base_width/2)
            x = self.xscale.xmap[posi+1]['cpos']
            # x = int((posi - g_spos) * self.scale_x) 
            y1 = h
            y2 = round(h - (cov / max_cov * h), 0)
            y11 = y1
            vaf = self.get_vaf(base_composition, cov, posi, refseq)
            if vaf >= self.coverage_vaf:
                for base in base_composition.keys():
                    h2 = base_composition[base] / max_cov * h
                    y21 = y11-h2
                    dr.line([(x, y11), (x, y21)], fill=COLOR[base], width=self.xscale.base_width)
                    y11 = y21

        
        x1 = 0
        # dr.line([(x1, 0), (x1+3, 0)], fill=getrgb(self.axis_color), width=1)
        # dr.line([(x1, int(h/2)), (x1+3, int(h/2))], fill=getrgb(self.axis_color), width=1)
        txt = "[0-" + str(max_cov) + "]"
        fontsize = self.font.getsize(txt)
        x1 = w - fontsize[0] - 5
        dr.text( (x1, 0), txt, font=self.font, fill=getrgb(self.axis_color))
        # dr.text( (x1+3, int(h/2-fontsize[1]/2)), str(int(max_cov/2)), font=self.font, fill=getrgb(self.axis_color))

        x1 = 0
        x2 = w
        y2 = h - 1
        dr.line([(x1, y2), (x2, y2)], fill=COLOR['COVERAGE_BASE'], width=1)


class CoverageHeatmap(CoveragePlot):

    def get_heatmap_color(self, ratio):
        r1 = int(255*(1-ratio))
        return (r1, r1, r1)

    def draw_coverage(self, dr, w, h):
        covmap = self.readset.covmap
        max_cov = self.readset.max_cov
        g_spos = self.readset.g_spos
        g_epos = self.readset.g_epos
        refseq = self.readset.refseq
        is_OK = self.readset.is_OK
        # self.set_scale(g_spos, g_epos, w)

        alt_pos_list = []
        for posi in sorted(covmap.keys()):
            cov = covmap[posi][0]
            base_composition = covmap[posi][1]
            # x = int((posi - g_spos) * self.scale_x)  - int(self.base_width/2)
            x = self.xscale.xmap[posi]['cpos']

            if max_cov > 0:
                y1 = 0
                y2 = h
                col = self.get_heatmap_color(cov / max_cov)
                dr.line([(x, y1), (x, y2)], fill=col, width=self.xscale.base_width + 1)
                if len(base_composition.keys()) > 1:
                    if is_OK(base_composition, refseq[posi]):
                        alt_pos_list.append((cov, posi))

        for (cov, posi) in alt_pos_list:
            cov = covmap[posi][0]
            base_composition = covmap[posi][1]
            # x = int((posi - g_spos) * self.scale_x)  - int(self.base_width/2)
            x = self.xscale.xmap[posi]['cpos']
            y1 = h
            y2 = round(h - (cov / max_cov * h), 0)
            y11 = y1
            sum_cov = 0
            for base in base_composition.keys():
                sum_cov += base_composition[base]
            for base in base_composition.keys():
                h2 = base_composition[base] / sum_cov * h
                y21 = y11-h2
                dr.line([(x, y11), (x, y21)], fill=COLOR[base], width=self.xscale.base_width)
                y11 = y21


class DrawReadSet():
    readset = {}
    readmap = {}
    covmap = {}
    chrom = ""
    g_spos = 0
    g_epos = 0
    read_gap_w = 7
    read_gap_h = 2
    read_thickness = 5
    refseq = {}
    coverage_vaf = 10
    STRAND_GROUP_LIST = ['pos_strand', 'neg_strand']

    def __init__(self, bam, chrom, g_spos, g_epos, xscale, refseq="",  coverage_vaf=10):
        # self.samAlign = bam.samAlign
        self.samAlign = pysam.AlignmentFile(bam.filename, "rb")
        self.chrom = chrom
        self.refseq = refseq
        self.g_spos = g_spos
        self.g_epos = g_epos
        self.g_len = abs(self.g_epos - self.g_spos)
        # self.coverage_vaf = coverage_vaf
        self.covmap = {}
        self.max_cov = {'all':0}
        self.readmap = {}
        self.readset = {}
        self.readlist = {'all':[]}
        self.im = None
        self.xscale = xscale
        self.yidxmap = {}
        
        for gpos in range(self.g_spos-1000, self.g_epos+1000+1):
            self.readmap[gpos] = {}

    def get_yidx(self, r, group='all'):
        try:
            yidx = self.yidxmap[group][r.id]
        except KeyError:
            yidxmap = {}
            for gpos in range(r.g_spos-self.read_gap_w, r.g_epos+1+self.read_gap_w):
                try:
                    self.readmap[gpos][group]
                except KeyError:
                    self.readmap[gpos][group] = []

                for y1 in self.readmap[gpos][group]:
                    yidxmap[y1] = 1
            # print(len(yidxmap.keys()))
            ak = sorted(yidxmap.keys())
            if len(ak) == 0:
                yidx = 1
            else:
                for i in range(1, max(ak)+2):
                    try:
                        tmp = yidxmap[i]
                    except KeyError:
                        yidx = i
                        break
            for gpos in range(r.g_spos-self.read_gap_w, r.g_epos+1+self.read_gap_w):
                self.readmap[gpos][group].append(yidx)
            try:
                self.yidxmap[group][r.id] = yidx
            except KeyError:
                self.yidxmap[group] = {r.id:yidx}
        return yidx

    def is_exist_read(self, rid):
        flag = True
        try:
            tmp = self.readset[rid]
        except KeyError:
            flag = False
        return flag

    def get_rid(self, a):
        return (a.query_name + "_" + str(a.positions[0]))

    # def check_and_draw_read(self, a, dr, panel_xy):
    #     rid = self.get_rid(a)
    #     if not self.is_exist_read(rid):
    #         r=DrawRead(a)
    #         r.yidx = self.get_yidx(r)
    #         r.draw(dr, panel_xy, self.base_width)
    #         self.readset[rid] = 1

    def add_base_composition(self, base_composition, group, base, posi):
        base_composition = init_dict(base_composition, group)
        try:
            base_composition[group][self.refseq[posi+1]]
        except KeyError:
            base_composition[group][self.refseq[posi+1]] = 0
        base_composition[group] = add_dict_value(base_composition[group], base, 1)
        return base_composition

    def calculate_readmap(self, is_strand_group=False):
        group_list = ['all']
        if is_strand_group:
            group_list.extend(self.STRAND_GROUP_LIST)

        for group in group_list:
            self.max_cov[group] = 0
        
        for x in self.samAlign.pileup(self.chrom, self.g_spos-self.read_gap_w, self.g_epos):
            gpos = x.reference_pos
            cov = {}
            base_composition = {}
            for group in group_list:
                cov[group] = 0
                base_composition[group] = {}

            for pr in x.pileups:
                a = pr.alignment
                rid = self.get_rid(a)
                
                if not self.is_exist_read(rid):
                    r = DrawRead(a)
                    r.refseq = self.refseq
                    r.id = rid
                    if r.is_OK():
                        # r.yidx = self.get_yidx(r)
                        r.read_gap_h = self.read_gap_h
                        r.read_gap_w = self.read_gap_w
                        r.panel_g_spos = self.g_spos
                        self.readset[rid] = r
                else:
                    r = self.readset[rid]
                
                if r.is_OK():
                    if pr.query_position != None:
                        cov = add_dict_value(cov, 'all', 1)
                        base = a.query_sequence[pr.query_position]
                        base_composition = self.add_base_composition(base_composition, 'all', base, gpos)
                        
                    if rid not in self.readlist['all']:
                        self.readlist['all'].append(rid)

                    if is_strand_group:
                        if a.is_reverse:
                            group = 'neg_strand'
                        else:
                            group = 'pos_strand'

                        try:
                            self.readlist[group]
                        except KeyError:
                            self.readlist[group] = []

                        if rid not in self.readlist[group]:
                            self.readlist[group].append(rid)

                        cov = add_dict_value(cov, group, 1)
                        base_composition = self.add_base_composition(base_composition, group, base, gpos)
            
            for group in group_list:
                self.covmap = init_dict(self.covmap, group)
                self.covmap[group][gpos] = (cov[group], base_composition[group])
            
            
        
        for group in group_list:
            try:
                for rid in self.readlist[group]:
                    yidx = self.get_yidx(self.readset[rid], group)
                    if self.max_cov[group] < yidx:
                        self.max_cov[group] = yidx
            except KeyError:
                self.max_cov[group] = 0
        
                

    def get_estimated_height(self, group='all'):
        h = self.max_cov[group] * (self.read_thickness + self.read_gap_h) + self.read_thickness
        return h


    def get_image(self, w, h, group, readcolor="C8C8C8", bgcolor="FFFFFF"):
        self.im = Image.new('RGBA', (w, h), getrgb(bgcolor))
        dr = ImageDraw.Draw(self.im)
        self.draw_read(dr, group, readcolor)
        return self.im


    def draw_read(self, dr, group, col1="C8C8C8"):
        # for rid in self.readset.keys():
        if group in self.readlist.keys():
            for rid in self.readlist[group]:
                r = self.readset[rid]
                r.yidx = self.get_yidx(r, group)
                r.xscale = self.xscale
                r.read_thickness = self.read_thickness
                r.draw(dr, col1)
    

    def is_OK(self, base_composition, ref):
        flag = False
        i = 0
        minor_cnt = -9
        total = 0
        for b1 in base_composition.keys():
            total += base_composition[b1]
            if b1 != ref:
                if minor_cnt < base_composition[b1]:
                    minor_cnt = base_composition[b1]
        af = minor_cnt / total
        if minor_cnt > 1 and af >= self.coverage_vaf/100:
            flag = True
        flag=True
        return flag
