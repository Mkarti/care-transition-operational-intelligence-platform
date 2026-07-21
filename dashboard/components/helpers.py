"""
helpers.py

Reusable helper utilities for the
Care Transition Operational Intelligence Platform.
"""

import streamlit as st


# ==========================================================
# DASHBOARD DATA VALIDATION
# ==========================================================

def validate_dashboard_data(df):
    """
    Prevent dashboard rendering when no records are available after filtering.

    Returns
    -------
    bool
        True if data exists.
        False otherwise.
    """

    if df.empty:

        st.warning(
            """
            No records match the selected filters.

            Please modify the reporting period or filter selection to continue.
            """
        )

        return False

    return True