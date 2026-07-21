"""
insight_formatter.py

Reusable formatter for executive insight cards.

Creates a standardized structure for all executive,
operations, risk, and AI recommendation cards.
"""


def build_executive_card(
    title,
    icon,
    status,
    summary,
    recommendation,
    impact
):
    """
    Build a standardized executive insight card.
    """

    return {

        "title": title,

        "icon": icon,

        "status": status,

        "summary": summary,

        "recommendation": recommendation,

        "impact": impact

    }