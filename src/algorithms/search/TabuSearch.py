from algorithms.Algorithm import *


class TabuSearch(Algorithm):
	def __init__(self, initial_solution, tabu_tenure=40, max_iterations=10000, max_iterations_no_imp=1000):
		super().__init__(initial_solution, max_iterations, max_iterations_no_imp)
		self.tabu_tenure = tabu_tenure
		self.tabu_memory = {}  

	def execute(self, callback, file = 'tabu_search_5.json'):
		start = perf_counter()

		iteration = 0
		iteration_no_imp = 0

		solution = self.initial_solution
		best_solution = solution.evaluation

		self.open_file(file)
		solution.time = perf_counter() - start
		self.write_to_file(file, solution, iteration)
		
		while not self.stop(iteration, iteration_no_imp):
			iteration += 1
			iteration_no_imp += 1

			neighbours = self.neighbour_solutions(solution)
			new_solution = self.get_best_solution(neighbours)

			key = hash(new_solution)
			if key not in self.tabu_memory:
				if new_solution.evaluation > best_solution:
					iteration_no_imp = 0
					solution = new_solution
					best_solution = new_solution.evaluation
					self.tabu_memory[key] = solution
					self.tabu_memory[key].tenure = self.tabu_tenure
				solution.time = perf_counter() - start
				self.write_to_file(file, solution, iteration)
			else:
				tenure = self.tabu_memory[key].tenure
				if tenure == 0: self.tabu_memory.pop(key)
				else: self.tabu_memory[key].tenure = tenure - 1


		elapsed = perf_counter() - start
		solution.time = elapsed
		self.close_file(file)

		callback(solution)
		return solution
