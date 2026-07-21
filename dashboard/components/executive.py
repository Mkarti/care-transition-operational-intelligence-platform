"""
executive.py

Executive Dashboard
----------------------------------------------------------

Executive overview of operational performance,
system health, organizational risk,
and strategic recommendations.
"""

import streamlit as st

from dashboard.components.helpers import (
    validate_dashboard_data
)

from utils.executive_summary_engine import (
    build_executive_alerts,
    build_executive_kpi_summary,
    build_executive_brief,
    build_executive_recommendations,
    build_executive_trend_summary,
    build_executive_health_summary,  
)

from utils.narrative_engine import (
    build_executive_narrative
)

from visuals.cards import (
    render_kpi_card,
    render_recommendation_card,
    render_alert_card,
    render_info_card
)

from visuals.charts import (
    create_system_load_chart,
    create_backlog_chart,
    create_throughput_chart
)

from visuals.gauges import (
    create_health_gauge
)

# ==========================================================
# EXECUTIVE DASHBOARD
# ==========================================================

def render_executive(df, insights):
    """
    Render Executive Dashboard.
    """

    if not validate_dashboard_data(df):
        return
    
    executive_kpis = build_executive_kpi_summary(
        insights
    )
    
    executive_brief = build_executive_brief(
        insights
    )

    health_score = insights["health_score"]

    processing_efficiency = insights["operations"]["processing_efficiency"]

    stress_percentage = insights["summary"]["stress_percentage"]

    risk_level = insights["risk_level"]   
    
    executive_narrative = build_executive_narrative(
        health_score,
        processing_efficiency,
        stress_percentage,
        risk_level
    )
    
    executive_recommendations = (
        build_executive_recommendations(
            insights
        )
    )
    
    executive_alerts = build_executive_alerts(
        insights.get("alerts", [])
    )
    
    executive_trend_summary = build_executive_trend_summary()
    
    executive_health = (
        build_executive_health_summary(
            insights
        )
    )

    render_header()

    render_kpis(
        executive_kpis
    )

    render_executive_brief(
        executive_brief
    )
    
    render_executive_narrative(
        executive_narrative
    )

    render_recommendations_alerts(
        executive_recommendations,
        executive_alerts
    )

    render_trend_analysis(
        df,
        executive_trend_summary
    )

    render_health_summary(
        executive_health
    )

    render_footer()


# ==========================================================
# HEADER
# ==========================================================

def render_header():
    """
    Render Executive Dashboard header.
    """

    st.markdown(
        """
        <div class="section-title">
            🧭 Executive Dashboard
        </div>

        <div class="section-subtitle">
            Executive overview of operational performance, organizational health,
            system resilience, and strategic decision support.
        </div>
        """,
        unsafe_allow_html=True
    )


# ==========================================================
# EXECUTIVE KPIs
# ==========================================================

def render_kpis(executive_kpis):
    """
    Display executive KPI overview.
    """

    health = executive_kpis["health_score"]

    efficiency = executive_kpis["processing_efficiency"]

    risk = executive_kpis["risk_level"]

    stress = executive_kpis["stress_days"]

    c1, c2, c3, c4 = st.columns(4)

    with c1:

        render_kpi_card(
            title=health["title"],
            value=health["value"],
            icon=health["icon"],
            subtitle=health["subtitle"]
        )

    with c2:

        render_kpi_card(
            title=efficiency["title"],
            value=efficiency["value"],
            icon=efficiency["icon"],
            subtitle=efficiency["subtitle"]
        )

    with c3:

        render_kpi_card(
            title=risk["title"],
            value=risk["value"],
            icon=risk["icon"],
            subtitle=risk["subtitle"]
        )

    with c4:

        render_kpi_card(
            title=stress["title"],
            value=stress["value"],
            icon=stress["icon"],
            subtitle=stress["subtitle"]
        )

    st.divider()


# ==========================================================
# EXECUTIVE BRIEF
# ==========================================================

