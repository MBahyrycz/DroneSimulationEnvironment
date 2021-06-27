import random


class Individual:
    def __init__(self, station_count):
        self.station_count = station_count
        self.mutation_probability = 0.77
        self.chromosome = [(random.randrange(0, 1000), random.randrange(0, 1000)) for _ in range(self.station_count)]
        self.quality = 0.0

    def mutate_random(self):
        if random.random() < self.mutation_probability:
            index = random.randint(0, self.station_count - 1)
            self.chromosome[index] = (random.randrange(0, 1000), random.randrange(0, 1000))
