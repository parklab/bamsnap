from .conf import COLOR
from PIL import ImageFont
from .util import getTemplatePath, getrgb

class DrawRead():
    read_alignment = ""
    yidx = 0
    flag_draw = False
    fill_color = COLOR['cov']
    outline_color = COLOR['cov']
    read_thickness = 5
    read_gap_h = 2
    del_width = 2
    ins_width = 2
    is_deletion = False
    is_insertion = False
    is_inversion = False
    refseq = {}
    x1 = 0
    x2 = 0
    y1 = 0
    opt = {}

    def __init__(self, a, refseq=""):  # a:alignment
        self.a = a
        self.mapq = a.mapq
        self.id = a.query_name
        self.is_proper_pair = a.is_proper_pair
        self.is_reverse = a.is_reverse

        self.g_positions = self.base_plus_1(a.positions)
        self.g_spos = self.g_positions[0] 
        self.g_epos = self.g_positions[-1]
        self.readseq = a.query_alignment_sequence
        self.readseq_with_softclipped = a.query_sequence
        
        self.base_qual = a.query_qualities
        self.refseq = refseq
        # try:
        #     self.refseq = a.get_reference_sequence()
        # except ValueError:
        #     self.refseq = {}
        self.g_spos = a.positions[0] + 1
        self.g_epos = a.positions[-1] + 1
        self.has_del = False
        self.has_ins = False
        self.has_softclipped = False
        self.has_mismatch = False
        self.cigar = a.cigartuples
        self.readseq_with_softclipped = a.query_sequence

        self.set_color()
        self.reference_name = a.reference_name
        self.mate_reference_name = a.next_reference_name
        self.mate_reference_start = a.next_reference_start
        self.mate_is_reverse = a.mate_is_reverse
        self.has_interchrom_mate = self.reference_name != self.mate_reference_name
        self.insert_size = a.tlen
        

        self.readseqinfo = {}
        self.ins_list = []
        self.del_list = []
        self.mismatch_list = []
        self.softclipped_list = []
        self.set_read_variant()
    
    def set_SV(self):
        if abs(self.insert_size) > 0:
            if abs(self.insert_size) >= self.opt['insert_size_del_threshold']:
                # print(self.insert_size, self.g_spos, self.g_epos, self.is_reverse,
                #       self.mate_reference_start, self.mate_is_reverse, self.id, self.a.tlen)
                self.is_deletion = True
            if abs(self.insert_size) <= self.opt['insert_size_ins_threshold']:
                # self.is_insertion = True
                pass
            if (not self.is_reverse and self.g_spos > self.mate_reference_start) or (self.is_reverse and self.g_spos < self.mate_reference_start):
                # self.is_inversion = True
                # print(self.insert_size, self.g_spos, self.g_epos, self.is_reverse,
                #     self.mate_reference_start, self.mate_is_reverse, self.id, self.a.tlen)
                pass
            

    def set_read_variant(self):
        gpos = self.g_spos
        self.g_spos_with_softclipped = self.g_spos
        self.g_epos_with_softclipped = self.g_epos
        prev_gpos = gpos
        bidx = 0
        ridx = 0

        for cidx in range(len(self.cigar)):
            cg = self.cigar[cidx]
            gpos += cg[1]
            if cg[0] == 2:
                self.has_del = True
                self.del_list.append((prev_gpos, gpos))
                ridx += cg[1]
            elif cg[0] == 1:
                gpos -= cg[1]
                self.has_ins = True
                self.ins_list.append(gpos)
                bidx += cg[1]
            elif cg[0] == 4:  # soft clipped
                self.has_softclipped = True
                if cidx == 0:
                    self.g_spos_with_softclipped = self.g_spos - cg[1]
                    gpos = self.g_spos
                    for gp in range(self.g_spos_with_softclipped, self.g_spos):
                        self.softclipped_list.append(gp)
                        base = self.readseq_with_softclipped[bidx]
                        self.readseqinfo[gp] = (base, '', 'C', self.base_qual[bidx])
                        bidx += 1
                else:
                    self.g_epos_with_softclipped = self.g_epos + cg[1]
                    for gp in range(self.g_epos+1, self.g_epos_with_softclipped+1):
                        self.softclipped_list.append(gp)
                        base = self.readseq_with_softclipped[bidx]
                        self.readseqinfo[gp] = (base, '', 'C', self.base_qual[bidx])
                        bidx += 1
            elif cg[0] == 5:
                gpos -= cg[1]
            else:
                for gp in range(prev_gpos, gpos):
                    base = self.readseq_with_softclipped[bidx]
                    refbase = self.refseq[gp].upper()
                    if base != refbase:
                        btype = 'S'
                        self.mismatch_list.append(gp)
                    else:
                        btype = 'M'
                    self.readseqinfo[gp] = (base, refbase, btype, self.base_qual[bidx])
                    bidx += 1
                    ridx += 1
            prev_gpos = gpos

    def base_plus_1(self, poslist):
        for i in range(len(poslist)):
            poslist[i] = poslist[i] + 1
        return poslist

    def get_genomic_spos_epos(self):
        if self.opt['show_soft_clipped']:
            g_spos = self.g_spos_with_softclipped
            g_epos = self.g_epos_with_softclipped
        else:
            g_spos = self.g_spos
            g_epos = self.g_epos
        return (g_spos, g_epos)

    def set_color(self):
        self.outline_color = COLOR['READ']
        if self.mapq == 0:
            self.fill_color = COLOR['MAPQ_0']
        elif not self.is_proper_pair:
            self.fill_color = COLOR['NONPROPER_PAIR']
        else:
            self.fill_color = COLOR['READ']

    def get_scaled_y(self, yidx):
        return yidx * (self.read_thickness+self.read_gap_h)

    def read_arrowhead_thickness(self, read_thickness):
        t1 = 3
        if read_thickness >= 5:
            t1 = 4
        if read_thickness >= 10:
            t1 = 6
        if read_thickness >= 20:
            t1 = 13
        return t1

    def get_readcolor_by_interchrom(self, default_color):
        if self.has_interchrom_mate and self.mate_reference_name != None:
            mate_chrom = self.mate_reference_name.replace('chr','')
            try:
                rst_color = self.opt['read_color_interchrom_chr' + mate_chrom]
            except KeyError:
                rst_color = self.opt['read_color_interchrom_other']
        else:
            rst_color = default_color
        return rst_color

    def get_readcolor_by_strand(self, default_color):
        if self.is_reverse:
            rst_color = self.opt['read_neg_color']
        else:
            rst_color = self.opt['read_pos_color']
        return rst_color

    def draw(self, dr, col1="C8C8C8", readcolorby=""):
        if not self.flag_draw:
            if not self.has_interchrom_mate:
                self.set_SV()
            
            y1 = int(self.get_scaled_y(self.yidx))
            self.draw_read_body(dr, y1, col1, readcolorby)
            self.draw_mismatch(dr, y1)
            if self.opt['show_soft_clipped'] and self.has_softclipped:
                self.draw_softclipped(dr, y1)
            if self.has_ins:
                self.draw_ins(dr, y1)
            if self.has_del:
                self.draw_del(dr, y1)
            self.flag_draw = True

    def draw_read_body(self, dr, y1, col1, readcolorby=""):
        if self.opt['show_soft_clipped'] and self.has_softclipped:
            x1 = self.xscale.xmap[self.g_spos_with_softclipped]['spos']
            x2 = self.xscale.xmap[self.g_epos_with_softclipped]['epos']
        else:
            x1 = self.xscale.xmap[self.g_spos]['spos']
            x2 = self.xscale.xmap[self.g_epos]['epos']
    
        xy = []
        if self.read_thickness > 1:
            raht = self.read_arrowhead_thickness(self.read_thickness)
            if not self.is_reverse:
                xy.append((x1, y1 - int(self.read_thickness / 2) ))
                xy.append((x2, y1 - int(self.read_thickness / 2) ))
                xy.append((x2 + raht, y1))
                xy.append((x2, y1 + int(self.read_thickness / 2) ))
                xy.append((x1, y1 + int(self.read_thickness / 2) ))
            else:
                xy.append((x1, y1 - int(self.read_thickness / 2) ))
                xy.append((x2, y1 - int(self.read_thickness / 2) ))
                xy.append((x2, y1 + int(self.read_thickness / 2) ))
                xy.append((x1, y1 + int(self.read_thickness / 2) ))
                xy.append((x1 - raht, y1))

            if self.is_deletion:
                col1 = self.opt['read_color_deletion']
            if self.is_inversion:
                col1 = self.opt['read_color_inversion']

            if readcolorby == "interchrom":
                col1 = self.get_readcolor_by_interchrom(col1)
            elif readcolorby == "strand":
                col1 = self.get_readcolor_by_strand(col1)
            

            if self.mapq == 0:
                dr.polygon(xy, fill=getrgb(col1, 60), outline=self.outline_color)
            else:
                dr.polygon(xy, fill=getrgb(col1))
        else:
            dr.line([(x1, y1), (x2, y1)], fill=getrgb(col1), width=self.read_thickness)

    def draw_mismatch(self, dr, y1):
        for gpos in self.mismatch_list:
            base_qual = self.readseqinfo[gpos][3]
            color_tag = "w" if base_qual < 15 else ""
            alt = self.readseqinfo[gpos][0]
            x1 = self.xscale.xmap[gpos]['spos']
            x2 = self.xscale.xmap[gpos]['epos']
            if x1 == x2:
                x2 = x1 + 1
            dr.line([(x1, y1), (x2, y1)], fill=COLOR[color_tag+alt], width=self.read_thickness)

    def draw_softclipped(self, dr, y1):
        for gpos in self.softclipped_list:
            base_qual = self.readseqinfo[gpos][3]
            color_tag = "w" if base_qual < 15 else ""
            alt = self.readseqinfo[gpos][0]
            x1 = self.xscale.xmap[gpos]['spos']
            x2 = self.xscale.xmap[gpos]['epos']
            if x1 == x2:
                x2 = x1 + 1
            dr.line([(x1, y1), (x2, y1)], fill=COLOR[color_tag+alt], width=self.read_thickness)

    def draw_ins(self, dr, y1):
        for gpos in self.ins_list:
            x1 = self.xscale.xmap[gpos]['spos']
            dr.line([(x1, y1-self.read_thickness/2), (x1, y1+self.read_thickness/2)],
                    fill=COLOR['INS'], width=self.ins_width)
            dr.line([(x1-1, y1-self.read_thickness/2), (x1+2, y1-self.read_thickness/2)],
                    fill=COLOR['INS'], width=self.ins_width)
            dr.line([(x1-1, y1+self.read_thickness/2), (x1+2, y1+self.read_thickness/2)],
                    fill=COLOR['INS'], width=self.ins_width)

    def draw_del(self, dr, y1):
        for gpos in self.del_list:
            x1 = self.xscale.xmap[gpos[0]]['spos']
            x2 = self.xscale.xmap[gpos[1]]['spos']
            if self.read_thickness > 1:
                xy = []
                xy.append((x1, y1-self.read_thickness/2))
                xy.append((x2, y1-self.read_thickness/2))
                xy.append((x2, y1+self.read_thickness/2))
                xy.append((x1, y1+self.read_thickness/2))
                dr.polygon(xy, fill=COLOR['BG'], outline=COLOR['BG'])
                dr.line([(x1, y1), (x2, y1)], fill=COLOR['DEL'], width=self.del_width)
            else:
                dr.line([(x1, y1), (x2, y1)], fill=COLOR['DEL'], width=self.del_width)
