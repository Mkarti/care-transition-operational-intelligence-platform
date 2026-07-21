import numpy as np
import pandas as pd

def add_kpis(df: pd.DataFrame) -> pd.DataFrame:
    """
    Generate system efficiency KPIs for care transition pipeline.
    """
    df = df.copy()

    # KPI 1: CBP Backlog Pressure
    df['cbp_backlog'] = (
        df['children_apprehended_and_placed_in_cbp_custody']
        - df['children_transferred_out_of_cbp_custody']
    )

    # KPI 2: HHS Backlog Pressure
    df['hhs_backlog'] = (
        df['children_in_hhs_care']
        - df['children_discharged_from_hhs_care']
    )

    # KPI 3: Net Flow Pressure
    df['net_flow'] = (
        df['children_transferred_out_of_cbp_custody']
        - df['children_discharged_from_hhs_care']
    )
    
    # KPI 4: Capacity Utilization
    df["capacity_utilization"] = (
        df["children_in_hhs_care"]
        / df["children_in_hhs_care"].max()
    ) * 100
    
    
    df["processing_efficiency"] = (
        df["children_transferred_out_of_cbp_custody"]
        / df["children_apprehended_and_placed_in_cbp_custody"]
    ) * 100

    df["processing_efficiency"] = (
        df["processing_efficiency"]
        .fillna(0)
        .clip(0, 100)
    )

    df["rolling_efficiency"] = (
        df["processing_efficiency"]
        .rolling(window=7, min_periods=1)
        .mean()
    )
    
    df["placement_efficiency"] = (
        df["children_discharged_from_hhs_care"]
        /
        df["children_in_hhs_care"]
    ).replace([np.inf, -np.inf], 0).fillna(0) * 100
    
    return df  