import util
from matplotlib import pyplot as plt
from util.dataset import DataSet

# Generate a list that has the time data [multiple of 5, 0 until 65]
def visualize_concentration_resistance(dataset: DataSet):
    time_range = util.generate_time_range(14)
    time_range.reverse()

    for time_index, time in enumerate(time_range):
        plt.figure(time_index)
        plt.xlabel("mass of solute [g]")
        plt.ylabel("resistance [ohm]")
        plt.title(f"R-C Graph, t={time}")

        list_solution_name, list_solution_x, list_solution_y = dataset.concentration_resistance_data(time)
        
        for solution_index, solution_name in enumerate(list_solution_name):
            plt.plot(list_solution_x[solution_index], list(map(lambda mA: util.APPLIED_VOLTAGE / mA / 0.001, list_solution_y[solution_index])), marker="D")

        plt.legend(list_solution_name)

    plt.show()