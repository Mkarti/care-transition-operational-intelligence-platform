"""
header.py

Global application header for the
Care Transition Operational Intelligence Platform.
"""

import streamlit as st

# ==========================================================
# APPLICATION INFORMATION
# ==========================================================

APPLICATION_TITLE = (
    "🧭 Care Transition Efficiency & Placement Outcome Analytics"
)

APPLICATION_SUBTITLE = (
    "Operational Intelligence Platform | "
    "CBP → HHS → Placement Analytics"
)

# ==========================================================
# GLOBAL HEADER
# ==========================================================

def render_header():
    """
    Render the global application header.
    """

    st.title(APPLICATION_TITLE)

    st.caption(APPLICATION_SUBTITLE)

    st.divider()