import pandas as pd

APPLIED_VOLTAGE = 5

def generate_time_range(n):
    return [5 * j for j in range(n)]

def get_solution_names(data: pd.DataFrame):
    return list(set(map(lambda x: " ".join(x.split(" ")[:-1]), data.iloc[:, 0])))

def mAToOhm(mA):
    return 5 / mA / 0.001