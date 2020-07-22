from PIL import ImageFont, Image, ImageDraw
from .conf import COLOR
from .util import getTemplatePath, get_scale, getrgb
import tabix


class BaseTrack():
    def __init__(self, chrom, spos, epos, refseq, xscale, w):
        self.chrom = chrom
        self.nchrom = chrom.replace('chr', '')
        self.spos = spos
        self.epos = epos
        self.w = w
        self.h = 0
        self.refseq = refseq
        self.g_len = self.epos - self.spos + 1
        self.font = None
        self.im = None
        self.xscale = xscale
        self.bgcolor = "FFFFFF"
        self.margin_top = 0
        self.margin_bottom = 0
        self.fontsize = None

    def draw(self, dr):
        y = self.h - 1
        y1 = 0
        y2 = y
        x1 = 0
        x2 = self.w

        yi = int( y / 2 ) - 5
        h = 10
        dr.line([(x1, 0), (x2, 0)], fill=COLOR['SEPARATE'], width=1)
        dr.line([(x1, y), (x2, y)], fill=COLOR['SEPARATE'], width=1)

        vcls = ""
        for i in range(self.g_len):
            posi = self.spos + i
            base = self.refseq[posi]
            # x1 = int(i * self.scale_x) + int(self.scale_x/2) - int(fontsize[0]/2)
            x1 = self.xscale.xmap[posi]['spos']
            x2 = self.xscale.xmap[posi]['epos']
            if vcls == "":
                if (x2 - x1) > self.fontsize[0] + 5:
                    vcls = "textoutline"
                elif (x2 - x1) > self.fontsize[0]:
                    vcls = "text"
                elif (x2 - x1) >= 3:
                    vcls = "outline"
                else:
                    vcls = "fill"

            if vcls == "textoutline":
                xi = self.xscale.xmap[posi]['cpos'] - int(self.fontsize[0]/2)
                dr.rectangle([(x1, y1), (x2, y2)], fill=(255,255,255,255), outline=COLOR['w'+base], width=1)
                dr.text((xi, 0), base, font=self.font, fill=COLOR['d'+base])
                
            elif vcls == "text":
                xi = self.xscale.xmap[posi]['cpos'] - int(self.fontsize[0]/2)
                dr.text((xi, 0), base, font=self.font, fill=COLOR['d'+base])
            elif vcls == "outline":
                dr.rectangle([(x1, y1), (x2, y2)], fill=COLOR[base], outline=COLOR['w'+base], width=1)
            else:
                dr.rectangle([(x1, y1), (x2, y2)], fill=COLOR[base], width=0)


    def set_height(self):
        self.fontsize = self.font.getsize('C')
        self.h = self.fontsize[1] + 2


    def get_image(self, margin_top=0, margin_bottom=0):
        self.set_height()
        self.im = Image.new('RGBA', (self.w, self.h), getrgb(self.bgcolor))
        dr = ImageDraw.Draw(self.im)
        self.draw(dr)
        return self.im