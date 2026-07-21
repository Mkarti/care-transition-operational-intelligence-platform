"""
ai_decision_engine.py

Business logic for the AI Decision Intelligence dashboard.

This module converts operational, performance, and risk metrics
into executive-ready insights for presentation by the UI layer.
"""


def run_ai_decision_engine(
    summary,
    operations,
    health_score,
    risk_level,
    anomalies
):
    """
    Generate AI Decision insights.
    """

    processing_efficiency = operations["processing_efficiency"]

    return {

        "kpis": build_ai_kpis(
            health_score,
            risk_level,
            processing_efficiency
        ),

        "operational_summary": build_ai_operational_summary(
            summary,
            health_score,
            risk_level,
            anomalies,
            processing_efficiency
        ),

        "predictive_summary": build_predictive_summary(
            summary,
            health_score,
            risk_level,
            anomalies,
            processing_efficiency
        ),

        "decision_simulation": {
            scenario: build_decision_simulation(
                health_score,
                risk_level,
                processing_efficiency,
                scenario
            )
            for scenario in [
                "Increase Staffing",
                "Expand Capacity",
                "Process Optimization"
            ]
        },

        "executive_summary": build_ai_executive_summary(
            health_score,
            risk_level,
            processing_efficiency
        ),

        "recommendations": build_ai_recommendations(
            health_score,
            risk_level,
            processing_efficiency,
            summary["stress_percentage"]
        )

    }
    
    
# ==========================================================
# AI KPI's
# ========================================================== 

def build_ai_kpis(
    health_score,
    risk_level,
    processing_efficiency
):
    """
    Build executive KPI cards for the AI Decision dashboard.
    """

    if health_score < 70:
        priority = "Critical Recovery"

    elif risk_level == "Critical":
        priority = "Risk Mitigation"

    elif processing_efficiency < 80:
        priority = "Operational Optimization"

    else:
        priority = "Maintain Performance"

    confidence = round(
        (health_score + processing_efficiency) / 2,
        1
    )

    return {

        "ai_confidence": {
            "title": "AI Confidence",
            "value": f"{confidence}%",
            "icon": "🧠",
            "subtitle": "AI Confidence"
        },

        "system_health": {
            "title": "System Health",
            "value": f"{health_score:.1f}%",
            "icon": "💚",
            "subtitle": "Overall Health"
        },

        "risk_level": {
            "title": "Risk Level",
            "value": risk_level,
            "icon": "⚠️",
            "subtitle": "Current Status"
        },

        "priority": {
            "title": "Executive Priority",
            "value": priority,
            "icon": "🎯",
            "subtitle": "Recommended Focus"
        }

    }
    

# ==========================================================
# AI Operational Summary
# ========================================================== 
    
def build_ai_operational_summary(
    summary,
    health_score,
    risk_level,
    anomalies,
    processing_efficiency
):
    """
    Build executive operational intelligence cards.
    """

    stress_percent = summary["stress_percentage"]

    # -----------------------------------------------------
    # Current Situation
    # -----------------------------------------------------

    if health_score >= 90:
        situation = (
            "Operations are performing at an excellent level with "
            "minimal signs of system stress."
        )

    elif health_score >= 75:
        situation = (
            "Operations remain stable with occasional periods of "
            "increased workload."
        )

    elif health_score >= 60:
        situation = (
            "System performance is acceptable, although operational "
            "pressure is beginning to affect efficiency."
        )

    else:
        situation = (
            "Operations are under sustained pressure and require "
            "immediate executive attention."
        )

    # -----------------------------------------------------
    # Pattern Detection
    # -----------------------------------------------------

    if stress_percent < 10:

        pattern = (
            "Operational demand remained consistent with no major "
            "stress clusters detected."
        )

    elif stress_percent < 25:

        pattern = (
            "Periodic workload spikes suggest recurring operational "
            "pressure during selected reporting periods."
        )

    else:

        pattern = (
            "Persistent stress patterns indicate structural capacity "
            "constraints across the care transition pipeline."
        )

    # -----------------------------------------------------
    # Operational Driver
    # -----------------------------------------------------

    if processing_efficiency < 70:

        driver = (
            "Reduced transfer efficiency is the primary contributor "
            "to current operational performance."
        )

    elif stress_percent > 25:

        driver = (
            "High operational demand is currently the dominant driver "
            "of system workload."
        )

    else:

        driver = (
            "Operations remain primarily influenced by normal daily "
            "variation rather than systemic issues."
        )

    # -----------------------------------------------------
    # System Status
    # -----------------------------------------------------

    status = (
        f"The platform maintains a health score of "
        f"{health_score:.1f}% with an overall "
        f"{risk_level} risk classification."
    )

    # -----------------------------------------------------
    # Emerging Risks
    # -----------------------------------------------------

    if len(anomalies) > 10:

        future = (
            "Repeated anomaly detection suggests an increased likelihood "
            "of operational disruption if current trends continue."
        )

    elif stress_percent > 20:

        future = (
            "Growing operational pressure may reduce processing "
            "efficiency during future reporting periods."
        )

    else:

        future = (
            "Current operational trends indicate a low probability "
            "of significant disruption."
        )

    # -----------------------------------------------------
    # Executive Insight
    # -----------------------------------------------------

    if health_score >= 85:

        insight = (
            "Maintain existing operational practices while continuing "
            "routine monitoring of performance indicators."
        )

    elif health_score >= 70:

        insight = (
            "Targeted capacity improvements could further strengthen "
            "system resilience and processing efficiency."
        )

    else:

        insight = (
            "Executive intervention should prioritize resource "
            "allocation, backlog reduction, and operational stabilization."
        )

    return {

        "current_situation": {
            "title": "Current Situation",
            "icon": "🤖",
            "content": situation
        },

        "pattern_detection": {
            "title": "Pattern Detection",
            "icon": "🔍",
            "content": pattern
        },

        "operational_driver": {
            "title": "Operational Driver",
            "icon": "🚦",
            "content": driver
        },

        "system_status": {
            "title": "System Status",
            "icon": "💚",
            "content": status
        },

        "emerging_risks": {
            "title": "Emerging Risks",
            "icon": "⚠️",
            "content": future
        },

        "executive_insight": {
            "title": "Executive Insight",
            "icon": "🎯",
            "content": insight
        }

    } 
    

