"""
ai_decision.py

AI Decision Intelligence Dashboard
----------------------------------------------------------

Executive decision support powered by operational, performance, and risk intelligence.
"""

import streamlit as st

from utils.ai_decision_engine import (
    build_ai_kpis,
    build_ai_operational_summary,
    build_predictive_summary,
    build_decision_simulation,
    build_ai_executive_summary,
    build_ai_recommendations
)

from visuals.cards import (
    render_kpi_card,
    render_info_card
)


# ==========================================================
# AI DECISION DASHBOARD
# ==========================================================

from dashboard.components.helpers import validate_dashboard_data

def render_ai_decision(df, insights):
    """
    Render the AI Decision Intelligence Dashboard.
    """

    if not validate_dashboard_data(df):
        return

    summary = insights["summary"]

    health_score = insights["health_score"]

    risk_level = insights["risk_level"]

    anomalies = insights["anomalies"]

    processing_efficiency = insights["operations"]["processing_efficiency"] 
    
    ai_kpis = build_ai_kpis(
        health_score,
        risk_level,
        processing_efficiency
    )
    
    operational_summary = build_ai_operational_summary(
        summary,
        health_score,
        risk_level,
        anomalies,
        processing_efficiency
    )
    
    predictive_summary = build_predictive_summary(
        summary,
        health_score,
        risk_level,
        anomalies,
        processing_efficiency
    )
    
    executive_summary = build_ai_executive_summary(
        health_score,
        risk_level,
        processing_efficiency
    )
    
    ai_recommendations = build_ai_recommendations(
        health_score,
        risk_level,
        processing_efficiency,
        summary["stress_percentage"]
    )

    render_header()

    render_ai_kpis(ai_kpis)
    
    render_operational_intelligence(
        operational_summary
    )
    
    render_predictive_intelligence(
        predictive_summary
    )
    
    render_decision_simulation(
        health_score,
        risk_level,
        processing_efficiency
    )

    render_executive_summary(
        executive_summary
    )
    
    render_executive_recommendations(
        ai_recommendations
    )

    render_footer()
    
    
# ==========================================================
# HEADER
# ==========================================================

def render_header():
    """
    AI Decision Intelligence Header.
    """

    st.markdown(
        """
        <div class="section-title">
            🤖 AI Decision Intelligence
        </div>

        <div class="section-subtitle">
            Consolidate operational, performance, and risk intelligence into AI-assisted executive recommendations 
            that support informed, proactive decision-making across the care transition pipeline.
        </div>
        """,
        unsafe_allow_html=True
    )  
   
    
# ==========================================================
# EXECUTIVE AI KPIs
# ==========================================================

def render_ai_kpis(ai_kpis):
    """
    Render executive AI KPI cards.
    """

    c1, c2, c3, c4 = st.columns(4)

    cards = [
        ai_kpis["ai_confidence"],
        ai_kpis["system_health"],
        ai_kpis["risk_level"],
        ai_kpis["priority"]
    ]

    for col, card in zip((c1, c2, c3, c4), cards):

        with col:

            render_kpi_card(
                title=card["title"],
                value=card["value"],
                icon=card["icon"],
                subtitle=card["subtitle"]
            )

    st.divider()


# ==========================================================
# OPERATIONAL INTELLIGENCE
# ==========================================================

def render_operational_intelligence(
    operational_summary
):
    """
    Provide AI-generated interpretation of operational performance, emerging patterns, and system resilience to support
    executive decision-making.
    """
    
    st.markdown(
        """
        <div class="section-title">
           🧠 Operational Intelligence
        </div>

        <div class="section-subtitle">
            AI-generated interpretation of operational performance, system behavior, and organizational resilience 
            to support executive decision-making.
        </div>
        """,
        unsafe_allow_html=True
    )
     
    col1, col2 = st.columns(2)

    with col1:

        for key in [
            "current_situation",
            "operational_driver",
            "emerging_risks"
        ]:

            card = operational_summary[key]

            render_info_card(
                title=card["title"],
                icon=card["icon"],
                content=card["content"]
            )

    with col2:

        for key in [
            "pattern_detection",
            "system_status",
            "executive_insight"
        ]:

            card = operational_summary[key]

            render_info_card(
                title=card["title"],
                icon=card["icon"],
                content=card["content"]
            )

    st.divider()   


# ==========================================================
# PREDICTIVE INTELLIGENCE
# ==========================================================

