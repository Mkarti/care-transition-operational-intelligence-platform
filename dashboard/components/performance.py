"""
performance.py

Performance Intelligence Dashboard
----------------------------------------------------------

Performance monitoring and long-term operational
efficiency analytics.
"""

import streamlit as st

from utils.metrics_engine import (
    calculate_average_throughput,
    calculate_combined_backlog,
    calculate_peak_throughput
)

from utils.rules_engine import (
    get_performance_rating,
    get_performance_assessment,
)

from utils.executive_summary_engine import (
    build_performance_kpi_summary,
    build_performance_recommendations,
    build_performance_summary,
    build_performance_trend_summary,
    build_performance_benchmark_summary,
    build_stability_summary
)

from visuals.cards import (
    render_kpi_card,
    render_info_card
)

from visuals.charts import (
    create_rolling_efficiency_chart,
    create_daily_throughput_chart,
    create_rolling_backlog_chart,
    create_capacity_chart
)


# ==========================================================
# PERFORMANCE DASHBOARD
# ==========================================================

from dashboard.components.helpers import validate_dashboard_data

def render_performance(df, insights):
    """
    Render the Performance Intelligence Dashboard.
    """

    if not validate_dashboard_data(df):
        return

    operations = insights["operations"]

    summary = operations["summary"]

    processing_efficiency = operations["processing_efficiency"]
    
    performance_kpis = build_performance_kpi_summary(
        df,
        processing_efficiency
    )
    
    performance_trends = build_performance_trend_summary()
    
    performance_benchmark = (
        build_performance_benchmark_summary(df)
    )
    
    stability_summary = build_stability_summary(df)

    combined_backlog = calculate_combined_backlog(df)

    peak_throughput = calculate_peak_throughput(df)

    performance_rating = get_performance_rating(
        processing_efficiency
    )
    
    performance_assessment = get_performance_assessment(
        processing_efficiency
    )

    average_throughput = calculate_average_throughput(df)

    performance_summary = build_performance_summary(
        processing_efficiency=processing_efficiency,
        performance_rating=performance_rating,
        performance_assessment=performance_assessment,
        average_throughput=average_throughput,
        combined_backlog=combined_backlog,
        peak_throughput=peak_throughput
    )
    
    performance_recommendations = (
        build_performance_recommendations(
            summary,
            processing_efficiency,
            average_throughput
        )
    )

    render_header()

    render_performance_kpis(
        performance_kpis
    )
    
    render_performance_trends(
        df,
        performance_trends
    )
    
    render_performance_benchmarks(
        df,
        performance_benchmark
    )
    
    render_stability_analysis(
        stability_summary
    )
    
    render_performance_summary(
        performance_summary
    )

    render_performance_recommendations(
        performance_recommendations
    )

    render_footer()
 
    
# ==========================================================
# HEADER
# ==========================================================

def render_header():
    """
    Render Performance Dashboard header.    
    """

    st.markdown(
        """
        <div class="section-title">
            📈 Performance Intelligence
        </div>

        <div class="section-subtitle">
            Examine long-term efficiency, throughput consistency, operational capacity, and backlog evolution to 
            understand how system performance changes throughout the reporting period.
        </div>
        """,
        unsafe_allow_html=True
    )
 
    
# ==========================================================
# PERFORMANCE KPIs
# ==========================================================

def render_performance_kpis(
    performance_kpis
):
    """
    Render executive KPI cards for performance dashboard.
    """

    processing_card = performance_kpis["processing_efficiency"]

    throughput_card = performance_kpis["daily_throughput"]

    transfer_card = performance_kpis["daily_transfers"]

    peak_card = performance_kpis["peak_throughput"]

    c1, c2, c3, c4 = st.columns(4)

    with c1:

        render_kpi_card(
            title=processing_card["title"],
            value=processing_card["value"],
            icon=processing_card["icon"],
            subtitle=processing_card["subtitle"]
        )

    with c2:

        render_kpi_card(
            title=throughput_card["title"],
            value=throughput_card["value"],
            icon=throughput_card["icon"],
            subtitle=throughput_card["subtitle"]
        )

    with c3:

        render_kpi_card(
            title=transfer_card["title"],
            value=transfer_card["value"],
            icon=transfer_card["icon"],
            subtitle=transfer_card["subtitle"]
        )

    with c4:

        render_kpi_card(
            title=peak_card["title"],
            value=peak_card["value"],
            icon=peak_card["icon"],
            subtitle=peak_card["subtitle"]
        )

    st.divider()


# ==========================================================
# PERFORMANCE TRENDS
# ==========================================================

