import pandas as pd
import os

def load_data(file_path: str) -> pd.DataFrame:
    """
    Load raw CSV data from given path.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found at: {file_path}")
    
    df = pd.read_csv(file_path)
    
    return df