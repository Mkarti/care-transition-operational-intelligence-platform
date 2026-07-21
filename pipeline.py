from utils.data_loader import load_data
from utils.data_cleaner import clean_data
from utils.kpi_engine import add_kpis
from utils.stress_engine import add_stress_metrics
from utils.performance_metrics_engine import (
    add_performance_metrics
)

def build_pipeline(file_path):
    df = load_data(file_path)
    df = clean_data(df)
    df = add_kpis(df)
    df = add_stress_metrics(df)
    df = add_performance_metrics(df)
    return df