"""
executive_engine.py

Executive Analytics Engine
----------------------------------------------------------

Builds executive analytics and executive intelligence.
"""

from utils.insight_engine import (
    stress_summary,
    peak_stress_days,
    system_health_score,
    detect_anomalies,
    classify_risk_level
)

from utils.insight_generator import (
    generate_all_insights
)


# ==========================================================
# EXECUTIVE ENGINE
# ==========================================================

def run_executive(df):
    """
    Build executive analytics and intelligence.
    """

    executive = {}

    executive["summary"] = stress_summary(df)

    executive["health_score"] = system_health_score(df)

    executive["peak_stress"] = peak_stress_days(df)

    executive["anomalies"] = detect_anomalies(df)

    executive["risk_level"] = classify_risk_level(
        executive["health_score"]
    )

    executive.update(
        generate_all_insights(
            df,
            executive
        )
    )

    return executive


# ==========================================================
# EXECUTIVE SNAPSHOTS
# ==========================================================

def get_flow_snapshot(df):
    """
    Build executive flow snapshot metrics.
    """

    return {

        "apprehended": int(
            df["children_apprehended_and_placed_in_cbp_custody"].sum()
        ),

        "avg_cbp_load": int(
            df["children_in_cbp_custody"].mean()
        ),

        "transferred": int(
            df["children_transferred_out_of_cbp_custody"].sum()
        ),

        "avg_hhs_load": int(
            df["children_in_hhs_care"].mean()
        ),

        "discharged": int(
            df["children_discharged_from_hhs_care"].sum()
        )
    }