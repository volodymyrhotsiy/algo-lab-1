import unittest
from src.lab6 import strStr

class TestLab(unittest.TestCase):
        def test_default(self):
            res = [(4, 8), (9, 13)]
            self.assertEqual(strStr("AAAXAAAAXAAAA", "AAAA"), res)
        
        def test_one(self):
            res = [(0, 3)]
            self.assertEqual(strStr("AAA", "AAA"), res)

        def test_none(self):
            res = -1
            self.assertEqual(strStr("AAAXAAAAXAAAA", "BBB"), res)     


if __name__=="__main__":
    unittest.main()            