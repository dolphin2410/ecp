import pandas as pd
from util.dataset import DataSet
import visualizer

# Generate a dataset instance based on csv
electrolyte_data = pd.read_csv("dataset/solution_concentration_dataset.CSV")
temperature_data = pd.read_csv("dataset/temperature_dataset.CSV")
nonelectrolute_data = pd.read_csv("dataset/nonelectrolyte_dataset.CSV")
depolarizer_data = pd.read_csv("dataset/depolarized_dataset.CSV")
geometric_data = pd.read_csv("dataset/geometric_shape_dataset.CSV")
size_pole_data = pd.read_csv("dataset/size_pole_dataset.CSV")
distance_pole_data = pd.read_csv("dataset/distance_pole_dataset.CSV")

dataset_electrolyte = DataSet(electrolyte_data, temperature_data)
dataset_nonelectrolyte = DataSet(nonelectrolute_data, temperature_data)
dataset_depolarizer = DataSet(depolarizer_data, temperature_data)
dataset_geometric = DataSet(geometric_data, temperature_data)
dataset_size_pole = DataSet(size_pole_data, temperature_data)
dataset_distance_pole = DataSet(distance_pole_data, temperature_data)

# visualizer.visualize_time_resistance_temperature(dataset_electrolyte)
# visualizer.visualize_temperature_resistance(dataset_electrolyte)

# visualizer.visualize_time_resistance_concentration(dataset_nonelectrolyte)
# visualizer.visualize_concentration_resistance(dataset_nonelectrolyte)

visualizer.visualize_time_resistance_concentration(dataset_electrolyte)
visualizer.visualize_concentration_resistance(dataset_electrolyte)

# visualizer.visualize_time_resistance_concentration(dataset_depolarizer)
# visualizer.visualize_concentration_resistance(dataset_depolarizer)
# visualizer.visualize_time_resistance_concentration(dataset_geometric)
# visualizer.visualize_concentration_resistance(dataset_geometric)
# visualizer.visualize_time_resistance_concentration(dataset_size_pole)
# visualizer.visualize_concentration_resistance(dataset_size_pole)
# visualizer.visualize_time_resistance_concentration(dataset_distance_pole)
# visualizer.visualize_concentration_resistance(dataset_distance_pole)