from config_import import *

from algorithms.genetic.Selection import RoulleteSelection, TournamentSelection
from algorithms.genetic.Crossover import PoolsCrossover, ServersCrossover

class TestAlgorithms(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data_center = DataCenter('input_xl.txt')
        cls.solution = cls.data_center.solution
        cls.i = 0
        print(cls.solution, "Eval Initial ",cls.solution.evaluation)

    def callback(self, solution):
        print('got solution')
    
    """     def test_simulated_annealing(self):
        simulated_annealing = SimulatedAnnealing(initial_solution=self.solution, 
                                                 initial_temperature=100000, 
                                                 temperature_decrease_factor=0.75)
        solution = simulated_annealing.execute(self.callback,f'simulated_annealing_100000_75.json')

        simulated_annealing = SimulatedAnnealing(initial_solution=self.solution, 
                                                 initial_temperature=100000, 
                                                 temperature_decrease_factor=0.80)
        solution = simulated_annealing.execute(self.callback,f'simulated_annealing_100000_80.json')

        simulated_annealing = SimulatedAnnealing(initial_solution=self.solution, 
                                                 initial_temperature=100000, 
                                                 temperature_decrease_factor=0.90)
        solution = simulated_annealing.execute(self.callback,f'simulated_annealing_100000_90.json')

        simulated_annealing = SimulatedAnnealing(initial_solution=self.solution, 
                                                 initial_temperature=100000, 
                                                 temperature_decrease_factor=0.95)
        solution = simulated_annealing.execute(self.callback,f'simulated_annealing_100000_95.json')

    def test_genetic(self):
        genetics = GeneticAlgorithm(initial_solution=self.solution,
                                    selection_method=TournamentSelection(),
                                    crossover_method=PoolsCrossover())
        solution = genetics.execute(self.callback, f'genetic_pools_tournament.json')
        genetics = GeneticAlgorithm(initial_solution=self.solution,
                                    selection_method=RoulleteSelection(),
                                    crossover_method=PoolsCrossover())
        solution = genetics.execute(self.callback, f'genetic_pools_roullete.json')
        genetics = GeneticAlgorithm(initial_solution=self.solution,
                                    selection_method=TournamentSelection(),
                                    crossover_method=ServersCrossover())
        solution = genetics.execute(self.callback, f'genetic_servers_tournament.json')
        genetics = GeneticAlgorithm(initial_solution=self.solution,
                                    selection_method=RoulleteSelection(),
                                    crossover_method=ServersCrossover())
        solution = genetics.execute(self.callback, f'genetic_servers_roullete.json')
    def test_hill_climbing(self):
        hill_climbing = HillClimbing(initial_solution=self.solution)
        solution = hill_climbing.execute(self.callback, f'hill_climbing_best.json')
        print("Hill\n", solution, "Eval ", solution.evaluation)
    """
    def test_tabu_search(self):
        tabu_search = TabuSearch(initial_solution=self.solution, tabu_tenure=40)
        solution = tabu_search.execute(self.callback,f'tabu_search_best.json') 
        hill_climbing = HillClimbing(initial_solution=self.solution)
        solution = hill_climbing.execute(self.callback, f'hill_climbing_best.json')
        simulated_annealing = SimulatedAnnealing(initial_solution=self.solution, 
                                                 initial_temperature=1000, 
                                                 temperature_decrease_factor=0.95)
        solution = simulated_annealing.execute(self.callback,f'simulated_annealing_best.json') 
        genetics = GeneticAlgorithm(initial_solution=self.solution,
                                    selection_method=RoulleteSelection(),
                                    crossover_method=ServersCrossover())
                                    
        solution = genetics.execute(self.callback, f'genetic_best.json')


if __name__ == '__main__':
    unittest.main()