def render_executive_brief(executive_brief):
    """
    Display the Executive Brief.
    """

    st.markdown(
        """
        <div class="section-title">
            🧠 Executive Brief
        </div>

        <div class="section-subtitle">
            AI-generated executive assessment summarizing the current operational situation, primary performance drivers,
            organizational impact, and recommended leadership actions.
        </div>
        """,
        unsafe_allow_html=True
    )

    content = f"""
<b>Executive Summary</b><br>
{executive_brief["summary"]}

<br><br>

<b>Primary Driver</b><br>
{executive_brief["driver"]}

<br><br>

<b>Business Impact</b><br>
{executive_brief["impact"]}

<br><br>

<b>Leadership Action</b><br>
{executive_brief["action"]}
"""

    col1, col2 = st.columns(2)

    with col1:

        render_info_card(
            title="Executive Summary",
            icon="📌",
            content=executive_brief["summary"]
        )

        render_info_card(
            title="Business Impact",
            icon="📈",
            content=executive_brief["impact"]
        )

    with col2:

        render_info_card(
            title="Primary Driver",
            icon="⚙️",
            content=executive_brief["driver"]
        )

        render_info_card(
            title="Leadership Action",
            icon="🎯",
            content=executive_brief["action"]
        )

    st.divider()
    

# ==========================================================
# AI EXECUTIVE NARRATIVE
# ==========================================================

def render_executive_narrative(narrative):
    """
    Display the AI-generated executive narrative.
    """

    st.markdown(
        """
        <div class="section-title">
            🤖 AI Executive Narrative
        </div>

        <div class="section-subtitle">
            Automatically generated executive interpretation of
            organizational health, operational performance, and
            strategic priorities.
        </div>
        """,
        unsafe_allow_html=True
    )

    render_info_card(
        title=narrative["title"],
        icon=narrative["icon"],
        content=narrative["content"]
    )

    st.divider()

# ==========================================================
# RECOMMENDATIONS & ALERTS
# ==========================================================

def render_recommendations_alerts(
    executive_recommendations,
    executive_alerts
):
    st.markdown(
        """
        <div class="section-title">
            🎯 Executive Action Center
        </div>

        <div class="section-subtitle">
            Prioritized strategic actions to improve operational efficiency, strengthen resilience, and support executive decision-making.
        </div>
        """,
        unsafe_allow_html=True
    )

    left, right = st.columns([1.2, 1])

    # ------------------------------------------------------
    # RECOMMENDATIONS
    # ------------------------------------------------------

    with left:
        
        st.subheader("📋 Strategic Recommendations")
        
        recommendations = (
            executive_recommendations["recommendations"]
        )

        if recommendations:

            for recommendation in recommendations:
                render_recommendation_card(recommendation)
                st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)

        else:

            render_info_card(

                title="No Recommendations",

                icon="✅",

                content=(
                    "Current operational performance "
                    "is stable."
                )

            )

    # ------------------------------------------------------
    # ALERTS
    # ------------------------------------------------------

    with right:

        st.subheader("🚨 Executive Alerts")

        if executive_alerts:

            for alert in executive_alerts:

                render_alert_card(alert)

                st.markdown(
                    "<div style='height:10px'></div>",
                    unsafe_allow_html=True
                )

        else:

            render_info_card(
                title="No Alerts",
                icon="🟢",
                content="No operational alerts are currently active."
            )
            
    st.divider()        


# ==========================================================
# TREND ANALYSIS
# ==========================================================

