from algorithms.Algorithm import *


class TabuSearch(Algorithm):
	def __init__(self, initial_solution, tabu_tenure=40, max_iterations=10000, max_iterations_no_imp=1000):
		super().__init__(initial_solution, max_iterations, max_iterations_no_imp)
		self.tabu_tenure = tabu_tenure
		self.tabu_memory = {}  

	def execute(self, callback):
		"""
        Runs the Tabu Search algorithm
        ...
        Returns:
            The best solution found
        """
		start = perf_counter()

		iteration = 0
		iteration_no_imp = 0

		solution = self.initial_solution
		best_solution = solution.evaluation

		while not self.stop(iteration, iteration_no_imp):
			iteration += 1
			iteration_no_imp += 1

			neighbours = self.neighbour_solutions(solution)
			new_solution = neighbours[0]

			for neighbour in neighbours:
				key = hash(neighbour)
				if (key not in self.tabu_memory):
					if neighbour.evaluation > new_solution.evaluation:
						new_solution = neighbour
				else:
					tenure = self.tabu_memory[key].tenure
					if tenure == 0: self.tabu_memory.pop(key)
					else: self.tabu_memory[key].tenure = tenure - 1

			if new_solution.evaluation > best_solution:
				solution = new_solution
				best_solution = new_solution.evaluation

			key = hash(new_solution)
			self.tabu_memory[key] = new_solution
			self.tabu_memory[key].tenure = self.tabu_tenure

		elapsed = perf_counter() - start
		solution.time = elapsed

		callback(solution)
		return solution