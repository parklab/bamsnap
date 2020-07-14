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
    refseq = {}
    x1 = 0
    x2 = 0
    y1 = 0

    def __init__(self, a):  # a:alignment
        #self.a = a
        self.mapq = a.mapq
        self.id = ''
        self.is_proper_pair = a.is_proper_pair
        self.is_reverse = a.is_reverse

        self.base_qual = a.query_alignment_qualities  # two qual scores : a.query_alignment_qualities and a.query_qualities
        self.g_positions = self.base_plus_1(a.positions)

        self.g_spos = self.g_positions[0] 
        self.g_epos = self.g_positions[-1]

        self.readseq = a.query_alignment_sequence

        
        self.cigar = a.cigartuples
        self.set_cigar()

        self.readseqpos = {}
        self.set_readseqpos()
        # print(self.readseq)
        # print(self.g_positions)
        # print(self.readseqpos)
        # print(self.ins_pos_map)

        self.g_len = self.g_epos - self.g_spos + 1
        self.set_color()
        pass

    def base_plus_1(self, poslist):
        for i in range(len(poslist)):
            poslist[i] = poslist[i] + 1
        return poslist

    def set_readseqpos(self):
        j = 0
        for i in range(len(self.g_positions)):
            if self.has_ins:
                try:
                    self.ins_pos_map[self.g_positions[i]]
                    j += self.ins_pos_map[self.g_positions[i]]
                    # print(self.g_positions[i], self.ins_pos_map[self.g_positions[i]], self.readseq[j])
                except KeyError:
                    pass
            self.readseqpos[self.g_positions[i]] = self.readseq[j]
            # print(self.g_positions[i], self.readseqpos[self.g_positions[i]], i, j)
            j += 1

    def set_cigar(self):
        self.has_del = False
        self.has_ins = False
        self.ins_pos_map = {}
        gpos = self.g_spos - 1
        for cg in self.cigar:
            gpos += cg[1]
            # print(gpos, cg, self.cigar, self.g_spos)
            if cg[0] == 2:
                self.has_del = True
            if cg[0] == 1:
                self.has_ins = True
                self.ins_pos_map[gpos] = cg[1]

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

    def draw(self, dr, col1="C8C8C8"):
        if not self.flag_draw:
            x1 = self.xscale.xmap[self.g_spos]['spos']
            x2 = self.xscale.xmap[self.g_epos]['epos']
            y1 = int(self.get_scaled_y(self.yidx))

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
                    x1 
                    xy.append((x1, y1 - int(self.read_thickness / 2) ))
                    xy.append((x2, y1 - int(self.read_thickness / 2) ))
                    xy.append((x2, y1 + int(self.read_thickness / 2) ))
                    xy.append((x1, y1 + int(self.read_thickness / 2) ))
                    xy.append((x1 - raht, y1))

                if self.mapq == 0:
                    dr.polygon(xy, fill=getrgb(col1, 60), outline=self.outline_color)
                else:
                    dr.polygon(xy, fill=getrgb(col1))
            else:
                dr.line([(x1, y1), (x2, y1)], fill=col1, width=self.read_thickness)

            self.draw_cigar(dr, y1)
            self.draw_variants(dr, y1)
            self.flag_draw = True


    def draw_cigar(self, dr, y1):
        if self.has_ins or self.has_del:
            xidx = 0
            for cg in self.cigar:
                if cg[0] == 2:  # DEL
                    xpos1 = self.g_spos + xidx
                    xpos2 = self.g_spos + xidx + cg[1]

                    # if the read has insertion. 
                    for p1 in self.ins_pos_map.keys():
                        if p1 <= xpos1:
                            xpos1 -= self.ins_pos_map[p1]
                            xpos2 -= self.ins_pos_map[p1]
                    x1 = self.xscale.xmap[xpos1]['spos']
                    x2 = self.xscale.xmap[xpos2]['spos']

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
                if cg[0] == 1:  # INS
                    x1 = self.xscale.xmap[self.g_spos + xidx]['spos']

                    dr.line([(x1, y1-self.read_thickness/2), (x1, y1+self.read_thickness/2)],
                            fill=COLOR['INS'], width=self.ins_width)
                    dr.line([(x1-1, y1-self.read_thickness/2), (x1+2, y1-self.read_thickness/2)],
                            fill=COLOR['INS'], width=self.ins_width)
                    dr.line([(x1-1, y1+self.read_thickness/2), (x1+2, y1+self.read_thickness/2)],
                            fill=COLOR['INS'], width=self.ins_width)
                if cg[0] == 3:  # soft clip
                    pass
                if cg[0] < 3:
                    xidx += cg[1]

    def is_OK(self):
        i = 0
        no_variant = 0
        flag = False
        for gpos in self.g_positions:
            # IF INS, change seq idx
            try:
                ins_base_len = self.ins_pos_map[gpos]
                i += ins_base_len
            except KeyError:
                pass
            
            if self.refseq[gpos] != self.readseqpos[gpos]:
                no_variant += 1
            i += 1
        flag = True
        return flag

    def draw_variants(self, dr, y1):
        i = 0
        no_variant = 0
        for gpos in self.g_positions:
            # IF INS, change seq idx
            try:
                ins_base_len = self.ins_pos_map[gpos]
                i += ins_base_len
            except KeyError:
                pass

            if self.refseq[gpos] != self.readseq[i]:
                no_variant += 1
            i += 1

        # if no_variant < 5:
        if True:
            i = 0
            # if self.has_ins:
            #     print (self.cigar, self.g_positions, self.g_len, len(self.g_positions), self.ins_pos_map)
            for gpos in self.g_positions:
                # IF INS, change seq idx
                try:
                    ins_base_len = self.ins_pos_map[gpos]
                    i += ins_base_len
                except KeyError:
                    pass

                if self.refseq[gpos] != self.readseqpos[gpos]:
                    # print(gpos, self.refseq[gpos], self.readseqpos[gpos])
                    color_tag = ''
                    if self.base_qual[i] < 15:
                        color_tag = 'w'
                    alt = self.readseqpos[gpos]
                    x1 = self.xscale.xmap[gpos]['spos']
                    x2 = self.xscale.xmap[gpos]['epos']
                    if x1 == x2:
                        x2 = x1 + 1
                    dr.line([(x1, y1 ), (x2, y1 )], fill=COLOR[color_tag+alt], width=self.read_thickness)

                i += 1
