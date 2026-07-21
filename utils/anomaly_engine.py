"""
anomaly_engine.py

Detect operational anomalies using
statistical thresholds.
"""

import pandas as pd


def detect_anomalies(df):
    """
    Detect unusually high operational values
    using the IQR (Interquartile Range) method.
    """

    columns = [
        "children_apprehended_and_placed_in_cbp_custody",
        "children_in_cbp_custody",
        "children_transferred_out_of_cbp_custody",
        "children_in_hhs_care",
        "children_discharged_from_hhs_care",
        "cbp_backlog",
        "hhs_backlog",
        "net_flow"
    ]

    anomalies = {}

    for column in columns:

        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)

        IQR = Q3 - Q1

        upper = Q3 + 1.5 * IQR
        lower = Q1 - 1.5 * IQR

        anomaly_df = df[
            (df[column] > upper) |
            (df[column] < lower)
        ]

        anomalies[column] = anomaly_df

    return anomalies