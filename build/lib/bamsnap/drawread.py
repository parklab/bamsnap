from .conf import COLOR

class DrawRead():
    read_alignment = ""
    yidx = 0
    flag_draw = False
    fill_color=COLOR['cov']
    outline_color=COLOR['cov']
    read_thickness = 5
    read_gap_h = 2
    del_width = 2
    ins_width = 2
    refseq = {}
    scale_x = 1.0
    base_width = 1
    x1 = 0
    x2 = 0
    y1 = 0

    def __init__(self, a):  ## a:alignment
        #self.a = a
        self.mapq = a.mapq
        #print(a.get_aligned_pairs())
        self.is_proper_pair = a.is_proper_pair
        self.is_reverse = a.is_reverse
        
        self.base_qual = a.query_alignment_qualities   #### two qual scores : a.query_alignment_qualities and a.query_qualities
        self.g_positions = a.positions
        

        self.g_spos = self.g_positions[0]
        self.g_epos = self.g_positions[-1]

        self.readseq = a.query_alignment_sequence
        self.cigar = a.cigartuples
        
        self.set_cigar()
        
        #print (self.readseq)
        self.g_len = self.g_epos - self.g_spos + 1
        self.set_color()
        pass

    def set_cigar(self):
        self.has_del = False
        self.has_ins = False
        self.ins_pos_map = {}
        gpos = self.g_spos
        for cg in self.cigar:
            gpos += cg[1]
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
            

    def get_scaled_x(self, gpos):
        return (gpos-self.panel_g_spos)*self.scale_x

    def get_scaled_y(self, yidx):
        return yidx * (self.read_thickness+self.read_gap_h)

    def read_arrowhead_thickness(self, read_thickness):
        t1 = 2
        if read_thickness >= 5:
            t1 = 3
        if read_thickness >= 10:
            t1 = 5
        if read_thickness >= 20:
            t1 = 10
        return t1

    def draw(self, dr, panel_xy, base_width=1):
        if not self.flag_draw:
            # if self.g_len != 100:
            # #     #print ([(self.x1,self.y1),(self.x2,self.y1)], self.g_spos, self.g_epos, self.g_len, self.yidx)
            #     print (self.readseq, len(self.readseq), self.cigar, self.g_spos)
            self.base_width = base_width
            x1 = self.get_scaled_x(self.g_spos) + panel_xy[0][0]
            x2 = self.get_scaled_x(self.g_epos) + panel_xy[0][0]
            y1 = self.get_scaled_y(self.yidx)+ panel_xy[0][1]
            xy = []
            # print (x1, x2, self.g_spos, self.g_epos)
            
            if self.read_thickness > 1:
                raht = self.read_arrowhead_thickness(self.read_thickness)
                if not self.is_reverse:
                    xy.append((x1, y1-self.read_thickness/2))
                    xy.append((x2, y1-self.read_thickness/2))
                    xy.append((x2+raht, y1))
                    xy.append((x2, y1+self.read_thickness/2))
                    xy.append((x1, y1+self.read_thickness/2))
                else:
                    xy.append((x1, y1-self.read_thickness/2))
                    xy.append((x2, y1-self.read_thickness/2))
                    xy.append((x2, y1+self.read_thickness/2))
                    xy.append((x1, y1+self.read_thickness/2))
                    xy.append((x1-raht, y1))
                dr.polygon(xy, fill=self.fill_color, outline=self.outline_color)
            else:
                dr.line([(x1,y1),(x2,y1)], fill=self.fill_color, width=self.read_thickness)
               
            self.draw_cigar(dr, panel_xy, y1)
            self.draw_variants(dr, panel_xy, y1)
            self.flag_draw = True

    def draw_cigar(self, dr, panel_xy, y1):
        if self.has_ins or self.has_del:
            xidx = 0
            for cg in self.cigar:
                if cg[0] == 2: ### DEL
                    x1 = self.get_scaled_x(self.g_spos + xidx) + panel_xy[0][0]
                    x2 = self.get_scaled_x(self.g_spos + xidx + cg[1]) + panel_xy[0][0]
                    
                    if self.read_thickness > 1:
                        xy = []
                        xy.append((x1, y1-self.read_thickness/2))
                        xy.append((x2, y1-self.read_thickness/2))
                        xy.append((x2, y1+self.read_thickness/2))
                        xy.append((x1, y1+self.read_thickness/2))
                        dr.polygon(xy, fill=COLOR['BG'], outline=COLOR['BG'])
                        dr.line([(x1,y1),(x2,y1)], fill=COLOR['DEL'], width=self.del_width)
                    else:
                        dr.line([(x1,y1),(x2,y1)], fill=COLOR['DEL'], width=self.del_width)
                if cg[0] == 1: ### INS
                    x1 = int(self.get_scaled_x(self.g_spos + xidx) + panel_xy[0][0])
                    dr.line([(x1,y1-self.read_thickness/2),(x1,y1+self.read_thickness/2)], fill=COLOR['INS'], width=self.ins_width)
                    dr.line([(x1-1,y1-self.read_thickness/2),(x1+2,y1-self.read_thickness/2)], fill=COLOR['INS'], width=self.ins_width)
                    dr.line([(x1-1,y1+self.read_thickness/2),(x1+2,y1+self.read_thickness/2)], fill=COLOR['INS'], width=self.ins_width)
                if cg[0] == 3: ### soft clip
                    pass   
                if cg[0] < 3:                     
                    xidx += cg[1]

    def is_OK(self):
        i = 0
        no_variant = 0
        flag = False
        # print (len(self.g_positions))
        # print (len(self.refseq.keys()))
        for gpos in self.g_positions:
            ### IF INS, change seq idx
            try:
                ins_base_len = self.ins_pos_map[gpos]
                i += ins_base_len
            except KeyError:
                pass
            # print (len(self.refseq.keys()))
            # print (self.refseq.keys())
            # print (self.readseq[i])
            if self.refseq[gpos] != self.readseq[i]:
                no_variant += 1
            i += 1      
        flag = True
        # for cg in self.cigar:
        #     if cg[0] >= 3:
        #         flag = False
        return flag

    def draw_variants(self, dr, panel_xy, y1):
        i = 0
        no_variant = 0
        for gpos in self.g_positions:
            ### IF INS, change seq idx
            try:
                ins_base_len = self.ins_pos_map[gpos]
                i += ins_base_len
            except KeyError:
                pass

            if self.refseq[gpos] != self.readseq[i]:
                no_variant += 1
            i += 1

        #if no_variant < 5:
        if True:
            i = 0
            # if self.has_ins:
            #     print (self.cigar, self.g_positions, self.g_len, len(self.g_positions), self.ins_pos_map)
            for gpos in self.g_positions:
                ### IF INS, change seq idx
                try:
                    ins_base_len = self.ins_pos_map[gpos]
                    i += ins_base_len
                except KeyError:
                    pass

                if self.refseq[gpos] != self.readseq[i]:
                    #print (gpos, self.refseq[gpos], self.readseq[i])
                    # print (self.readseq[i], self.base_qual[i])
                    color_tag = ''
                    if self.base_qual[i] < 15:
                        color_tag = 'w'
                    alt = self.readseq[i]
                    x = self.get_scaled_x(gpos) + panel_xy[0][0]
                    dr.line([(x,y1-self.read_thickness/2),(x,y1+self.read_thickness/2)], fill=COLOR[color_tag+alt], width=self.base_width)
                i += 1
        