# main.py
import sys
import os

# Ensure the root directory is in the PYTHONPATH
root_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(root_dir)

# Rest of your code
import os

def main():
    os.system("python scripts/data_fetcher.py")      # Fetch latest BTC data
    os.system("python scripts/train_model.py")       # Train model
    os.system("python scripts/generate_signals.py")  # Generate signals

if __name__ == "__main__":
    main()
