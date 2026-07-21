"""
executive_summary_engine.py

Executive Summary Engine
----------------------------------------------------------

Generates executive-ready narrative summaries for dashboard components.

This module contains NO calculations.

It converts metrics into leadership-friendly insights.
"""

from utils.metrics_engine import (
    calculate_average_capacity_utilization,
    calculate_average_cbp_backlog,
    calculate_average_cbp_load,
    calculate_average_hhs_backlog,
    calculate_average_hhs_load,
    calculate_average_throughput,
    calculate_average_transfer,
    calculate_minimum_throughput,
    calculate_peak_hhs_load,
    calculate_peak_throughput,
    get_total_anomalies
)

from utils.operations_engine import calculate_average_backlogs

from utils.rules_engine import (
    get_capacity_assessment,
    get_capacity_recommendation,
    get_cbp_workload_assessment,
    get_hhs_capacity_assessment,
    get_primary_risk_driver,
    get_processing_efficiency_recommendation,
    get_risk_assessment,
    get_risk_recommendations,
    get_stability_assessment,
    get_stress_trend_assessment
)

from utils.insight_formatter import build_executive_card

from utils.narrative_engine import build_executive_narrative


# ==========================================================
# AVERAGE CAPACITY UTILIZATION
# ==========================================================

def calculate_average_capacity_utilization(df):

    return round(
        df["capacity_utilization"].mean(),
        2
    )


# ==========================================================
# AVERAGE CBP LOAD
# ==========================================================

def calculate_average_cbp_load(df):

    return round(
        df["children_in_cbp_custody"].mean(),
        2
    )


# ==========================================================
# AVERAGE HHS LOAD
# ==========================================================

def calculate_average_hhs_load(df):

    return round(
        df["children_in_hhs_care"].mean(),
        2
    )


# ==========================================================
# PEAK HHS LOAD
# ==========================================================

def calculate_peak_hhs_load(df):

    return int(
        df["children_in_hhs_care"].max()
    )
    

# ==========================================================
# CAPACITY SUMMARY
# ==========================================================

def build_capacity_summary(df):

    avg_utilization = calculate_average_capacity_utilization(df)

    avg_cbp = calculate_average_backlogs(df)["cbp"]

    avg_hhs = calculate_average_backlogs(df)["hhs"]

    avg_cbp_load = calculate_average_cbp_load(df)

    avg_hhs_load = calculate_average_hhs_load(df)

    peak_hhs_load = calculate_peak_hhs_load(df)

    return {

        "kpis": {

            "average_cbp_load": {

                "title": "Average CBP Load",

                "value": f"{avg_cbp_load:.0f}",

                "icon": "🚔",

                "subtitle": "Children"

            },

            "average_hhs_load": {

                "title": "Average HHS Load",

                "value": f"{avg_hhs_load:.0f}",

                "icon": "🏥",

                "subtitle": "Children"

            },

            "peak_hhs_capacity": {

                "title": "Peak HHS Capacity",

                "value": f"{peak_hhs_load:.0f}",

                "icon": "📈",

                "subtitle": "Highest Occupancy"

            },

            "average_utilization": {

                "title": "Average Utilization",

                "value": f"{avg_utilization:.1f}%",

                "icon": "⚡",

                "subtitle": "Capacity"

            }

        },

        "capacity_assessment": {

            "title": "Capacity Assessment",

            "icon": "🏥",

            "content": get_capacity_assessment(
                avg_utilization
            )

        },

        "cbp_workload": {

            "title": "CBP Workload",

            "icon": "🚔",

            "content": get_cbp_workload_assessment(
                avg_cbp_load
            )

        },

        "hhs_capacity": {

            "title": "HHS Capacity",

            "icon": "🏥",

            "content": get_hhs_capacity_assessment(
                avg_hhs_load,
                peak_hhs_load
            )

        },

        "recommendation": {

            "title": "Executive Recommendation",

            "icon": "💡",

            "content": get_capacity_recommendation(
                avg_utilization
            )

        }

    }

    
# ==========================================================
# OPERATIONS SUMMARY
# ==========================================================

