import unittest
import bamsnap

class TestXscale(unittest.TestCase):
    def setUp(self):
        self.w = 1000
        self.scale_x = 0.1
        self.x1 = bamsnap.scale.Xscale(10000, 20000, self.w)
    
    def test_default_value(self):
        self.assertEqual(self.x1.w, self.w)
        self.assertEqual(self.x1.scale_x, self.scale_x)
        self.assertEqual(self.x1.xmap[9000], {'spos': -100, 'epos': -101, 'cpos': -100})
        self.assertEqual(self.x1.get_x(9000), {'spos': -100, 'epos': -101, 'cpos': -100})

if __name__ == "__main__":
    unittest.main()