# scripts/train_model.py
import sys
import os

# Add the root directory to sys.path
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(root_dir)

# Now import modules
from preprocessing.data_preprocessing import load_data, clean_data, scale_data
from models.lstm_model import create_model, train_model
from utils.utils import reshape_data


def main():
    # Load and preprocess data
    data = load_data('data/btc_data.csv')
    data = clean_data(data)
    scaled_data, scaler = scale_data(data)

    # Prepare training data
    X, y = reshape_data(scaled_data, window_size=30)
    model = create_model((X.shape[1], X.shape[2]))

    # Train and save model
    model = train_model(model, X, y)
    model.save('models/btc_lstm_model.keras')

if __name__ == "__main__":
    main()
