import unittest
from source.lab5bfsrc import solution

class TestSolutionFunction(unittest.TestCase):

    def test_solution_case_with_no_solution(self):
        self.assertEqual(solution(3, 2, "YNN YNN YNN"), (1, [0]))

    def test_solution_case_with_single_worker(self):
        self.assertEqual(solution(6, 3, "YNN YNY YNY NYY NYY NYN"), (2, [0, 1]))
        
    def test_solution_case_with_single_worker(self):
        self.assertEqual(solution(2, 2, "YN NY"), (2, [0, 1]))    

if __name__ == '__main__':
    unittest.main()