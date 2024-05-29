import pandas as pd

class SolutionNotFound(Exception):
    pass

class Solution:
    def __init__(self, dataset: pd.DataFrame, solution_name: str, concentration: float):
        self.solution_name = solution_name
        self.concentration = concentration
    
    def get_conductivity_of(self, data: pd.DataFrame, time):
        search_key = f'{self.solution_name} {self.concentration}g'
        time_key = f'time_{time}'

        if len(data[data['solution type'] == search_key]) == 0:
            print(self.solution_name)
            print(self.concentration)
            raise SolutionNotFound()

        return float(data[data['solution type'] == search_key].reset_index().iloc[0][time_key])