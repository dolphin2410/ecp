import pandas as pd
from util.dataset import DataSet
import visualizer

# Generate a dataset instance based on csv
pandas_data = pd.read_csv("csvdataset.CSV")
dataset = DataSet(pandas_data)

visualizer.visualize_time_resistance(dataset)
visualizer.visualize_concentration_resistance(dataset)