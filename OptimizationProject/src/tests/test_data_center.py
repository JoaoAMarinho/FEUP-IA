from config_import import *


class TestDataCenter(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.data_center = DataCenter('input.txt')

    def test_read_rows(self):
        self.assertEqual(len(self.data_center.rows), 2)

    def test_read_pool(self):
        self.assertEqual(self.data_center.pools, 2)

    def test_initial_sol(self):
        solution = self.data_center.initial_solution()
        print(solution)

    def test_solution_evaluation(self):
        solution = self.data_center.initial_solution()
        print(f'Evaluation: {solution.evaluation}')


if __name__ == '__main__':
    unittest.main()
