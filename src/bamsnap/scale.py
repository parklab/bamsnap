
from .util import get_scale


class Xscale():
    def __init__(self, spos, epos, w):
        self.spos = spos
        self.epos = epos
        self.w = w
        self.scale_x = get_scale(spos, epos, w)
        self.base_width = int(w / abs(epos - spos))
        if self.base_width < 1:
            self.base_width = 1
        self.set_xmap()

    def set_xmap(self):
        self.xmap = {}
        for g_pos in range(self.spos-1000, self.epos+1000):
            d = {}
            d['spos'] = int(round((g_pos - self.spos) * self.scale_x))
            d['epos'] = int(round((g_pos - self.spos + 1) * self.scale_x)) - 1
            d['cpos'] = int(round((d['spos'] + d['epos']) / 2))
            self.xmap[g_pos] = d

    def get_x(self, g_pos):
        try:
            tpos = self.xmap[g_pos]
        except KeyError:
            tpos = {}
            tpos['spos'] = int(round((g_pos - self.spos) * self.scale_x))
            tpos['epos'] = int(round((g_pos - self.spos + 1) * self.scale_x)) - 1
            tpos['cpos'] = int(round((tpos['spos'] + tpos['epos']) / 2))
            self.xmap[g_pos] = tpos
        return tpos

        

