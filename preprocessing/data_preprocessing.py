# preprocessing/data_preprocessing.py
import pandas as pd
from sklearn.preprocessing import StandardScaler

def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

def clean_data(data):
    # Convert "Date" to datetime format if needed
    data["Date"] = pd.to_datetime(data["Date"])
    # Retain only the required columns as per the Bitcoin dataset
    return data[["Date", "Open", "High", "Low", "Close", "Volume"]]



def scale_data(data):
    # Drop "Date" column only if it exists
    if "Date" in data.columns:
        data_no_date = data.drop(columns=["Date"])
    else:
        data_no_date = data

    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data_no_date)
    
    # Convert back to DataFrame
    scaled_data = pd.DataFrame(scaled_data, columns=data_no_date.columns)
    if "Date" in data.columns:
        scaled_data["Date"] = data["Date"].values
    return scaled_data, scaler

