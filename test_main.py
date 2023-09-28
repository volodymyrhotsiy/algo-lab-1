import unittest
import main

class TestMain(unittest.TestCase):
    def test_base_case(self):
        result = main.solution([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19])
        self.assertEqual((3,9), result)

    def test_sorted_list(self):
        result = main.solution([1,2,3,4,5])
        self.assertEquals((-1, -1), result)    

    def test_empty_list(self):
        result = main.solution([])
        self.assertEquals((-1, -1), result)  

    def test_fully_not_sorted_list(self):
        result = main.solution([5,4,3,2,1]) 
        self.assertEquals((0, 4), result)    

    def test_reversed(self):
        result = main.solution([19,18,16,7,6,12,7,11,10,7,4,2,1], reversed=True) 
        self.assertEquals((3, 9), result)

    def test_reverse_second(self):
        result = main.solution([8, 7, 6, 5, 4, 2, 3, 1], reversed=True)   
        self.assertEquals((5, 6), result) 

if __name__=="__main__":
    unittest.main()