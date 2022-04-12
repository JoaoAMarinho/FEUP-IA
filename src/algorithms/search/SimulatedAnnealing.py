from algorithms.search.SearchAlgorithm import SearchAlgorithm


class SimulatedAnnealing(SearchAlgorithm):
    def __init__(self, max_iterations=10000, max_execution_time=300, initial_temperature=1000, temperature_decrease_factor=0.9):
        super.__init__(max_iterations, max_execution_time)
        self.initial_temp = initial_temperature
        self.temp_decrease_factor = temperature_decrease_factor

    def schedule_temperature(self, t):
        return t * self.temperature_decrease_factor

    def execute(self):
        return
