# ==========================================================
# INSIGHT BUILDER
# ==========================================================

def build_insight(
    severity,
    title,
    description
):
    """
    Build a standardized insight object used throughout
    the Operational Intelligence Platform.
    """

    return {

        "severity": severity,

        "title": title,

        "description": description

    }

# ==========================================================
# EXECUTIVE SUMMARY
# ==========================================================

def generate_executive_summary(df, insights):
    """
    Generate a concise executive overview.
    """

    health = insights["health_score"]
    stress = insights["summary"]["stress_percentage"]

    if health >= 85:
        return (
            f"The operational pipeline remained stable with a "
            f"Health Score of {health:.1f}%. "
            f"Only {stress:.1f}% of reporting days experienced "
            f"operational stress."
        )

    elif health >= 70:
        return (
            f"The system operated under moderate pressure. "
            f"The Health Score reached {health:.1f}% while "
            f"{stress:.1f}% of reporting days exceeded "
            f"the operational stress threshold."
        )

    else:
        return (
            f"The operational pipeline experienced sustained "
            f"pressure. Health Score declined to {health:.1f}% "
            f"with {stress:.1f}% stress days."
        )


# ==========================================================
# RISK SUMMARY
# ==========================================================

def generate_risk_summary(df, insights):

    stress = insights["summary"]["stress_percentage"]

    if stress < 10:
        return "Overall operational risk is LOW."

    elif stress < 20:
        return "Operational risk is MODERATE and should be monitored."

    elif stress < 35:
        return "Operational risk is HIGH. Capacity constraints are emerging."

    return (
        "Operational risk is CRITICAL. "
        "Persistent bottlenecks require immediate attention."
    )


# ==========================================================
# OPERATIONS SUMMARY
# ==========================================================

def generate_operations_summary(df):

    avg_transfer = df[
        "children_transferred_out_of_cbp_custody"
    ].mean()

    avg_discharge = df[
        "children_discharged_from_hhs_care"
    ].mean()

    return (
        f"Average daily transfers from CBP reached "
        f"{avg_transfer:.1f} children, while "
        f"average HHS discharges were "
        f"{avg_discharge:.1f} children."
    )


# ==========================================================
# RECOMMENDATIONS
# ==========================================================

def generate_recommendations(df, insights):
    """
    Generate executive recommendations based on
    operational performance.
    """

    recommendations = []

    # ------------------------------------------------------
    # Operational Stress
    # ------------------------------------------------------

    if insights["summary"]["stress_percentage"] > 20:

        recommendations.append({

            "icon": "🟠",

            "title": "Operational Monitoring",

            "priority": "Medium",

            "summary": (
                "Operational stress exceeded the recommended "
                "monitoring threshold."
            ),

            "recommendation": (
                "Increase operational monitoring during "
                "high-stress reporting periods."
            ),

            "impact": (
                "Earlier identification of operational issues "
                "will reduce the likelihood of prolonged system stress."
            )

        })

    # ------------------------------------------------------
    # CBP Capacity
    # ------------------------------------------------------

    if df["cbp_backlog"].max() > 150:

        recommendations.append({

            "icon": "🟡",

            "title": "CBP Capacity Planning",

            "priority": "Medium",

            "summary": (
                "CBP backlog exceeded the preferred operating range."
            ),

            "recommendation": (
                "Review CBP processing capacity to reduce "
                "backlog accumulation."
            ),

            "impact": (
                "Lower backlog levels and faster transfers "
                "into HHS care."
            )

        })

    # ------------------------------------------------------
    # HHS Placement Capacity
    # ------------------------------------------------------

    if df["hhs_backlog"].max() > 7000:

        recommendations.append({

            "icon": "🟡",

            "title": "Placement Capacity",

            "priority": "Medium",

            "summary": (
                "Placement demand is approaching available "
                "operational capacity."
            ),

            "recommendation": (
                "Evaluate HHS placement capacity to improve "
                "operational throughput."
            ),

            "impact": (
                "Improved placement efficiency and reduced "
                "waiting time for children in care."
            )

        })

    # ------------------------------------------------------
    # Operational Anomalies
    # ------------------------------------------------------

    if len(insights["anomalies"]["net_flow"]) > 10:

        recommendations.append({

            "icon": "🔴",

            "title": "Investigate Net Flow",

            "priority": "High",

            "summary": (
                "Repeated net-flow anomalies indicate "
                "potential operational bottlenecks."
            ),

            "recommendation": (
                "Investigate transfer bottlenecks and "
                "rebalance operational resources."
            ),

            "impact": (
                "Improved system stability, smoother care "
                "transitions, and reduced operational delays."
            )

        })

    # ------------------------------------------------------
    # Stable Operations
    # ------------------------------------------------------

    if not recommendations:

        recommendations.append({

            "icon": "🟢",

            "title": "Maintain Operations",

            "priority": "Low",

            "summary": (
                "Current operational indicators remain "
                "within expected performance thresholds."
            ),

            "recommendation": (
                "Continue routine monitoring while pursuing "
                "incremental process improvements."
            ),

            "impact": (
                "Maintains current operational resilience "
                "and organizational efficiency."
            )

        })

    return recommendations