# ==========================================================
# AI Predictive Summary
# ========================================================== 
    
def build_predictive_summary(
    summary,
    health_score,
    risk_level,
    anomalies,
    processing_efficiency
):
    """
    Build AI-generated predictive intelligence cards.
    """

    stress_percent = summary["stress_percentage"]
    anomaly_count = len(anomalies)

    confidence = (
        health_score + processing_efficiency
    ) / 2

    # -----------------------------------------------------
    # Future Outlook
    # -----------------------------------------------------

    if health_score >= 90:

        future_outlook = (
            "Operational performance is expected to remain highly "
            "stable with sustained processing efficiency and minimal "
            "organizational disruption."
        )

    elif health_score >= 75:

        future_outlook = (
            "Current operating conditions suggest stable performance "
            "with only moderate fluctuations expected during future "
            "reporting periods."
        )

    elif health_score >= 60:

        future_outlook = (
            "Increasing operational pressure may gradually affect "
            "system performance if current trends continue."
        )

    else:

        future_outlook = (
            "Without corrective intervention, operational conditions "
            "are likely to deteriorate further due to sustained system "
            "pressure."
        )

    # -----------------------------------------------------
    # Capacity Forecast
    # -----------------------------------------------------

    if stress_percent < 10:

        capacity = (
            "Current operational capacity is expected to remain "
            "sufficient for projected workload."
        )

    elif stress_percent < 25:

        capacity = (
            "Moderate workload growth is anticipated. Resource "
            "planning should continue to ensure operational stability."
        )

    else:

        capacity = (
            "Capacity expansion should be considered as recurring "
            "operational stress is likely to increase future demand."
        )

    # -----------------------------------------------------
    # Risk Projection
    # -----------------------------------------------------

    if risk_level == "Low":

        projection = (
            "Organizational risk is expected to remain low if current "
            "operational practices continue."
        )

    elif risk_level == "Moderate":

        projection = (
            "Risk levels are likely to remain manageable with ongoing "
            "monitoring and incremental process improvements."
        )

    elif risk_level == "High":

        projection = (
            "Operational risk may increase unless backlog growth and "
            "capacity constraints are proactively addressed."
        )

    else:

        projection = (
            "Critical operational risk is projected to persist without "
            "immediate executive intervention."
        )

    # -----------------------------------------------------
    # System Stability
    # -----------------------------------------------------

    if anomaly_count < 5:

        stability = (
            "System behaviour remains consistent with a low probability "
            "of significant operational disruption."
        )

    elif anomaly_count < 10:

        stability = (
            "Several operational anomalies warrant continued monitoring "
            "to maintain long-term stability."
        )

    else:

        stability = (
            "Persistent anomaly activity increases the likelihood of "
            "future operational instability."
        )

    # -----------------------------------------------------
    # Forecast Confidence
    # -----------------------------------------------------

    if confidence >= 90:

        confidence_text = (
            "Forecast confidence is very high because operational "
            "indicators remain consistently stable."
        )

    elif confidence >= 80:

        confidence_text = (
            "Forecast confidence is high with strong agreement across "
            "health, efficiency, and risk indicators."
        )

    elif confidence >= 70:

        confidence_text = (
            "Forecast confidence is moderate due to emerging operational "
            "variability."
        )

    else:

        confidence_text = (
            "Forecast confidence is limited because current operational "
            "conditions remain highly dynamic."
        )

    # -----------------------------------------------------
    # Executive Outlook
    # -----------------------------------------------------

    if health_score >= 85:

        outlook = (
            "Leadership should maintain current operational strategy "
            "while continuing routine performance monitoring."
        )

    elif health_score >= 70:

        outlook = (
            "Targeted operational improvements and proactive capacity "
            "planning will strengthen long-term resilience."
        )

    else:

        outlook = (
            "Executive leadership should prioritize immediate capacity "
            "optimization, backlog reduction, and operational recovery."
        )

    return {

        "future_outlook": {
            "title": "Future Outlook",
            "icon": "🔮",
            "content": future_outlook
        },

        "capacity_forecast": {
            "title": "Capacity Forecast",
            "icon": "🏥",
            "content": capacity
        },

        "risk_projection": {
            "title": "Risk Projection",
            "icon": "⚠️",
            "content": projection
        },

        "system_stability": {
            "title": "System Stability",
            "icon": "🛡️",
            "content": stability
        },

        "forecast_confidence": {
            "title": "Forecast Confidence",
            "icon": "🤖",
            "content": confidence_text
        },

        "executive_outlook": {
            "title": "Executive Outlook",
            "icon": "🎯",
            "content": outlook
        }

    }       


