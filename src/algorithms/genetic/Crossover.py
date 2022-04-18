from abc import ABC, abstractmethod
from copy import deepcopy


class CrossoverMethod(ABC):
    """
    General abstract crossover class
    Crossover, also called recombination, is a genetic operator used to combine the genetic information of two parents to generate new offspring
    """

    @abstractmethod
    def run(self, parent1, parent2):
        pass


class ServersCrossover(CrossoverMethod):
    """
    TO DO
    """

    def run(self, parent1, parent2):
        """
        Runs the one point crossover
        ...
        Returns:
            The newly generated offspring(s)
        """
        
        offspring1, offspring2 = deepcopy(parent1), deepcopy(parent2)
        _, servers1, _ = offspring1
        _, servers2, _ = offspring2

        crossover_point = len(offspring1['servers']) // 2
        for idx in range(0, crossover_point):
          


        return


class PoolsCrossover(CrossoverMethod):
    """
    TO DO
    """

    def run(self, parent1, parent2):
        """
        Runs the recombination crossover
        ...
        Returns:
            The newly generated offspring(s)
        """

        offspring1, offspring2 = deepcopy(parent1), deepcopy(parent2)
        _, servers1, _ = offspring1
        _, servers2, _ = offspring2

        crossover_point = len(offspring1['servers']) // 2
        for idx in range(0, crossover_point):
            # se a pool do server idx da offs1 != -1 entao mudar para pool do server idx do pai2 (caso este não seja -1)  
            # se a pool do server idx da offs2 != -1 entao mudar para pool do server idx do pai1 (caso este não seja -1)    

        pass
