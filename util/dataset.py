import pandas as pd
from .solution import Solution
import math

class DataSet:
    # todo: more intuitive naming
    def __init__(self, pandas_data_1: pd.DataFrame, pandas_data_2: pd.DataFrame):
        self.pandas_data_1 = pandas_data_1
        self.pandas_data_2 = pandas_data_2
    
    def list_solutions(self) -> list[Solution]:
        list_solution = []

        for solution_full_name in self.pandas_data_1.iloc[:, 0]:
            solution_sliced = solution_full_name.split(" ")
            solution_concentration = float(solution_sliced[-1].split("g")[0])
            solution_name = " ".join(solution_sliced[:-1])
            list_solution.append(Solution(self.pandas_data_1, solution_name, solution_concentration))
        
        return list_solution
    
    def group_solutions(self):
        data: dict[str, list[Solution]] = dict()
    
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
    
    def temperature_resistance_data(self, time_list) -> tuple[list[float], list[float]]:
        return list(map(lambda x: self.pandas_data_2.iloc[0, 1:][f'time_{x}'], time_list)), list(map(lambda x: self.pandas_data_2.iloc[1, 1:][f'time_{x}'], time_list))
        
        