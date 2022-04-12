from abc import abstractmethod


class Algorithm():
    def __init__(self, max_iterations=10000, max_execution_time=300):
        self.max_iterations = max_iterations
        self.max_execution_time = max_execution_time

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def evaluate(self, solution):
        pass