# ==========================================================
# AI Decision Simulation
# ========================================================== 

def build_decision_simulation(
    health_score,
    risk_level,
    processing_efficiency,
    scenario
):
    """
    Simulate the projected impact of executive decisions.
    """

    projected_health = health_score
    projected_efficiency = processing_efficiency
    projected_risk = risk_level

    # -----------------------------------------------------
    # Scenario Simulation
    # -----------------------------------------------------

    if scenario == "Increase Staffing":

        projected_health += 4
        projected_efficiency += 6

        benefit = (
            "Additional staffing is expected to reduce operational "
            "delays and improve throughput across the care pipeline."
        )

        tradeoff = (
            "Requires increased staffing expenditure and workforce "
            "planning before measurable improvements occur."
        )

    elif scenario == "Expand Capacity":

        projected_health += 6
        projected_efficiency += 3

        benefit = (
            "Expanded HHS capacity should reduce backlog accumulation "
            "and improve organizational resilience."
        )

        tradeoff = (
            "Infrastructure expansion requires significant investment "
            "and implementation time."
        )

    else:

        projected_health += 5
        projected_efficiency += 10

        benefit = (
            "Workflow optimization improves transfer efficiency without "
            "major infrastructure expansion."
        )

        tradeoff = (
            "Process redesign requires organizational coordination and "
            "change management."
        )

    projected_health = min(projected_health, 100)
    projected_efficiency = min(projected_efficiency, 100)

    # -----------------------------------------------------
    # Risk Projection
    # -----------------------------------------------------

    if projected_health >= 90:

        projected_risk = "Low"

    elif projected_health >= 75:

        projected_risk = "Moderate"

    elif projected_health >= 60:

        projected_risk = "High"

    else:

        projected_risk = "Critical"

    # -----------------------------------------------------
    # Expected Outcome
    # -----------------------------------------------------

    if projected_health >= 90:

        outcome = "Excellent Stability"

    elif projected_health >= 75:

        outcome = "Improved Operations"

    elif projected_health >= 60:

        outcome = "Moderate Improvement"

    else:

        outcome = "Requires Further Action"

    return {

        "kpis": {

            "projected_health": {

                "title": "Projected Health",

                "value": f"{projected_health:.1f}%",

                "icon": "💚",

                "subtitle": "Estimated Outcome"

            },

            "projected_efficiency": {

                "title": "Projected Efficiency",

                "value": f"{projected_efficiency:.1f}%",

                "icon": "⚙️",

                "subtitle": "Expected Processing"

            },

            "projected_risk": {

                "title": "Projected Risk",

                "value": projected_risk,

                "icon": "⚠️",

                "subtitle": "Estimated Risk"

            },

            "expected_outcome": {

                "title": "Expected Outcome",

                "value": outcome,

                "icon": "🎯",

                "subtitle": "Simulation Result"

            }

        },

        "strategic_impact": {

            "title": "Strategic Impact",

            "icon": "📈",

            "content": benefit

        },

        "expected_benefits": {

            "title": "Expected Benefits",

            "icon": "✅",

            "content": (
                "Higher operational throughput, reduced backlog "
                "pressure, improved care transitions, and stronger "
                "organizational resilience."
            )

        },

        "tradeoffs": {

            "title": "Potential Trade-offs",

            "icon": "⚖️",

            "content": tradeoff

        },

        "recommendation": {

            "title": "Executive Recommendation",

            "icon": "🧠",

            "content": (
                f"Based on the current operational profile, "
                f"'{scenario}' is projected to improve system "
                f"health to {projected_health:.1f}% while "
                f"maintaining a {projected_risk} risk posture."
            )

        }

    }  
    
    