def build_operations_summary(
    summary,
    bottlenecks,
    processing_efficiency
):
    """
    Build executive narrative for the Operations dashboard.
    """

    if bottlenecks.empty:

        operational_status = {

            "title": "Operational Status",

            "icon": "✅",

            "content": (
                "No abnormal congestion patterns "
                "were identified."
            )

        }

    else:

        operational_status = {

            "title": "Operational Alert",

            "icon": "🚨",

            "content": (
                f"{len(bottlenecks)} bottleneck periods "
                "require operational review."
            )

        }

    return {

        "processing_efficiency": {

            "title": "Processing Efficiency",

            "icon": "⚡",

            "content": (
                f"The overall transfer efficiency is "
                f"{processing_efficiency:.2f}%. "
                "Higher values indicate smoother "
                "transitions from CBP custody into "
                "HHS care."
            )

        },

        "backlog_assessment": {

            "title": "Backlog Assessment",

            "icon": "📊",

            "content": (
                f"Average CBP backlog is "
                f"{summary['avg_cbp_backlog']:.1f}, "
                f"while average HHS backlog is "
                f"{summary['avg_hhs_backlog']:.1f}."
            )

        },

        "operational_capacity": {

            "title": "Operational Capacity",

            "icon": "🏥",

            "content": (
                f"Peak CBP backlog reached "
                f"{summary['peak_cbp']} children, "
                f"while HHS peaked at "
                f"{summary['peak_hhs']}."
            )

        },

        "operational_status": operational_status

    }
    

# ==========================================================
# BOTTLENECK SUMMARY
# ==========================================================

def build_bottleneck_summary(bottlenecks):
    """
    Build executive bottleneck intelligence.
    """
    
    total = len(bottlenecks)

    if total:

        max_cbp = bottlenecks["cbp_backlog"].max()

        max_hhs = bottlenecks["hhs_backlog"].max()

        avg_flow = bottlenecks["net_flow"].mean()

    else:

        max_cbp = 0
        max_hhs = 0
        avg_flow = 0
        
    if bottlenecks.empty:

        message = (
            "Operational flow remained stable throughout "
            "the reporting period with no significant "
            "capacity disruptions."
        )

        recommendation_text = (
            "Continue routine operational monitoring."
        )

    else:

        message = (
            f"{len(bottlenecks)} congestion periods were "
            "identified where system backlog exceeded "
            "expected operational thresholds."
        )

        recommendation_text = (
            "Review staffing levels, transfer timing and "
            "placement capacity during identified periods."
        )    

    kpis = {

            "bottlenecks": {

                "title": "Bottlenecks",

                "value": total,

                "icon": "🚧",

                "subtitle": "Detected"

            },

            "peak_cbp": {

                "title": "Peak CBP",

                "value": int(max_cbp),

                "icon": "🚔",

                "subtitle": "Children"

            },

            "peak_hhs": {

                "title": "Peak HHS",

                "value": int(max_hhs),

                "icon": "🏥",

                "subtitle": "Children"

            },

            "average_flow": {

                "title": "Average Net Flow",

                "value": f"{avg_flow:.1f}",

                "icon": "➡️",

                "subtitle": "Transfer Rate"

            }

        }

    assessment = {

        "title": "Operational Assessment",

        "icon": "📊",

        "content": message

    }

    recommendation = {

        "title": "Recommended Action",

        "icon": "💡",

        "content": recommendation_text

    }

    return {

        "kpis": kpis,

        "assessment": assessment,

        "recommendation": recommendation

    }    


# ==========================================================
# RISK SUMMARY
# ==========================================================

