import streamlit as st


# ==========================================================
# KPI CARD
# ==========================================================

import streamlit as st

def render_kpi_card(title, value, icon="📊", subtitle=None):

    html = f"""
<div style="
background:#1f2937;
padding:20px;
border-radius:15px;
border:2px solid #2563EB;
margin-bottom:10px;
">

<h3 style="color:white;">
{icon} {title}
</h3>

<h1 style="color:#60A5FA;">
{value}
</h1>

<p style="color:#d1d5db;">
{subtitle or ""}
</p>

</div>
"""

    st.markdown(html, unsafe_allow_html=True)


# ==========================================================
# RECOMMENDATION CARD
# ==========================================================

def render_recommendation_card(rec):
    """
    Render a professional executive recommendation card.
    """

    priority = rec.get("priority", "Low")

    # ------------------------------------------------------
    # Priority Badge Colors
    # ------------------------------------------------------

    if priority == "High":

        badge_bg = "#FDECEC"
        badge_fg = "#D93025"

    elif priority == "Medium":

        badge_bg = "#FFF4E5"
        badge_fg = "#F29900"

    else:

        badge_bg = "#EAF7EE"
        badge_fg = "#188038"

    st.markdown(
        f"""
<div class="dashboard-card">

<div style="display:flex;
justify-content:space-between;
align-items:center;
margin-bottom:15px;">

<div style="
font-size:22px;
font-weight:700;">

{rec["icon"]} {rec["title"]}

</div>

<div style="
background:{badge_bg};
color:{badge_fg};
padding:6px 14px;
border-radius:20px;
font-size:12px;
font-weight:700;">

{priority} Priority

</div>

</div>

<hr style="margin-bottom:18px;">

<div style="font-weight:700;
margin-bottom:6px;">

📌 Operational Summary

</div>

<div style="margin-bottom:18px;
line-height:1.7;">

{rec["summary"]}

</div>

<div style="font-weight:700;
margin-bottom:6px;">

🎯 Recommended Action

</div>

<div style="margin-bottom:18px;
line-height:1.7;">

{rec["recommendation"]}

</div>

<div style="font-weight:700;
margin-bottom:6px;">

📈 Expected Impact

</div>

<div style="line-height:1.7;">

{rec["impact"]}

</div>

</div>
""",
        unsafe_allow_html=True,
    )


# ==========================================================
# ALERT CARD
# ==========================================================

def render_alert_card(alert):
    """
    Render professional executive alert card.
    """

    severity = alert["severity"]

    # ------------------------------------------------------
    # Severity Colors
    # ------------------------------------------------------

    if severity == "High":

        bg = "#FDECEC"
        fg = "#D93025"

    elif severity == "Medium":

        bg = "#FFF4E5"
        fg = "#F29900"

    else:

        bg = "#EAF7EE"
        fg = "#188038"

    st.markdown(
        f"""
<div class="dashboard-card">

<div style="display:flex;justify-content:space-between;align-items:center;">

<div style="font-size:22px;font-weight:700;">
{alert["icon"]} {alert["title"]}
</div>

<div style="
background:{bg};
color:{fg};
padding:4px 12px;
border-radius:20px;
font-size:12px;
font-weight:700;">

{severity} Alert

</div>

</div>

<hr style="margin:14px 0;">

<b>Executive Summary</b>

<div style="margin-top:6px;margin-bottom:15px;">
{alert["summary"]}
</div>

<b>Recommended Action</b>

<div style="margin-top:6px;margin-bottom:15px;">
{alert["action"]}
</div>

<b>Potential Impact</b>

<div style="margin-top:6px;">
{alert["impact"]}
</div>

</div>
""",
        unsafe_allow_html=True
    )


# ==========================================================
# INFORMATION CARD
# ==========================================================

def render_info_card(
    title=None,
    content=None,
    icon="ℹ️",
    card=None
):
    """
    Render an information card.

    Supports:
    1. Legacy cards (title + content + icon)
    2. Executive cards (card dictionary)
    """

    # --------------------------------------------------
    # Legacy Card (Current Behaviour)
    # --------------------------------------------------

    if card is None:

        st.markdown(
            f"""
<div class="dashboard-card">

<div style="font-size:22px;font-weight:700;">
{icon} {title}
</div>

<div style="margin-top:15px;">
{content}
</div>

</div>
""",
            unsafe_allow_html=True,
        )

        return

    # --------------------------------------------------
    # Executive Card
    # --------------------------------------------------

    st.markdown(
        f"""
<div class="dashboard-card">

<div style="font-size:22px;font-weight:700;">
{card["icon"]} {card["title"]}
</div>

<div style="margin-top:12px;">

<b>Status</b><br>
{card["status"]}

<br><br>

<b>Summary</b><br>
{card["summary"]}

<br><br>

<b>💡 Recommendation</b><br>
{card["recommendation"]}

<br><br>

<b>📈 Expected Impact</b><br>
{card["impact"]}

</div>

</div>
""",
        unsafe_allow_html=True,
    )