# ==========================================================
# AI Executive Summary
# ==========================================================  
   
def build_ai_executive_summary(
    health_score,
    risk_level,
    processing_efficiency
):
    """
    Build the executive AI summary.
    """

    situation = (

        f"The platform is currently operating with "
        f"a health score of {health_score:.1f}% "
        f"and an operational efficiency of "
        f"{processing_efficiency:.1f}%. "
        f"The overall organizational risk "
        f"is classified as {risk_level}."

    )

    if health_score >= 90:

        interpretation = (

            "Operational performance remains excellent. "
            "Leadership should maintain current strategy "
            "while continuing routine monitoring."

        )

    elif health_score >= 75:

        interpretation = (

            "The organization is performing well with "
            "moderate operational risk. Incremental "
            "optimization will further improve resilience."

        )

    elif health_score >= 60:

        interpretation = (

            "Operational pressure is increasing. "
            "Leadership should prioritize capacity "
            "optimization and backlog reduction."

        )

    else:

        interpretation = (

            "Critical operational conditions detected. "
            "Immediate executive intervention is "
            "recommended to restore system stability."

        )

    return {

        "executive_situation": {

            "title": "Executive Situation",
            "icon": "📋",
            "content": situation

        },

        "executive_interpretation": {

            "title": "Executive Interpretation",
            "icon": "🧠",
            "content": interpretation

        }

    }
  
    
# ==========================================================
# AI Recommendations
# ========================================================== 
  
def build_ai_recommendations(
    health_score,
    risk_level,
    processing_efficiency,
    stress_percentage
):
    """
    Build executive AI recommendations.
    """

    recommendations = []

    # -----------------------------------------------------
    # Operational Stability
    # -----------------------------------------------------

    if health_score < 70:

        recommendations.append({

            "title": "Restore System Stability",

            "icon": "🚨",

            "message": (
                "Prioritize immediate operational stabilization by "
                "reducing backlog, reallocating resources, and "
                "increasing processing capacity."
            )

        })

    # -----------------------------------------------------
    # Processing Efficiency
    # -----------------------------------------------------

    if processing_efficiency < 80:

        recommendations.append({

            "title": "Improve Processing Efficiency",

            "icon": "⚙️",

            "message": (
                "Review transfer workflows between CBP and HHS to "
                "minimize delays and improve throughput."
            )

        })

    # -----------------------------------------------------
    # Capacity Planning
    # -----------------------------------------------------

    if stress_percentage > 25:

        recommendations.append({

            "title": "Expand Capacity Planning",

            "icon": "📈",

            "message": (
                "Implement proactive staffing and resource planning "
                "during recurring high-demand periods."
            )

        })

    # -----------------------------------------------------
    # Risk Monitoring
    # -----------------------------------------------------

    if risk_level in ["High", "Critical"]:

        recommendations.append({

            "title": "Strengthen Risk Monitoring",

            "icon": "🛡️",

            "message": (
                "Increase monitoring frequency and establish "
                "early-warning alerts for emerging operational risks."
            )

        })

    # -----------------------------------------------------
    # Healthy System
    # -----------------------------------------------------

    if not recommendations:

        recommendations.append({

            "title": "Maintain Current Strategy",

            "icon": "✅",

            "message": (
                "Operational performance remains strong. Continue "
                "monitoring key indicators while pursuing "
                "incremental improvements."
            )

        })

    conclusion = {

        "title": "AI Executive Conclusion",

        "icon": "🧠",

        "message": (

            "Based on operational performance, organizational risk, "
            "and system efficiency, the AI Decision Intelligence engine "
            "recommends prioritizing sustainable operational improvements "
            "while continuously monitoring emerging risks to maintain a "
            "resilient care transition pipeline."

        )

    }

    return {

        "recommendations": recommendations,

        "conclusion": conclusion

    }          