def render_performance_trends(
    df,
    performance_trends
):
    """
    Display long-term operational performance trends.
    """

    st.markdown(
        """
        <div class="section-title">
            📈 Performance Trends
        </div>

        <div class="section-subtitle">
            Analyze operational performance across the reporting period.
        </div>
        """,
        unsafe_allow_html=True
    )

    # ------------------------------------------------------
    # Rolling Efficiency
    # ------------------------------------------------------

    efficiency_fig = create_rolling_efficiency_chart(df)

    st.plotly_chart(
        efficiency_fig,
        use_container_width=True
    )
    
    st.caption(
        "Rolling processing efficiency highlights sustained operational performance rather than isolated daily fluctuations."
    )

    # ------------------------------------------------------
    # Throughput & Capacity
    # ------------------------------------------------------

    left, right = st.columns(2)

    with left:

        throughput_fig = create_daily_throughput_chart(df)

        st.plotly_chart(
            throughput_fig,
            use_container_width=True
        )
        
        st.caption(
            "Daily throughput reflects the volume of children successfully processed through the care transition pipeline."
        )

    with right:

        capacity_fig = create_capacity_chart(df)

        st.plotly_chart(
            capacity_fig,
            use_container_width=True
        )
        
        st.caption(
            "Operational capacity illustrates workload distribution and changing demand across the reporting period."
        )

    # ------------------------------------------------------
    # Rolling Backlog
    # ------------------------------------------------------

    backlog_fig = create_rolling_backlog_chart(df)

    st.plotly_chart(
        backlog_fig,
        use_container_width=True
    )
    
    st.caption(
        "Rolling backlog exposes persistent congestion trends and long-term operational pressure."
    )

    st.divider()
  
    # ------------------------------------------------------
    # Performance Interpretation
    # ------------------------------------------------------
    
    st.markdown(
        """
        <div class="section-title">
            📊 Performance Interpretation
        </div>

        <div class="section-subtitle">
            Executive interpretation of long-term operational efficiency, workload patterns, and system performance trends.
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:

        efficiency = performance_trends["efficiency_trend"]

        render_info_card(
            title=efficiency["title"],
            icon=efficiency["icon"],
            content=efficiency["content"]
        )

    with col2:
        
        capacity = performance_trends["capacity_trend"]

        render_info_card(
            title=capacity["title"],
            icon=capacity["icon"],
            content=capacity["content"]
        )

    st.divider()
   
    
# ==========================================================
# PERFORMANCE BENCHMARKING
# ==========================================================

def render_performance_benchmarks(
    df,
    performance_benchmark
):
    """
    Compare average, peak and variability of operational performance.
    """

    st.markdown(
        """
        <div class="section-title">
            🏆 Performance Benchmarking
        </div>

        <div class="section-subtitle">
            Compare operational throughput, consistency, and processing efficiency against historical operating
            patterns to evaluate long-term organizational performance.
        </div>
        """,
        unsafe_allow_html=True
    ) 
    
    kpis = performance_benchmark["kpis"]

    average = kpis["average_throughput"]
    peak = kpis["peak_throughput"]
    lowest = kpis["lowest_throughput"]
    consistency = kpis["consistency"]
    
    # ------------------------------------------------------
    # Benchmark KPI Cards
    # ------------------------------------------------------
    c1, c2, c3, c4 = st.columns(4)

    with c1:

        render_kpi_card(
            title=average["title"],
            value=average["value"],
            icon=average["icon"],
            subtitle=average["subtitle"]
        )

    with c2:

        render_kpi_card(
            title=peak["title"],
            value=peak["value"],
            icon=peak["icon"],
            subtitle=peak["subtitle"]
        )

    with c3:

        render_kpi_card(
            title=lowest["title"],
            value=lowest["value"],
            icon=lowest["icon"],
            subtitle=lowest["subtitle"]
        )

    with c4:

        render_kpi_card(
            title=consistency["title"],
            value=consistency["value"],
            icon=consistency["icon"],
            subtitle=consistency["subtitle"]
        )

    
    # ------------------------------------------------------
    # Benchmark Interpretation
    # ------------------------------------------------------
    st.markdown(
        """
        <div class="section-title">
            📋 Benchmark Interpretation
        </div>

        <div class="section-subtitle">
            Executive assessment of historical performance consistency, throughput capability, and operational efficiency relative to long-term benchmarks.
        </div>
        """,
        unsafe_allow_html=True
    )

    left, right = st.columns(2)

    with left:
        
        benchmark = performance_benchmark["benchmark"]

        render_info_card(
            title=benchmark["title"],
            icon=benchmark["icon"],
            content=benchmark["content"]
        )

    with right:
        
        assessment = performance_benchmark["consistency_assessment"]

        render_info_card(
            title=assessment["title"],
            icon=assessment["icon"],
            content=assessment["content"]
        )

    st.divider()   


# ==========================================================
# PERFORMANCE STABILITY
# ==========================================================

def render_stability_analysis(
    stability_summary
):
    """
    Evaluate operational stability throughout the reporting period.
    """

    st.markdown(
        """
        <div class="section-title">
            🛡️ Performance Stability
        </div>

        <div class="section-subtitle">
            Evaluate long-term operational resilience by identifying stable, moderate, and high-pressure 
            operating conditions throughout the reporting period.
        </div>
        """,
        unsafe_allow_html=True
    )
    
    kpis = stability_summary["kpis"]

    stable_days = kpis["stable_days"]

    peak_days = kpis["peak_days"]

    unstable_days = kpis["unstable_days"]

    stability_score = kpis["stability_score"]
    
    c1, c2, c3, c4 = st.columns(4)

    with c1:

        render_kpi_card(
            title=stable_days["title"],
            value=stable_days["value"],
            icon=stable_days["icon"],
            subtitle=stable_days["subtitle"]
        )

    with c2:

        render_kpi_card(
            title=peak_days["title"],
            value=peak_days["value"],
            icon=peak_days["icon"],
            subtitle=peak_days["subtitle"]
        )

    with c3:

        render_kpi_card(
            title=unstable_days["title"],
            value=unstable_days["value"],
            icon=unstable_days["icon"],
            subtitle=unstable_days["subtitle"]
        )

    with c4:

        render_kpi_card(
            title=stability_score["title"],
            value=stability_score["value"],
            icon=stability_score["icon"],
            subtitle=stability_score["subtitle"]
        )
    
        
    # ------------------------------------------------------
    # Stability Assessment
    # ------------------------------------------------------    

    st.markdown(
        """
        <div class="section-title">
            📋 Stability Assessment
        </div>

        <div class="section-subtitle">
            Executive interpretation of operational resilience, workload stability, and long-term system reliability.
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)
    
    with col1:
        
        stability = stability_summary["operational_stability"]

        render_info_card(
            title=stability["title"],
            icon=stability["icon"],
            content=stability["content"]
        )    
   
    with col2:

        assessment = stability_summary["executive_assessment"]

        render_info_card(
            title=assessment["title"],
            icon=assessment["icon"],
            content=assessment["content"]
        )

    st.divider()


