"""
operations.py

Operations Intelligence Dashboard
----------------------------------------------------------

Operational analytics and flow monitoring for the
Care Transition Operational Intelligence Platform.
"""

import streamlit as st

from utils.executive_engine import (
    get_flow_snapshot
)

from visuals.cards import (
    render_kpi_card,
    render_info_card
)

from visuals.charts import (
    create_throughput_chart,
    create_system_load_chart,
    create_rolling_backlog_chart,
    create_rolling_efficiency_chart,
    create_daily_throughput_chart,
    create_capacity_chart,
    add_anomaly_markers
)

from visuals.sankey import create_care_transition_sankey

from utils.executive_summary_engine import (
    build_bottleneck_summary,
    build_operations_summary,
    build_capacity_summary,
    build_operations_recommendations
)


# ==========================================================
# OPERATIONS DASHBOARD
# ==========================================================

from dashboard.components.helpers import validate_dashboard_data

def render_operations(df, insights):
    """
    Render the Operations Intelligence Dashboard.
    """
    if not validate_dashboard_data(df):
        return

    operations = insights["operations"]

    summary = operations["summary"]
    bottlenecks = operations["bottlenecks"]
    processing_efficiency = operations["processing_efficiency"]
    
    flow_snapshot = get_flow_snapshot(df)
    
    operations_summary = build_operations_summary(
        summary,
        bottlenecks,
        processing_efficiency
    )

    capacity_summary = build_capacity_summary(df)
    
    bottleneck_summary = build_bottleneck_summary(
        bottlenecks
    )
    
    operations_recommendations = (
        build_operations_recommendations(
            summary,
            bottlenecks,
            processing_efficiency
        )
    )

    render_header()

    render_operations_kpis(
        summary,
        processing_efficiency
    )

    render_operational_flow(df)
    
    render_flow_snapshot(flow_snapshot)

    render_operational_trends(
        df,
        bottlenecks
    )
    
    render_capacity_intelligence(
        df,
        bottlenecks,
        capacity_summary
    )

    render_bottleneck_detection(
        bottlenecks,
        bottleneck_summary
    )

    render_operational_insights(
        operations_summary
    )
    
    render_executive_recommendations(
        operations_recommendations  
    )

    render_footer()
  
    
# ======================================================
# HEADER
# ======================================================

def render_header():
    """
    Render Operations Dashboard header.
    """

    st.markdown(
        """
        <div class="section-title">
            ⚙️ Operations Intelligence
        </div>

        <div class="section-subtitle">
            End-to-end operational monitoring of the Care Transition pipeline, enabling visibility into workflow 
            performance, processing efficiency, capacity utilization, and operational bottlenecks.
        </div>
        """,
        unsafe_allow_html=True
    )


# ======================================================
# KPI CARDS
# ======================================================

def render_operations_kpis(
    summary,
    processing_efficiency
):
    """
    Render executive KPI cards for operations dashboard.
    """
    
    c1, c2, c3, c4 = st.columns(4)

    with c1:
        render_kpi_card(
            title="Processing Efficiency",
            value=f"{processing_efficiency:.1f}%",
            icon="⚡",
            subtitle="Overall Pipeline Efficiency"
        )

    with c2:
        render_kpi_card(
            title="Avg CBP Backlog",
            value=summary["avg_cbp_backlog"],
            icon="🚔",
            subtitle="Average Daily Queue"
        )

    with c3:
        render_kpi_card(
            title="Avg HHS Backlog",
            value=summary["avg_hhs_backlog"],
            icon="🏥",
            subtitle="Average Daily Care Load"
        )

    with c4:
        render_kpi_card(
            title="Peak CBP Backlog",
            value=summary["peak_cbp"],
            icon="📈",
            subtitle="Highest Recorded Queue"
        )

    st.divider()


# ==========================================================
# OPERATIONAL FLOW
# ==========================================================
    
def render_operational_flow(df):
    """
    Display the overall care transition flow.
    """

    st.markdown(
        """
        <div class="section-title">
            🌊 Operational Flow
        </div>

        <div class="section-subtitle">
            End-to-end visualization of the care transition pipeline, illustrating how children progress from 
            initial CBP custody through HHS care to successful discharge.
        </div>
        """,
        unsafe_allow_html=True
    )

    fig = create_care_transition_sankey(df)

    st.plotly_chart(
        fig,
        use_container_width=True
    )
    
    st.caption(
            "The operational flow illustrates the movement of children across each stage of the care transition process, helping identify throughput efficiency and potential transition bottlenecks."
        )

    
