"""
risk.py

Risk Intelligence Dashboard
----------------------------------------------------------

Identify operational risk, monitor stress patterns, detect anomalies, and support proactive decision-making.
"""

import streamlit as st

from dashboard.components.helpers import validate_dashboard_data

from utils.executive_summary_engine import (
    build_risk_summary,
    build_risk_recommendations
)

from visuals.cards import (
    render_kpi_card,
    render_info_card
)

from visuals.charts import (
    create_stress_timeline
)

from visuals.heatmaps import (
    create_operational_heatmap
)

# ==========================================================
# RISK DASHBOARD
# ==========================================================

def render_risk(df, insights):
    """
    Render the Risk Intelligence Dashboard.
    """

    if not validate_dashboard_data(df):
        return

    summary = insights["summary"]

    health_score = insights["health_score"]

    risk_level = insights["risk_level"]
    
    anomalies = insights["anomalies"]
    
    risk_summary = build_risk_summary(
        summary,
        health_score,
        risk_level,
        anomalies
    )
    
    risk_recommendations = (
        build_risk_recommendations(
            summary,
            health_score,
            anomalies
        )
    )

    render_header()

    render_risk_kpis(
        risk_summary
    )
    
    render_risk_trends(
        df,
        risk_summary
    )
    
    render_risk_hotspots(df)

    render_risk_intelligence(
        risk_summary
    )
    
    render_risk_summary(
        risk_summary
    )
    
    render_risk_recommendations(
        risk_recommendations
    )

    render_footer()
    
    
# ==========================================================
# HEADER
# ==========================================================

def render_header():
    """
    Render Risk Intelligence Dashboard header.
    """

    st.markdown(
        """
        <div class="section-title">
            🚨 Risk Intelligence
        </div>

        <div class="section-subtitle">
            Monitor operational resilience, identify emerging risks, evaluate system stress, and support proactive 
            executive decision-making across the care transition lifecycle.
        </div>
        """,
        unsafe_allow_html=True
    )    


# ==========================================================
# RISK KPI CARDS
# ==========================================================

def render_risk_kpis(
    risk_summary
):
    """
    Display executive risk indicators.
    """
    
    kpis = risk_summary["kpis"]

    system_health = kpis["system_health"]

    risk_level = kpis["risk_level"]

    stress_days = kpis["stress_days"]

    anomalies = kpis["anomalies"]

    c1, c2, c3, c4 = st.columns(4)

    with c1:

        render_kpi_card(
            title=system_health["title"],
            value=system_health["value"],
            icon=system_health["icon"],
            subtitle=system_health["subtitle"]
        )

    with c2:

        render_kpi_card(
            title=risk_level["title"],
            value=risk_level["value"],
            icon=risk_level["icon"],
            subtitle=risk_level["subtitle"]
        )

    with c3:

        render_kpi_card(
            title=stress_days["title"],
            value=stress_days["value"],
            icon=stress_days["icon"],
            subtitle=stress_days["subtitle"]
        )

    with c4:

        render_kpi_card(
            title=anomalies["title"],
            value=anomalies["value"],
            icon=anomalies["icon"],
            subtitle=anomalies["subtitle"]
        )

    st.divider()  


# ==========================================================
# RISK TREND ANALYSIS
# ==========================================================

