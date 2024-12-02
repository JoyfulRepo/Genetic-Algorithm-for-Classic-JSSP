from selection_operators import Rank_Selection, Tournament_Selection
from crossover_operators import PMX_Crossover, Order_Crossover
from mutation_operators import Inversion_Mutation, Scramble_Mutation
from genetic_algorithm import GeneticAlgorithm
from JSSP import JSSP

import natsort
from tabulate import tabulate
import matplotlib.pyplot as plt
import json
import os

class Experiment:
    def __init__(self,
                 jssp_01=JSSP(solver=GeneticAlgorithm(selection_operator=Rank_Selection(),      # First given best GA (Rank + PMX + Inversion)
                                                      crossover_operator=PMX_Crossover(),
                                                      mutation_operator=Inversion_Mutation())),
                 jssp_02=JSSP(solver=GeneticAlgorithm(selection_operator=Rank_Selection(),
                                                      crossover_operator=PMX_Crossover(),
                                                      mutation_operator=Scramble_Mutation())),
                 jssp_03=JSSP(solver=GeneticAlgorithm(selection_operator=Rank_Selection(),
                                                      crossover_operator=Order_Crossover(),
                                                      mutation_operator=Inversion_Mutation())),
                 jssp_04=JSSP(solver=GeneticAlgorithm(selection_operator=Rank_Selection(),
                                                      crossover_operator=Order_Crossover(),
                                                      mutation_operator=Scramble_Mutation())),
                 jssp_05=JSSP(solver=GeneticAlgorithm(selection_operator=Tournament_Selection(),
                                                      crossover_operator=PMX_Crossover(),
                                                      mutation_operator=Inversion_Mutation())),
                 jssp_06=JSSP(solver=GeneticAlgorithm(selection_operator=Tournament_Selection(),
                                                      crossover_operator=PMX_Crossover(),
                                                      mutation_operator=Scramble_Mutation())),
                 jssp_07=JSSP(solver=GeneticAlgorithm(selection_operator=Tournament_Selection(),
                                                      crossover_operator=Order_Crossover(),
                                                      mutation_operator=Inversion_Mutation())),
                 jssp_08=JSSP(solver=GeneticAlgorithm(selection_operator=Tournament_Selection(),
                                                      crossover_operator=Order_Crossover(),
                                                      mutation_operator=Scramble_Mutation())),
                 data_path='Data/Experiment',
                 result_path='Data/ExperimentResult'):


        self.jssp_01 = jssp_01
        self.jssp_02 = jssp_02
        self.jssp_03 = jssp_03
        self.jssp_04 = jssp_04
        self.jssp_05 = jssp_05
        self.jssp_06 = jssp_06
        self.jssp_07 = jssp_07
        self.jssp_08 = jssp_08

        self.data_path = data_path
        self.result_path = result_path

        self.jssp_info_experimental_files = [f'{self.data_path}/{f}'
                                     for f in os.listdir(self.data_path)
                                     if os.path.isfile(os.path.join(self.data_path, f))]
        self.num_test = len(self.jssp_info_experimental_files)

        self.experiment_history = {
            'jssp_01': [],
            'jssp_02': [],
            'jssp_03': [],
            'jssp_04': [],
            'jssp_05': [],
            'jssp_06': [],
            'jssp_07': [],
            'jssp_08': [],
        }

        self.experiment_result_plot_path = f'{self.result_path}/Plot'


    def start_experiment(self, print_out=False, save_history=False):
        for exp_num, file in enumerate(natsort.natsorted(self.jssp_info_experimental_files)):
            print(f'>>>>>>>>>>>>>>>>>>>>Test {exp_num + 1:03}<<<<<<<<<<<<<<<<<<<<')

            print(f'..........JSSP_01..........')
            self.jssp_01.load_info_from_json(file, print_out=print_out)
            self.jssp_01.assign_task_id()
            print(f'Assign task id successfully')
            searching_history_01 = self.jssp_01.solve(print_out=print_out)
            print(f'Finishing solving')
            self.experiment_history['jssp_01'].append(searching_history_01)
            print(f'Finish storing searching history')
            print(f'Done')

            print(f'..........JSSP_02..........')
            self.jssp_02.load_info_from_json(file, print_out=print_out)
            self.jssp_02.assign_task_id()
            print(f'Assign task id successfully')
            searching_history_02 = self.jssp_02.solve(print_out=print_out)
            print(f'Finishing solving')
            self.experiment_history['jssp_02'].append(searching_history_02)
            print(f'Finish storing searching history')
            print(f'Done')

            print(f'..........JSSP_03..........')
            self.jssp_03.load_info_from_json(file, print_out=print_out)
            self.jssp_03.assign_task_id()
            print(f'Assign task id successfully')
            searching_history_03 = self.jssp_03.solve(print_out=print_out)
            print(f'Finishing solving')
            self.experiment_history['jssp_03'].append(searching_history_03)
            print(f'Finish storing searching history')
            print(f'Done')

            print(f'..........JSSP_04..........')
            self.jssp_04.load_info_from_json(file, print_out=print_out)
            self.jssp_04.assign_task_id()
            print(f'Assign task id successfully')
            searching_history_04 = self.jssp_04.solve(print_out=print_out)
            print(f'Finishing solving')
            self.experiment_history['jssp_04'].append(searching_history_04)
            print(f'Finish storing searching history')
            print(f'Done')

            print(f'..........JSSP_05..........')
            self.jssp_05.load_info_from_json(file, print_out=print_out)
            self.jssp_05.assign_task_id()
            print(f'Assign task id successfully')
            searching_history_05 = self.jssp_05.solve(print_out=print_out)
            print(f'Finishing solving')
            self.experiment_history['jssp_05'].append(searching_history_05)
            print(f'Finish storing searching history')
            print(f'Done')

            print(f'..........JSSP_06..........')
            self.jssp_06.load_info_from_json(file, print_out=print_out)
            self.jssp_06.assign_task_id()
            print(f'Assign task id successfully')
            searching_history_06 = self.jssp_06.solve(print_out=print_out)
            print(f'Finishing solving')
            self.experiment_history['jssp_06'].append(searching_history_06)
            print(f'Finish storing searching history')
            print(f'Done')

            print(f'..........JSSP_07..........')
            self.jssp_07.load_info_from_json(file, print_out=print_out)
            self.jssp_07.assign_task_id()
            print(f'Assign task id successfully')
            searching_history_07 = self.jssp_07.solve(print_out=print_out)
            print(f'Finishing solving')
            self.experiment_history['jssp_07'].append(searching_history_07)
            print(f'Finish storing searching history')
            print(f'Done')

            print(f'..........JSSP_08..........')
            self.jssp_08.load_info_from_json(file, print_out=print_out)
            self.jssp_08.assign_task_id()
            print(f'Assign task id successfully')
            searching_history_08 = self.jssp_08.solve(print_out=print_out)
            print(f'Finishing solving')
            self.experiment_history['jssp_08'].append(searching_history_08)
            print(f'Finish storing searching history')
            print(f'Done')

            print(f'-----Finish test {exp_num + 1:03}th-----')

        print(f'[[[[[[[[[[ Finish all {len(self.jssp_info_experimental_files)} experiments ]]]]]]]]]]')
        if save_history:
            save_path = f'{self.result_path}/experiment_history.json'
            with open(save_path, 'w') as json_file:
                json.dump(self.experiment_history, json_file, indent=4)

            print(f'Successfully save the experiment history at {save_path}')



    def plot_best_fitnesses_in_test(self, test_num, save_plot=False):
        if test_num not in range(1, len(self.jssp_info_experimental_files) + 1):
            print(f'The test number is not suitable.')
            return

        experiment_history = {}
        experiment_history_path = f'{self.result_path}/experiment_history.json'
        with open(experiment_history_path, 'r') as json_file:
            experiment_history = json.load(json_file)

        jssp_01_best_fitness = experiment_history['jssp_01'][test_num - 1]['best_fitness']
        jssp_02_best_fitness = experiment_history['jssp_02'][test_num - 1]['best_fitness']
        jssp_03_best_fitness = experiment_history['jssp_03'][test_num - 1]['best_fitness']
        jssp_04_best_fitness = experiment_history['jssp_04'][test_num - 1]['best_fitness']
        jssp_05_best_fitness = experiment_history['jssp_05'][test_num - 1]['best_fitness']
        jssp_06_best_fitness = experiment_history['jssp_06'][test_num - 1]['best_fitness']
        jssp_07_best_fitness = experiment_history['jssp_07'][test_num - 1]['best_fitness']
        jssp_08_best_fitness = experiment_history['jssp_08'][test_num - 1]['best_fitness']

        plt.figure(figsize=(15, 9))

        plt.plot(range(len(jssp_01_best_fitness)), jssp_01_best_fitness, label='Solver 01', color='b')
        plt.plot(range(len(jssp_02_best_fitness)), jssp_02_best_fitness, label='Solver 02', color='g')
        plt.plot(range(len(jssp_03_best_fitness)), jssp_03_best_fitness, label='Solver 03', color='r')
        plt.plot(range(len(jssp_04_best_fitness)), jssp_04_best_fitness, label='Solver 04', color='c')
        plt.plot(range(len(jssp_05_best_fitness)), jssp_05_best_fitness, label='Solver 05', color='m')
        plt.plot(range(len(jssp_06_best_fitness)), jssp_06_best_fitness, label='Solver 06', color='y')
        plt.plot(range(len(jssp_07_best_fitness)), jssp_07_best_fitness, label='Solver 07', color='k')
        plt.plot(range(len(jssp_08_best_fitness)), jssp_08_best_fitness, label='Solver 08', color='#FFA500')

        # Add labels and legend
        plt.xlabel("Generation number")
        plt.ylabel("Best fitness score")
        plt.legend()

        if save_plot:
            save_path = f'{self.experiment_result_plot_path}/BestFitness/Test_{test_num:03}_best_fitness_plot.png'
            plt.savefig(save_path, format="png", dpi=300)
            print(f'This plot is saved at {save_path}')

        plt.show()


    def plot_average_fitnesses_in_test(self, test_num, save_plot=False):
        if test_num not in range(1, len(self.jssp_info_experimental_files) + 1):
            print(f'The test number is not suitable.')
            return

        experiment_history = {}
        experiment_history_path = f'{self.result_path}/experiment_history.json'
        with open(experiment_history_path, 'r') as json_file:
            experiment_history = json.load(json_file)

        jssp_01_average_fitness = experiment_history['jssp_01'][test_num - 1]['average_fitness']
        jssp_02_average_fitness = experiment_history['jssp_02'][test_num - 1]['average_fitness']
        jssp_03_average_fitness = experiment_history['jssp_03'][test_num - 1]['average_fitness']
        jssp_04_average_fitness = experiment_history['jssp_04'][test_num - 1]['average_fitness']
        jssp_05_average_fitness = experiment_history['jssp_05'][test_num - 1]['average_fitness']
        jssp_06_average_fitness = experiment_history['jssp_06'][test_num - 1]['average_fitness']
        jssp_07_average_fitness = experiment_history['jssp_07'][test_num - 1]['average_fitness']
        jssp_08_average_fitness = experiment_history['jssp_08'][test_num - 1]['average_fitness']

        plt.figure(figsize=(15, 9))

        plt.plot(range(len(jssp_01_average_fitness)), jssp_01_average_fitness, label='Solver 01', color='b')
        plt.plot(range(len(jssp_02_average_fitness)), jssp_02_average_fitness, label='Solver 02', color='g')
        plt.plot(range(len(jssp_03_average_fitness)), jssp_03_average_fitness, label='Solver 03', color='r')
        plt.plot(range(len(jssp_04_average_fitness)), jssp_04_average_fitness, label='Solver 04', color='c')
        plt.plot(range(len(jssp_05_average_fitness)), jssp_05_average_fitness, label='Solver 05', color='m')
        plt.plot(range(len(jssp_06_average_fitness)), jssp_06_average_fitness, label='Solver 06', color='y')
        plt.plot(range(len(jssp_07_average_fitness)), jssp_07_average_fitness, label='Solver 07', color='k')
        plt.plot(range(len(jssp_08_average_fitness)), jssp_08_average_fitness, label='Solver 08', color='#FFA500')

        # Add labels and legend
        plt.xlabel("Generation number")
        plt.ylabel("Average fitness score")
        plt.legend()

        if save_plot:
            save_path = f'{self.experiment_result_plot_path}/AverageFitness/Test_{test_num:03}_average_fitness_plot.png'
            plt.savefig(save_path, format="png", dpi=300)
            print(f'This plot is saved at {save_path}')

        plt.show()

    def show_searching_results_in_test(self, test_num):
        if test_num not in range(1, len(self.jssp_info_experimental_files) + 1):
            print(f'The test number is not suitable.')
            return

        experiment_history = {}
        experiment_history_path = f'{self.result_path}/experiment_history.json'
        with open(experiment_history_path, 'r') as json_file:
            experiment_history = json.load(json_file)

        headers = ["Solver", "Best fitness", "Best time", "Total Generation", "Searching Time"]

        print(len(experiment_history['jssp_01']))

        jssp_01_results = []
        jssp_01_results.append("JSSP_01.solver")
        jssp_01_results.append(experiment_history['jssp_01'][test_num - 1]['best_chromosome'][1])
        jssp_01_results.append(experiment_history['jssp_01'][test_num - 1]['best_time'])
        jssp_01_results.append(experiment_history['jssp_01'][test_num - 1]['num_generations'])
        jssp_01_results.append(experiment_history['jssp_01'][test_num - 1]['searching_time'])

        jssp_02_results = []
        jssp_02_results.append("JSSP_02.solver")
        jssp_02_results.append(experiment_history['jssp_02'][test_num - 1]['best_chromosome'][1])
        jssp_02_results.append(experiment_history['jssp_02'][test_num - 1]['best_time'])
        jssp_02_results.append(experiment_history['jssp_02'][test_num - 1]['num_generations'])
        jssp_02_results.append(experiment_history['jssp_02'][test_num - 1]['searching_time'])

        jssp_03_results = []
        jssp_03_results.append("JSSP_03.solver")
        jssp_03_results.append(experiment_history['jssp_03'][test_num - 1]['best_chromosome'][1])
        jssp_03_results.append(experiment_history['jssp_03'][test_num - 1]['best_time'])
        jssp_03_results.append(experiment_history['jssp_03'][test_num - 1]['num_generations'])
        jssp_03_results.append(experiment_history['jssp_03'][test_num - 1]['searching_time'])

        jssp_04_results = []
        jssp_04_results.append("JSSP_04.solver")
        jssp_04_results.append(experiment_history['jssp_04'][test_num - 1]['best_chromosome'][1])
        jssp_04_results.append(experiment_history['jssp_04'][test_num - 1]['best_time'])
        jssp_04_results.append(experiment_history['jssp_04'][test_num - 1]['num_generations'])
        jssp_04_results.append(experiment_history['jssp_04'][test_num - 1]['searching_time'])

        jssp_05_results = []
        jssp_05_results.append("JSSP_05.solver")
        jssp_05_results.append(experiment_history['jssp_05'][test_num - 1]['best_chromosome'][1])
        jssp_05_results.append(experiment_history['jssp_05'][test_num - 1]['best_time'])
        jssp_05_results.append(experiment_history['jssp_05'][test_num - 1]['num_generations'])
        jssp_05_results.append(experiment_history['jssp_05'][test_num - 1]['searching_time'])

        jssp_06_results = []
        jssp_06_results.append("JSSP_06.solver")
        jssp_06_results.append(experiment_history['jssp_06'][test_num - 1]['best_chromosome'][1])
        jssp_06_results.append(experiment_history['jssp_06'][test_num - 1]['best_time'])
        jssp_06_results.append(experiment_history['jssp_06'][test_num - 1]['num_generations'])
        jssp_06_results.append(experiment_history['jssp_06'][test_num - 1]['searching_time'])

        jssp_07_results = []
        jssp_07_results.append("JSSP_07.solver")
        jssp_07_results.append(experiment_history['jssp_07'][test_num - 1]['best_chromosome'][1])
        jssp_07_results.append(experiment_history['jssp_07'][test_num - 1]['best_time'])
        jssp_07_results.append(experiment_history['jssp_07'][test_num - 1]['num_generations'])
        jssp_07_results.append(experiment_history['jssp_07'][test_num - 1]['searching_time'])

        jssp_08_results = []
        jssp_08_results.append("JSSP_08.solver")
        jssp_08_results.append(experiment_history['jssp_08'][test_num - 1]['best_chromosome'][1])
        jssp_08_results.append(experiment_history['jssp_08'][test_num - 1]['best_time'])
        jssp_08_results.append(experiment_history['jssp_08'][test_num - 1]['num_generations'])
        jssp_08_results.append(experiment_history['jssp_08'][test_num - 1]['searching_time'])

        data = []
        data.append(jssp_01_results)
        data.append(jssp_02_results)
        data.append(jssp_03_results)
        data.append(jssp_04_results)
        data.append(jssp_05_results)
        data.append(jssp_06_results)
        data.append(jssp_07_results)
        data.append(jssp_08_results)
        print(f'Searching results of test {test_num:03}')
        print(tabulate(data, headers=headers, tablefmt="grid"))


    def demo_one_test(self, save_history=True):
        file = self.jssp_info_experimental_files[45]

        self.jssp_01.load_info_from_json(file, print_out=False)
        self.jssp_02.load_info_from_json(file, print_out=False)
        self.jssp_03.load_info_from_json(file, print_out=False)

        self.jssp_01.assign_task_id()
        self.jssp_02.assign_task_id()
        self.jssp_03.assign_task_id()

        searching_history_01 = self.jssp_01.solve(print_out=False)
        print(f'JSSP_01 - Finishing solving')

        searching_history_02 = self.jssp_02.solve(print_out=False)
        print(f'JSSP_02 - Finishing solving')

        searching_history_03 = self.jssp_03.solve(print_out=False)
        print(f'JSSP_03 - Finishing solving')

        self.experiment_history['jssp_01'].append(searching_history_01)
        self.experiment_history['jssp_02'].append(searching_history_02)
        self.experiment_history['jssp_03'].append(searching_history_03)

        if save_history:
            save_path = f'{self.result_path}/experiment_history.json'
            with open(save_path, 'w') as json_file:
                json.dump(self.experiment_history, json_file, indent=4)

            print(f'Successfully save the history at {save_path}')


    def load_history_from_json(self):
        self.experiment_history = {}
        experiment_history_path = f'{self.result_path}/experiment_history.json'
        with open(experiment_history_path, 'r') as json_file:
            self.experiment_history = json.load(json_file)

        print(f'Load history from {experiment_history_path} successfully.')
