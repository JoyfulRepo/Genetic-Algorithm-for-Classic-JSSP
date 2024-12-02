import random


class PMX_Crossover():
    def __init__(self):
        pass

    def process_crossover(self, parent1, parent2):
        size = len(parent1)

        offspring1 = [-1] * size
        offspring2 = [-1] * size
        cx_point1, cx_point2 = sorted(random.sample(range(size), 2))

        offspring1[cx_point1:cx_point2] = parent2[cx_point1:cx_point2]
        offspring2[cx_point1:cx_point2] = parent1[cx_point1:cx_point2]

        for i in range(size):
            if offspring1[i] == -1:
                value = parent1[i]
                while value in offspring1:
                    value = parent2[parent1.index(value)]
                offspring1[i] = value

        for i in range(size):
            if offspring2[i] == -1:
                value = parent2[i]
                while value in offspring2:
                    value = parent1[parent2.index(value)]
                offspring2[i] = value

        return offspring1, offspring2


class Order_Crossover:
    def __init__(self):
        pass


    def process_crossover(self, parent1, parent2):
        size = len(parent1)

        offspring1 = [-1] * size
        offspring2 = [-1] * size

        cx_point1, cx_point2 = sorted(random.sample(range(size), 2))
        offspring1[cx_point1:cx_point2] = parent1[cx_point1:cx_point2]
        offspring2[cx_point1:cx_point2] = parent2[cx_point1:cx_point2]

        current_pos = cx_point2
        for i in range(size):
            gene = parent2[(cx_point2 + i) % size]
            if gene not in offspring1:
                if current_pos == size:
                    current_pos = 0
                offspring1[current_pos] = gene
                current_pos += 1

        current_pos = cx_point2
        for i in range(size):
            gene = parent1[(cx_point2 + i) % size]
            if gene not in offspring2:
                if current_pos == size:
                    current_pos = 0
                offspring2[current_pos] = gene
                current_pos += 1

        return offspring1, offspring2