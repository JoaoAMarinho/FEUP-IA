import unittest
from algorithms.Algorithm import Algorithm
from model.DataCenter import DataCenter

class TestDataCenter(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.data_center = DataCenter('input.txt')
        cls.algorithm = Algorithm()

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

if __name__ == '__main__':
    unittest.main()
