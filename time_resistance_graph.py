import math
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

APPLIED_VOLTAGE = 5

plt.title("Time Resistance Graph")

plt.xlabel = "time [s]"
plt.ylabel = "resistance [ohm]"

data = pd.read_csv("csvdataset.CSV")

for i in range(len(data)):
    solution_name = data.iloc[i, 0]
    solution_mA_data = []

    for time in ["time_" + str(5 * j) for j in range(14)]:
        solution_mA_data.append(data.iloc[i, :][time])

    solution_mA_data = list(filter(lambda x: not math.isnan(x), solution_mA_data))    

    if len(solution_mA_data) <= 0:
        continue

    initial_mA = solution_mA_data[0]
    final_mA = solution_mA_data[-1]
    delta_mA = final_mA - initial_mA

    solution_resistance_data = list(map(lambda mA: APPLIED_VOLTAGE / mA / 0.001, solution_mA_data))

    x_list = [5 * j for j in range(len(solution_resistance_data))]
    y_list = solution_resistance_data
    
    plt.scatter(x_list, y_list)
    
    print()

plt.show()