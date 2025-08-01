
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

    def _calculate_position_dict(self, g_pos):
        """
        Calculate position dictionary for a given genomic position.
        
        Args:
            g_pos: Genomic position
            
        Returns:
            dict: Dictionary with 'spos', 'epos', and 'cpos' keys
        """
        spos = int(round((g_pos - self.spos) * self.scale_x))
        epos = int(round((g_pos - self.spos + 1) * self.scale_x)) - 1
        cpos = int(round((spos + epos) / 2))
        
        return {
            'spos': spos,
            'epos': epos, 
            'cpos': cpos
        }

    def set_xmap(self):
        self.xmap = {}
        for g_pos in range(self.spos-1000, self.epos+1000):
            self.xmap[g_pos] = self._calculate_position_dict(g_pos)

    def get_x(self, g_pos):
        """
        Get x-coordinate mapping for a genomic position.
        
        Uses cached values from xmap when available, calculates and caches
        new values for positions not in the initial range.
        
        Args:
            g_pos: Genomic position
            
        Returns:
            dict: Position dictionary with 'spos', 'epos', and 'cpos' keys
        """
        # Use get() method for more efficient lookup with default handling
        if g_pos not in self.xmap:
            self.xmap[g_pos] = self._calculate_position_dict(g_pos)
        
        return self.xmap[g_pos]

        

