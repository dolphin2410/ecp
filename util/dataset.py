import pandas as pd
from .solution import Solution
from .temperature import TemperatureData
import math

class DataSet:
    # todo: more intuitive naming
    def __init__(self, solution_concentration_data: pd.DataFrame, temperature_data: pd.DataFrame):
        self.solution_concentration_data = solution_concentration_data
        self.temperature_data = temperature_data

    def time_solutions_max(self) -> int:
        list_times = []
        
        for solution in self.list_solutions():
            list_times.append(solution.time_len)
        
        return max(list_times)
    
    def list_solutions(self) -> list[Solution]:
        list_solution = []

        for solution_full_name in self.solution_concentration_data.iloc[:, 0]:
            solution_sliced = solution_full_name.split(" ")
            solution_concentration = float(solution_sliced[-1].split("g")[0])
            solution_name = " ".join(solution_sliced[:-1])
            list_solution.append(Solution(self.solution_concentration_data, solution_name, solution_concentration))
        
        return list_solution
    
    def list_temperature_data(self) -> list[TemperatureData]:
        list_temperature_data = []

        for index in range(int(len(self.temperature_data) / 2)):
            data_id = str(self.temperature_data.iloc[2 * index + 1]["temperature data"]).split("/")[1]
            list_temperature_data.append(TemperatureData(self.temperature_data, data_id))

        return list_temperature_data

    
    def group_solutions(self)-> dict[str, list[Solution]]:
        data = dict()
    
        for solution in self.list_solutions():
            if solution.solution_name in data:
                data[solution.solution_name].append(solution)
            else:
                data[solution.solution_name] = [solution]

        return data
    
    def concentration_resistance_data(self, time) -> tuple[list[str], list[list[float]], list[list[float]]]:
        map_solution_group = self.group_solutions()

        list_graph_solution_name = []
        list_graph_x = []
        list_graph_y = []

        for solution_group_name in map_solution_group:
            solution_group = map_solution_group[solution_group_name]
            graph_x: list[float] = [] # x axis = concentration
            graph_y: list[float] = [] # y axis = conductivity

            for solution in solution_group:
                currentInMA = solution.get_conductivity_of(time)
                if math.isnan(currentInMA):
                    continue
                graph_x.append(solution.concentration)
                graph_y.append(currentInMA)
            
            sort_map = list(range(len(graph_x)))
            sort_map.sort(key=lambda x: graph_x[x])

            if sort_map == None: 
                continue
            
            graph_x = list(map(lambda i: graph_x[i], sort_map))
            graph_y = list(map(lambda i: graph_y[i], sort_map))

            list_graph_x.append(graph_x)
            list_graph_y.append(graph_y)
            list_graph_solution_name.append(solution.solution_name)

        return (list_graph_solution_name, list_graph_x, list_graph_y)
    
    
    def temperature_resistance_data(self) -> tuple[list[str], list[list[float]], list[list[float]]]:
        """names, time, temperature, resistance"""

        temperature_data_names = []
        time_list_list = []
        resistance_list_list = []
        temperature_list_list = []

        for temperature_data in self.list_temperature_data():
            temperature_data_names.append(temperature_data.data_id)
            time_data, current_values, temperature_values = temperature_data.get_conductivity_data()
            
            time_list_list.append(time_data)
            temperature_list_list.append(temperature_values)
            resistance_list_list.append(list(map(lambda x: 5 / 0.001 / x, current_values)))

        return temperature_data_names, time_list_list, temperature_list_list, resistance_list_list
        
        