def render_trend_analysis(
    df,
    trend_summary
):
    """
    Display executive operational trend analysis.
    """

    st.markdown(
        """
        <div class="section-title">
            📈 Executive Trend Analysis
        </div>

        <div class="section-subtitle">
            Monitor workload dynamics, operational throughput, and backlog trends to understand how the care transition system performed throughout the selected reporting period.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.subheader("📊 System Load Over Time")
    st.plotly_chart(
        create_system_load_chart(df),
        use_container_width=True
    )
    
    st.caption(
    "Shows how the combined operational workload evolved over time, highlighting periods of increasing or decreasing system demand."
    )

    left, right = st.columns(2)

    with left:
        
        st.subheader("🚚 Daily Throughput")
        st.plotly_chart(
            create_throughput_chart(df),
            use_container_width=True
        )
        
        st.caption(
            "Measures the total number of children successfully processed each day through transfers and discharges.."
        )

    with right:
        
        st.subheader("📦 Operational Backlog")
        st.plotly_chart(
            create_backlog_chart(df),
            use_container_width=True
        )
        
        st.caption(
            "Tracks the number of children awaiting processing, helping identify sustained congestion or capacity pressure."
        )  
    
    st.markdown("<br>", unsafe_allow_html=True) 
    
    st.subheader("Key Operational Insights")   
    col1, col2, col3 = st.columns(3)

    with col1:

        card = trend_summary["system_load"]

        render_info_card(
            title=card["title"],
            icon=card["icon"],
            content=card["content"]
        )

    with col2:

        card = trend_summary["throughput"]

        render_info_card(
            title=card["title"],
            icon=card["icon"],
            content=card["content"]
        )

    with col3:

        card = trend_summary["backlog"]

        render_info_card(
            title=card["title"],
            icon=card["icon"],
            content=card["content"]
        )   


# ==========================================================
# HEALTH SUMMARY
# ==========================================================

def render_health_summary(executive_health):
    """
    Display organizational health and executive summaries.
    """

    gauge_left, gauge_right = st.columns([1.15, 1.1])

    # ------------------------------------------------------
    # HEALTH GAUGE
    # ------------------------------------------------------

    with gauge_left:

        st.plotly_chart(
            create_health_gauge(
                executive_health["health_score"]
            ),
            use_container_width=True
        )

    # ------------------------------------------------------
    # EXECUTIVE SUMMARY
    # ------------------------------------------------------

    with gauge_right:

        st.markdown(
            """
            <div class="section-title">
                💡 Executive Summary
            </div>

            <div class="section-subtitle">
                Executive interpretation of organizational health,
                operational risk, system performance, expected impact,
                and recommended leadership actions.
            </div>
            """,
            unsafe_allow_html=True
        )

        operational = executive_health["operational_status"]
        risk = executive_health["operational_risk"]
        performance = executive_health["system_performance"]

        col1, col2 = st.columns(2)

        # ==================================================
        # LEFT COLUMN
        # ==================================================

        with col1:

            render_info_card(
                title="Operational Status",
                icon="💚",
                content=f"""
<div style="font-size:28px;font-weight:700;color:#4FD1C5;margin-bottom:14px;">
{operational['status']}
</div>

{operational['summary']}
"""
            )

            render_info_card(
                title="System Performance",
                icon="⚙️",
                content=f"""
<div style="font-size:28px;font-weight:700;color:#60A5FA;margin-bottom:14px;">
{performance['status']}
</div>

{performance['summary']}
"""
            )

            render_info_card(
                title="Leadership Recommendation",
                icon="🎯",
                content=performance["recommendation"]
            )

        # ==================================================
        # RIGHT COLUMN
        # ==================================================

        with col2:

            render_info_card(
                title="Operational Risk",
                icon="⚠️",
                content=f"""
<div style="font-size:28px;font-weight:700;color:#F97316;margin-bottom:14px;">
{risk['status']}
</div>

{risk['summary']}
"""
            )

            render_info_card(
                title="Expected Impact",
                icon="📈",
                content=operational["impact"]
            )

            render_info_card(
                title="Executive Outlook",
                icon="🧠",
                content=risk["recommendation"]
            )


# ==========================================================
# FOOTER
# ==========================================================

def render_footer():
    """
   Render Executive Dashboard footer.
    """

    st.markdown("---")

    st.caption(
        "Care Transition Operational Intelligence Platform • Executive Dashboard"
    )

    st.caption(
        "Historical Analytics • Version 1.0 • Data Source: HHS Unaccompanied Children Program"
    )