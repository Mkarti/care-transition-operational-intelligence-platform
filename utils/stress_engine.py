import pandas as pd

def add_stress_metrics(df: pd.DataFrame) -> pd.DataFrame:
    """
    Detect system stress and bottlenecks using percentile thresholds.
    """
    df = df.copy()

    # Thresholds
    cbp_threshold = df['cbp_backlog'].quantile(0.85)
    hhs_threshold = df['hhs_backlog'].quantile(0.85)

    # Stress indicators
    df['cbp_stress'] = df['cbp_backlog'] > cbp_threshold
    df['hhs_overload'] = df['hhs_backlog'] > hhs_threshold

    # Combined system stress
    df['system_stress'] = df['cbp_stress'] | df['hhs_overload']

    return df