from config_import import *
from algorithms.search.SearchAlgorithm import SearchAlgorithm

class TestNeighborFunc(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.data_center = DataCenter('input_4x5.txt')
        cls.algorithm = SearchAlgorithm(cls.data_center.solution)

        # Print initial solution
        for key, value in cls.data_center.solution.items():
            print('\n')
            print(key, ' : ', value)

    def test_change_pool(self):
        algorithm = self.algorithm
        new_sol = algorithm.change_pool(algorithm.initial_solution)
        
        for key, value in new_sol.items():
            print('\n')
            print(key, ' : ', value)
    
    def test_change_row(self):
        algorithm = self.algorithm
        new_sol = algorithm.change_row(algorithm.initial_solution)
        
        print('Change Row')
        for key, value in new_sol.items():
            print('\n')
            print(key, ' : ', value)

if __name__ == '__main__':
    unittest.main()
