import pysam
from .drawread import DrawRead
from .conf import COLOR

class DrawReadSet():
    readset = {}
    readmap = {}
    covmap = {}
    ymap = {}
    chrom = ""
    g_spos = 0
    g_epos = 0
    read_gap_w = 7
    read_gap_h = 2
    read_thickness = 5
    scale_x = 0.0
    refseq = {}
    max_cov = 0
    coverage_vaf = 10
    
    def __init__(self,bam, chrom,g_spos,g_epos, refseq="", coverage_vaf=10):
        self.bam = bam
        self.samAlign = pysam.AlignmentFile(self.bam, "rb")
        self.chrom =chrom
        self.refseq = refseq
        self.g_spos = g_spos
        self.g_epos = g_epos
        self.g_len = self.g_epos - self.g_spos + 1
        # self.coverage_vaf = coverage_vaf
        self.covmap = {}
        self.readmap = {}
        self.readset = {}
        self.ymap = {}
        for gpos in range(self.g_spos-1000,self.g_epos+1000+1):
            self.readmap[gpos] = []
        
        

    
    def set_scale(self, panel_xy):
        self.scale_x = 1.0*(panel_xy[1][0]-panel_xy[0][0])/self.g_len
        self.set_base_width(panel_xy)
        #self.scale_y = 1.0*(panel_xy[1][1]-panel_xy[0][1])/self.g_len

    def set_base_width(self, panel_xy):
        # print (int((panel_xy[1][0] - panel_xy[0][0])))
        # print (self.g_epos - self.g_spos)
        self.base_width = int((panel_xy[1][0] - panel_xy[0][0]) / (self.g_epos - self.g_spos))
        if self.base_width < 1:
            self.base_width = 1
        # print (self.base_width)

    def get_yidx(self, r):
        yidxmap = {}
        for gpos in range(r.g_spos-self.read_gap_w, r.g_epos+1+self.read_gap_w):
            for y1 in self.readmap[gpos]:
                yidxmap[y1] = 1
        ak = sorted(yidxmap.keys())
        if len(ak) == 0:
            yidx = 1
        else:
            for i in range(1,max(ak)+2):
                try:
                    tmp = yidxmap[i]
                except KeyError:
                    yidx = i
                    break
        for gpos in range(r.g_spos-self.read_gap_w, r.g_epos+1+self.read_gap_w):
            self.readmap[gpos].append(yidx)
        return yidx

    def is_exist_read(self, rid):
        flag = True
        try:
            tmp = self.readset[rid]
        except KeyError:
            flag = False
        return flag

    def get_rid(self,a):
        return (a.query_name + "_" + str(a.positions[0]))

    # def check_and_draw_read(self, a, dr, panel_xy):
    #     rid = self.get_rid(a)
    #     if not self.is_exist_read(rid):
    #         r=DrawRead(a)
    #         r.yidx = self.get_yidx(r)
    #         r.draw(dr, panel_xy, self.base_width)
    #         self.readset[rid] = 1

    def calculate_readmap(self):
        # print (self.coverage_vaf)
        for x in self.samAlign.pileup(self.chrom,self.g_spos-self.read_gap_w, self.g_epos):
            gpos = x.reference_pos
            # cov = len(x.pileups)
            cov = 0
            base_composition = {}
            for pr in x.pileups:
                a = pr.alignment
                rid = self.get_rid(a)
                if not self.is_exist_read(rid):
                    r=DrawRead(a)
                    r.refseq = self.refseq
                    if r.is_OK():
                        r.yidx = self.get_yidx(r)
                        r.read_gap_h = self.read_gap_h
                        r.read_gap_w = self.read_gap_w
                        r.panel_g_spos = self.g_spos
                        self.readset[rid] = r
                else:
                    r = self.readset[rid]
                # if a.mapq > 20 and r.is_OK():
                if r.is_OK():
                    if pr.query_position != None:
                        cov += 1
                        base = a.query_sequence[pr.query_position]
                        
                        try:
                            base_composition[base] += 1
                        except KeyError:
                            base_composition[base] = 1
            self.covmap[gpos] = (cov,base_composition)
            if self.max_cov < cov:
                self.max_cov = cov
        # print (self.max_cov)

    def draw_read(self,dr, panel_xy):
        self.set_scale(panel_xy)
        for rid in self.readset.keys():
            r = self.readset[rid]
            r.scale_x = self.scale_x
            r.read_thickness = self.read_thickness
            r.draw(dr, panel_xy, self.base_width)

    def draw_coverage(self, dr, panel_xy):
        self.set_scale(panel_xy)
        
        alt_gpos_list = []
        # print ("self.covmap.keys()", list(self.covmap.keys())[0], list(self.covmap.keys())[-1])
        for gpos in sorted(self.covmap.keys()):
            cov = self.covmap[gpos][0]
            base_composition = self.covmap[gpos][1]
            x = (gpos-self.g_spos)*self.scale_x
            if self.max_cov > 0:
                h = cov / self.max_cov*(panel_xy[1][1]-panel_xy[0][1])
                y1 = panel_xy[1][1]
                y2 = panel_xy[1][1]-h
                
                dr.line([(x,y1),(x,y2)], fill=COLOR['READ'], width=self.base_width+1)
                if len(base_composition.keys()) > 1:
                    #print (base_composition)
                    # print (self.refseq, gpos)
                    if self.is_OK(base_composition, self.refseq[gpos]):
                        alt_gpos_list.append((cov,gpos))
                # print (gpos, len(self.readmap[gpos]))

        for (cov,gpos) in alt_gpos_list:
            cov = self.covmap[gpos][0]
            base_composition = self.covmap[gpos][1]
            x = (gpos-self.g_spos)*self.scale_x
            h = cov / self.max_cov*(panel_xy[1][1]-panel_xy[0][1])
            y1 = panel_xy[1][1]
            y2 = panel_xy[1][1]-h
            y11 = y1
            for base in base_composition.keys():
                h2 = base_composition[base]/ self.max_cov*(panel_xy[1][1]-panel_xy[0][1])
                y21 = y11-h2  
                dr.line([(x,y11),(x,y21)], fill=COLOR[base], width=self.base_width)
                y11 = y21

    def get_heatmap_color(self, ratio):
        r1 = int(255*(1-ratio))
        # return ImageColor.rgb(r1,r1,r1)
        return (r1,r1,r1)

    def draw_coverage_heatmap(self, dr, panel_xy):
        self.set_scale(panel_xy)
        alt_gpos_list = []
        for gpos in sorted(self.covmap.keys()):
            cov = self.covmap[gpos][0]
            base_composition = self.covmap[gpos][1]
            x = (gpos-self.g_spos)*self.scale_x
            if self.max_cov > 0:
                # h = cov / self.max_cov*(panel_xy[1][1]-panel_xy[0][1])
                h = panel_xy[1][1]-panel_xy[0][1]
                y1 = panel_xy[1][1]
                y2 = panel_xy[1][1]-h
                col = self.get_heatmap_color(cov / self.max_cov)
                dr.line([(x,y1),(x,y2)], fill=col, width=self.base_width+1)
                if len(base_composition.keys()) > 1:
                    #print (base_composition)
                    if self.is_OK(base_composition, self.refseq[gpos]):
                        alt_gpos_list.append((cov,gpos))
                # print (gpos, len(self.readmap[gpos]))

        for (cov,gpos) in alt_gpos_list:
            cov = self.covmap[gpos][0]
            base_composition = self.covmap[gpos][1]
            x = (gpos-self.g_spos)*self.scale_x
            h = cov / self.max_cov*(panel_xy[1][1]-panel_xy[0][1])
            y1 = panel_xy[1][1]
            y2 = panel_xy[1][1]-h
            y11 = y1
            sum_cov = 0
            for base in base_composition.keys():
                sum_cov += base_composition[base]
            for base in base_composition.keys():
                # h2 = base_composition[base]/self.max_cov*(panel_xy[1][1]-panel_xy[0][1])
                h2 = base_composition[base]/sum_cov*(panel_xy[1][1]-panel_xy[0][1])
                y21 = y11-h2  
                dr.line([(x,y11),(x,y21)], fill=COLOR[base], width=self.base_width)
                y11 = y21

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
        return flag
