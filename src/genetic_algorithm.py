import random
import time


class GeneticAlgorithm:
    def __init__(self,
                 selection_operator,
                 crossover_operator,
                 mutation_operator,
                 population_size=200,
                 max_generations = 1000):
        self.selection_operator = selection_operator
        self.crossover_operator = crossover_operator
        self.mutation_operator = mutation_operator

        self.population_size = population_size
        self.max_generations = max_generations


    def initialize_population(self, num_tasks):
        population = []
        for _ in range(self.population_size):
            chromosome = list(range(num_tasks))
            random.shuffle(chromosome)

            population.append(chromosome)
        return population


    def fitness_function(self, chromosome, lookup_table, num_machines, alpha=0.95, beta=0.05):
        total_runtime = 0
        total_penalty = 0
        remaining_tasks = list(chromosome)
        machine_status = [0] * num_machines
        running_task = [-1] * num_machines

        while remaining_tasks:
            for machine in range(num_machines):
                if machine_status[machine] == 0:
                    for task in remaining_tasks:
                        dependencies, machine_id, task_duration, task_deadline, job_id, task_id = lookup_table[task]

                        if (machine_id != machine): continue
                        dependencies_done = all(
                          dep not in remaining_tasks and all(running_task[machine] != dep for machine in range(num_machines))
                          for dep in dependencies
                        )

                        if dependencies_done:
                            machine_status[machine] += task_duration
                            running_task[machine] = task
                            remaining_tasks.remove(task)

                            if ( total_runtime + task_duration > task_deadline ):
                              total_penalty += total_runtime + task_duration - task_deadline
                            break

            shortest_time = min(time for time in machine_status if time > 0)
            for i in range(num_machines):
                if machine_status[i] > 0:
                    machine_status[i] -= shortest_time

            total_runtime += shortest_time

            for i in range(num_machines):
                if machine_status[i] == 0 and running_task[i] != -1:
                    running_task[i] = -1

        total_runtime += max(time for time in machine_status if time >= 0)
        return alpha * total_runtime + beta * total_penalty


    def create_schedule(self, best_chromosome, lookup_table, num_machines):
        total_runtime = 0
        remaining_tasks = list(best_chromosome[0])
        machine_status = [0] * num_machines
        running_task = [-1] * num_machines
        schedule = []
        while remaining_tasks:
            for machine in range(num_machines):
                if machine_status[machine] == 0:
                    for task in remaining_tasks:
                        dependencies, machine_id, task_duration, task_deadline, job_id, task_id = lookup_table[task]

                        if (machine_id != machine): continue
                        dependencies_done = all(
                          dep not in remaining_tasks and all(running_task[machine] != dep for machine in range(num_machines))
                          for dep in dependencies
                        )

                        if dependencies_done:
                            machine_status[machine] += task_duration
                            running_task[machine] = task
                            schedule.append((job_id, task_id, machine_id, total_runtime, task_duration))
                            remaining_tasks.remove(task)
                            break

            shortest_time = min(time for time in machine_status if time > 0)
            for i in range(num_machines):
                if machine_status[i] > 0:
                    machine_status[i] -= shortest_time

            total_runtime += shortest_time

            for i in range(num_machines):
                if machine_status[i] == 0 and running_task[i] != -1:
                    running_task[i] = -1

        total_time =0
        for i in best_chromosome[0]:
          dependencies, machine_id, task_duration, task_deadline, job_id, task_id = lookup_table[i]
          total_time+=task_duration
        return schedule, total_time/num_machines


    def start_processing(self, num_tasks, num_machines, lookup_table, stop_threshold = 0.001, not_improve_gen = 0.05, print_out=True):
        population = self.initialize_population(num_tasks=num_tasks)
        best_fitness = float('inf')
        improvement_threshold = 0
        generation_not_sufficient = 0
        best_chromosome = []
        current_generation = 0

        # Added to store the searching history
        searching_history = {
            'best_fitness': [],
            'average_fitness': [],
            'schedule': [],
            'best_chromosome': [],
            'best_time': 0,
            'num_generations': 0,
            'searching_time': 0,
        }

        start_time = time.time()
        for generation in range(self.max_generations):
            current_generation = generation
            fitness_scores = [self.fitness_function(chromosome, lookup_table, num_machines) for chromosome in population]
            best_chromosome = min(zip(population, fitness_scores), key=lambda x: x[1])

            if best_chromosome[1] < best_fitness:
                improvement_threshold = 1 - (best_chromosome[1]/ best_fitness)
                best_fitness = best_chromosome[1]
            else:
                improvement_threshold = 0

            if improvement_threshold < stop_threshold:
                generation_not_sufficient +=1
            else:
                generation_not_sufficient = 0

            if generation_not_sufficient >= not_improve_gen * self.max_generations:
                break;

            selected_population, elite_chromosome = self.selection_operator.process_selection(population, fitness_scores)

            new_population = elite_chromosome
            for i in range(0, len(selected_population), 2):
                if i + 1 < len(selected_population):
                    parent1 = selected_population[i]
                    parent2 = selected_population[i + 1]

                    offspring1, offspring2 = self.crossover_operator.process_crossover(parent1, parent2)

                    self.mutation_operator.process_mutation(offspring1)
                    self.mutation_operator.process_mutation(offspring2)

                    new_population.extend([offspring1, offspring2])
                else:
                    new_population.append(selected_population[i])

            average_fitness_score = sum(fitness_scores) / len(fitness_scores) if fitness_scores else 0

            if print_out:
                print('------------------------------')
                print(f"Generation: {generation}")
                print(f"Best chromosome: {best_chromosome[0]}")
                print(f"Best fitness: {best_chromosome[1]}")
                print("Average Fitness Score:", average_fitness_score)

            searching_history['best_fitness'].append(best_chromosome[1])
            searching_history['average_fitness'].append(average_fitness_score)

            population = new_population

        end_time = time.time()
        searching_time = end_time - start_time
        schedule, best_time = self.create_schedule(best_chromosome, lookup_table, num_machines)

        searching_history['schedule'] = schedule
        searching_history['best_chromosome'] = best_chromosome
        searching_history['best_time'] = best_time
        searching_history['num_generations'] = current_generation
        searching_history['searching_time'] = searching_time

        return searching_history