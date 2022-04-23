from config_import import *


class TestAlgorithms(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data_center = DataCenter('input_xl.txt')
        cls.solution = cls.data_center.solution
        cls.i = 4
        print(cls.solution, "Eval Initial ", cls.solution.evaluation)

    def callback(self, solution):
        print('got solution')

    def test_simulated_annealing(self):
        simulated_annealing = SimulatedAnnealing(self.solution)
        solution = simulated_annealing.execute(
            self.callback, f'simulated_annealing_{self.i}.json')
        print("Sim\n", solution, "Eval: ",
              solution.evaluation, " Time: ", solution.time)

    def test_genetic(self):
        genetics = GeneticAlgorithm(self.solution)
        solution = genetics.execute(self.callback, f'genetic_{self.i}.json')
        print("Tabu\n", solution, "Eval ", solution.evaluation)

    def test_hill_climbing(self):
        solution = self.data_center.initial_solution()
        hill_climbing = HillClimbing(solution)
        solution = hill_climbing.execute(
            self.callback, f'hill_climbing_{self.i}.json')
        print("Hill\n", solution, "Eval ", solution.evaluation)

    def test_tabu_search(self):
        tabu_search = TabuSearch(self.solution)
        solution = tabu_search.execute(
            self.callback, f'tabu_search_{self.i}.json')
        print("Tabu\n", solution, "Eval ", solution.evaluation)


if __name__ == '__main__':
    unittest.main()
