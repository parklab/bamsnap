from PIL import Image, ImageDraw, ImageFont
from .conf import COLOR
from .util import getTemplatePath, comma, getrgb, get_scale


class COORDINATES():
    MIN_BAR_SIZE = 3
    MIN_AXIS_LABEL_WIDTH = 180
    GAP_LABEL_AND_BAR = 1

    def __init__(self, chrom, spos, epos, xscale, w, h, debug=False):
        self.chrom = chrom
        self.spos = spos
        self.epos = epos
        self.glen = self.epos - self.spos
        self.font = None
        self.font_size = 12
        self.axisloc = "bottom" # or "top" or "middle"
        self.bgcolor = "FFFFFF"
        self.axiscolor = "000000"
        self.labelcolor = "000000"
        self.w = w
        self.h = h
        self.im = None
        self.axis_pos_list = []
        self.bar_size = 3
        self.single_font_size = None
        self.xscale = xscale
        self.debug = debug
        if self.debug:
            self.h += 20

    def set_font(self, font_size=12):
        self.font_size = font_size
        self.font = ImageFont.truetype(getTemplatePath('VeraMono.ttf'), font_size)

    def resize_height(self):
        self.single_font_size = self.font.getsize('C')
        if self.axisloc == "middle":
            self.h = max(self.h, self.single_font_size[1] + self.MIN_BAR_SIZE * 2)
            self.bar_size = int((self.h - self.single_font_size[1]) / 2) - self.GAP_LABEL_AND_BAR * 2
        else:
            self.h = max(self.h, self.single_font_size[1] + self.MIN_BAR_SIZE)
            self.bar_size = self.h - self.single_font_size[1] - self.GAP_LABEL_AND_BAR

    def cal_axis(self):
        min_base_number = int(self.MIN_AXIS_LABEL_WIDTH / (self.w/self.glen))
        for k in [1, 5, 10, 20, 50, 100, 150, 200, 300, 400, 500, 800, 1000, 1500, 2000, 3000, 5000, 10000, 20000, 50000, 100000]:
            if min_base_number <= k:
                axis_base_unit = k
                break
        unitlen = 10 ** (len(str(axis_base_unit)) - 1)
        axis_spos = int(self.spos/unitlen) * unitlen + axis_base_unit
        self.axis_pos_list = range(axis_spos, self.epos, axis_base_unit)
        self.axis_x_list = []
        for posi in self.axis_pos_list:
            self.axis_x_list.append(self.xscale.xmap[posi]['cpos'])
            # self.axis_x_list.append(round((posi - self.spos) * self.scale_x - axis_base_unit/2, 0))
        
    def draw(self, dr):
        self.resize_height()
        self.cal_axis()

        x1 = 0
        x2 = self.w
        yi = 0

        if self.axisloc == "top" or self.axisloc == "middle":
            dr.line([(x1, yi), (x2, yi)], fill=getrgb(self.axiscolor), width=1)
            for xi in self.axis_x_list:
                dr.line([(xi, yi), (xi, yi + self.bar_size)], fill=getrgb(self.axiscolor), width=1)
            yi += self.bar_size

        for i, posi in enumerate(self.axis_pos_list):
            pos1 = comma(posi)
            xi = self.axis_x_list[i]
            d = int(len(pos1) * self.single_font_size[0]) / 2
            if self.axisloc == "middle":
                dr.text((xi - d, yi), pos1, font=self.font, fill=getrgb(self.labelcolor))
            else:
                dr.text((xi - d, yi), pos1, font=self.font, fill=getrgb(self.labelcolor))

        if self.debug:
            for posi in range(self.spos, self.epos+1):
                d = int(self.single_font_size[0]/2)
                xi = self.xscale.xmap[posi]['cpos']
                last_digit = str(posi)[-1]
                dr.text((xi - d, yi + 20), last_digit, font=self.font, fill=getrgb(self.labelcolor))            

        pos_str = self.chrom
        dr.text((1, yi), pos_str, font=self.font, fill=getrgb(self.labelcolor))
        

        if self.axisloc == "bottom" or self.axisloc == "middle":
            yi = self.h - 1
            dr.line([(x1, yi), (x2, yi)], fill=getrgb(self.axiscolor), width=1)
            for xi in self.axis_x_list:
                dr.line([(xi, yi), (xi, yi - self.bar_size)], fill=getrgb(self.axiscolor), width=1)
        
    def get_image(self):
        if self.im is None:
            if self.font is None:
                self.set_font()
            self.im = Image.new('RGBA', (self.w, self.h), getrgb(self.bgcolor))
            dr = ImageDraw.Draw(self.im)
            self.draw(dr)
        return self.im