# ==========================================================
# Performance Assessment
# ==========================================================

def render_performance_summary(
    performance_summary
):
    """
    Executive-level summary of overall operational performance.
    """

    st.markdown(
        """
        <div class="section-title">
            💡 Performance Assessment
        </div>

        <div class="section-subtitle">
            Executive overview of operational efficiency, throughput performance, backlog management,
            and organizational resilience to support strategic decision-making.
        </div>
        """,
        unsafe_allow_html=True
    )
    
    col1, col2 = st.columns(2)

    with col1:
        
        card = performance_summary["operational_performance"]

        render_info_card(
            title=card["title"],
            icon=card["icon"],
            content=card["content"]
        )

        card = performance_summary["capacity_management"]
        
        render_info_card(
            title=card["title"],
            icon=card["icon"],
            content=card["content"]
        )
    
    with col2:

        card = performance_summary["executive_assessment"]

        render_info_card(
            title=card["title"],
            icon=card["icon"],
            content=card["content"]
        )
        
        card = performance_summary["peak_performance"]

        render_info_card(
            title=card["title"],
            icon=card["icon"],
            content=card["content"]
        )    


# ==========================================================
# EXECUTIVE RECOMMENDATIONS
# ==========================================================

def render_performance_recommendations(
    recommendations
):
    """
    Display executive recommendations for the Performance Intelligence dashboard.
    """

    st.markdown(
        """
        <div class="section-title">
            🎯 Executive Recommendations
        </div>

        <div class="section-subtitle">
            Priority recommendations derived from operational efficiency, throughput trends, backlog behavior,
            and long-term system performance.
        </div>
        """,
        unsafe_allow_html=True
    )

    left, right = st.columns(2)

    for i, recommendation in enumerate(recommendations):

        with left if i % 2 == 0 else right:

            render_info_card(
                title=recommendation["title"],
                icon=recommendation["icon"],
                content=recommendation["message"]
            )                           


# ======================================================
# FOOTER
# ======================================================

def render_footer():
    """
    Render Performance Dashboard footer.
    """

    st.markdown("---")

    st.caption(
        "Care Transition Operational Intelligence Platform • Performance Dashboard"
    )

    st.caption(
        "Historical Analytics • Version 1.0 • Data Source: HHS Unaccompanied Children Program"
    )            