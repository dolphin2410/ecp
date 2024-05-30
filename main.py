import pandas as pd
from util.dataset import DataSet
import visualizer

# Generate a dataset instance based on csv
pandas_data_1 = pd.read_csv("solution_concentration_dataset.CSV")
pandas_data_2 = pd.read_csv("temperature_dataset.CSV")
dataset = DataSet(pandas_data_1, pandas_data_2)

# visualizer.visualize_time_resistance_temperature(dataset)
# visualizer.visualize_temperature_resistance(dataset)
# visualizer.visualize_time_resistance_concentration(dataset)
# visualizer.visualize_concentration_resistance(dataset)