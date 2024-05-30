import pandas as pd
import util

class TemperatureDataNotFound(Exception):
    pass

class TemperatureData:
    def __init__(self, dataset: pd.DataFrame, data_id: str):
        self.dataset = dataset
        self.data_id = data_id
        self.time_len = len(self.dataset.iloc[0]) - 1
    
    def get_temperature_of(self, time):
        search_key = f'temperature/{self.data_id}'
        time_key = f'time_{time}'

        if len(self.dataset[self.dataset['temperature data'] == search_key]) == 0:
            print(self.data_id)
            raise TemperatureDataNotFound()

        return float(self.dataset[self.dataset['temperature data'] == search_key].reset_index().iloc[0][time_key])
    
    def get_conductivity_of(self, time):
        search_key = f'current/{self.data_id}'
        time_key = f'time_{time}'

        if len(self.dataset[self.dataset['temperature data'] == search_key]) == 0:
            print(self.data_id)
            raise TemperatureDataNotFound()

        return float(self.dataset[self.dataset['temperature data'] == search_key].reset_index().iloc[0][time_key])
    
    def get_conductivity_data(self) -> tuple[list[int], list[float], list[float]]:
        time_range = util.generate_time_range(self.time_len)

        solution_mA_data = []
        solution_temperature_data = []

        for time in time_range:
            solution_mA_data.append(self.get_conductivity_of(time))
            solution_temperature_data.append(self.get_temperature_of(time))
        
        return time_range, solution_mA_data, solution_temperature_data