"""
rules_engine.py

Business Rules Engine
----------------------------------------------------------

Centralizes business logic, classifications, executive
assessments, and recommendation rules used across the
Care Transition Operational Intelligence Platform.

This module contains NO calculations.
Only decision rules.
"""

# ==========================================================
# PERFORMANCE RULES
# ==========================================================

def get_performance_rating(processing_efficiency):
    """
    Classify overall operational performance.
    """

    if processing_efficiency >= 90:
        return "Excellent"

    if processing_efficiency >= 75:
        return "Good"

    return "Needs Improvement"


def get_performance_assessment(processing_efficiency):
    """
    Executive interpretation of performance.
    """

    if processing_efficiency >= 90:
        return (
            "Operations demonstrated consistently high efficiency "
            "with strong throughput and minimal operational friction."
        )

    if processing_efficiency >= 75:
        return (
            "Operational performance remained stable with moderate "
            "opportunities to improve throughput and reduce backlog."
        )

    return (
        "Performance variability suggests additional operational "
        "optimization, capacity planning, and workflow refinement "
        "are recommended."
    )
    
    
# ==========================================================
# CAPACITY RULES
# ==========================================================

def get_capacity_recommendation(avg_utilization):
    """
    Executive recommendation for capacity utilization.
    """

    if avg_utilization > 90:
        return (
            "Capacity utilization is critically high. "
            "Additional placement resources should be considered."
        )

    if avg_utilization > 75:
        return (
            "Capacity utilization is elevated. Continue "
            "monitoring for sustained growth."
        )

    return (
        "Capacity utilization remains within acceptable "
        "operational limits."
    )
    

# ==========================================================
# STRESS RULES
# ==========================================================

def get_stress_trend_assessment(stress_percent):
    """
    Executive assessment of operational stress.
    """

    if stress_percent < 10:
        return (
            "Operational stress remained consistently low "
            "throughout the reporting period."
        )

    if stress_percent < 20:
        return (
            "Moderate stress events occurred periodically, "
            "suggesting manageable operational pressure."
        )

    if stress_percent < 35:
        return (
            "Frequent stress periods indicate elevated "
            "operational risk requiring continued monitoring."
        )

    return (
        "Persistent operational stress suggests systemic "
        "capacity constraints and elevated organizational risk."
    )
    
    
# ==========================================================
# STABILITY RULES
# ==========================================================

def get_stability_assessment(stability_score):
    """
    Executive assessment of operational stability.
    """

    if stability_score >= 85:
        return (
            "Excellent resilience. The operational pipeline "
            "remained consistently stable."
        )

    if stability_score >= 70:
        return (
            "Generally stable with periodic performance "
            "fluctuations."
        )

    return (
        "Frequent operational instability detected. "
        "Resource allocation and workflow optimisation "
        "should be reviewed."
    )
    

# ==========================================================
# HEALTH RULES
# ==========================================================

def get_health_assessment(health_score):
    """
    Overall operational health assessment.
    """

    if health_score >= 90:
        return (
            "The care transition system demonstrated excellent "
            "operational resilience throughout the reporting period."
        )

    if health_score >= 75:
        return (
            "The system maintained a healthy operational posture "
            "with only moderate periods of stress."
        )

    if health_score >= 60:
        return (
            "Operational performance remained acceptable; however, "
            "recurring stress periods indicate areas requiring "
            "closer monitoring."
        )

    return (
        "The reporting period indicates sustained operational risk. "
        "Immediate leadership attention is recommended."
    )
    
    
# ==========================================================
# RISK RULES
# ==========================================================

def get_primary_risk_driver(
    health_score,
    stress_percent,
    anomaly_count
):
    """
    Determine the dominant operational risk driver.
    """

    if health_score < 60:
        return (
            "Overall system health has declined significantly, "
            "indicating elevated operational vulnerability."
        )

    if stress_percent > 30:
        return (
            "Frequent operational stress periods are the primary "
            "driver of organizational risk."
        )

    if anomaly_count > 10:
        return (
            "Repeated anomaly detection suggests unstable "
            "operational behaviour requiring investigation."
        )

    return (
        "No dominant operational risk driver was identified. "
        "Current system behaviour remains relatively stable."
    )            
     

# ==========================================================
# # RISK ASSESSMENT RULES
# ==========================================================

def get_risk_assessment(health_score):
    """
    Executive summary assessment.
    """

    if health_score >= 90:

        return (
            "The care transition system demonstrated excellent "
            "operational resilience throughout the reporting period. "
            "Risk exposure remained minimal with consistently stable "
            "performance and limited operational disruption."
        )

    if health_score >= 75:

        return (
            "The system maintained a healthy operational posture with "
            "only moderate periods of stress. While several operational "
            "risks emerged, overall resilience remained strong."
        )

    if health_score >= 60:

        return (
            "Operational performance remained acceptable; however, "
            "recurring stress periods and elevated workload indicate "
            "areas requiring closer monitoring and proactive management."
        )

    return (
        "The reporting period indicates sustained operational risk. "
        "Frequent stress events, reduced system resilience, and "
        "operational instability suggest immediate leadership attention "
        "is warranted."
    )


# ==========================================================
# # RISK RECOMMENDATION RULES
# ==========================================================

