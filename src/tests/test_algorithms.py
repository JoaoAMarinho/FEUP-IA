from config_import import *

class TestAlgorithms(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.data_center = DataCenter('input.txt')

    def test_initial_sol(self):
        solution = self.data_center.initial_solution()
        print(solution)

    def test_hill_climbing(self):
        solution = self.data_center.initial_solution()
        hill_climbing = HillClimbing(solution)
        solution = hill_climbing.execute()
        print(solution)
    def test_simulated_annealing(self):
        solution = self.data_center.initial_solution()
        simulated_annealing = SimulatedAnnealing(solution)
        solution = simulated_annealing.execute()
        print(solution)
    def test_tabu_search(self):
        solution = self.data_center.initial_solution()
        tabu_search = TabuSearch(solution)
        solution = tabu_search.execute()
        print(solution)
    def test_genetic(self):
        solution = self.data_center.initial_solution()
        genetic = GeneticAlgorithm(solution)
        solution = genetic.execute()
        print(solution)

    

if __name__ == '__main__':
    unittest.main()
