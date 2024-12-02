from genetic_algorithm import GeneticAlgorithm

import random
import json


class JSSP:
    def __init__(self,
                 solver:GeneticAlgorithm,
                 num_jobs=30,
                 max_task_per_job=10,
                 num_machines=4,
                 max_hour_per_task=6):
        self.solver = solver
        self.num_jobs = num_jobs
        self.max_task_per_job = max_task_per_job
        self.num_machines = num_machines
        self.max_hour_per_task = max_hour_per_task

        self.jobs = []
        self.num_task = 0
        self.lookup_table = []

    def generate_random_jobs(self, save_path=''):
        print(f'-----Generating random jobs-----')
        print(f'Num Jobs: {self.num_jobs} | Num Machines: {self.num_machines}')
        print(f'Max task per job: {self.max_task_per_job}')
        print(f'Max duration per task: {self.max_hour_per_task}')

        created_jobs = []
        total_tasks = 0
        for job_id in range(1, self.num_jobs + 1):
            num_tasks = random.randint(1, self.max_task_per_job)

            total_tasks += num_tasks
            tasks = []

            for task_num in range(1, num_tasks + 1):
                task_id = f'T{task_num}'
                machine_id = random.randint(0, self.num_machines - 1)
                task_duration = random.randint(1, self.max_hour_per_task)
                task_deadline = random.randint(int(num_tasks * self.max_hour_per_task / 2), num_tasks * self.max_hour_per_task)

                dependencies = random.sample(
                    [f'T{i}' for i in range(1, task_num)],
                    random.randint(0, min(2, task_num - 1))
                )

                tasks.append({
                    'task_id': task_id,
                    'machine_id': machine_id,
                    'dependencies': dependencies,
                    'task_duration': task_duration,
                    'task_deadline': task_deadline
                })

            created_jobs.append({
                'job_id': job_id,
                'tasks': tasks
            })

        self.jobs = created_jobs
        self.num_task = total_tasks
        print(f'Generated random jobs ({self.num_task} tasks) successfully.')

        jssp_info = {
            'num_jobs': self.num_jobs,
            'num_task': total_tasks,
            'max_task_per_job': self.max_task_per_job,
            'num_machines': self.num_machines,
            'max_hour_per_task': self.max_hour_per_task,
            'jobs': created_jobs
        }

        if save_path != '':
            with open(save_path, 'w') as json_file:
                json.dump(jssp_info, json_file, indent=4)

            print(f'Successfully save the job at {save_path}')


    def load_info_from_json(self, jssp_info_path, print_out=True):
        self.num_jobs = 0
        self.max_task_per_job = 0
        self.num_machines = 0
        self.max_hour_per_task = 0

        self.jobs = []
        self.num_task = 0

        jssp_info = {}
        with open(jssp_info_path, 'r') as json_file:
            jssp_info = json.load(json_file)

        self.num_jobs = jssp_info['num_jobs']
        self.max_task_per_job = jssp_info['max_task_per_job']
        self.num_machines = jssp_info['num_machines']
        self.max_hour_per_task = jssp_info['max_hour_per_task']

        self.jobs = jssp_info['jobs']
        self.num_task = jssp_info['num_task']

        if print_out:
            print(f'----------Loading JSSP info from {jssp_info_path}----------')
            print(f'Num Jobs: {self.num_jobs}')
            print(f'Num Tasks: {self.num_task}')
            print(f'Num Machines: {self.num_machines}')
            print(f'Max task per job: {self.max_task_per_job}')
            print(f'Max hour per task: {self.max_hour_per_task}')
            print(f'Load JSSP info successfully.')
        else:
            print(f'Loading JSSP info from {jssp_info_path} successfully')


    def assign_task_id(self):
        """
            Assigns unique integer IDs to tasks and creates a dependency list (lookup table).
            Returns lookup_table where each index is a task ID and lists its dependencies and machine ID
        """
        created_lookup_table = []
        task_id_map = {}
        current_id = 0

        # Assign unique ID to each task in each job
        for job in self.jobs:
            for task in job['tasks']:
                task_id_map[(job['job_id'], task['task_id'])] = current_id
                current_id += 1

        for job in self.jobs:
            for task in job['tasks']:
                task_id = task_id_map[(job['job_id'], task['task_id'])]
                dependencies = [
                    task_id_map[(job['job_id'], dep)] for dep in task['dependencies']
                ]
                machine_id = task['machine_id']
                task_duration = task['task_duration']
                task_deadline = task['task_deadline']
                job_id = job['job_id']
                task_id = task['task_id']
                created_lookup_table.append((dependencies, machine_id, task_duration, task_deadline, job_id, task_id))

        self.lookup_table = created_lookup_table


    def solve(self, print_out=True):
        searching_history = self.solver.start_processing(num_tasks=self.num_task,
                                                         num_machines=self.num_machines,
                                                         lookup_table=self.lookup_table,
                                                         print_out=print_out)
        return searching_history


    def run_generated_test(self, job_data_save_path):
        self.generate_random_jobs(save_path=job_data_save_path)
        self.assign_task_id()
        searching_history = self.solve()
        print(f'\n----------Testing done----------')
        print(f'Searching history:  {searching_history}')
        print(f'Schedule')


    def run_existed_test(self, job_data_save_path):
        self.load_info_from_json(jssp_info_path=job_data_save_path)
        self.assign_task_id()
        searching_history = self.solve()
        print(f'\n----------Testing done----------')
        print(f'Searching history:  {searching_history}')
        print(f'Schedule')
