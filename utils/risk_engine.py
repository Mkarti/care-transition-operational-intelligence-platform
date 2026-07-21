def run_risk_engine(executive):
    """
    Risk Analytics Engine

    Produces dashboard-ready risk intelligence.
    """

    return {

        # --------------------------------------------------
        # Executive Risk Summary
        # --------------------------------------------------

        "summary": {

            "risk_level": executive["risk_level"],

            "health_score": executive["health_score"]

        },

        # --------------------------------------------------
        # Risk KPIs
        # --------------------------------------------------

        "kpis": {

            "overall_risk": {

                "title": "Overall Risk",

                "value": executive["risk_level"],

                "icon": "⚠️",

                "subtitle": "Current Status"

            },

            "health_score": {

                "title": "System Health",

                "value": f"{executive['health_score']:.1f}%",

                "icon": "💚",

                "subtitle": "Operational Health"

            }

        },

        # --------------------------------------------------
        # Risk Trends
        # --------------------------------------------------

        "risk_trends": {

            "system_risk": {

                "title": "System Risk",

                "icon": "📈",

                "content":
                    "Operational risk has remained stable across the reporting period."

            }

        },

        # --------------------------------------------------
        # Risk Factors
        # --------------------------------------------------

        "risk_factors": [

            {

                "title": "Backlog Pressure",

                "icon": "🚔",

                "severity": executive["risk_level"],

                "content":
                    "CBP backlog continues to influence operational capacity."

            },

            {

                "title": "Placement Capacity",

                "icon": "🏥",

                "severity": executive["risk_level"],

                "content":
                    "Placement capacity should continue to be monitored."

            }

        ],

        # --------------------------------------------------
        # Recommendations
        # --------------------------------------------------

        "recommendations": [

            {

                "title": "Maintain Monitoring",

                "icon": "💡",

                "priority": "Medium",

                "message":
                    "Continue monitoring backlog and transfer efficiency."

            }

        ]

    }