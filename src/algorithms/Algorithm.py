from abc import abstractmethod

class Algorithm():
    def __init__(self, max_iterations=10000, max_iterations_no_imp=1000):
        self.max_iterations = max_iterations
        self.max_iterations_no_imp = max_iterations_no_imp

    @abstractmethod
    def execute(self):
        pass

    def stop(self, iteration, iteration_no_imp):
        return iteration >= self.max_iterations or iteration_no_imp >= self.max_iterations_no_imp
