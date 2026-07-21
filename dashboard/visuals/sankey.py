import plotly.graph_objects as go


def create_care_transition_sankey(df):
    """
    Create a Sankey diagram representing the
    CBP → HHS care transition process.
    """

    apprehended = df[
        "children_apprehended_and_placed_in_cbp_custody"
    ].sum()

    cbp = df[
        "children_in_cbp_custody"
    ].mean()

    transferred = df[
        "children_transferred_out_of_cbp_custody"
    ].sum()

    hhs = df[
        "children_in_hhs_care"
    ].mean()

    discharged = df[
        "children_discharged_from_hhs_care"
    ].sum()

    labels = [

        "Apprehended",

        "CBP Custody",

        "Transferred",

        "HHS Care",

        "Discharged"

    ]

    source = [

        0,

        1,

        2,

        3

    ]

    target = [

        1,

        2,

        3,

        4

    ]

    values = [

        apprehended,

        transferred,

        transferred,

        discharged

    ]

    fig = go.Figure(

        go.Sankey(

            arrangement="snap",

            node=dict(

                pad=20,

                thickness=22,

                line=dict(color="black", width=0.5),

                label=labels,

                color=[
                    "#2563EB",
                    "#3B82F6",
                    "#0EA5E9",
                    "#10B981",
                    "#059669"
                ]

            ),

            link=dict(

                source=source,

                target=target,

                value=values,

                color="rgba(37,99,235,0.25)"

            )

        )

    )

    fig.update_layout(

        title="Care Transition Flow",

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