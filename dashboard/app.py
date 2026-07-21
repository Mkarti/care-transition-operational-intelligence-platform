"""
app.py

Care Transition Operational Intelligence Platform
----------------------------------------------------------

Application entry point.

Responsible for:

• Initializing Streamlit
• Loading global styling
• Executing the data pipeline
• Running the analytics engine
• Rendering dashboard navigation
• Routing between dashboards
"""

import os
import sys
import streamlit as st

# ==========================================================
# PROJECT ROOT
# ==========================================================

PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

sys.path.insert(0, PROJECT_ROOT)

# ==========================================================
# INTERNAL IMPORTS
# ==========================================================

from pipeline import build_pipeline
from analytics import run_insights

from components.header import render_header
from components.sidebar import render_sidebar

from components.executive import render_executive
from components.operations import render_operations
from components.performance import render_performance
from components.risk import render_risk
from components.ai_decision import render_ai_decision

# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="Care Transition Operational Intelligence Platform",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================================
# CONSTANTS
# ==========================================================

FILE_PATH = os.path.join(
    PROJECT_ROOT,
    "data",
    "raw",
    "HHS_Unaccompanied_Alien_Children_Program.csv"
)

# ==========================================================
# LOAD GLOBAL CSS
# ==========================================================

@st.cache_data(show_spinner=False)
def load_css():
    """
    Load global dashboard stylesheet.
    """

    css_path = os.path.join(
        os.path.dirname(__file__),
        "assets",
        "design_system.css"
    )

    if os.path.exists(css_path):

        with open(css_path, encoding="utf-8") as f:

            return f.read()

    return ""


# ==========================================================
# LOAD DATA PIPELINE
# ==========================================================

@st.cache_data(show_spinner=False)
def load_dataset():
    """
    Execute the complete ETL pipeline.
    """
    return build_pipeline(FILE_PATH)


# ==========================================================
# APPLICATION
# ==========================================================

def main():
    """
    Launch the Care Transition Operational
    Intelligence Platform.
    """

    css = load_css()

    if css:
        st.markdown(
            f"<style>{css}</style>",
            unsafe_allow_html=True
        )    

    with st.spinner(
        "Loading Operational Intelligence Platform..."
    ):

        # --------------------------------------------------
        # Data Pipeline
        # --------------------------------------------------

        df = load_dataset()

        # --------------------------------------------------
        # Sidebar
        # --------------------------------------------------

        navigation = render_sidebar(df)

        selected_dashboard = navigation["page"]
        
        filtered_df = navigation["data"]

        # --------------------------------------------------
        # Analytics Engine
        # --------------------------------------------------

        insights = run_insights(filtered_df)

    # ------------------------------------------------------
    # Global Header
    # ------------------------------------------------------

    render_header()

    # ------------------------------------------------------
    # Dashboard Router
    # ------------------------------------------------------

    dashboards = {
        "🏠 Executive": render_executive,
        "⚙️ Operations": render_operations,
        "📈 Performance": render_performance,
        "🚨 Risk Intelligence": render_risk,
        "🤖 AI Decision": render_ai_decision
    }

    dashboard = dashboards.get(selected_dashboard)

    if dashboard:
        dashboard(filtered_df, insights)
    else:
        st.error(
            "Selected dashboard could not be loaded."
        )


# ==========================================================
# APPLICATION ENTRY POINT
# ==========================================================

if __name__ == "__main__":
    main()