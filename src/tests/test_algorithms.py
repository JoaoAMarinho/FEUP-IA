from config_import import *

from algorithms.genetic.Selection import RoulleteSelection
from algorithms.genetic.Crossover import PoolsCrossover

class TestAlgorithms(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data_center = DataCenter('input_xl.txt')
        cls.solution = cls.data_center.solution
        cls.i = 9
        print(cls.solution, "Eval Initial ",cls.solution.evaluation)

    def callback(self, solution):
        print('got solution')
    
    def test_simulated_annealing(self):
        simulated_annealing = SimulatedAnnealing(initial_solution=self.solution, 
                                                 initial_temperature=1000000, 
                                                 temperature_decrease_factor=0.75)
        solution = simulated_annealing.execute(self.callback,f'simulated_annealing_best.json')
        print("Sim\n",solution, "Eval: ",solution.evaluation, " Time: ",solution.time)

    def test_genetic(self):
        genetics = GeneticAlgorithm(initial_solution=self.solution,
                                    selection_method=RoulleteSelection(),
                                    crossover_method=PoolsCrossover())
        solution = genetics.execute(self.callback, f'genetic_best.json')
        print("Tabu\n", solution, "Eval ", solution.evaluation)

    def test_hill_climbing(self):
        hill_climbing = HillClimbing(initial_solution=self.solution)
        solution = hill_climbing.execute(self.callback, f'hill_climbing_best.json')
        print("Hill\n", solution, "Eval ", solution.evaluation)

    def test_tabu_search(self):
        tabu_search = TabuSearch(initial_solution=self.solution)
        solution = tabu_search.execute(self.callback,f'tabu_search_best.json')
        print("Tabu\n", solution, "Eval ", solution.evaluation)

if __name__ == '__main__':
    unittest.main()
