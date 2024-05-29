import pandas as pd
from util.dataset import DataSet
import visualizer

# Generate a dataset instance based on csv
pandas_data_1 = pd.read_csv("csvdataset.CSV")
pandas_data_2 = pd.read_csv("csvdataset2.CSV")
dataset = DataSet(pandas_data_1, pandas_data_2)

visualizer.visualize_time_resistance(dataset)
# visualizer.visualize_temperature_resistance(dataset)
# visualizer.visualize_time_resistance(dataset)
# visualizer.visualize_concentration_resistance(dataset)