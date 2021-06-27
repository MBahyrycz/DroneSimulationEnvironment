from math import sqrt
from enum import Enum

from App.Environment.GeneticAlgorythm.Individual import *


class MutationType(Enum):
    RANDOM = 0


class GeneticAlgorythm:

    @staticmethod
    def init(station_count, drone_trace, population_count=100, iteration_count=1000):
        global g_Population
        global g_PopulationCount
        global g_StationCount
        global g_DroneTrace
        global g_AlphaMale
        global g_IterationCount
        g_IterationCount = iteration_count
        g_DroneTrace = drone_trace
        g_PopulationCount = population_count
        g_StationCount = station_count
        g_AlphaMale = Individual(g_StationCount)
        g_AlphaMale.quality = GeneticAlgorythm.goal_function(g_AlphaMale)
        g_Population = [Individual(g_StationCount) for _ in range(g_PopulationCount)]

    @staticmethod
    def solve():
        end_condition = 0
        while end_condition < g_IterationCount:
            GeneticAlgorythm.calculate_quality()
            GeneticAlgorythm.rank_selection()
            GeneticAlgorythm.cross_over()
            GeneticAlgorythm.mutate()

            end_condition += 1

        return g_AlphaMale

    @staticmethod
    def print_population():
        GeneticAlgorythm.print_alpha_male()
        for index, i in enumerate(g_Population):
            print("{0}. ".format(index), i.chromosome, " quality: {0:.2f}".format(i.quality))

    @staticmethod
    def print_alpha_male():
        print("A. ", g_AlphaMale.chromosome, " quality: {0:.2f}".format(g_AlphaMale.quality))

    @staticmethod
    def goal_function(individual):
        sum = 0
        index = 0
        for j in range(len(g_DroneTrace)):
            while index < g_StationCount - 1:
                index += 1
            sum += sqrt((individual.chromosome[index][0] - g_DroneTrace[j][0]) ** 2 +
                        (individual.chromosome[index][1] - g_DroneTrace[j][1]) ** 2)

        return sum

    @staticmethod
    def calculate_quality():
        for i in range(g_PopulationCount):
            g_Population[i].quality = GeneticAlgorythm.goal_function(g_Population[i])

    @staticmethod
    def rank_selection():
        g_Population.sort(key=lambda a: a.quality)

        if g_Population[0].quality < g_AlphaMale.quality:
            g_AlphaMale.chromosome = g_Population[0].chromosome[:]
            g_AlphaMale.quality = g_Population[0].quality

        for i in range(g_PopulationCount // 2, g_PopulationCount):
            g_Population[i] = Individual(g_StationCount)

    @staticmethod
    def mutate(type=MutationType.RANDOM):
        for i in g_Population:
            if type == MutationType.RANDOM:
                i.mutate_random()
            else:
                raise ValueError("Unknown mutation method")

    @staticmethod
    def cross_over():
        for i in range(0, g_PopulationCount, 2):
            crossover_index = random.randint(0, max((g_StationCount - 2), 0))
            g_Population[i].chromosome[crossover_index:-1], g_Population[i + 1].chromosome[crossover_index:-1] = \
            g_Population[i + 1].chromosome[crossover_index:-1], g_Population[i].chromosome[crossover_index:-1]