def render_flow_snapshot(flow_snapshot):
    """
    Executive summary of the operational flow.
    """

    apprehended = flow_snapshot["apprehended"]

    avg_cbp_load = flow_snapshot["avg_cbp_load"]

    transferred = flow_snapshot["transferred"]

    avg_hhs_load = flow_snapshot["avg_hhs_load"]

    discharged = flow_snapshot["discharged"]

    st.markdown(
        """
        <div class="section-title">
            📌 Flow Snapshot
        </div>

        <div class="section-subtitle">
            High-level operational snapshot summarizing the volume of children moving through each stage of the care transition
            process during the selected reporting period.
        </div>
        """,
        unsafe_allow_html=True
    )

    c1, c2, c3, c4, c5 = st.columns(5)

    with c1:
        render_kpi_card(
            "Apprehended",
            f"{apprehended:,}",
            icon="🚔",
            subtitle="Total Apprehended"
        )

    with c2:
        render_kpi_card(
            "CBP Custody",
            avg_cbp_load,
            icon="🏢",
            subtitle="Avg Daily Load"
        )

    with c3:
        render_kpi_card(
            "Transferred",
            f"{transferred:,}",
            icon="➡️",
            subtitle="Successfully Transferred"
        )

    with c4:
        render_kpi_card(
            "HHS Care",
            avg_hhs_load,
            icon="🏥",
            subtitle="Avg Daily Care"
        )

    with c5:
        render_kpi_card(
            "Discharged",
            f"{discharged:,}",
            icon="🏠",
            subtitle="Successfully Discharged"
        )

    st.divider()


# ======================================================
# 📈 Operational Trends
# ======================================================

def render_operational_trends(df, bottlenecks):
    """
    Display operational performance trends.
    """

    st.markdown(
        """
        <div class="section-title">
            📈 Operational Trends
        </div>

        <div class="section-subtitle">
            Evaluate operational throughput, processing efficiency, workload distribution, and transition performance across
            the reporting period to identify emerging trends and potential capacity constraints.
        </div>
        """,
        unsafe_allow_html=True
    )

    # ======================================================
    # Row 1
    # ======================================================

    left, right = st.columns(2)

    with left:

        throughput_fig = create_throughput_chart(df)

        throughput_fig = add_anomaly_markers(
            throughput_fig,
            bottlenecks,
            "date",
            "children_transferred_out_of_cbp_custody"
        )

        st.plotly_chart(
            throughput_fig,
            use_container_width=True
        )
        
        st.caption(
                "Daily transfer throughput highlighting processing volume and detected operational anomalies."
            )

    with right:

        efficiency_fig = create_rolling_efficiency_chart(df)

        st.plotly_chart(
            efficiency_fig,
            use_container_width=True
        )
        
        st.caption(
                "Rolling processing efficiency illustrates how effectively children transition through the care pipeline over time."
            )  

    # ======================================================
    # Row 2
    # ======================================================

    left, right = st.columns(2)

    with left:

        throughput_daily = create_daily_throughput_chart(df)

        st.plotly_chart(
            throughput_daily,
            use_container_width=True
        )
        
        st.caption(
                "Daily operational activity showing the total number of children processed throughout the reporting period."
            )

    with right:

        capacity_fig = create_capacity_chart(df)

        st.plotly_chart(
            capacity_fig,
            use_container_width=True
        )
        
        st.caption(
                "Operational workload comparison between CBP custody and HHS care, illustrating how demand shifts across the transition pipeline."
        )
        
    st.markdown("<br>", unsafe_allow_html=True)    

    st.divider()
   
    
# ======================================================
# SYSTEM LOAD + BACKLOG
# ======================================================

def render_capacity_intelligence(df, bottlenecks, capacity_summary):
    """
    Display capacity utilization and operational load.
    """

    st.markdown(
        """
        <div class="section-title">
            🏥 Capacity Intelligence
        </div>

        <div class="section-subtitle">
            Assess system capacity, monitor operational workload, and identify resource pressure across CBP and HHS to support proactive planning.
        </div>
        """,
        unsafe_allow_html=True
    )


