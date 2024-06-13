import util
from matplotlib import pyplot as plt
from util.dataset import DataSet
import pandas as pd
import math
from util.compound_data import CompoundData

def visualize_time_resistance_concentration(dataset: DataSet):
    time_range = util.generate_time_range(dataset.time_solutions_max())

    solution_group_map = dataset.group_solutions()
    
    for solution_index, solution_name in enumerate(solution_group_map):
        if solution_index % 4 == 0:
            plt.figure(solution_index // 4)

        subplot_index = 4 if (solution_index + 1) % 4 == 0 else (solution_index + 1) % 4

        plt.subplot(2, 2, subplot_index)

        plt.xlabel(f"time [s]\n({chr(97 + solution_index)})")
        plt.ylabel("resistance [ohm]")
        plt.title(f"Resistance-Time Graph, solution={solution_name}")
        solution_group = solution_group_map[solution_name]

        legend_list = []

        for solution in solution_group:
            conductivity_data = solution.get_conductivity_data()
            resistance_data = list(map(util.mAToOhm, conductivity_data))
            plt.plot(time_range, resistance_data, marker="o", markersize=2)
            legend_list.append(solution.concentration)
        
        plt.legend(legend_list, prop={'size': 8})
        plt.ylim(bottom=0, top=100)
        plt.xlim(right=80)

        plt.subplots_adjust(hspace=0.5)
    plt.show()

def visualize_temp(dataset_trainable: DataSet, dataset_dictionary: pd.DataFrame):
    plt.xlabel("temp")
    plt.ylabel("resistance [ohm]")

    solution_groups = dataset_trainable.group_solutions()

    list_solution_name = []
    for solution_name in solution_groups:
        print(solution_name)
        compound_data = CompoundData(dataset_dictionary, solution_name)
        
        list_solution_name.append(solution_name)

        list_x = []
        list_y = []
        for solution in solution_groups[solution_name]:
            IMC = compound_data.get_ionization_concentration(compound_data.from_grams_to_molar_conductivity(solution.concentration))
            CHARGE = compound_data.get_ion_charge()
            MASS = compound_data.get_ion_mass()
            list_x.append(IMC[0] * IMC[1])
            list_y.append(solution.get_averaged_conductivity())
        print(IMC[0] * IMC[1])
        plt.plot(list_x, list_y)

        # print("CONDUCTIVITY = ", end="")
        # print(solution_groups[solution_name][0].get_conductivity_of(0))
        # print("ION_NUM = ", end="")
        # print(compound_data.get_ion_num())
        # print("ION_CHARGE = ", end="")
        # print(compound_data.get_ion_charge())
        # print("ION_MASS = ", end="")
        # print(compound_data.get_ion_mass())
        # print("IONIZATION_MOLAR_CONCENTRATION = ", end="")
        # print(IMC)
        # print("--------")

    plt.legend(list_solution_name)
    plt.ylim(bottom=0)
    plt.show()


# Generate a list that has the time data [multiple of 5, 0 until 65]
def visualize_concentration_resistance(dataset: DataSet):
    time_range = util.generate_time_range(dataset.time_solutions_max())
    time_range.reverse()

    for time_index, time in enumerate(time_range):
        plt.figure(time_index)
        plt.xlabel("mass of solute [g]")
        plt.ylabel("resistance [ohm]")
        plt.title(f"Resistance-Concentration Graph, t={time}")

        list_solution_name, list_solution_x, list_solution_y = dataset.concentration_resistance_data(time)
        
        for solution_index in range(len(list_solution_name)):
            plt.plot(list_solution_x[solution_index], list(map(lambda mA: util.APPLIED_VOLTAGE / mA / 0.001, list_solution_y[solution_index])), marker="o", markersize=2)

        plt.legend(list_solution_name)
        plt.ylim(bottom=0)

    plt.show()

def visualize_temperature_resistance(dataset: DataSet):
    plt.xlabel("temperature [°C]")
    plt.ylabel("resistance [ohm]")
    plt.title(f"Resistance-Temperature Graph, NaHCO3")

        # todo: a more intuitive naming
    list_names, list_time, list_temperature, list_resistance = dataset.temperature_resistance_data()

    for temperature_data_index in range(len(list_names)):
        plt.plot(list_temperature[temperature_data_index], list_resistance[temperature_data_index], marker="o", markersize=2)

    plt.legend(list_names)
    plt.ylim(bottom=0)

    plt.show()

def visualize_time_resistance_temperature(dataset: DataSet):
    plt.xlabel("time [s]")
    plt.ylabel("resistance [ohm]")
    plt.title(f"Resistance-Time Graph, NaHCO3")

    list_names, list_time, list_temperature, list_resistance = dataset.temperature_resistance_data()

    for temperature_data_index in range(len(list_names)):
        plt.plot(list_time[temperature_data_index], list_resistance[temperature_data_index], marker="o", markersize=2)

    plt.legend(list_names)
    plt.ylim(bottom=0)
    plt.show()

