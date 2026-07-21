"""
charts.py

Reusable Plotly chart library for the
Care Transition Operational Intelligence Platform.
"""

import plotly.graph_objects as go


# ==========================================================
# COMMON LAYOUT
# ==========================================================

def apply_layout(fig, title):
    """
    Apply consistent styling across all charts.
    """

    fig.update_layout(

        font=dict(
            family="Inter, Arial, sans-serif",
            size=13
        ),

        title={

            "text": f"<b>{title}</b>",

            "x": 0.02,

            "font": {

                "size": 20

            }

        },

        template="plotly_white",

        hovermode="x unified",

        height=480,

        legend=dict(

            orientation="h",

            yanchor="bottom",

            y=1.02,

            xanchor="left",

            x=0

        ),

        margin=dict(

            l=30,

            r=30,

            t=70,

            b=30

        ),

        xaxis=dict(

            showgrid=False,

            zeroline=False,

            showline=True,

            linecolor="#D6D6D6"

        ),

        yaxis=dict(

            showgrid=True,

            gridcolor="#ECECEC",

            zeroline=False,

            showline=True,

            linecolor="#D6D6D6"

        )
    )
    return fig

# ==========================================================
# GENERIC CHART BUILDERS
# ==========================================================

# MULTI-LINE CHART

def create_line_chart(
    df,
    x,
    y_columns,
    title
):
    """
    Create reusable multi-line trend chart.
    """

    fig = go.Figure()

    colors = [
        "#2563EB",
        "#10B981",
        "#F59E0B",
        "#EF4444",
        "#8B5CF6",
        "#06B6D4"
    ]

    for i, column in enumerate(y_columns):

        fig.add_trace(

            go.Scatter(

                x=df[x],

                y=df[column],

                mode="lines",

                name=column.replace("_", " ").title(),

                line=dict(
                    width=3,
                    color=colors[i % len(colors)]
                )

            )

        )

    return apply_layout(fig, title)


# DUAL AXIS CHART

def create_dual_axis_chart(
    df,
    x,
    left_y,
    right_y,
    title,
    left_name,
    right_name
):
    """
    Create dual-axis operational chart.
    """

    fig = go.Figure()

    fig.add_trace(

        go.Scatter(

            x=df[x],

            y=df[left_y],

            mode="lines",

            name=left_name,

            line=dict(
                width=3,
                color="#2563EB"
            )

        )

    )

    fig.add_trace(

        go.Scatter(

            x=df[x],

            y=df[right_y],

            mode="lines",

            name=right_name,

            line=dict(
                width=3,
                color="#10B981"
            ),

            yaxis="y2"

        )

    )

    fig.update_layout(

        yaxis=dict(
            title=left_name
        ),

        yaxis2=dict(

            title=right_name,

            overlaying="y",

            side="right"

        )

    )

    return apply_layout(fig, title)


# ANOMALY OVERLAY

def add_anomaly_markers(
    fig,
    anomaly_df,
    x_column,
    y_column
):
    """
    Overlay anomaly markers on an existing figure.
    """

    if anomaly_df.empty:
        return fig

    fig.add_trace(

        go.Scatter(

            x=anomaly_df[x_column],

            y=anomaly_df[y_column],

            mode="markers",

            name="Anomalies",

            marker=dict(
                size=13,
                color="#DC2626",
                symbol="diamond",
                line=dict(
                    color="white",
                    width=1.5
                )
            )
        )
    )

    return fig


# AREA CHART

def create_area_chart(
    df,
    x,
    y,
    title
):
    """
    Create filled area chart.
    """

    fig = go.Figure(

        go.Scatter(

            x=df[x],

            y=df[y],

            fill="tozeroy",

            mode="lines",

            line=dict(
                width=3,
                color="#2563EB"
            ),

            name=y.replace("_", " ").title()

        )

    )

    return apply_layout(fig, title)


# BAR CHART

def create_bar_chart(
    df,
    x,
    y,
    title
):
    """
    Create reusable bar chart.
    """

    fig = go.Figure(

        go.Bar(

            x=df[x],

            y=df[y],

            marker_color="#2563EB",

            name=y.replace("_", " ").title()

        )

    )

    return apply_layout(fig, title)

# ==========================================================
# EXECUTIVE DASHBOARD CHARTS
# ==========================================================

# SYSTEM LOAD

def create_system_load_chart(df):
    """
    Executive system load chart.
    """

    return create_line_chart(

        df=df,

        x="date",

        y_columns=[

            "children_in_cbp_custody",

            "children_in_hhs_care"

        ],

        title="System Load Over Time"

    )


# THROUGHPUT

def create_throughput_chart(df):
    """
    Executive throughput chart.
    """

    return create_dual_axis_chart(

        df=df,

        x="date",

        left_y="children_transferred_out_of_cbp_custody",

        right_y="children_discharged_from_hhs_care",

        title="Operational Throughput",

        left_name="Transferred",

        right_name="Discharged"

    )
 
 
