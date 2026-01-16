import streamlit as st
import requests
import pandas as pd

API_BASE = "http://localhost:8000"

st.set_page_config(
    page_title="Ops Dashboard",
    layout="wide"
)

st.title("🚀 AI Operations Dashboard")

# KPIs
kpis = requests.get(f"{API_BASE}/incidents/kpis").json()

col1, col2, col3 = st.columns(3)
col1.metric("Total Incidents", kpis["total"])
col2.metric("SLA Breaches", kpis["sla_breaches"])
col3.metric("Avg Resolution (min)", kpis["avg_resolution"])

st.divider()

# Incident table
st.subheader("📋 Incident Overview")
df = pd.DataFrame(requests.get(f"{API_BASE}/incidents").json())
st.dataframe(df)

# Charts
st.subheader("📊 Incidents by Service")
st.bar_chart(df.groupby("SERVICE").size())

# AI insights
st.subheader("🔥 High-Risk Incidents (AI)")
high_risk_df = pd.DataFrame(requests.get(f"{API_BASE}/incidents/high-risk").json())
st.dataframe(high_risk_df)
