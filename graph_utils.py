import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

APPLIED_VOLTAGE = 5

plot = plt.title("Concentration Resistance Graph")

data = pd.read_csv("csvdataset.CSV")

def generate_time_range(n):
    return [5 * j for j in range(n)]

def get_solution_names(data: pd.DataFrame):
    return list(set(map(lambda x: " ".join(x.split(" ")[:-1]), data.iloc[:, 0])))

solution_list = get_solution_names(data)

def get_conductivity_of(solution_name: str, data: pd.DataFrame, time, concentration):
    search_key = f'{solution_name} {concentration}g'
    time_key = f'time_{time}'

    if len(data[data['solution type'] == search_key]) == 0:
        return None

    return data[data['solution type'] == search_key].reset_index().iloc[0][time_key]