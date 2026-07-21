"""
performance_metrics_engine.py

---------------------------------------------------------
Performance Metrics Engine

Creates all derived performance metrics used throughout the Operational Intelligence Platform.

This module enriches the dataframe by generating rolling KPIs, efficiency metrics, capacity indicators and operational indexes.

Pipeline

Raw Data
      ↓
Data Cleaner
      ↓
KPI Engine
      ↓
Stress Engine
      ↓
Performance Metrics Engine   
      ↓
Analytics Engine
      ↓
Dashboard
---------------------------------------------------------
"""

import numpy as np


# ==========================================================
# PERFORMANCE METRICS ENGINE
# ==========================================================

def add_performance_metrics(df):
    """
    Add all derived operational performance metrics.
    """

    df = df.copy()

    # ------------------------------------------------------
    # Total Backlog
    # ------------------------------------------------------

    df["total_backlog"] = (
        df["cbp_backlog"] +
        df["hhs_backlog"]
    )

    # ------------------------------------------------------
    # Rolling CBP Backlog
    # ------------------------------------------------------

    df["rolling_cbp_backlog"] = (
        df["cbp_backlog"]
        .rolling(7, min_periods=1)
        .mean()
    )

    # ------------------------------------------------------
    # Rolling HHS Backlog
    # ------------------------------------------------------

    df["rolling_hhs_backlog"] = (
        df["hhs_backlog"]
        .rolling(7, min_periods=1)
        .mean()
    )

    # ------------------------------------------------------
    # Rolling Total Backlog
    # ------------------------------------------------------

    df["rolling_backlog"] = (
        df["total_backlog"]
        .rolling(7, min_periods=1)
        .mean()
    )

    # ------------------------------------------------------
    # Daily Backlog Change
    # ------------------------------------------------------

    df["backlog_change"] = (
        df["total_backlog"].diff().fillna(0)
    )

    # ------------------------------------------------------
    # Backlog Growth Rate
    # ------------------------------------------------------

    df["backlog_growth_rate"] = (
        df["total_backlog"]
        .pct_change()
        .replace([np.inf, -np.inf], np.nan)
        .fillna(0)
        * 100
    )
    
    # ------------------------------------------------------
    # Daily Throughput
    # ------------------------------------------------------
    df["daily_throughput"] = (
        df["children_transferred_out_of_cbp_custody"] +
        df["children_discharged_from_hhs_care"]
    )

    # ------------------------------------------------------
    # Rolling Throughput
    # ------------------------------------------------------
    
    df["rolling_throughput"] = (
        df["daily_throughput"]
        .rolling(7, min_periods=1)
        .mean()
    )

    # ------------------------------------------------------
    # Throughput Growth
    # ------------------------------------------------------
    
    df["throughput_growth"] = (
        df["daily_throughput"]
        .pct_change()
        .replace([np.inf, -np.inf], np.nan)
        .fillna(0)
        * 100
    )
   
    # ------------------------------------------------------
    # System Load
    # ------------------------------------------------------
        
    df["system_load"] = (
        df["children_in_cbp_custody"] +
        df["children_in_hhs_care"]
    )

    # ------------------------------------------------------
    # Rolling System Load
    # ------------------------------------------------------
    
    df["rolling_system_load"] = (
        df["system_load"]
        .rolling(7, min_periods=1)
        .mean()
    )

    # ------------------------------------------------------
    # Capacity Pressure
    # ------------------------------------------------------
    
    df["capacity_pressure"] = (
        df["cbp_backlog"] /
        (
            df["cbp_backlog"] +
            df["children_transferred_out_of_cbp_custody"]
        )
    ).replace([np.inf, -np.inf], np.nan).fillna(0) * 100

    # ------------------------------------------------------
    # System Utilization
    # ------------------------------------------------------
    
    df["system_utilization"] = (
        df["children_in_hhs_care"] /
        (
            df["children_in_hhs_care"] +
            df["cbp_backlog"]
        )
    ).replace([np.inf, -np.inf], np.nan).fillna(0) * 100

    # ------------------------------------------------------
    # Rolling Utilization
    # ------------------------------------------------------
    
    df["rolling_utilization"] = (
        df["system_utilization"]
        .rolling(7, min_periods=1)
        .mean()
    )

    # ------------------------------------------------------
    # Flow Balance
    # ------------------------------------------------------
        
    df["flow_balance"] = (
        df["children_transferred_out_of_cbp_custody"]
        -
        df["children_discharged_from_hhs_care"]
    )

    # ------------------------------------------------------
    # Rolling Flow Balance
    # ------------------------------------------------------
    
    df["rolling_flow_balance"] = (
        df["flow_balance"]
        .rolling(7, min_periods=1)
        .mean()
    )

    # ------------------------------------------------------
    # Transfer Gap
    # ------------------------------------------------------
    
    df["transfer_gap"] = (
        df["children_apprehended_and_placed_in_cbp_custody"]
        -
        df["children_transferred_out_of_cbp_custody"]
    )

    # ------------------------------------------------------
    # Throughput Volatility
    # ------------------------------------------------------
        
    df["throughput_volatility"] = (
        df["daily_throughput"]
        .rolling(14, min_periods=2)
        .std()
        .fillna(0)
    )

    # ------------------------------------------------------
    # Backlog Volatility
    # ------------------------------------------------------
    
    df["backlog_volatility"] = (
        df["total_backlog"]
        .rolling(14, min_periods=2)
        .std()
        .fillna(0)
    )

    # ------------------------------------------------------
    # Load Volatility
    # ------------------------------------------------------
    
    df["load_volatility"] = (
        df["system_load"]
        .rolling(14, min_periods=2)
        .std()
        .fillna(0)
    )

    # ------------------------------------------------------
    # Performance Index
    # ------------------------------------------------------
    
    df["performance_index"] = (
        0.40 * df["processing_efficiency"] +
        0.30 * df["placement_efficiency"] +
        0.30 * df["system_utilization"]
    )

    # ------------------------------------------------------
    # Rolling Performance Index
    # ------------------------------------------------------
    
    df["rolling_performance_index"] = (
        df["performance_index"]
        .rolling(7, min_periods=1)
        .mean()
    )
    
    # ------------------------------------------------------
    # Operational Load
    # ------------------------------------------------------
        
    df["operational_load"] = (
        df["cbp_backlog"] +
        df["hhs_backlog"] +
        df["children_in_hhs_care"]
    )

    # ------------------------------------------------------
    # Rolling Operational Load
    # ------------------------------------------------------

    df["rolling_operational_load"] = (
        df["operational_load"]
        .rolling(7, min_periods=1)
        .mean()
    )

    return df   