# ==========================================================
# ALERTS
# ==========================================================

def generate_alerts(df, insights):
    """
    Generate executive operational alerts.
    """

    alerts = []

    # ------------------------------------------------------
    # Operational Anomalies
    # ------------------------------------------------------

    for metric, anomaly_df in insights["anomalies"].items():

        if anomaly_df.empty:
            continue

        count = len(anomaly_df)

        # --------------------------------------------------
        # Severity
        # --------------------------------------------------

        if count >= 20:

            severity = "High"
            icon = "🔴"

        elif count >= 10:

            severity = "Medium"
            icon = "🟠"

        else:

            severity = "Low"
            icon = "🟡"

        # --------------------------------------------------
        # Alert
        # --------------------------------------------------

        alerts.append({

            "icon": icon,

            "severity": severity,

            "title": metric.replace("_", " ").title(),

            "summary": (
                f"{count} anomaly events were detected "
                f"during the selected reporting period."
            ),

            "action": (
                "Investigate operational activity and "
                "identify the root cause of abnormal behavior."
            ),

            "impact": (
                "Delayed intervention may increase operational "
                "risk and reduce system efficiency."
            )

        })

    # ------------------------------------------------------
    # No Active Alerts
    # ------------------------------------------------------

    if not alerts:

        alerts.append({

            "icon": "🟢",

            "severity": "Normal",

            "title": "System Stable",

            "summary": (
                "No operational anomalies were detected "
                "during the selected reporting period."
            ),

            "action": (
                "Continue routine monitoring of operational "
                "performance indicators."
            ),

            "impact": (
                "Current operating conditions indicate a "
                "stable and resilient care transition system."
            )

        })

    return alerts


# ==========================================================
# MASTER ENGINE
# ==========================================================

def generate_all_insights(df, insights):
    """
    Generate every dashboard insight.
    """

    return {

        "executive_summary":
            generate_executive_summary(df, insights),

        "executive_brief":
        generate_executive_brief(df, insights),
        
        "risk_summary":
            generate_risk_summary(df, insights),

        "operations_summary":
            generate_operations_summary(df),

        "recommendations":
            generate_recommendations(df, insights),

        "alerts":
            generate_alerts(df, insights)

    }
    
# ==========================================================
# EXECUTIVE BRIEF
# ==========================================================

def generate_executive_brief(df, insights):
    """
    Generate a dynamic executive briefing.
    """

    summary = insights["summary"]
    health = insights["health_score"]
    risk = insights["risk_level"]

    total_days = summary["total_days"]
    stress_days = summary["total_stress_days"]
    stress_pct = summary["stress_percentage"]

    peak_cbp = int(df["cbp_backlog"].max())
    peak_hhs = int(df["hhs_backlog"].max())

    avg_transfer = round(
        df["children_transferred_out_of_cbp_custody"].mean(), 1
    )

    avg_discharge = round(
        df["children_discharged_from_hhs_care"].mean(), 1
    )

    brief = f"""

**Observation Period:** {total_days} reporting days

**Operational Health:** {health:.1f}% ({risk})

During the selected reporting period, the care transition
pipeline recorded **{stress_days} stress days**
({stress_pct:.2f}% of all observations).

Peak CBP backlog reached **{peak_cbp}**, while
maximum HHS backlog reached **{peak_hhs}**.

Average daily transfers from CBP were **{avg_transfer}**
children, with average HHS discharges of
**{avg_discharge}** children.

The dashboard recommends reviewing the operational
recommendations below before making capacity decisions.
"""

    return brief    