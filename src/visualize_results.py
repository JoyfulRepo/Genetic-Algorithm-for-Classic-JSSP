from experiment import Experiment

if __name__ == '__main__':
    my_experiment = Experiment()

    # Load our searching history from json file
    my_experiment.load_history_from_json()

    # Set a suitable test_num
    #   The test_num ranges in [1, 100]
    test_num = 88

    # -----------------------------------------------------------------------------------------------
    # Method to plot the convergence of the best fitness scores in one specific test
    # By default: 
    #       Experiment().plot_best_fitnesses_in_test(test_num=test_num, save_plot=False)
    # To save the the plot
    #       -   Set: save_plot=True
    #       -   The plot will be saved in folder 'data/ExperimentResult/Plot/BestFitness'
    my_experiment.plot_best_fitnesses_in_test(test_num=test_num)
    # -----------------------------------------------------------------------------------------------

    
    # -----------------------------------------------------------------------------------------------
    # Method to plot the convergence of the average fitness scores in one specific test
    # By default: 
    #       Experiment().plot_average_fitnesses_in_test(test_num=test_num, save_plot=False)
    # To save the the plot
    #       -   Set: save_plot=True
    #       -   The plot will be saved in folder 'data/ExperimentResult/Plot/AverageFitness'
    my_experiment.plot_average_fitnesses_in_test(test_num=test_num, save_plot=True)
    # -----------------------------------------------------------------------------------------------


    # -----------------------------------------------------------------------------------------------
    # Method to show the searching results, including: 
    #       -   Final best fitness scores
    #       -   Best time
    #       -   Total Generation
    #       -   Searching time
    # By default:
    #       Experiment().show_searching_results_in_test(test_num=test_num)
    # Notice: 
    #       -   The results are shown in the table format in terminal. 
    #       -   This table cannot be saved, just for viewing only.
    my_experiment.show_searching_results_in_test(test_num=test_num)
    # -----------------------------------------------------------------------------------------------