import pandas as pd
import util
import math
import matplotlib.pyplot as plt
import graph_utils as crg

dataset = pd.read_csv("csvdataset.CSV")

concentration_list = [0.5, 1.0, 1.5, 2.0, 2.5]
solution_list = util.get_solution_names(dataset)

i = 0

time_range = util.generate_time_range(14)
time_range.reverse()

for time in time_range:
    i += 1
    plt.figure(i)
    plt.xlabel("mass of solute [g]")
    plt.ylabel("resistance [ohm]")
    plt.title(f"R-C Graph, t={time}")

    legend_list = []
    
    for solution in solution_list:
        data = []
        concentration_list = [0.5, 1.0, 1.5, 2.0, 2.5]
        to_remove = []
        for concentration in concentration_list:
            conductivity = crg.get_conductivity_of(solution, dataset, time, concentration)
            if conductivity == None:
                to_remove.insert(0, concentration_list.index(concentration))
                continue
            if not math.isnan(conductivity):
                data.append(conductivity)
        
        concentration_list = [concentration_list[i] for i in range(5) if to_remove.count(i) == 0]
        
        if len(data) != len(concentration_list):
            continue

        if len(data) == 0:
            continue

        plt.plot(concentration_list, list(map(lambda mA: util.APPLIED_VOLTAGE / mA / 0.001, data)), marker='D')
        legend_list.append(solution)

    plt.legend(legend_list)
plt.show()
