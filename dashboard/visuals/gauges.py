import plotly.graph_objects as go


# ==========================================================
# HEALTH GAUGE
# ==========================================================

def create_health_gauge(score):
    """
    Executive System Health Gauge.

    Parameters
    ----------
    score : float
        Health score between 0 and 100.

    Returns
    -------
    plotly.graph_objects.Figure
    """

    fig = go.Figure(

        go.Indicator(

            mode="gauge+number",

            value=score,

            number={
                "suffix": "%",
                "font": {
                    "size": 42
                }
            },

            title={
                "text": "<b>System Health Score</b>",
                "font": {
                    "size": 24
                }
            },

            gauge={

                "axis": {
                    "range": [0, 100],
                    "tickwidth": 1
                },

                "bar": {
                    "thickness": 0.35,
                    "color": "#1F77B4"
                },

                "bgcolor": "white",

                "borderwidth": 2,

                "bordercolor": "#D3D3D3",

                "steps": [

                    {
                        "range": [0, 40],
                        "color": "#FDEDEC"
                    },

                    {
                        "range": [40, 70],
                        "color": "#FCF3CF"
                    },

                    {
                        "range": [70, 100],
                        "color": "#E8F8F5"
                    }

                ],

                "threshold": {

                    "line": {
                        "color": "#D62728",
                        "width": 6
                    },

                    "thickness": 0.85,

                    "value": score

                }

            }

        )

    )

    fig.update_layout(

        template="plotly_white",

        height=420,

        margin=dict(
            l=30,
            r=30,
            t=80,
            b=30
        )

    )

    return fig


# ==========================================================
# RISK GAUGE
# ==========================================================

def create_risk_gauge(risk_percentage):
    """
    Displays operational risk level.
    """

    fig = go.Figure(

        go.Indicator(

            mode="gauge+number",

            value=risk_percentage,

            number={
                "suffix": "%"
            },

            title={
                "text": "<b>Operational Risk</b>"
            },

            gauge={

                "axis": {
                    "range": [0, 100]
                },

                "bar": {
                    "color": "#FF7F0E"
                },

                "steps": [

                    {
                        "range": [0, 30],
                        "color": "#E8F8F5"
                    },

                    {
                        "range": [30, 60],
                        "color": "#FCF3CF"
                    },

                    {
                        "range": [60, 100],
                        "color": "#FDEDEC"
                    }

                ]

            }

        )

    )

    fig.update_layout(

        template="plotly_white",

        height=380,

        margin=dict(
            l=20,
            r=20,
            t=70,
            b=20
        )

    )

    return fig


# ==========================================================
# KPI PROGRESS GAUGE
# ==========================================================

def create_progress_gauge(
    value,
    title,
    color="#2CA02C"
):
    """
    Generic circular KPI gauge.

    Parameters
    ----------
    value : float
    title : str
    color : str

    Returns
    -------
    Plotly Figure
    """

    fig = go.Figure(

        go.Indicator(

            mode="gauge+number",

            value=value,

            number={
                "suffix": "%"
            },

            title={
                "text": f"<b>{title}</b>"
            },

            gauge={

                "axis": {
                    "range": [0, 100]
                },

                "bar": {
                    "color": color
                }

            }

        )

    )

    fig.update_layout(

        template="plotly_white",

        height=320,

        margin=dict(
            l=20,
            r=20,
            t=60,
            b=20
        )

    )

    return fig