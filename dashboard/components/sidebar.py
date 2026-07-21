"""
sidebar.py

Sidebar navigation and filtering for the
Care Transition Operational Intelligence Platform.
"""

import pandas as pd
import streamlit as st

# ==========================================================
# DASHBOARD OPTIONS
# ==========================================================

DASHBOARDS = [

    "🏠 Executive",

    "⚙️ Operations",

    "📈 Performance",

    "🚨 Risk Intelligence",

    "🤖 AI Decision"

]

# ==========================================================
# PLATFORM INFORMATION
# ==========================================================

PLATFORM_VERSION = "1.0"

PIPELINE_STATUS = "Production"

EDITION = "Enterprise Edition"


# ==========================================================
# SIDEBAR
# ==========================================================

def render_sidebar(df):
    """
    Render the application sidebar and return the
    selected dashboard together with the filtered dataset.
    """
    
    # ======================================================
    # APPLICATION BRANDING
    # ======================================================

    st.sidebar.markdown(
        """
        ## 🧭 Care Transition

        ### Operational Intelligence Platform
        """
    )

    st.sidebar.caption(
        f"Enterprise Dashboard • Version {PLATFORM_VERSION}"
    )

    st.sidebar.divider()

    # ======================================================
    # DASHBOARD NAVIGATION
    # ======================================================

    selected_dashboard = st.sidebar.radio(

        "Dashboard",

        DASHBOARDS

    )

    st.sidebar.divider()

    # ======================================================
    # DATA FILTERS
    # ======================================================

    st.sidebar.markdown("## 🔎 Data Filters")

    min_date = df["date"].min()

    max_date = df["date"].max()

    selected_dates = st.sidebar.date_input(

        "Date Range",

        [min_date, max_date]

    )

    filtered_df = df.copy()

    start_date = min_date

    end_date = max_date

    if len(selected_dates) == 2:

        start_date, end_date = selected_dates

        filtered_df = filtered_df[

            (filtered_df["date"] >= pd.to_datetime(start_date))

            &

            (filtered_df["date"] <= pd.to_datetime(end_date))

        ]

    st.sidebar.divider()

    # ======================================================
    # FILTER SUMMARY
    # ======================================================

    st.sidebar.markdown("## 📊 Filter Summary")

    st.sidebar.caption(
        f"Reporting Years: "
        f"{df['date'].dt.year.min()} – "
        f"{df['date'].dt.year.max()}"
    )

    st.sidebar.caption(
        f"Filtered Records: {len(filtered_df):,}"
    )

    st.sidebar.caption(

        f"Selected Range:\n"

        f"{start_date:%d %b %Y} → {end_date:%d %b %Y}"

    )

    st.sidebar.divider()

    # ======================================================
    # PLATFORM INFORMATION
    # ======================================================

    st.sidebar.markdown("## ℹ Platform")

    st.sidebar.caption(
        f"Version: {PLATFORM_VERSION}"
    )

    st.sidebar.caption(
        f"Pipeline: {PIPELINE_STATUS}"
    )

    st.sidebar.caption(
        f"Dashboard: {EDITION}"
    )

    # ======================================================
    # RETURN
    # ======================================================

    return {

        "page": selected_dashboard,

        "data": filtered_df

    }