def build_risk_summary(
    summary,
    health_score,
    risk_level,
    anomalies
):
    """
    Build executive summary for the Risk Intelligence dashboard.
    """

    total_anomalies = get_total_anomalies(
        anomalies
    )

    return {

        "kpis": {

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

            "stress_days": {

                "title": "Stress Days",

                "value": summary["total_stress_days"],

                "icon": "📈",

                "subtitle": "Operational Pressure"

            },

            "anomalies": {

                "title": "Anomalies",

                "value": total_anomalies,

                "icon": "🚨",

                "subtitle": "Detected Events"

            }

        },

        "trend_summary": {

            "stress_trend": {

                "title": "Stress Trend",

                "icon": "📈",

                "content": (
                    f"The reporting period recorded "
                    f"{summary['total_stress_days']} operational stress days, "
                    f"representing {summary['stress_percentage']:.1f}% "
                    "of all observations."
                )

            },

            "executive_interpretation": {

                "title": "Executive Interpretation",

                "icon": "🧠",

                "content": get_stress_trend_assessment(
                    summary["stress_percentage"]
                )

            }

        },

        "risk_intelligence": {

            "primary_risk_driver": {

                "title": "Primary Risk Driver",

                "icon": "🚨",

                "content": get_primary_risk_driver(
                    health_score,
                    summary["stress_percentage"],
                    total_anomalies
                )

            },

            "system_resilience": {

                "title": "System Resilience",

                "icon": "🛡️",

                "content": (
                    f"The platform currently maintains a "
                    f"{health_score:.1f}% system health score "
                    f"with an overall risk classification of "
                    f"{risk_level}."
                )

            },

            "operational_stress": {

                "title": "Operational Stress",

                "icon": "📈",

                "content": (
                    f"{summary['total_stress_days']} stress days "
                    f"were detected during the reporting period "
                    f"({summary['stress_percentage']:.1f}% of observations)."
                )

            },

            "anomaly_assessment": {

                "title": "Anomaly Assessment",

                "icon": "🔍",

                "content": (
                    f"{total_anomalies} operational anomalies "
                    "were identified across monitored indicators, "
                    "providing early warning signals for potential "
                    "system instability."
                )

            }

        },
        
        "executive_summary": {

            "overall_risk_assessment": {

                "title": "Overall Risk Assessment",

                "icon": "📋",

                "content": get_risk_assessment(
                    health_score
                )

            },

            "operational_summary": {

                "title": "Operational Summary",

                "icon": "📊",

                "content": (
                    f"The reporting period recorded "
                    f"{summary['total_stress_days']} operational stress days "
                    f"({summary['stress_percentage']:.1f}% of all observations) "
                    f"with an overall system health score of "
                    f"{health_score:.1f}%."
                )

            },

            "executive_outlook": {

                "title": "Executive Outlook",

                "icon": "🎯",

                "content": (
                    f"The system is currently classified as "
                    f"{risk_level} risk with "
                    f"{total_anomalies} detected operational anomalies. "
                    "Continued monitoring and targeted interventions "
                    "will help sustain long-term system stability."
                )

            }

        },

    }


# ==========================================================
# PERFORMANCE KPI SUMMARY
# ==========================================================

def build_performance_kpi_summary(
    df,
    processing_efficiency
):
    """
    Build executive KPI summary for the
    Performance Intelligence dashboard.
    """

    avg_daily_transfers = calculate_average_transfer(df)

    avg_daily_throughput = calculate_average_throughput(df)

    peak_daily_throughput = calculate_peak_throughput(df)

    return {

        "processing_efficiency": {

            "title": "Processing Efficiency",

            "value": f"{processing_efficiency:.1f}%",

            "icon": "⚡",

            "subtitle": "Average System Efficiency"

        },

        "daily_throughput": {

            "title": "Daily Throughput",

            "value": f"{avg_daily_throughput:.0f}",

            "icon": "📈",

            "subtitle": "Average Children Processed"

        },

        "daily_transfers": {

            "title": "Daily Transfers",

            "value": f"{avg_daily_transfers:.0f}",

            "icon": "➡️",

            "subtitle": "Average CBP → HHS"

        },

        "peak_throughput": {

            "title": "Peak Throughput",

            "value": f"{peak_daily_throughput:.0f}",

            "icon": "🚀",

            "subtitle": "Highest Daily Processing"

        }

    }


# ==========================================================
# PERFORMANCE TREND SUMMARY
# ==========================================================

def build_performance_trend_summary():
    """
    Build executive summary for Performance Trends.
    """

    return {

        "efficiency_trend": {

            "title": "Efficiency Trend",

            "icon": "⚡",

            "content": (
                "Rolling efficiency illustrates how consistently "
                "the system processes children over time. Stable "
                "performance reflects resilient operational capacity."
            )

        },

        "capacity_trend": {

            "title": "Capacity Trend",

            "icon": "🏥",

            "content": (
                "Capacity utilization and backlog trends help identify "
                "whether demand is approaching operational limits or "
                "remaining within sustainable levels."
            )

        }

    }


# ==========================================================
# PERFORMANCE BENCHMARK SUMMARY
# ==========================================================

