from random import randint
from copy import deepcopy

from algorithms.Algorithm import Algorithm
from model.Solution import Solution

class SearchAlgorithm(Algorithm):
    def __init__(self, initial_solution, max_iterations=10000, max_iterations_no_imp=1000):
        super().__init__(max_iterations, max_iterations_no_imp)
        self.initial_solution = initial_solution

    def change_pool(self, solution):
        """
        Generates a neighbour solution by changing the pool of a randomly selected server from the original solution
        """

        if solution['pools'] <= 1: 
            return solution

        new_solution = deepcopy(solution)
        servers = new_solution.servers
        pools = new_solution.pools

        allocated = [server for server in servers if server.pool != -1]
        server = allocated[randint(0, len(allocated) - 1)]
        while (new_pool:=randint(0, pools - 1)) == server.pool:
            pass

        server.pool = new_pool
        return new_solution

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

    def neighbour_solutions(self, solution):
        """
        Obtains neighbour solution by applying one of the available strategies
        """

        return [self.__change_pool, self.__change_row, self.__change_slot, self.__swap_allocation]

    def get_best_solution(self, solution):
        return max(solution, key= lambda sol: sol.evaluation)