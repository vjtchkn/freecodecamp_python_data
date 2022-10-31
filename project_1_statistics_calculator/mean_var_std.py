# Create a function calculate() that uses Numpy
# to output mean, variance, standard deviation, max, min, and sum of rows, columns, and elements in a 3x3 matrix
# input should be a list containing 9 digits
# function should convert the list into a 3x3 Numpy array
# and return a dictionary containing all the values for both axes and flattened matrix in lists (not Numpy arrays)
# if list contaings less than 9 values, raise ValueError

import numpy as np


def calculate(lst):
    if len(lst) < 9:
        raise ValueError("List must contain nine numbers.")
    arr = np.array(lst)
    arr.shape = (3, 3)
    calculations = {
        "mean": [arr.mean(axis=0).tolist(), arr.mean(axis=1).tolist(), arr.mean()],
        "variance": [arr.var(axis=0).tolist(), arr.var(axis=1).tolist(), arr.var()],
        "standard deviation": [
            arr.std(axis=0).tolist(),
            arr.std(axis=1).tolist(),
            arr.std(),
        ],
        "max": [arr.max(axis=0).tolist(), arr.max(axis=1).tolist(), arr.max()],
        "min": [arr.min(axis=0).tolist(), arr.min(axis=1).tolist(), arr.min()],
        "sum": [arr.sum(axis=0).tolist(), arr.sum(axis=1).tolist(), arr.sum()],
    }
    return calculations