def build_performance_benchmark_summary(
    df
):
    """
    Build executive summary for Performance Benchmarking.
    """

    throughput = (
        df["children_transferred_out_of_cbp_custody"] +
        df["children_discharged_from_hhs_care"]
    )

    avg_throughput = calculate_average_throughput(df)

    peak_throughput = calculate_peak_throughput(df)

    min_throughput = calculate_minimum_throughput(df)

    throughput_std = throughput.std()

    consistency = max(
        0,
        100 - (throughput_std / avg_throughput * 100)
    )

    if consistency >= 90:

        consistency_message = (
            "Operational performance is highly consistent "
            "with minimal day-to-day variation."
        )

    elif consistency >= 75:

        consistency_message = (
            "Performance is generally stable with "
            "occasional fluctuations."
        )

    else:

        consistency_message = (
            "Significant variability exists across "
            "daily operations. Additional monitoring "
            "is recommended."
        )

    return {

        "kpis": {

            "average_throughput": {

                "title": "Average Throughput",

                "value": f"{avg_throughput:.0f}",

                "icon": "📊",

                "subtitle": "Daily Average"

            },

            "peak_throughput": {

                "title": "Peak Throughput",

                "value": f"{peak_throughput:.0f}",

                "icon": "🚀",

                "subtitle": "Best Performance"

            },

            "lowest_throughput": {

                "title": "Lowest Throughput",

                "value": f"{min_throughput:.0f}",

                "icon": "📉",

                "subtitle": "Weakest Day"

            },

            "consistency": {

                "title": "Consistency",

                "value": f"{consistency:.1f}%",

                "icon": "🎯",

                "subtitle": "Operational Stability"

            }

        },

        "benchmark": {

            "title": "Performance Benchmark",

            "icon": "🏆",

            "content": (
                f"The system averages approximately "
                f"{avg_throughput:.0f} processed children "
                f"per day, reaching a historical peak of "
                f"{peak_throughput:.0f}."
            )

        },

        "consistency_assessment": {

            "title": "Consistency Assessment",

            "icon": "📈",

            "content": consistency_message

        }

    }


# ==========================================================
# STABILITY SUMMARY
# ==========================================================

def build_stability_summary(df):
    """
    Build executive stability summary for the
    Performance Intelligence dashboard.
    """

    throughput = (
        df["children_transferred_out_of_cbp_custody"] +
        df["children_discharged_from_hhs_care"]
    )

    mean = throughput.mean()

    std = throughput.std()

    stable_days = (
        (throughput >= mean - std) &
        (throughput <= mean + std)
    ).sum()

    peak_days = (
        throughput > mean + std
    ).sum()

    unstable_days = (
        throughput < mean - std
    ).sum()

    total_days = len(df)

    stability_score = stable_days / total_days * 100

    return {

        "kpis": {

            "stable_days": {
                "title": "Stable Days",
                "value": stable_days,
                "icon": "🟢",
                "subtitle": "Expected Performance"
            },

            "peak_days": {
                "title": "Peak Days",
                "value": peak_days,
                "icon": "🚀",
                "subtitle": "Above Average"
            },

            "unstable_days": {
                "title": "Unstable Days",
                "value": unstable_days,
                "icon": "🔴",
                "subtitle": "Below Average"
            },

            "stability_score": {
                "title": "Stability Score",
                "value": f"{stability_score:.1f}%",
                "icon": "🛡️",
                "subtitle": "Operational Resilience"
            }

        },

        "operational_stability": {

            "title": "Operational Stability",

            "icon": "🛡️",

            "content": (
                f"The system maintained expected operational "
                f"performance during {stable_days} of "
                f"{total_days} reporting days."
            )

        },

        "executive_assessment": {

            "title": "Executive Assessment",

            "icon": "📈",

            "content": get_stability_assessment(
                stability_score
            )

        }

    }
    

# ==========================================================
# PERFORMANCE EXECUTIVE SUMMARY
# ==========================================================

def build_performance_summary(
    processing_efficiency,
    performance_rating,
    performance_assessment,
    average_throughput,
    combined_backlog,
    peak_throughput
):
    """
    Build executive summary for the
    Performance Intelligence dashboard.
    """

    return {

        "operational_performance": {

            "title": "Operational Performance",

            "icon": "⚙️",

            "content": (
                f"The care transition system maintained an average "
                f"daily throughput of {average_throughput:.1f} children "
                f"while achieving an overall processing efficiency of "
                f"{processing_efficiency:.1f}%."
            )

        },

        "capacity_management": {

            "title": "Capacity Management",

            "icon": "🏥",

            "content": (
                f"Average combined operational backlog remained at "
                f"{combined_backlog:.1f} children across CBP and HHS, "
                "reflecting current system demand and resource utilization."
            )

        },

        "executive_assessment": {

            "title": f"Executive Assessment — {performance_rating}",

            "icon": "🧠",

            "content": performance_assessment

        },

        "peak_performance": {

            "title": "Peak System Performance",

            "icon": "🚀",

            "content": (
                f"The highest observed operational throughput reached "
                f"{peak_throughput:.0f} children processed in a single day, "
                "demonstrating the system's maximum observed capacity."
            )

        }

    }


