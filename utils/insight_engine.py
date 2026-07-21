"""
insight_engine.py

Core analytical engine for operational intelligence.
Provides summary metrics, health scoring,
peak stress identification, and anomaly detection.
"""

import numpy as np
import pandas as pd


# ==========================================================
# STRESS SUMMARY
# ==========================================================

def stress_summary(df):
    """
    Generate high-level stress statistics.
    """

    total_days = len(df)
    stress_days = int(df["system_stress"].sum())

    stress_percentage = (
        (stress_days / total_days) * 100
        if total_days > 0 else 0
    )

    return {
        "total_days": total_days,
        "total_stress_days": stress_days,
        "stress_percentage": round(stress_percentage, 2)
    }


# ==========================================================
# SYSTEM HEALTH SCORE
# ==========================================================

def system_health_score(df):
    """
    Calculate overall operational health score.
    """

    summary = stress_summary(df)

    health = max(
        0,
        100 - summary["stress_percentage"]
    )

    return round(health, 2)


# ==========================================================
# PEAK STRESS DAYS
# ==========================================================

def peak_stress_days(df):
    """
    Return highest operational stress days.
    """

    return (

        df[df["system_stress"]]

        .sort_values(
            by="cbp_backlog",
            ascending=False
        )

        .reset_index(drop=True)

    )


# ==========================================================
# Z-SCORE ANOMALY DETECTION
# ==========================================================

def detect_anomalies(
    df,
    columns=None,
    threshold=3
):
    """
    Detect anomalies using Z-score.

    Returns
    -------
    dict
        {
            column_name : dataframe_of_anomalies
        }
    """

    if columns is None:

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

        mean = df[column].mean()

        std = df[column].std()

        # Avoid divide-by-zero
        if std == 0:

            anomalies[column] = pd.DataFrame()

            continue

        z_score = (

            (df[column] - mean)

            / std

        )

        anomaly_df = df[
            np.abs(z_score) > threshold
        ].copy()

        anomaly_df["z_score"] = z_score[
            np.abs(z_score) > threshold
        ]

        anomalies[column] = anomaly_df

    return anomalies


# ==========================================================
# RISK LEVEL
# ==========================================================

def classify_risk_level(health_score):
    """
    Convert health score into
    executive-friendly labels.
    """

    if health_score >= 90:
        return "🟢 Low"

    elif health_score >= 75:
        return "🟡 Moderate"

    elif health_score >= 60:
        return "🟠 High"

    return "🔴 Critical"