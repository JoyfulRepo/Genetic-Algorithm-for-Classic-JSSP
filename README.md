# Genetic-Algorithm-for-Classic-JSSP

Welcome! This is a repository about experimenting 8 Genetic Algorithms in solving Classic JSSP.

## I - PROJECT INFORMATION

### 1. VARIANCES OF GENETIC ALGORITHM
This project has examined ***8 combinations*** of Genetic Algorithms in total:
- GA 01: Rank Selection + PMX Crossover + Inversion Mutation
- GA 02: Rank Selection + PMX Crossover + Scramble Mutation
- GA 03: Rank Selection + Order Crossover + Inversion Mutation
- GA 04: Rank Selection + Order Crossover + Scramble Mutation
- GA 05: Tournament Selection + PMX Crossover + Inversion Mutation
- GA 06: Tournament Selection + PMX Crossover + Scramble Mutation
- GA 07: Tournament Selection + Order Crossover + Inversion Mutation
- GA 08: Tournament Selection + Order Crossover + Scramble Mutation

### 2. EXPERIMENT INFORMATION
In this project, there are ***100 separate experiements*** that have been done in total:
- Experiment 1 -> 2: 2 jobs
- Experiment 3 -> 5: 3 jobs
- Experiment 6 -> 10: 5 jobs
- Experiment 11 - 40: 10 jobs
- Experiment 41 - 70: 20 jobs
- Experiment 71 - 100: 30 jobs

## II - USAGE GUIDE

### 1. SETTING UP THE REPOSITORY LOCALLY

Clone this repository locally. Make sure the environment satisfies the **`requirements.txt`**


### 2. HOW TO USE
#### 2.1. USE OUR RESULTS
Move to the file **`src/visualize_results.py`**

**Step 1: Create new experiment**
```
new_experiment = Experiment()
```

**Step 2: Load our searching history**

All the 100 tests above have already been executed successfully, the result of these tests are stored in `data\ExperimentResult\experiment_history.json`. We now need to load the history only for use.


The class Experiment has the method to load the experiment history from json file as given:

```
Experiment().load_history_from_json()
```

**Step 3: Visualize our results. Methods for visualizing the results are given.** 

In all three methods below, the variable `test_num` must be given with a appropriate value. The range of this variable is [1, 100].

- **Plotting the convergence of best fitness scores**

Class Experiment has the method for plotting the convergence of best fitness scores as given below.

**Notice:** The parameter `save_plot` is set to `False` by default, meaning that the plot is only for visuallizing. In order to save the image, change the setting to `save_plot=True`. The plot is saved at the folder `data/ExperimentResult/Plot/BestFitness`

```
Experiment().plot_best_fitnesses_in_test(test_num, save_plot=False)
```

- **Plotting the convergence of average fitness scores**

Class Experiment has the method for plotting the convergence of average fitness scores*** as given below.

**Notice:** The parameter `save_plot` is set to `False` by default, meaning that the plot is only for visuallizing. In order to save the image, change the setting to `save_plot=True`.

```
Experiment().plot_average_fitnesses_in_test(test_num, save_plot=False)
```

- **Showing the searching results**

Class Experiment has a method to show the searching resutls as given:

The searching results including:
- Solver: The combination used to solve.
- Best fitness: The best fitness score of the last generation before the algorithm is terminated.
- Best time: The finally best time of the problem.
- Total generation: The number of generation that the GA needs to achieve that best fitness score.
- Searching time: Total runtime of GA to achieve the best fitness score.

Class Experiment has a method to show the searching resutls as given:

```
Experiment().show_searching_results_in_test(test_num)
```

**Notice:** This table is for viewing only and can not be saved.

#### 2.2. START YOUR OWN SEARCHING
Move to the file **`src/run_experiment.py`**

The class Experiment has already bene implemented with a searching loop for this purpose. The method is given:
```
Experiment().start_experiment(print_out=False, save_history=False)
```

Paramenters explanation:
- To see the whole searching information, kindly set the `print_out=True`. If not, it will just print out the checkpoint of the searching process.
- If you want to save your searching history, please set `save_history=True`. 

**Notice**: Once the `save_history=True` is set, all of your searching history will be saved in the same file as our results (which is the file `data/ExperimentResult/experiment_history.json`). This means that your results will override my results and that when you start to visualize the results in this file, you actually visualize your result.

For testing only, you can use the methods for visualizing your results after executing `start_experiment()` the need of setting `save_history=True`.

