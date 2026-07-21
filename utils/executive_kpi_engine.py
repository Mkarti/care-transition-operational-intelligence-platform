import pandas as pd


def calculate_executive_kpis(df):
    """
    Calculate executive-level KPIs for the dashboard.
    """

    apprehended = df["children_apprehended_and_placed_in_cbp_custody"].sum()

    transferred = df["children_transferred_out_of_cbp_custody"].sum()

    discharged = df["children_discharged_from_hhs_care"].sum()

    avg_hhs = df["children_in_hhs_care"].mean()

    max_hhs = df["children_in_hhs_care"].max()

    stress_days = df["system_stress"].sum()

    total_days = len(df)

    transition_efficiency = (
        transferred / apprehended * 100
        if apprehended else 0
    )

    placement_efficiency = (
        discharged / avg_hhs * 100
        if avg_hhs else 0
    )

    throughput = (
        transferred + discharged
    ) / total_days

    capacity_utilization = (
        avg_hhs / max_hhs * 100
        if max_hhs else 0
    )

    stress_percentage = (
        stress_days / total_days * 100
        if total_days else 0
    )

    return {

        "transition_efficiency": transition_efficiency,

        "placement_efficiency": placement_efficiency,

        "daily_throughput": throughput,

        "capacity_utilization": capacity_utilization,

        "stress_percentage": stress_percentage

    }