# ==========================================================
# EXECUTIVE KPI SUMMARY
# ==========================================================

def build_executive_kpi_summary(insights):
    """
    Build executive KPI cards for the Executive Dashboard.
    """

    summary = insights["summary"]

    health_score = insights["health_score"]

    risk_level = insights["risk_level"]

    operations = insights["operations"]

    processing_efficiency = operations["processing_efficiency"]

    return {

        "health_score": {

            "title": "System Health",

            "value": f"{health_score:.1f}%",

            "icon": "💚",

            "subtitle": "Overall Health"

        },

        "processing_efficiency": {

            "title": "Processing Efficiency",

            "value": f"{processing_efficiency:.1f}%",

            "icon": "⚡",

            "subtitle": "Transfer Efficiency"

        },

        "risk_level": {

            "title": "Risk Level",

            "value": risk_level,

            "icon": "⚠️",

            "subtitle": "Current Status"

        },

        "stress_days": {

            "title": "Stress Days",

            "value": summary["total_stress_days"],

            "icon": "📈",

            "subtitle": "Operational Pressure"

        }

    }
    

# ==========================================================
# EXECUTIVE BRIEF
# ==========================================================

def build_executive_brief(insights):
    """
    Build a dynamic executive briefing for leadership.
    """

    health_score = insights["health_score"]
    risk_level = insights["risk_level"]
    processing_efficiency = insights["operations"]["processing_efficiency"]
    stress_percentage = insights["summary"]["stress_percentage"]

    # ------------------------------------------------------
    # Executive Summary
    # ------------------------------------------------------

    summary = (
        f"The organization is currently operating with a "
        f"{health_score:.1f}% system health score and "
        f"{processing_efficiency:.1f}% operational efficiency. "
        f"Overall organizational risk is classified as "
        f"{risk_level}."
    )

    # ------------------------------------------------------
    # Primary Driver
    # ------------------------------------------------------

    if stress_percentage > 25:

        driver = (
            "Persistent operational stress is the primary factor "
            "affecting overall system performance."
        )

    elif processing_efficiency < 80:

        driver = (
            "Reduced processing efficiency is currently limiting "
            "overall operational throughput."
        )

    else:

        driver = (
            "Current performance is largely influenced by routine "
            "operational workload fluctuations."
        )

    # ------------------------------------------------------
    # Business Impact
    # ------------------------------------------------------

    if risk_level == "Critical":

        impact = (
            "Current operating conditions significantly increase "
            "the likelihood of service disruption and delayed care transitions."
        )

    elif risk_level == "High":

        impact = (
            "Operational resilience is beginning to decline, "
            "requiring proactive executive oversight."
        )

    elif risk_level == "Moderate":

        impact = (
            "Operations remain stable, although targeted improvements "
            "would strengthen long-term resilience."
        )

    else:

        impact = (
            "Current operational conditions remain stable with "
            "minimal organizational risk."
        )

    # ------------------------------------------------------
    # Executive Action
    # ------------------------------------------------------

    if health_score < 70:

        action = (
            "Prioritize backlog reduction, capacity expansion, and "
            "resource allocation to stabilize operations."
        )

    elif health_score < 85:

        action = (
            "Continue optimizing operational workflows while "
            "closely monitoring system performance."
        )

    else:

        action = (
            "Maintain current operational strategy and continue "
            "routine executive monitoring."
        )

    return {

        "title": "Executive Brief",

        "icon": "🧠",

        "summary": summary,

        "driver": driver,

        "impact": impact,

        "action": action

    }
    
    
# ==========================================================
# EXECUTIVE ALERT SUMMARY
# ==========================================================

def build_executive_alerts(alerts):
    """
    Build executive alert summary.
    """

    return alerts
    

# ==========================================================
# EXECUTIVE TREND SUMMARY
# ==========================================================

