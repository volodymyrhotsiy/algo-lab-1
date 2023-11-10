import unittest
from lab2_3 import FindSquare  

class TestFindSquare(unittest.TestCase):
    def test_case_1(self):
        N, W, H = 10, 2, 3
        self.assertEqual(FindSquare(N, W, H), 9)

    def test_case_2(self):
        N, W, H = 4, 1, 1
        self.assertEqual(FindSquare(N, W, H), 2)

    def test_case_3(self):
        N, W, H = 5, 1, 1
        self.assertEqual(FindSquare(N, W, H), 3)

    def test_case_4(self):
        N, W, H = 4, 2, 4
        self.assertEqual(FindSquare(N, W, H), 8)

    def test_case_5(self):
        N, W, H = 3, 5, 2
        self.assertEqual(FindSquare(N, W, H), 6)

    def test_case_6(self):
        N, W, H = 2, 1000000000, 999999999
        self.assertEqual(FindSquare(N, W, H), 1999999998)

    def test_case_7(self):
        N, W, H = 1, 2, 2
        self.assertEqual(FindSquare(N, W, H), 2)

    def test_case_8(self):
        N, W, H = 6, 2, 2
        self.assertEqual(FindSquare(N, W, H), 6)

    def test_case_9(self):
        N, W, H = 7, 4, 2
        self.assertEqual(FindSquare(N, W, H), 8)

    def test_case_10(self):
        N, W, H = 3, 3, 1
        self.assertEqual(FindSquare(N, W, H), 3)

    def test_case_11(self):
        N, W, H = 3, 5, 2
        self.assertEqual(FindSquare(N, W, H), 6)

    def test_case_12(self):
        N, W, H = 3, 1, 10
        self.assertEqual(FindSquare(N, W, H), 10)

    def test_case_13(self):
        N, W, H = 3, 6, 2
        self.assertEqual(FindSquare(N, W, H), 6)

    def test_case_14(self):
        N, W, H = 9, 7, 1
        self.assertEqual(FindSquare(N, W, H), 9)

    def test_case_15(self):
        N, W, H = 11, 3, 1
        self.assertEqual(FindSquare(N, W, H), 6)

if __name__ == "__main__":
    unittest.main()
