import unittest
from algorithms.search.SearchAlgorithm import SearchAlgorithm
from model.DataCenter import DataCenter

class TestDataCenter(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.data_center = DataCenter('input.txt')
        cls.algorithm = SearchAlgorithm(cls.data_center.solution)

    def test_read_rows(self):
        self.assertEqual(len(self.data_center.rows), 2) 

    def test_read_pool(self):
        self.assertEqual(self.data_center.pools, 2)

    def test_initial_sol(self):
        for key, value in self.data_center.solution.items():
            print('\n')
            print(key, ' : ', value)

    def test_algorithm_evaluate(self):
        solution = self.data_center.solution
        print(f'Eval: {self.algorithm.evaluate(solution)}')

    def test_change_pool(self):
        algorithm = self.algorithm
        new_sol = algorithm.change_pool(algorithm.initial_solution)
        for key, value in new_sol.items():
            print('\n')
            print(key, ' : ', value)

if __name__ == '__main__':
    unittest.main()
