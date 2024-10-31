# scripts/generate_signals.py
import sys
import os

# Add the root directory to sys.path
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(root_dir)

# scripts/generate_signals.py

import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model
from preprocessing.data_preprocessing import scale_data
from utils.utils import reshape_data

def generate_signals(file_path):
    # Load model and data
    model = load_model('models/btc_lstm_model.keras')
    data = pd.read_csv(file_path)
    
    # Preprocess data and reshape for prediction
    _, scaler = scale_data(data)
    scaled_data, _ = scale_data(data)
    X, _ = reshape_data(scaled_data, window_size=30)
    
    # Predict and generate signals
    predictions = model.predict(X)
    signals = np.where(predictions > 0.5, 'Buy', 'Sell')  # Example thresholding

    # Align signals with the DataFrame by starting at index 'window_size'
    data['signal'] = np.nan  # Set up a column to insert signals
    data = data.astype({'signal': 'object'})  # Ensure the dtype is compatible
    data.loc[30:, 'signal'] = signals  # Start assigning signals from the 30th row

    
    data.to_csv('data/btc_signals.csv', index=False)
    print("Signals generated and saved to data/btc_signals.csv")

if __name__ == "__main__":
    generate_signals('data/btc_data.csv')
