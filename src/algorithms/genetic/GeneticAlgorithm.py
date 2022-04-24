from copy import deepcopy
from random import randint, uniform

from algorithms.Algorithm import *
from algorithms.genetic.Selection import TournamentSelection, RoulleteSelection
from algorithms.genetic.Crossover import ServersCrossover, PoolsCrossover


class GeneticAlgorithm(Algorithm):
    def __init__(self,
                 initial_solution,
                 max_iterations=10000,
                 max_iterations_no_imp=1000,
                 population_size=30,
                 mutation_threshold=0.2,
                 selection_method=TournamentSelection(),
                 crossover_method=PoolsCrossover()):

        super().__init__(max_iterations, max_iterations_no_imp)
        self.max_iterations_no_imp = 1000
        self.population_size = population_size
        self.initial_solution = initial_solution
        self.mutation_threshold = mutation_threshold
        self.selection_method = selection_method
        self.crossover_method = crossover_method

    def fittest_chromosome(self, population):
        """
        Gets the fittest chromosome in the population
        """

        return max(population, key=lambda solution: solution.evaluation)

    def initial_population(self):
        """
        Builds the initial population of chromosomes
        """

        population = []
        new_solution = self.initial_solution

        while len(population) < self.population_size:
            population.extend(self.neighbour_solutions(new_solution))

            new_solution = population[randint(0, len(population) - 1)]


        return population[:30]

    def mutate(self, offspring):
        """
        Performs mutation on the offspring with a very small random probability
        ...
        Returns:
          The possibly mutated offspring
        """

        probability = uniform(0, 1)
        if probability <= self.mutation_threshold:
            mutant = self.neighbour_solution(offspring)
            mutant.evaluate()
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
        for idx in range(0, len(population)-2, 2):
            parent1, parent2 = population[idx], population[idx + 1]
            offspring1, offspring2 = self.crossover_method.run(
                parent1, parent2)
            offspring1 = self.mutate(offspring1)
            offspring2 = self.mutate(offspring2)
            new_population.append(offspring1)
            new_population.append(offspring2)

        return new_population

    def write_to_file(self, file, solution, iteration):
        crossover = "servers crossover"
        selection = "tournament selection"
        data = {'evaluation': solution.evaluation,
                'time': solution.time,
                'iteration': iteration,
                'initial population': self.population_size,
                'crossover method': crossover,
                'selection method': selection}

        with open(file, 'a') as outfile:
            outfile.write(json.dumps(data,default=vars)+',\n')
            outfile.close()

    def execute(self, callback, file = 'genetic_algorithm_5.json'):

        """
        Runs the genetic algorithm
        ...
        Returns:
            The best chromosome solution
        """

        start = perf_counter()

        iteration = 0
        iteration_no_imp = 0

        population = self.initial_population()
        fittest = self.fittest_chromosome(population)

        self.open_file(file)
        fittest.time = perf_counter() - start
        self.write_to_file(file, fittest, iteration)

        while not self.stop(iteration, iteration_no_imp):
            iteration += 1
            iteration_no_imp += 1

            new_population = self.selection_method.run(population)
            new_population = self.reproduce(new_population)
            new_fittest = self.fittest_chromosome(new_population)

            if new_fittest.evaluation > fittest.evaluation:
                   fittest = new_fittest
                   iteration_no_imp = 0
            fittest.time = perf_counter() - start       
            self.write_to_file(file,fittest, iteration)

        elapsed = perf_counter() - start
        fittest.time = elapsed
        self.close_file(file)

        callback(fittest)
        return fittest
