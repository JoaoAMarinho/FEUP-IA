
from time import perf_counter

from algorithms.Algorithm import Algorithm


class TabuSearch(Algorithm):
    def __init__(self, initial_solution, tabu_tenure=3, max_iterations=10000, max_iterations_no_imp=1000):
        super().__init__(initial_solution, max_iterations, max_iterations_no_imp)
        self.tabu_tenure = tabu_tenure
        self.tabu_memory = {}  

    def execute(self):
        start = perf_counter()

        iteration = 0
        iteration_no_imp = 0

        solution = self.initial_solution
        best_solution = solution.evaluation
        
        while not self.stop(iteration, iteration_no_imp):
            iteration += 1
            iteration_no_imp += 1

            neighbours = self.neighbour_solutions(solution)
            new_best_solution = self.get_best_solution(neighbours)

            key = hash(new_best_solution)
            if key not in self.tabu_tenure:
              if solution.evaluation > best_solution.evaluation:
                solution = new_best_solution
                self.tabu_memory[key] = solution
                self.tabu_memory[key]['tenure'] = self.tabu_tenure
            else:
              tenure = self.tabu_memory[key]['tenure']
              if tenure == 0: self.tabu_memory.pop(key)
              else: self.tabu_memory[key]['tenure'] = tenure - 1


        elapsed = perf_counter() - start
        
        return solution
