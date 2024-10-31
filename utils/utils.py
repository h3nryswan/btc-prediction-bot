# utils/utils.py

import numpy as np

def reshape_data(scaled_data, window_size):
    # Check if "Date" column is present before dropping
    if "Date" in scaled_data.columns:
        scaled_data_values = scaled_data.drop(columns=["Date"]).values
    else:
        scaled_data_values = scaled_data.values
    
    X, y = [], []
    for i in range(window_size, len(scaled_data_values)):
        X.append(scaled_data_values[i - window_size:i, :])  # Input features up to the target
        y.append(scaled_data_values[i, -1])  # Target value (e.g., close price or other prediction target)

    return np.array(X), np.array(y)