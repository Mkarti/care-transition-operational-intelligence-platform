"""
narrative_engine.py

Dynamic Executive Narrative Engine
----------------------------------------------------------

Generates data-driven executive narratives for every dashboard.

Instead of static paragraphs, this module creates
context-aware summaries using live analytics.

Used by:
    • Executive Dashboard
    • Operations Dashboard
    • Performance Dashboard
    • Risk Dashboard
    • AI Decision Dashboard
"""


# ==========================================================
# SHARED METRIC FORMATTER
# ==========================================================

def format_metrics(
    health_score,
    processing_efficiency,
    stress_percentage,
    risk_level
):
    """
    Format commonly used executive metrics.
    """

    return {
        "health": f"{health_score:.1f}%",
        "efficiency": f"{processing_efficiency:.1f}%",
        "stress": f"{stress_percentage:.1f}%",
        "risk": risk_level
    }


# ==========================================================
# EXECUTIVE NARRATIVE
# ==========================================================

def build_executive_narrative(
    health_score,
    processing_efficiency,
    stress_percentage,
    risk_level
):
    """
    Generate a dynamic executive narrative.
    """

    # ------------------------------------------------------
    # Overall Condition
    # ------------------------------------------------------

    if health_score >= 90:

        condition = (
            "The organization continues to demonstrate exceptional "
            "operational resilience and sustained system stability."
        )

    elif health_score >= 75:

        condition = (
            "The organization remains operationally stable with "
            "strong overall system performance."
        )

    elif health_score >= 60:

        condition = (
            "The organization is experiencing moderate operational "
            "pressure that warrants proactive management."
        )

    else:

        condition = (
            "Operational conditions require immediate executive "
            "attention to restore organizational stability."
        )

    # ------------------------------------------------------
    # Efficiency Assessment
    # ------------------------------------------------------

    if processing_efficiency >= 90:

        efficiency_comment = (
            "Processing efficiency remains excellent, indicating "
            "effective coordination throughout the care transition pipeline."
        )

    elif processing_efficiency >= 80:

        efficiency_comment = (
            "Processing efficiency remains within an acceptable range "
            "while offering opportunities for further optimization."
        )

    else:

        efficiency_comment = (
            "Current processing efficiency indicates operational "
            "bottlenecks that should be prioritized."
        )

    # ------------------------------------------------------
    # Stress Assessment
    # ------------------------------------------------------

    if stress_percentage < 10:

        stress_comment = (
            "Operational stress remained minimal throughout the "
            "selected reporting period."
        )

    elif stress_percentage < 25:

        stress_comment = (
            "Periodic workload spikes were observed but remained "
            "within manageable limits."
        )

    else:

        stress_comment = (
            "Persistent operational stress suggests growing "
            "capacity constraints across the organization."
        )

    # ------------------------------------------------------
    # Executive Outlook
    # ------------------------------------------------------

    if risk_level == "Low":

        outlook = (
            "Leadership should continue current operational strategy "
            "while monitoring key performance indicators."
        )

    elif risk_level == "Moderate":

        outlook = (
            "Incremental operational improvements are recommended "
            "to strengthen long-term resilience."
        )

    elif risk_level == "High":

        outlook = (
            "Executive leadership should prioritize backlog reduction "
            "and resource optimization."
        )

    else:

        outlook = (
            "Immediate executive intervention is recommended to "
            "restore operational stability."
        )

    return {

        "title": "AI Executive Narrative",

        "icon": "🤖",

        "content": (

            f"{condition}\n\n"

            f"The platform maintained an overall "
            f"health score of {health_score:.1f}% while "
            f"achieving {processing_efficiency:.1f}% "
            f"processing efficiency. Operational stress "
            f"was observed during {stress_percentage:.1f}% "
            f"of reporting periods, resulting in an overall "
            f"{risk_level} organizational risk classification.\n\n"

            f"{efficiency_comment}\n\n"

            f"{stress_comment}\n\n"

            f"{outlook}"

        )

    }

# ==========================================================
# OPERATIONS NARRATIVE
# ==========================================================

def build_operations_narrative(
    health_score,
    processing_efficiency,
    stress_percentage
):
    """
    Generate operational intelligence narrative.
    """

    metrics = format_metrics(
        health_score,
        processing_efficiency,
        stress_percentage,
        "Operational"
    )

    if health_score >= 90:

        conclusion = (
            "Operations remained highly stable with excellent "
            "resource utilization."
        )

    elif health_score >= 75:

        conclusion = (
            "Operations remained resilient despite moderate "
            "workload fluctuations."
        )

    else:

        conclusion = (
            "Operational pressure increased and capacity "
            "optimization should be prioritized."
        )

    return (
        f"Current operational performance achieved "
        f"{metrics['efficiency']} processing efficiency while "
        f"system health remained at {metrics['health']}. "
        f"Operational stress occurred during "
        f"{metrics['stress']} of reporting periods. "
        f"{conclusion}"
    )


# ==========================================================
# PERFORMANCE NARRATIVE
# ==========================================================

def build_performance_narrative(
    processing_efficiency,
    stress_percentage
):
    """
    Generate performance narrative.
    """

    if processing_efficiency >= 90:

        outlook = "Performance exceeded expected operational targets."

    elif processing_efficiency >= 80:

        outlook = "Performance remained stable across the reporting period."

    else:

        outlook = (
            "Performance indicates opportunities for workflow optimization."
        )

    return (
        f"The organization achieved "
        f"{processing_efficiency:.1f}% processing efficiency while "
        f"experiencing operational stress during "
        f"{stress_percentage:.1f}% of reporting periods. "
        f"{outlook}"
    )


# ==========================================================
# RISK NARRATIVE
# ==========================================================

def build_risk_narrative(
    health_score,
    stress_percentage,
    anomaly_count,
    risk_level
):
    """
    Generate executive risk narrative.
    """

    return (
        f"Operational risk is currently classified as "
        f"{risk_level}. The platform maintained a "
        f"{health_score:.1f}% health score while "
        f"{stress_percentage:.1f}% of reporting periods "
        f"experienced elevated operational stress. "
        f"{anomaly_count} operational anomalies were "
        f"identified during analysis."
    )


# ==========================================================
# AI DECISION NARRATIVE
# ==========================================================

def build_ai_narrative(
    health_score,
    processing_efficiency,
    risk_level
):
    """
    Generate AI executive recommendation narrative.
    """

    if health_score >= 85:

        recommendation = (
            "The AI engine recommends maintaining the current "
            "operational strategy while continuing routine monitoring."
        )

    elif health_score >= 70:

        recommendation = (
            "The AI engine recommends targeted operational "
            "optimization and proactive capacity planning."
        )

    else:

        recommendation = (
            "The AI engine recommends immediate executive "
            "intervention to restore operational stability."
        )

    return (
        f"AI Decision Intelligence evaluated a "
        f"{health_score:.1f}% health score with "
        f"{processing_efficiency:.1f}% processing efficiency "
        f"under a {risk_level} risk posture. "
        f"{recommendation}"
    )