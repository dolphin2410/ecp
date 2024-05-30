import pandas as pd
import util

class SolutionNotFound(Exception):
    pass

class Solution:
    def __init__(self, dataset: pd.DataFrame, solution_name: str, concentration: float):
        self.dataset = dataset
        self.solution_name = solution_name
        self.concentration = concentration
        self.time_len = len(self.dataset.iloc[0]) - 1
    
    def get_conductivity_of(self, time):
        search_key = f'{self.solution_name} {self.concentration}g'
        time_key = f'time_{time}'

        if len(self.dataset[self.dataset['solution type'] == search_key]) == 0:
            print(self.solution_name)
            print(self.concentration)
            raise SolutionNotFound()

        return float(self.dataset[self.dataset['solution type'] == search_key].reset_index().iloc[0][time_key])
    
    def get_conductivity_data(self):
        solution_mA_data = []
        for time in util.generate_time_range(self.time_len):
            solution_mA_data.append(self.get_conductivity_of(time))
        return solution_mA_data