# ======================================================
# CAPACITY VISUALS
# ======================================================

    left, right = st.columns(2)

    with left:

        load_fig = create_system_load_chart(df)

        st.plotly_chart(
            load_fig,
            use_container_width=True
        )
        
        st.caption(
                "Daily operational workload across CBP custody and HHS care, illustrating overall system demand throughout the reporting period."
            )

    with right:

        backlog_fig = create_rolling_backlog_chart(df)

        backlog_fig = add_anomaly_markers(
            backlog_fig,
            bottlenecks,
            "date",
            "rolling_cbp_backlog"
        )

        st.plotly_chart(
            backlog_fig,
            use_container_width=True
        )
        
        st.caption(
            "Rolling backlog highlights sustained congestion trends and helps identify prolonged periods of operational pressure."
        )

    render_capacity_summary(
        capacity_summary
    )
    
    st.markdown(
        """
        <div class="section-title">
            🧠 Capacity Assessment
        </div>

        <div class="section-subtitle">
            Executive interpretation of operational workload, capacity utilization, and resource readiness across the care transition pipeline.
        </div>
        """,
        unsafe_allow_html=True
    )

    render_capacity_interpretation(
        capacity_summary
    )

    st.divider()
    
def render_capacity_summary(
    capacity_summary
):
    """
    Display executive capacity KPIs.
    """

    kpis = capacity_summary["kpis"]

    average_cbp = kpis["average_cbp_load"]

    average_hhs = kpis["average_hhs_load"]

    peak_hhs = kpis["peak_hhs_capacity"]

    average_utilization = kpis["average_utilization"]

    c1, c2, c3, c4 = st.columns(4)

    with c1:

        render_kpi_card(
            title=average_cbp["title"],
            value=average_cbp["value"],
            icon=average_cbp["icon"],
            subtitle=average_cbp["subtitle"]
        )

    with c2:

        render_kpi_card(
            title=average_hhs["title"],
            value=average_hhs["value"],
            icon=average_hhs["icon"],
            subtitle=average_hhs["subtitle"]
        )

    with c3:

        render_kpi_card(
            title=peak_hhs["title"],
            value=peak_hhs["value"],
            icon=peak_hhs["icon"],
            subtitle=peak_hhs["subtitle"]
        )

    with c4:

        render_kpi_card(
            title=average_utilization["title"],
            value=average_utilization["value"],
            icon=average_utilization["icon"],
            subtitle=average_utilization["subtitle"]
        )
        
def render_capacity_interpretation(
    capacity_summary
):
    """
    Display executive capacity interpretation.
    """

    left, right = st.columns(2)

    with left:

        assessment = capacity_summary["capacity_assessment"]

        render_info_card(
            title=assessment["title"],
            icon=assessment["icon"],
            content=assessment["content"]
        )

        workload = capacity_summary["cbp_workload"]

        render_info_card(
            title=workload["title"],
            icon=workload["icon"],
            content=workload["content"]
        )

    with right:

        hhs = capacity_summary["hhs_capacity"]

        render_info_card(
            title=hhs["title"],
            icon=hhs["icon"],
            content=hhs["content"]
        )

        recommendation = capacity_summary["recommendation"]

        render_info_card(
            title=recommendation["title"],
            icon=recommendation["icon"],
            content=recommendation["content"]
        )            


# ======================================================
# 🚧 Bottleneck Intelligence
# ======================================================

def render_bottleneck_detection(
    bottlenecks,
    bottleneck_summary
):
    """
    Display operational bottleneck intelligence.
    """

    st.markdown(
        """
        <div class="section-title">
            🚧 Bottleneck Intelligence
        </div>

        <div class="section-subtitle">
            Detect operational congestion, identify workflow bottlenecks, and prioritize intervention 
            opportunities to maintain efficient care transitions.
        </div>
        """,
        unsafe_allow_html=True
    )

    render_bottleneck_summary(
        bottleneck_summary
    )

    render_bottleneck_table(
        bottlenecks
    )

    render_bottleneck_insights(
        bottleneck_summary
    )

    st.divider()
    
