import random

class Rank_Selection:
    def __init__(self, elitism_count=2):
        self.elitism_count = elitism_count


    def process_selection(self, population, fitness_scores):
        sorted_population = sorted(zip(population, fitness_scores), key=lambda x: x[1])
        ranks = range(1, len(sorted_population) + 1)
        total_rank = sum(ranks)
        probabilities = [rank / total_rank for rank in ranks]
        random_population = []
        for i in range(len(population) - self.elitism_count):
            selected_chromosome = random.choices(sorted_population, reversed(probabilities), k = 1)
            random_population.append(selected_chromosome[0][0])
        elite_chromosome =[]
        for i in range(self.elitism_count):
            elite_chromosome.append(sorted_population[i][0])
        return random_population, elite_chromosome


class Tournament_Selection:
    def __init__(self, elitism_count=2):
        self.elitism_count = elitism_count

    def process_selection(self, population, fitness_scores):
        sorted_population = sorted(zip(population, fitness_scores), key=lambda x: x[1])
        random_population = []
        for i in range(len(population) - self.elitism_count):
          selected_1 = random.randint(0, len(population) - 1 )
          selected_2 = random.randint(0, len(population) - 1)
          selected_3 = random.randint(0, len(population) - 1)
          selected_4 = random.randint(0, len(population) - 1)
          selected_5 = random.randint(0, len(population) - 1)

          Min = min( fitness_scores[selected_1], fitness_scores[selected_2], fitness_scores[selected_3])
          if ( fitness_scores[selected_1] == Min ): random_population.append(population[selected_1])
          elif ( fitness_scores[selected_2] == Min ): random_population.append(population[selected_2])
          elif ( fitness_scores[selected_3] == Min ): random_population.append(population[selected_3])
          elif ( fitness_scores[selected_4] == Min ): random_population.append(population[selected_4])
          elif ( fitness_scores[selected_5] == Min ): random_population.append(population[selected_5])

        elite_chromosome =[]
        # For elitism selection
        for i in range(self.elitism_count):
          elite_chromosome.append(sorted_population[i][0])
        return random_population, elite_chromosome
    