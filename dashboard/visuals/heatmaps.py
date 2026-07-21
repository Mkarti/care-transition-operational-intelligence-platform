import plotly.graph_objects as go
import pandas as pd


# ==========================================================
# OPERATIONAL STRESS HEATMAP
# ==========================================================

def create_operational_heatmap(df, selected_year="All Years"):
    """
    Create a weekday vs month heatmap showing
    operational stress frequency.

    Parameters
    ----------
    df : DataFrame

    selected_year : str
        "All Years", "2023", "2024", "2025"
    """

    heatmap_df = df.copy()

    # ------------------------------------------
    # FILTER YEAR
    # ------------------------------------------

    if selected_year != "All Years":

        heatmap_df = heatmap_df[
            heatmap_df["date"].dt.year == int(selected_year)
        ]

    # ------------------------------------------

    heatmap_df["Month"] = heatmap_df["date"].dt.strftime("%b")
    heatmap_df["Weekday"] = heatmap_df["date"].dt.day_name()

    weekday_order = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ]

    month_order = [
        "Jan","Feb","Mar","Apr","May","Jun",
        "Jul","Aug","Sep","Oct","Nov","Dec"
    ]

    stress_df = heatmap_df[heatmap_df["system_stress"]]

    pivot = (
        stress_df
        .groupby(["Weekday", "Month"])
        .size()
        .reset_index(name="Stress Events")
        .pivot(
            index="Weekday",
            columns="Month",
            values="Stress Events"
        )
        .fillna(0)
    )

    pivot = pivot.reindex(weekday_order)
    pivot = pivot.reindex(columns=month_order)

    fig = go.Figure(

        data=go.Heatmap(

            z=pivot.values,

            x=pivot.columns,

            y=pivot.index,

            colorscale="Reds",

            hoverongaps=False,

            colorbar=dict(
                title="Stress Days"
            )

        )

    )

    fig.update_layout(

        title=f"Operational Stress Distribution ({selected_year})",

        template="plotly_white",

        height=520,

        margin=dict(
            l=20,
            r=20,
            t=60,
            b=20
        )

    )

    return fig