def render_risk_trends(
    df, 
    risk_summary
):
    """
    Visualize operational risk patterns over time.
    """

    st.markdown(
        """
        <div class="section-title">
            📈 Risk Trend Analysis
        </div>

        <div class="section-subtitle">
            Analyze changes in operational stress, emerging risk patterns, and anomaly progression to understand how 
            system resilience evolved throughout the reporting period.
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # ======================================================
    # Operational Risk Timeline
    # ======================================================

    timeline = create_stress_timeline(df)

    st.plotly_chart(
        timeline,
        use_container_width=True
    )

    st.caption(
        "The timeline highlights periods where operational stress exceeded acceptable thresholds, helping identify sustained risk events and emerging operational disruptions."
    )
    

    trend_summary = risk_summary["trend_summary"]

    stress_trend = trend_summary["stress_trend"]
    
    executive_interpretation = (
        trend_summary["executive_interpretation"]
    )

    col1, col2 = st.columns(2)
    
    with col1:

        render_info_card(
            title=stress_trend["title"],
            icon=stress_trend["icon"],
            content=stress_trend["content"]
        )
        
    with col2:
        
        render_info_card(
            title=executive_interpretation["title"],
            icon=executive_interpretation["icon"],
            content=executive_interpretation["content"]
        )
        
    st.divider()                            


# ==========================================================
# RISK HOTSPOTS
# ==========================================================

def render_risk_hotspots(df):
    """
    Visualize where operational pressure is concentrated.
    """

    st.markdown(
        """
        <div class="section-title">
            🔥 Risk Hotspots
        </div>

        <div class="section-subtitle">
            Identify recurring periods of elevated operational pressure to uncover persistent congestion patterns,
            seasonal risk concentrations, and areas requiring proactive intervention.
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # ======================================================
    # Heatmap Section
    # ======================================================

    st.subheader("🔥 Operational Risk Heatmap")

    selected_year = st.radio(

        "Select Reporting Year",

        [

            "All Years",
            "2023",
            "2024",
            "2025"

        ],

        horizontal=True

    )

    heatmap = create_operational_heatmap(

        df,

        selected_year

    )

    st.plotly_chart(

        heatmap,

        use_container_width=True

    )

    st.caption(
        "The heatmap highlights periods of sustained operational stress, enabling rapid identification of recurring risk clusters and long-term pressure patterns."
    )


    col1, col2 = st.columns(2)
    
    with col1:

        render_info_card(

            title="Risk Concentration",

            icon="🔥",

            content=(
                "Recurring concentrations of operational stress indicate persistent pressure points "
                "within the care transition pipeline. Identifying these clusters helps prioritize "
                "resource allocation and operational improvements."
            )

        )
        
    with col2:

        render_info_card(

            title="Strategic Interpretation",

            icon="🧠",

            content=(
                "Persistent hotspot patterns may reflect seasonal demand, capacity limitations, or workflow inefficiencies."
                "Continuous monitoring enables earlier intervention and more resilient operational planning."
            )

        )
        
    st.divider()                        


# ==========================================================
# RISK INTELLIGENCE
# ==========================================================

def render_risk_intelligence(
    risk_summary
):
    """
    Provide executive interpretation of the system's current operational risk posture.
    """

    st.markdown(
        """
        <div class="section-title">
            🧠 Risk Intelligence
        </div>

        <div class="section-subtitle">
            Consolidated intelligence describing current operational resilience, primary risk drivers, emerging threats, and overall organizational readiness.
        </div>
        """,
        unsafe_allow_html=True
    )
    
    intelligence = risk_summary["risk_intelligence"]

    primary_driver = intelligence["primary_risk_driver"]

    system_resilience = intelligence["system_resilience"]

    operational_stress = intelligence["operational_stress"]

    anomaly_assessment = intelligence["anomaly_assessment"]
        
    col1, col2 = st.columns(2)   
    
    with col1:

        render_info_card(
            title=primary_driver["title"],
            icon=primary_driver["icon"],
            content=primary_driver["content"]
        )

        
    with col2:

        render_info_card(
            title=system_resilience["title"],
            icon=system_resilience["icon"],
            content=system_resilience["content"]
        )
        
    col3, col4 = st.columns(2)
    
    with col3:

        render_info_card(
            title=operational_stress["title"],
            icon=operational_stress["icon"],
            content=operational_stress["content"]
        )
        
    with col4:

        render_info_card(
            title=anomaly_assessment["title"],
            icon=anomaly_assessment["icon"],
            content=anomaly_assessment["content"]
        )

    st.divider()                                                     


# ==========================================================
# EXECUTIVE RISK SUMMARY
# ==========================================================

def render_risk_summary(
    risk_summary
):
    """
    Present an executive-level summary of the system's overall risk posture.
    """

    st.markdown(
        """
        <div class="section-title">
            📋 Executive Risk Summary
        </div>

        <div class="section-subtitle">
            Executive-level assessment summarizing organizational risk posture, operational resilience,
            and strategic readiness based on current system performance.
        </div>
        """,
        unsafe_allow_html=True
    )
    
    summary = risk_summary["executive_summary"]

    overall_risk = summary["overall_risk_assessment"]

    operational_summary = summary["operational_summary"]

    executive_outlook = summary["executive_outlook"]
        
    render_info_card(
        title=overall_risk["title"],
        icon=overall_risk["icon"],
        content=overall_risk["content"]
    )
    
    col1, col2 = st.columns(2)
    
    with col1:

        render_info_card(
            title=operational_summary["title"],
            icon=operational_summary["icon"],
            content=operational_summary["content"]
        )
        
    with col2:

        render_info_card(
            title=executive_outlook["title"],
            icon=executive_outlook["icon"],
            content=executive_outlook["content"]
        )
        
    st.divider()                                        


# ==========================================================
# EXECUTIVE RECOMMENDATIONS
# ==========================================================

def render_risk_recommendations(
    recommendations
):
    """
    Recommend executive actions based on the current operational risk profile.
    """

    st.markdown(
        """
        <div class="section-title">
            💡 Executive Recommendations
        </div>

        <div class="section-subtitle">
            Prioritized recommendations designed to strengthen operational resilience, reduce organizational risk,
            and improve long-term system performance.
        </div>
        """,
        unsafe_allow_html=True
    )
        
    col1, col2 = st.columns(2)

    for i, rec in enumerate(recommendations):

        with col1 if i % 2 == 0 else col2:

            render_info_card(
                title=rec["title"],
                icon=rec["icon"],
                content=rec["message"]
            )                                               


# ======================================================
# FOOTER
# ======================================================

def render_footer():
    """
    Render Risk Dashboard footer.
    """

    st.markdown("---")

    st.caption(
        "Care Transition Operational Intelligence Platform • Risk Dashboard"
    )

    st.caption(
        "Historical Analytics • Version 1.0 • Data Source: HHS Unaccompanied Children Program"
    )                                   