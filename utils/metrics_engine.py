"""
metrics_engine.py

Shared Metrics Engine
----------------------------------------------------------

Provides reusable business metrics for the Care Transition Operational Intelligence Platform.

These metrics are shared across Operations, Performance, Risk, AI Decision, and future analytics modules.

This module contains NO visualization code.
"""


# ==========================================================
# INTERNAL HELPERS
# ==========================================================

def _throughput(df):
    """
    Return total daily throughput.
    """
    return (
        df["children_transferred_out_of_cbp_custody"] +
        df["children_discharged_from_hhs_care"]
    )


def _combined_backlog(df):
    """
    Return combined CBP and HHS backlog.
    """
    return (
        df["cbp_backlog"] +
        df["hhs_backlog"]
    )


# ==========================================================
# THROUGHPUT METRICS
# ==========================================================

def calculate_average_throughput(df):
    """
    Average daily operational throughput.
    """
    return round(_throughput(df).mean(), 2)


def calculate_peak_throughput(df):
    """
    Highest daily throughput.
    """
    return int(_throughput(df).max())


def calculate_minimum_throughput(df):
    """
    Lowest daily throughput.
    """
    return int(_throughput(df).min())


# ==========================================================
# BACKLOG METRICS
# ==========================================================

def calculate_average_cbp_backlog(df):
    """
    Average CBP backlog.
    """
    return round(df["cbp_backlog"].mean(), 2)


def calculate_average_hhs_backlog(df):
    """
    Average HHS backlog.
    """
    return round(df["hhs_backlog"].mean(), 2)


def calculate_combined_backlog(df):
    """
    Average combined backlog.
    """
    return round(_combined_backlog(df).mean(), 2)


# ==========================================================
# CAPACITY METRICS
# ==========================================================

def calculate_average_cbp_load(df):
    """
    Average children in CBP custody.
    """
    return round(df["children_in_cbp_custody"].mean(), 2)


def calculate_average_hhs_load(df):
    """
    Average children in HHS care.
    """
    return round(df["children_in_hhs_care"].mean(), 2)


def calculate_peak_hhs_load(df):
    """
    Peak HHS occupancy.
    """
    return int(df["children_in_hhs_care"].max())


def calculate_average_capacity_utilization(df):
    """
    Average capacity utilization.
    Requires capacity_utilization column.
    """
    return round(df["capacity_utilization"].mean(), 2)


# ==========================================================
# TRANSFER METRICS
# ==========================================================

def calculate_average_transfer(df):
    """
    Average daily transfers.
    """
    return round(
        df["children_transferred_out_of_cbp_custody"].mean(),
        2
    )


def calculate_average_discharge(df):
    """
    Average daily discharges.
    """
    return round(
        df["children_discharged_from_hhs_care"].mean(),
        2
    )
    
    
# ==========================================================
# TOTAL ANOMALIES
# ==========================================================

def get_total_anomalies(anomalies):
    """
    Return the total number of detected anomalies
    across all monitored indicators.
    """

    return sum(
        len(df)
        for df in anomalies.values()
    )    