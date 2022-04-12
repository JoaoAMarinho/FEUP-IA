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
        """
        Performs a selection algorithm (tournament or roullete)
        ...
        Returns:
          The two parents selected
        """
        return

    def perform_crossover(self, parent1, parent2):
        """
        Performs a crossover algorithm (one-point or recombination)
        ...
        Returns:
          The two newly generated offsprings
        """
        return

    def perform_mutation(self, offspring):
        """
        Performs mutation on the offspring with a very small random probability
        ...
        Returns:
          The possibly mutated offspring 
        """
        return

    def perform_reproduction(self, population):
        """
        Performs population reprodution
        ...
        Returns:
          The new population (updated with the new generation of offsprings)
        """
        return

    def execute(self):
        """
        Runs the genetic algorithm
        ...
        Returns:
            The best chromosome solution
        """

        """ STEPS
        - obter população inicial
        - obter melhor cromossoma (current solution)
        - enquanto critério de paragem não for verdade
          - gerar nova população
          - obter melhor cromossoma da melhor população
          - se novo cromossoma for melhor, atualizar current solution
        """
        return