def build_executive_trend_summary():
    """
    Build executive narrative for the Executive Trend
    Analysis section.
    """

    return {

        "system_load": {

            "title": "System Load",

            "icon": "📈",

            "content": (
                "System load trends provide leadership with an "
                "overall view of operational demand across the "
                "reporting period, highlighting periods of "
                "increased workload and resource utilization."
            )

        },

        "throughput": {

            "title": "Throughput Performance",

            "icon": "🚀",

            "content": (
                "Daily throughput reflects the organization's "
                "ability to consistently process children through "
                "the care transition pipeline while maintaining "
                "operational continuity."
            )

        },

        "backlog": {

            "title": "Backlog Trend",

            "icon": "📊",

            "content": (
                "Backlog trends help identify whether operational "
                "pressure is increasing, stabilizing or declining, "
                "supporting proactive capacity planning and "
                "resource allocation."
            )

        }

    }           


# ==========================================================
# EXECUTIVE HEALTH SUMMARY
# ==========================================================

def build_executive_health_summary(insights):
    """
    Build executive health summary for the
    Executive Dashboard.
    """

    # -----------------------------------------------------
    # Extract Metrics
    # -----------------------------------------------------

    health_score = insights.get("health_score", 0)

    risk_level = insights.get("risk_level", "Unknown")

    operations = insights.get("operations", {})

    processing_efficiency = operations.get(
        "processing_efficiency",
        0
    )

    # -----------------------------------------------------
    # Operational Status Narrative
    # -----------------------------------------------------

    if health_score >= 90:

        operational_status_text = (
            "Operations are performing exceptionally well with "
            "minimal system stress and excellent organizational "
            "stability."
        )

    elif health_score >= 75:

        operational_status_text = (
            "Operations remain stable with only moderate workload "
            "variations across the reporting period."
        )

    elif health_score >= 60:

        operational_status_text = (
            "Operational pressure is beginning to affect system "
            "performance and should be monitored closely."
        )

    else:

        operational_status_text = (
            "Operations are experiencing sustained stress that "
            "requires immediate executive attention."
        )

    # -----------------------------------------------------
    # Operational Risk Narrative
    # -----------------------------------------------------

    if risk_level == "Low":

        operational_risk_text = (
            "Current organizational risk remains low with no major "
            "operational concerns."
        )

    elif risk_level == "Moderate":

        operational_risk_text = (
            "Moderate operational risks should continue to be monitored "
            "through routine executive oversight."
        )

    elif risk_level == "High":

        operational_risk_text = (
            "High operational risk requires proactive mitigation to "
            "prevent service disruption."
        )

    else:

        operational_risk_text = (
            "Critical operational risk demands immediate executive "
            "intervention."
        )

    # -----------------------------------------------------
    # System Performance Narrative
    # -----------------------------------------------------

    if processing_efficiency >= 90:

        performance_text = (
            "Processing efficiency remains excellent across the care "
            "transition pipeline."
        )

    elif processing_efficiency >= 80:

        performance_text = (
            "Operational performance remains strong with opportunities "
            "for incremental optimization."
        )

    elif processing_efficiency >= 70:

        performance_text = (
            "Processing efficiency is acceptable but additional workflow "
            "improvements are recommended."
        )

    else:

        performance_text = (
            "Processing efficiency is below the desired threshold and "
            "requires workflow optimization."
        )

    # -----------------------------------------------------
    # Build Executive Cards
    # -----------------------------------------------------

    operational_status = build_executive_card(
        title="Operational Status",
        icon="💚",
        status=f"{health_score:.1f}%",
        summary=operational_status_text,
        recommendation=(
            "Continue monitoring operational health while maintaining "
            "current workflow performance."
        ),
        impact=(
            "Stable operations improve organizational resilience and "
            "maintain uninterrupted care transitions."
        )
    )

    operational_risk = build_executive_card(
        title="Operational Risk",
        icon="⚠️",
        status=risk_level,
        summary=operational_risk_text,
        recommendation=(
            "Monitor workload spikes and strengthen early warning "
            "mechanisms across the operational pipeline."
        ),
        impact=(
            "Early mitigation reduces backlog growth and prevents "
            "future operational disruption."
        )
    )

    system_performance = build_executive_card(
        title="System Performance",
        icon="📈",
        status=f"{processing_efficiency:.1f}%",
        summary=performance_text,
        recommendation=(
            "Continue improving transfer efficiency through workflow "
            "optimization and proactive resource allocation."
        ),
        impact=(
            "Higher processing efficiency leads to faster transitions "
            "and stronger organizational performance."
        )
    )

    # -----------------------------------------------------
    # Return
    # -----------------------------------------------------

    return {

        "health_score": health_score,

        "operational_status": operational_status,

        "operational_risk": operational_risk,

        "system_performance": system_performance

    }


