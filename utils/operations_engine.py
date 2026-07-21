"""
operations_engine.py

Operations Analytics Engine
----------------------------------------------------------

Computes operational KPIs, throughput metrics,
capacity utilization, rolling analytics,
and bottleneck detection.

This module contains NO visualization code.
"""

import pandas as pd


# ==========================================================
# OPERATIONS SUMMARY
# ==========================================================

def get_operations_summary(df):
    """
    Generate high-level operational statistics.
    """

    return {

        "avg_cbp_backlog": round(
            df["cbp_backlog"].mean(), 2
        ),

        "avg_hhs_backlog": round(
            df["hhs_backlog"].mean(), 2
        ),

        "avg_transfer": round(
            df["children_transferred_out_of_cbp_custody"].mean(),
            2
        ),

        "avg_discharge": round(
            df["children_discharged_from_hhs_care"].mean(),
            2
        ),

        "peak_cbp": int(
            df["cbp_backlog"].max()
        ),

        "peak_hhs": int(
            df["hhs_backlog"].max()
        )
    }


# ==========================================================
# PROCESSING EFFICIENCY
# ==========================================================

def calculate_processing_efficiency(df):
    """
    Overall processing efficiency.

    Transfers / CBP Custody
    """

    custody = df["children_in_cbp_custody"].sum()

    transfers = df[
        "children_transferred_out_of_cbp_custody"
    ].sum()

    if custody == 0:
        return 0

    return round(
        (transfers / custody) * 100,
        2
    )


# ==========================================================
# NET FLOW
# ==========================================================

def calculate_net_flow(df):
    """
    Daily Net Flow

    Transfers - Discharges
    """

    data = df.copy()

    data["net_flow"] = (

        data["children_transferred_out_of_cbp_custody"]

        -

        data["children_discharged_from_hhs_care"]

    )

    return data


# ==========================================================
# AVERAGE BACKLOGS
# ==========================================================

def calculate_average_backlogs(df):
    """
    Average backlog values.
    """

    return {

        "cbp": round(
            df["cbp_backlog"].mean(),
            2
        ),

        "hhs": round(
            df["hhs_backlog"].mean(),
            2
        )
    }


# ==========================================================
# ROLLING PROCESSING EFFICIENCY
# ==========================================================

def calculate_rolling_efficiency(
    df,
    window=7
):
    """
    Rolling transfer efficiency.
    """

    data = df.copy()

    rolling_transfer = (

        data[
            "children_transferred_out_of_cbp_custody"
        ]

        .rolling(
            window=window,
            min_periods=1
        )

        .sum()

    )

    rolling_cbp = (

        data[
            "children_in_cbp_custody"
        ]

        .rolling(
            window=window,
            min_periods=1
        )

        .sum()

    )

    data["rolling_efficiency"] = (

        rolling_transfer

        /

        rolling_cbp.replace(
            0,
            pd.NA
        )

    ) * 100

    data["rolling_efficiency"] = (

        data["rolling_efficiency"]

        .fillna(0)

        .round(2)

    )

    return data


# ==========================================================
# CAPACITY UTILIZATION
# ==========================================================

def calculate_capacity_utilization(df):
    """
    HHS Capacity Utilization.
    """

    data = df.copy()

    peak_capacity = data[
        "children_in_hhs_care"
    ].max()

    if peak_capacity == 0:

        data["capacity_utilization"] = 0

    else:

        data["capacity_utilization"] = (

            data["children_in_hhs_care"]

            /

            peak_capacity

        ) * 100

    data["capacity_utilization"] = (

        data["capacity_utilization"]

        .round(2)

    )

    return data


# ==========================================================
# DAILY THROUGHPUT
# ==========================================================

def calculate_daily_throughput(df):
    """
    Daily operational throughput.
    """

    data = df.copy()

    data["daily_throughput"] = (

        data[
            "children_transferred_out_of_cbp_custody"
        ]

        +

        data[
            "children_discharged_from_hhs_care"
        ]

    )

    return data


# ==========================================================
# ROLLING BACKLOG
# ==========================================================

def calculate_rolling_backlog(
    df,
    window=7
):
    """
    Rolling backlog trends.
    """

    data = df.copy()

    data["rolling_cbp_backlog"] = (

        data["cbp_backlog"]

        .rolling(
            window=window,
            min_periods=1
        )

        .mean()

        .round(2)

    )

    data["rolling_hhs_backlog"] = (

        data["hhs_backlog"]

        .rolling(
            window=window,
            min_periods=1
        )

        .mean()

        .round(2)

    )

    return data


# ==========================================================
# BOTTLENECK DETECTION
# ==========================================================

def find_bottleneck_periods(
    df,
    window=7
):
    """
    Detect abnormal backlog periods using
    rolling mean + rolling standard deviation.
    """

    data = df.copy()

    rolling_mean = (

        data["cbp_backlog"]

        .rolling(
            window=window,
            min_periods=1
        )

        .mean()

    )

    rolling_std = (

        data["cbp_backlog"]

        .rolling(
            window=window,
            min_periods=1
        )

        .std()

        .fillna(0)

    )

    threshold = rolling_mean + rolling_std

    bottlenecks = data[
        data["cbp_backlog"] > threshold
    ].copy()

    return bottlenecks


# ==========================================================
# MASTER OPERATIONS ENGINE
# ==========================================================

def run_operations_engine(df):
    """
    Execute complete operations analytics pipeline.
    """

    data = calculate_net_flow(df)

    data = calculate_rolling_efficiency(data)

    data = calculate_capacity_utilization(data)

    data = calculate_daily_throughput(data)

    data = calculate_rolling_backlog(data)

    return {

        "summary":
            get_operations_summary(data),

        "processing_efficiency":
            calculate_processing_efficiency(data),

        "average_backlogs":
            calculate_average_backlogs(data),

        "rolling_efficiency":
            data[
                [
                    "date",
                    "rolling_efficiency"
                ]
            ],

        "capacity_utilization":
            data[
                [
                    "date",
                    "capacity_utilization"
                ]
            ],

        "daily_throughput":
            data[
                [
                    "date",
                    "daily_throughput"
                ]
            ],

        "rolling_backlog":
            data[
                [
                    "date",
                    "rolling_cbp_backlog",
                    "rolling_hhs_backlog"
                ]
            ],

        "bottlenecks":
            find_bottleneck_periods(data),

        "net_flow_df":
            data
    }