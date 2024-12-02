import random


class Inversion_Mutation:
    def __init__(self, mutation_rate=0.1):
        self.mutation_rate = mutation_rate


    def process_mutation(self, chromosome):
        if random.random() < self.mutation_rate:
            start, end = sorted(random.sample(range(len(chromosome)), 2))
            chromosome[start:end] = reversed(chromosome[start:end])


class Scramble_Mutation:
    def __init__(self, mutation_rate=0.1):
        self.mutation_rate = mutation_rate


    def process_mutation(self, chromosome):
        if random.random() < self.mutation_rate:
            start, end = sorted(random.sample(range(len(chromosome)), 2))
            shuffled_section = chromosome[start:end]
            random.shuffle(shuffled_section)
            chromosome[start:end] = shuffled_section