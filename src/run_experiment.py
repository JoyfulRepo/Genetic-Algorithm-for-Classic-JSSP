from experiment import Experiment


if __name__ == "__main__":
    my_experiment = Experiment()
    my_experiment.start_experiment(save_history=False) # Because our searching history is saved already.