def render_predictive_intelligence(
    predictive_summary
):
    """
    Forecast future operational conditions using current operational, performance, and risk indicators.
    """

    st.markdown(
        """
        <div class="section-title">
            🔮 Predictive Intelligence
        </div>

        <div class="section-subtitle">
            AI-generated outlook describing expected operational performance, organizational risk, and future capacity
            requirements based on current system behavior.
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:

        for key in [
            "future_outlook",
            "capacity_forecast",
            "forecast_confidence"
        ]:

            card = predictive_summary[key]

            render_info_card(
                title=card["title"],
                icon=card["icon"],
                content=card["content"]
            )

    with col2:

        for key in [
            "risk_projection",
            "system_stability",
            "executive_outlook"
        ]:

            card = predictive_summary[key]

            render_info_card(
                title=card["title"],
                icon=card["icon"],
                content=card["content"]
            )

    st.divider()                                                


# ==========================================================
# DECISION SIMULATION
# ==========================================================

def render_decision_simulation(
    health_score,
    risk_level,
    processing_efficiency
):
    """
    Render the Decision Simulation UI and invoke the simulation engine to compute results.
    """

    st.markdown(
        """
        <div class="section-title">
            🧪 Decision Simulation
        </div>

        <div class="section-subtitle">
            Evaluate potential operational outcomes under different strategic scenarios before implementing
            real-world organizational changes.
        </div>
        """,
        unsafe_allow_html=True
    )

    scenario = st.radio(
        "Select Strategic Scenario",
        [
            "Increase Staffing",
            "Expand Capacity",
            "Process Optimization"
        ],
        horizontal=True
    )

    simulation = build_decision_simulation(
        health_score,
        risk_level,
        processing_efficiency,
        scenario
    )
    
    kpis = simulation["kpis"]

    c1, c2, c3, c4 = st.columns(4)

    cards = [
        kpis["projected_health"],
        kpis["projected_efficiency"],
        kpis["projected_risk"],
        kpis["expected_outcome"]
    ]

    for col, card in zip((c1, c2, c3, c4), cards):

        with col:

            render_kpi_card(
                title=card["title"],
                value=card["value"],
                icon=card["icon"],
                subtitle=card["subtitle"]
            )

    col1, col2 = st.columns(2)

    with col1:

        for key in [
            "strategic_impact",
            "expected_benefits"
        ]:

            card = simulation[key]

            render_info_card(
                title=card["title"],
                icon=card["icon"],
                content=card["content"]
            )

    with col2:

        for key in [
            "tradeoffs",
            "recommendation"
        ]:

            card = simulation[key]

            render_info_card(
                title=card["title"],
                icon=card["icon"],
                content=card["content"]
            )                                
    
    st.caption(
        "Simulation results represent AI-assisted scenario estimates based on historical operational trends and are intended to support executive decision-making."
    )
     
    st.divider()      
               
# ==========================================================
# EXECUTIVE SUMMARY
# ==========================================================

def render_executive_summary(
    executive_summary
):
    """
    Display organizational health and executive summaries.
    """
    
    st.markdown(
        """
        <div class="section-title">
            📋 Executive Summary
        </div>

        <div class="section-subtitle">
            Consolidated AI assessment combining operational, performance, and organizational risk into a single
            executive decision overview.
        </div>
        """,
        unsafe_allow_html=True
    ) 
        
    col1, col2 = st.columns(2)

    with col1:

        card = executive_summary["executive_situation"]

        render_info_card(
            title=card["title"],
            icon=card["icon"],
            content=card["content"]
        )

    with col2:

        card = executive_summary["executive_interpretation"]

        render_info_card(
            title=card["title"],
            icon=card["icon"],
            content=card["content"]
        )

    st.divider()   


# ==========================================================
# EXECUTIVE RECOMMENDATIONS
# ==========================================================

def render_executive_recommendations(
    ai_recommendations
):
    """
    AI-generated executive recommendations based on operational, performance, and risk intelligence.
    """

    st.markdown(
        """
        <div class="section-title">
            💡 Executive Recommendations
        </div>

        <div class="section-subtitle">
            AI-generated strategic recommendations designed to improve operational efficiency, reduce organizational risk, and
            strengthen overall system performance.
        </div>
        """,
        unsafe_allow_html=True
    )
        
    recommendations = ai_recommendations["recommendations"]

    col1, col2 = st.columns(2)

    for i, rec in enumerate(recommendations):

        with (col1 if i % 2 == 0 else col2):

            render_info_card(
                title=rec["title"],
                icon=rec["icon"],
                content=rec["message"]
            )

    conclusion = ai_recommendations["conclusion"]

    render_info_card(
        title=conclusion["title"],
        icon=conclusion["icon"],
        content=conclusion["message"]
    )   
     
     
# ======================================================
# FOOTER
# ======================================================

def render_footer():
    """
    Render AI Decision Dashboard footer.
    """

    st.markdown("---")

    st.caption(
        "Care Transition Operational Intelligence Platform • AI Decision Dashboard"
    )

    st.caption(
        "Historical Analytics • Version 1.0 • Data Source: HHS Unaccompanied Children Program"
    )                                               