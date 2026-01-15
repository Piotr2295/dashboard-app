import streamlit as st
from services.incident_service import (
    get_incident_kpis,
    get_high_risk_incidents
)
from data.snowflake_client import fetch_incidents

st.set_page_config(
    page_title="Ops Dashboard",
    layout="wide"
)

st.title("🚀 AI Operations Dashboard")

# KPIs
kpis = get_incident_kpis()

col1, col2, col3 = st.columns(3)
col1.metric("Total Incidents", kpis["total"])
col2.metric("SLA Breaches", kpis["sla_breaches"])
col3.metric("Avg Resolution (min)", kpis["avg_resolution"])

st.divider()

# Incident table
st.subheader("📋 Incident Overview")
df = fetch_incidents()
st.dataframe(df)

# Charts
st.subheader("📊 Incidents by Service")
st.bar_chart(df.groupby("SERVICE").size())

# AI insights
st.subheader("🔥 High-Risk Incidents (AI)")
st.dataframe(get_high_risk_incidents())
