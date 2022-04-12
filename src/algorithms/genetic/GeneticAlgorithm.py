from algorithms.Algorithm import Algorithm


class GeneticAlgorithm(Algorithm):
    def __init__(self, max_iterations=10000, max_execution_time=300):
        super.__init__(max_iterations, max_execution_time)

    def fittest_chromosome(self, population):
        """
        Gets the fittest chromosome in the population
        """

    def initial_population(self):
        """
        Builds the initial population of chromosomes
        """
        return

    def perform_selection(self, population):
        return

    def perform_crossover(self, parent1, parent2):
        return

    def perform_mutation(self, chromosome):
        return

    def perform_reproduction(self, population):
        """
        Applies a selection algorithm (tournament or roullete) to select the parents.
        Applies a crossover algorithm (one-point or recombination) to generate two newly offsprings.
        Mutates the two newly offsprings with a very small random probability.
        Returns the population updated with the new generation.
        """
        return

    def execute(self):
        """
        - obter população inicial
        - obter melhor cromossoma (current solution)
        - enquanto critério de paragem não for verdade
          - gerar nova população
          - obter melhor cromossoma da melhor população
          - se novo cromossoma for melhor, atualizar current solution
        """
        return
