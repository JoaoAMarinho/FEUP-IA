from random import randint
from algorithms.Algorithm import Algorithm


class SearchAlgorithm(Algorithm):
    def __init__(self, max_iterations=10000, max_execution_time=300):
        super.__init__(max_iterations, max_execution_time)

    def initial_solution(self):
        """
        Obtains the initial solution 
        (tal como está implementado na classe DataCenter, acho que faz sentido que esteja antes aqui)
        """
        pass

    def __change_pool(self, solution):
        """
        Generates a neighbour solution by changing the pool of a randomly selected server from the original solution
        """
        return

    def __change_row(self, solution):
        """
        Generates a neighbour solution by changing the row of a randomly selected server from the original solution
        """
        return

    def __change_slot(self, solution):
        """
        Generates a neighbour solution by changing the slot of a randomly selected server from the original solution
        """
        return

    def __swap_allocation(self, solution):
        """
        Generates a neighbour solution by deallocating an allocated server and allocating a non-allocated server, both randomly selected
        """
        return

    def neighbour_solution(self, solution):
        """
        Obtains neighbour solution by applying one of the available strategies
        """

        operators = [self.__change_pool, self.__change_row, self.__change_slot, self.__swap_allocation]
        selected_operator = randint(0, len(operators) - 1)
        return operators[selected_operator](solution)
