import pandas as pd

APPLIED_VOLTAGE = 5

def generate_time_range(n):
    return [5 * j for j in range(n)]

def mAToOhm(mA):
    return 5 / mA / 0.001