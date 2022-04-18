from abc import ABC, abstractmethod
from random import sample


class SelectionMethod(ABC):
    """
    General abstract selection class
    A selection method is responsible for selecting two parent chromosomes to crossover
    """

    @abstractmethod
    def run(self, population):
        pass


class TournamentSelection(SelectionMethod):
    """
    Selects two chromosomes creating two random groups, selecting the best chromosome on both of them
    """
    
    def __init__(self, nr_competitors = 2):
        self.nr_competitors = nr_competitors

    def run(self, population):
        """
        Runs the tournament selection method
        ...
        Returns:
            List with the selected population chromosomes
        """
        
        competition_size = len(population)
        nr_competitors = min(self.nr_competitors, competition_size)

        selection = []
        for _ in range(competition_size):
            sample_population = sample(
                population=population,
                k=nr_competitors
            )
            fittest = max(sample_population, key=lambda solution: solution['fitness'])
            selection.append(fittest)
        
        return selection


class RoulleteSelection(SelectionMethod):
    """
    Selects two chromosomes randomly according to their fitness
    """

    def run(self, population):
        """
        Runs the roullete selection method
        ...
        Returns:
            List with the randomly selected population
        """

        fitness = [solution['fitness'] for solution in population]
        min_fitness = min(fitness)
        fitness = [fit - min_fitness + 1 for fit in fitness]

        # random.sample is used since the chromosome fitness is required to be an integer
        result_list = sample(
            population=population,
            counts=fitness,
            k=len(population)
        )
        return result_list
