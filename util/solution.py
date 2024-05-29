import pandas as pd
import util

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
    
    def get_conductivity_data(self, data: pd.DataFrame):
        solution_mA_data = []
        for time in util.generate_time_range(14):
            search_key = f'{self.solution_name} {self.concentration}g'
            time_key = f'time_{time}'
            if len(data[data['solution type'] == search_key]) == 0:
                print(self.solution_name)
                print(self.concentration)
                raise SolutionNotFound()

            solution_mA_data.append(float(data[data['solution type'] == search_key].reset_index().iloc[0][time_key]))
        return solution_mA_data