# ==========================================================
# OPERATIONS RECOMMENDATIONS
# ==========================================================

def build_operations_recommendations(
    summary,
    bottlenecks,
    processing_efficiency
):
    """
    Build executive recommendations for the
    Operations Intelligence dashboard.
    """

    recommendations = []

    recommendations.append(
        get_processing_efficiency_recommendation(
            processing_efficiency
        )
    )

    if summary["avg_cbp_backlog"] > summary["avg_hhs_backlog"]:

        recommendations.append({

            "title": "Reduce CBP Backlog",

            "priority": "🟡 Medium",

            "message":
                "Average CBP backlog exceeds downstream capacity. "
                "Increase transfer frequency where possible."

        })

    if bottlenecks.empty:

        recommendations.append({

            "title": "Operational Stability",

            "priority": "🟢 Low",

            "message":
                "No significant bottlenecks were identified during the selected period."

        })

    else:

        recommendations.append({

            "title": "Investigate Bottlenecks",

            "priority": "🔴 High",

            "message":
                f"{len(bottlenecks)} bottleneck periods were detected. "
                "Review staffing, transportation and placement availability."

        })

    return recommendations


# ==========================================================
# RISK RECOMMENDATIONS
# ==========================================================

def build_risk_recommendations(
    summary,
    health_score,
    anomalies
):
    """
    Build executive recommendations for the
    Risk Intelligence dashboard.
    """

    stress_percent = summary["stress_percentage"]

    anomaly_count = get_total_anomalies(
        anomalies
    )

    return get_risk_recommendations(
        health_score,
        stress_percent,
        anomaly_count
    )
    

# ==========================================================
# PERFORMANCE RECOMMENDATIONS
# ==========================================================

def build_performance_recommendations(
    summary,
    processing_efficiency,
    average_throughput
):
    """
    Build executive recommendations for the
    Performance Intelligence dashboard.
    """

    recommendations = []

    # --------------------------------------------------
    # Processing Efficiency
    # --------------------------------------------------

    if processing_efficiency < 75:

        recommendations.append({

            "title": "Improve Processing Efficiency",

            "icon": "⚡",

            "message":
                "Review transfer workflows between CBP and HHS to "
                "reduce delays and improve overall throughput."

        })

    elif processing_efficiency < 90:

        recommendations.append({

            "title": "Optimize Existing Workflow",

            "icon": "📈",

            "message":
                "Current efficiency is healthy but additional workflow "
                "optimization could further reduce transition times."

        })

    else:

        recommendations.append({

            "title": "Maintain Operational Excellence",

            "icon": "✅",

            "message":
                "Current processing efficiency reflects a highly effective "
                "care transition process. Continue monitoring for sustained performance."

        })

    # --------------------------------------------------
    # Backlog
    # --------------------------------------------------

    combined_backlog = (
        summary["avg_cbp_backlog"] +
        summary["avg_hhs_backlog"]
    )

    if combined_backlog > 500:

        recommendations.append({

            "title": "Reduce System Backlog",

            "icon": "🚨",

            "message":
                "Persistent backlog pressure indicates the need for "
                "additional operational capacity or workflow improvements."

        })

    else:

        recommendations.append({

            "title": "Backlog Under Control",

            "icon": "📊",

            "message":
                "Current backlog levels remain within an acceptable "
                "operational range."

        })

    # --------------------------------------------------
    # Throughput
    # --------------------------------------------------

    if average_throughput < 100:

        recommendations.append({

            "title": "Increase Throughput",

            "icon": "🚀",

            "message":
                "Evaluate staffing levels and operational scheduling to "
                "increase the number of children processed daily."

        })

    else:

        recommendations.append({

            "title": "Sustain Throughput",

            "icon": "🏆",

            "message":
                "Daily throughput demonstrates strong operational capacity. "
                "Maintain current performance while monitoring demand."

        })

    return recommendations 


# ==========================================================
# EXECUTIVE RECOMMENDATIONS
# ==========================================================

def build_executive_recommendations(insights):
    """
    Build executive recommendations and operational alerts
    for the Executive Dashboard.
    """

    return {

        "recommendations": insights.get(
            "recommendations",
            []
        ),

        "alerts": insights.get(
            "alerts",
            []
        )

    }   