# BACKLOG COMPARISON

def create_backlog_chart(df):
    """
    Compare CBP and HHS backlog trends.
    """

    return create_line_chart(

        df=df,

        x="date",

        y_columns=[
            "cbp_backlog",
            "hhs_backlog"
        ],

        title="Backlog Trend Comparison"

    )


# ==========================================================
# OPERATIONS DASHBOARD CHARTS
# ==========================================================

# DAILY THROUGHPUT

def create_daily_throughput_chart(df):
    """
    Display daily operational throughput.
    """

    fig = go.Figure()

    fig.add_trace(

        go.Bar(

            x=df["date"],

            y=df["daily_throughput"],

            name="Daily Throughput",

            marker_color="#2563EB"

        )

    )

    fig.update_yaxes(
        title="Children Processed"
    )

    return apply_layout(
        fig,
        "Daily Operational Throughput"
    ) 


# CAPACITY UTILIZATION

def create_capacity_chart(df):
    """
    Display HHS capacity utilization over time.
    """

    fig = go.Figure()

    fig.add_trace(

        go.Scatter(

            x=df["date"],

            y=df["capacity_utilization"],

            mode="lines",

            name="Capacity Utilization",

            line=dict(
                width=3,
                color="#10B981"
            ),

            fill="tozeroy"

        )

    )

    fig.update_yaxes(
        title="Capacity (%)"
    )

    return apply_layout(
        fig,
        "HHS Capacity Utilization"
    )
 
 
# ==========================================================
# PERFORMANCE DASHBOARD CHARTS
# ========================================================== 
   
# ROLLING EFFICIENCY CHART

def create_rolling_efficiency_chart(df):
    """
    Display 7-day rolling operational processing efficiency.
    """

    fig = go.Figure()

    fig.add_trace(

        go.Scatter(

            x=df["date"],

            y=df["rolling_efficiency"],

            mode="lines",

            name="Rolling Efficiency",

            line=dict(
                width=3,
                color="#2563EB"
            ),

            fill="tozeroy"

        )

    )

    fig.update_yaxes(
        title="Efficiency (%)"
    )

    return apply_layout(
        fig,
        "7-Day Rolling Processing Efficiency"
    )


# ROLLING BACKLOG

def create_rolling_backlog_chart(df):
    """
    Display rolling CBP and HHS backlog trends.
    """

    fig = go.Figure()

    fig.add_trace(

        go.Scatter(

            x=df["date"],

            y=df["rolling_cbp_backlog"],

            mode="lines",

            name="Rolling CBP",

            line=dict(
                width=3,
                color="#2563EB"
            )

        )

    )

    fig.add_trace(

        go.Scatter(

            x=df["date"],

            y=df["rolling_hhs_backlog"],

            mode="lines",

            name="Rolling HHS",

            line=dict(
                width=3,
                color="#10B981"
            )

        )

    )

    fig.update_yaxes(
        title="Children"
    )

    return apply_layout(
        fig,
        "7-Day Rolling Backlog Trends"
    )


# ==========================================================
# RISK DASHBOARD CHARTS
# ==========================================================

def create_stress_timeline(df):
    """
    Visualize operational stress events across the reporting period.
    """

    fig = go.Figure()

    # ------------------------------------------------------
    # CBP Backlog Trend
    # ------------------------------------------------------

    fig.add_trace(

        go.Scatter(

            x=df["date"],

            y=df["cbp_backlog"],

            mode="lines",

            name="CBP Backlog",

            line=dict(
                width=3,
                color="#2563EB"
            )

        )

    )

    # ------------------------------------------------------
    # Operational Stress Indicators
    # ------------------------------------------------------

    stress_df = df[df["system_stress"]]

    if not stress_df.empty:

        fig.add_trace(

            go.Scatter(

                x=stress_df["date"],

                y=stress_df["cbp_backlog"],

                mode="markers",

                name="Stress Period",

                marker=dict(
                    size=10,
                    color="#DC2626",
                    symbol="diamond"
                )

            )

        )

    # ------------------------------------------------------
    # Axis Configuration
    # ------------------------------------------------------

    fig.update_yaxes(
        title="CBP Backlog"
    )

    return apply_layout(
        fig,
        "Operational Stress Timeline"
    )
 
    
# ==========================================================
# AI DECISION DASHBOARD CHARTS
# ==========================================================

"""
Future AI visualizations for the Executive Decision Intelligence Dashboard.

Planned Visualizations
----------------------
• Decision Confidence Trend
• Risk Forecast Timeline
• Scenario Comparison Analysis
• Resource Allocation Impact
• AI Recommendation Distribution
• Forecast Confidence Bands

These visualizations will be introduced in future
platform versions as predictive analytics and
decision simulation capabilities continue to evolve.
"""    