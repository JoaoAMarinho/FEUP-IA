from copy import deepcopy
from random import randint, uniform
from time import perf_counter

from algorithms.Algorithm import Algorithm
from algorithms.genetic.Selection import TournamentSelection, RoulleteSelection
from algorithms.genetic.Crossover import OnePointCrossover, RecombinationCrossover

class GeneticAlgorithm(Algorithm):
    def __init__(self, 
                 initial_solution, 
                 max_iterations=10000, 
                 max_iterations_no_imp=1000, 
                 population_size=30, 
                 mutation_threshold=0.2, 
                 selection_method=TournamentSelection, 
                 crossover_method=RecombinationCrossover):

        super().__init__(max_iterations, max_iterations_no_imp)
        self.population_size = population_size
        self.initial_solution = initial_solution
        self.mutation_threshold = mutation_threshold
        self.selection_method = selection_method
        self.crossover_method = crossover_method

    def fittest_chromosome(self, population):
        """
        Gets the fittest chromosome in the population
        """

        return max(population, key=lambda solution: solution['fitness'])

    def initial_population(self):
        """
        Builds the initial population of chromosomes
        """
        
        population = []
        for _ in range(self.population_size - 1):
            # creates new solutions based on the initial one
            # changing pools

            new_solution = deepcopy(self.initial_solution)
            _, servers, pools = new_solution.values()
            #selected = [selection(pop, scores) for _ in range(n_pop)]
            server = servers[randint(0, len(servers)-1)]
            pools_array = [pool for pool in range(0, pools) if pool != server.pool]
            server.pool = pools_array[randint(0, pools - 1)]

            # changing all servers' pools
            '''
            for server in servers:
              pools_array = [pool for pool in range(0, pools) if pool != server.pool]
              server.pool = pools_array[randint(0, pools - 1)]
            '''

            new_solution['fitness'] = self.evaluate(new_solution)
            population.append(new_solution)

        return population

    def mutate(self, offspring):
        """
        Performs mutation on the offspring with a very small random probability
        ...
        Returns:
          The possibly mutated offspring 
        """
        
        probability = uniform(0, 1)
        if probability <= self.mutation_threshold:
          mutant = deepcopy(offspring)
          mutant = self.neighbour_solution(mutant)
          mutant['fitness'] = self.evaluate(mutant)
          return mutant
        
        return offspring

    def reproduce(self, population):
        """
        Performs population reprodution
        ...
        Returns:
          The new population (updated with the new generation of offsprings)
        """
        
        new_population = []
        for idx in range(0, len(population), 2):
            parent1, parent2 = population[idx], population[idx + 1]
            offspring = self.crossover_method.run(parent1, parent2)
            offspring = self.mutate(offspring)
            new_population.append(offspring)

        return new_population
    
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

        start = perf_counter()

        iteration = 0
        iteration_no_imp = 0

        population = self.initial_population()
        fittest = self.fittest_chromosome(population)

        while not self.stop(iteration):
            iteration += 1
            iteration_no_imp += 1

            new_population = self.selection_method.run(population)
            new_population = self.reproduce(new_population)
            new_fittest = self.fittest_chromosome(new_population)
			
            if new_fittest['fitness'] > fittest['fitness']:
                fittest = new_fittest
                iteration_no_imp = 0

        elapsed = perf_counter() - start

        return population