def get_risk_recommendations(
    health_score,
    stress_percent,
    anomaly_count
):
    """
    Generate executive risk recommendations.
    """

    recommendations = []

    if health_score < 70:

        recommendations.append({

            "title": "🔴 Immediate Action",

            "icon": "💡",

            "message":
                "Increase operational capacity and review staffing allocation "
                "to restore system resilience."

        })

    if stress_percent > 25:

        recommendations.append({

            "title": "🟠 Capacity Planning",

            "icon": "💡",

            "message":
                "Investigate recurring stress periods and implement proactive "
                "resource planning during high-demand intervals."

        })

    if anomaly_count > 10:

        recommendations.append({

            "title": "🟡 Operational Review",

            "icon": "💡",

            "message":
                "Conduct a detailed investigation into recurring anomalies "
                "to identify process inefficiencies or emerging operational risks."

        })

    if not recommendations:

        recommendations.append({

            "title": "🟢 Continue Monitoring",

            "icon": "💡",

            "message":
                "Current operational risk remains within acceptable limits. "
                "Maintain existing monitoring practices and periodic reviews."

        })

    return recommendations
     
# ==========================================================
# PROCESSING EFFICIENCY RULES
# ==========================================================

def get_processing_efficiency_recommendation(
    efficiency
):
    """
    Executive recommendation based on
    processing efficiency.
    """

    if efficiency < 75:

        return {
            "title": "Improve Transfer Efficiency",
            "priority": "🔴 High",
            "message": (
                "Processing efficiency is below the desired "
                "threshold. Review coordination between CBP "
                "and HHS transfers."
            )
        }

    if efficiency < 90:

        return {
            "title": "Monitor Operational Throughput",
            "priority": "🟡 Medium",
            "message": (
                "Current throughput remains acceptable but "
                "should be monitored to prevent future congestion."
            )
        }

    return {
        "title": "Maintain Current Operations",
        "priority": "🟢 Low",
        "message": (
            "Processing efficiency is performing well. "
            "Maintain current operational strategy."
        )
    } 
    
# ==========================================================
# CAPACITY ASSESSMENT
# ==========================================================

def get_capacity_assessment(avg_utilization):
    """
    Executive interpretation of capacity utilization.
    """

    if avg_utilization >= 90:

        return (
            "System capacity is operating near maximum utilization. "
            "Immediate expansion planning is recommended."
        )

    if avg_utilization >= 75:

        return (
            "Capacity utilization remains elevated but manageable. "
            "Continued monitoring is advised."
        )

    return (
        "Operational capacity remains within healthy limits with "
        "adequate flexibility to absorb demand fluctuations."
    )


# ==========================================================
# CBP WORKLOAD
# ==========================================================

def get_cbp_workload_assessment(avg_cbp_load):

    if avg_cbp_load >= 250:

        return (
            "CBP facilities experienced sustained workload pressure "
            "requiring close operational monitoring."
        )

    if avg_cbp_load >= 150:

        return (
            "CBP workload remained moderate with occasional increases "
            "during peak reporting periods."
        )

    return (
        "CBP workload remained stable throughout the reporting period."
    )


# ==========================================================
# HHS CAPACITY
# ==========================================================

def get_hhs_capacity_assessment(
    avg_hhs_load,
    peak_hhs_load
):

    if peak_hhs_load >= 10000:

        return (
            "HHS facilities reached very high occupancy levels, "
            "indicating elevated placement demand."
        )

    if avg_hhs_load >= 7000:

        return (
            "HHS maintained consistently high occupancy while "
            "continuing placement operations."
        )

    return (
        "HHS maintained healthy placement capacity with sufficient "
        "operational flexibility."
    )


# ==========================================================
# BACKLOG
# ==========================================================

def get_backlog_assessment(avg_backlog):

    if avg_backlog >= 3000:

        return (
            "Backlog levels indicate significant operational pressure "
            "requiring intervention."
        )

    if avg_backlog >= 1500:

        return (
            "Backlog remained manageable but should continue to be "
            "closely monitored."
        )

    return (
        "Backlog remained low throughout the reporting period."
    )


# ==========================================================
# UTILIZATION
# ==========================================================

def get_utilization_assessment(utilization):

    if utilization >= 90:

        return (
            "System utilization is approaching operational limits."
        )

    if utilization >= 75:

        return (
            "System utilization remains healthy with moderate pressure."
        )

    return (
        "System utilization remains comfortably within operational capacity."
    )


# ==========================================================
# OPERATIONAL LOAD
# ==========================================================

def get_operational_load_assessment(load):

    if load >= 12000:

        return (
            "Overall operational demand remained consistently high."
        )

    if load >= 8000:

        return (
            "Operational demand remained moderate throughout the reporting period."
        )

    return (
        "Operational demand remained relatively stable."
    )


# ==========================================================
# FLOW BALANCE
# ==========================================================

def get_flow_balance_assessment(flow_balance):

    if flow_balance < -100:

        return (
            "Discharges exceeded transfers, indicating downstream processing pressure."
        )

    if flow_balance > 100:

        return (
            "Transfer activity exceeded discharges, increasing placement workload."
        )

    return (
        "Transfer and discharge activity remained well balanced."
    )               