def render_bottleneck_summary(
    bottleneck_summary
):
    """
    Executive KPI summary.
    """

    kpis = bottleneck_summary["kpis"]

    bottlenecks_card = kpis["bottlenecks"]

    peak_cbp_card = kpis["peak_cbp"]

    peak_hhs_card = kpis["peak_hhs"]

    average_flow_card = kpis["average_flow"]

    c1, c2, c3, c4 = st.columns(4)

    with c1:

        render_kpi_card(
            title=bottlenecks_card["title"],
            value=bottlenecks_card["value"],
            icon=bottlenecks_card["icon"],
            subtitle=bottlenecks_card["subtitle"]
        )

    with c2:

        render_kpi_card(
            title=peak_cbp_card["title"],
            value=peak_cbp_card["value"],
            icon=peak_cbp_card["icon"],
            subtitle=peak_cbp_card["subtitle"]
        )

    with c3:

        render_kpi_card(
            title=peak_hhs_card["title"],
            value=peak_hhs_card["value"],
            icon=peak_hhs_card["icon"],
            subtitle=peak_hhs_card["subtitle"]
        )

    with c4:

        render_kpi_card(
            title=average_flow_card["title"],
            value=average_flow_card["value"],
            icon=average_flow_card["icon"],
            subtitle=average_flow_card["subtitle"]
        )
        
def render_bottleneck_table(bottlenecks):
    """
    Display prioritized bottleneck periods.
    """

    st.markdown(
        """
        <div class="section-title">
            📋 Priority Investigation Queue
        </div>

        <div class="section-subtitle">
            Highest-priority operational bottlenecks ranked by backlog severity for executive review and resource allocation.
        </div>
        """,
        unsafe_allow_html=True
    )

    if bottlenecks.empty:

        st.success(
            "No significant operational bottlenecks were detected during the selected reporting period."
        )

        return

    review = bottlenecks.copy()

    review = review.sort_values(
        "cbp_backlog",
        ascending=False
    )

    st.dataframe(

        review[
            [
                "date",
                "cbp_backlog",
                "hhs_backlog",
                "net_flow"
            ]
        ],

        use_container_width=True,

        hide_index=True
    )
    
def render_bottleneck_insights(
    bottleneck_summary
):
    """
    Executive interpretation.
    """

    left, right = st.columns(2)

    assessment = bottleneck_summary["assessment"]

    recommendation = bottleneck_summary["recommendation"]

    with left:

        render_info_card(
            title=assessment["title"],
            icon=assessment["icon"],
            content=assessment["content"]
        )

    with right:

        render_info_card(
            title=recommendation["title"],
            icon=recommendation["icon"],
            content=recommendation["content"]
        )                


# ======================================================
# OPERATIONAL ASSESSMENT
# ======================================================

def render_operational_insights(
    operations_summary
):
    """
    Executive interpretation of overall operational performance.
    """

    st.markdown(
        """
        <div class="section-title">
            🧠 Operational Assessment
        </div>

        <div class="section-subtitle">
            Executive interpretation of processing efficiency, operational capacity, backlog conditions, and overall system readiness.
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:

        processing_card = operations_summary["processing_efficiency"]

        render_info_card(
            title=processing_card["title"],
            icon=processing_card["icon"],
            content=processing_card["content"]
        )

        backlog_card = operations_summary["backlog_assessment"]

        render_info_card(
            title=backlog_card["title"],
            icon=backlog_card["icon"],
            content=backlog_card["content"]
        )

    with col2:

        capacity_card = operations_summary["operational_capacity"]

        render_info_card(
            title=capacity_card["title"],
            icon=capacity_card["icon"],
            content=capacity_card["content"]
        )

        status_card = operations_summary["operational_status"]

        render_info_card(
            title=status_card["title"],
            icon=status_card["icon"],
            content=status_card["content"]
        )

    st.divider()
 
    
# ======================================================
# OPERATIONAL RECOMMENDATIONS
# ======================================================

def render_executive_recommendations(
    recommendations
):
    """
    AI-assisted operational recommendations.
    """

    st.markdown(
        """
        <div class="section-title">
            💡 Operational Recommendations
        </div>

        <div class="section-subtitle">
            AI-assisted recommendations generated from workflow performance, capacity utilization, and operational bottleneck analysis to support informed decision-making.
        </div>
        """,
        unsafe_allow_html=True
    )

    cols = st.columns(len(recommendations))

    for col, rec in zip(cols, recommendations):

        with col:

            render_info_card(

                title=f"{rec['priority']} • {rec['title']}",

                icon="💡",

                content=rec["message"]

            )   


# ======================================================
# FOOTER
# ======================================================

def render_footer():
    """
    Render Operations Dashboard footer.
    """

    st.markdown("---")

    st.caption(
        "Care Transition Operational Intelligence Platform • Operation Dashboard"
    )

    st.caption(
        "Historical Analytics • Version 1.0 • Data Source: HHS Unaccompanied Children Program"
    )