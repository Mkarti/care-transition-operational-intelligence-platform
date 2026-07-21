"""
analytics.py

Central Analytics Engine
----------------------------------------------------------

This module orchestrates all analytics for the
Care Transition Operational Intelligence Platform.

Architecture
------------
Pipeline
    ↓
Analytics Engine
    ├── Executive Analytics
    ├── Executive Intelligence
    ├── Operations Analytics
    ├── Risk Analytics 
    ├── Performance Analytics (Future)
    └── Forecasting Analytics (Future)

The dashboard should only interact with this file.
"""


# ==========================================================
# EXECUTIVE ANALYTICS
# ==========================================================

from utils.anomaly_engine import detect_anomalies

from utils.insight_engine import (
    classify_risk_level,
    peak_stress_days,
    stress_summary,
    system_health_score
)

from utils.insight_generator import (
    generate_all_insights
)

from utils.ai_decision_engine import run_ai_decision_engine


# ==========================================================
# OPERATIONS ANALYTICS
# ==========================================================

from utils.operations_engine import (
    run_operations_engine
)


# ==========================================================
# PERFORMANCE ANALYTICS
# ==========================================================
from utils.performance_engine import (
    run_performance_engine
)


# ==========================================================
# RISK ANALYTICS
# ==========================================================
from utils.risk_engine import (
    run_risk_engine
)


# ==========================================================
# AI DECISION ANALYTICS
# ==========================================================
from utils.ai_decision_engine import (
    run_ai_decision_engine
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
# OPERATIONS ENGINE
# ==========================================================

def run_operations(df):
    """
    Build operations analytics.
    """

    return {
        "operations": run_operations_engine(df)
    }


# ==========================================================
# PERFORMANCE ENGINE
# ==========================================================

def run_performance(df):

    return {

        "performance":
            run_performance_engine(df)

    }


# ==========================================================
# RISK ENGINE
# ==========================================================

def run_risk(executive):

    return {

        "risk":
            run_risk_engine(executive)

    }


# ==========================================================
# AI DECISION ENGINE
# ==========================================================

def run_ai_decisions(
    summary,
    operations,
    health_score,
    risk_level,
    anomalies
):

    return run_ai_decision_engine(
        summary,
        operations,
        health_score,
        risk_level,
        anomalies
    )

# ==========================================================
# RUN COMPLETE ANALYTICS PIPELINE
# ==========================================================

def run_insights(df):
    """
    Execute the complete analytics engine.
    """

    insights = {}

    # Executive Intelligence
    executive = run_executive(df)
    insights.update(executive)
    # Extract executive pieces needed downstream
    summary = executive.get("summary")
    health_score = executive.get("health_score")
    risk_level = executive.get("risk_level")
    anomalies = executive.get("anomalies")

    # Operations
    operations_dict = run_operations(df)
    insights.update(operations_dict)
    operations = operations_dict.get("operations")

    # Performance
    performance_dict = run_performance(df)
    insights.update(performance_dict)

    # Risk
    risk_dict = run_risk(executive)
    insights.update(risk_dict)

    # AI Decisions
    ai_result = run_ai_decisions(
        summary,
        operations,
        health_score,
        risk_level,
        anomalies
    )
    insights.update({"ai_decision": ai_result})

    return insights