import streamlit as st
import numpy as np
import pandas as pd
import time

st.set_page_config(page_title="InfraGuard Pro", layout="wide")

st.title("InfraGuard Pro - Predictive Infrastructure Intelligence")

st.markdown("Advanced AI-powered system for predictive maintenance and infrastructure risk analysis.")

st.markdown("---")

# ==============================
# SELECT INFRASTRUCTURE ASSET
# ==============================

asset = st.selectbox(
    "Select Infrastructure Asset",
    ["Bridge A", "Transformer B", "Factory Machine C"]
)

# ==============================
# WHAT-IF SIMULATION
# ==============================

st.subheader("Operational Simulation")
load_factor = st.slider("Simulate Load Increase (%)", 0, 50, 0)

# ==============================
# SENSOR BASELINES
# ==============================

baseline_temp = 70
baseline_vibration = 15

# Simulated data with load effect
temperature = np.random.normal(baseline_temp + load_factor * 0.3, 5)
vibration = np.random.normal(baseline_vibration + load_factor * 0.2, 3)

# Store historical data
if "data" not in st.session_state:
    st.session_state.data = []

st.session_state.data.append([temperature, vibration])

df = pd.DataFrame(st.session_state.data, columns=["Temperature", "Vibration"])

# ==============================
# DISPLAY SENSOR DATA
# ==============================

st.subheader("Live Sensor Data")
st.line_chart(df)

# ==============================
# ADVANCED RISK CALCULATION
# ==============================

temp_deviation = abs(temperature - baseline_temp)
vib_deviation = abs(vibration - baseline_vibration)

risk_score = 100 - (temp_deviation * 2 + vib_deviation * 3)
risk_score = max(0, min(100, int(risk_score)))

# ==============================
# HEALTH CREDIT SCORE
# ==============================

st.subheader("Infrastructure Health Credit Score")
st.metric("Health Score", f"{risk_score}/100")

if risk_score > 80:
    st.success("Status: Stable")
elif risk_score > 60:
    st.warning("Status: Minor Deviation")
elif risk_score > 40:
    st.warning("Status: Warning Level")
else:
    st.error("Status: Critical Risk - Immediate Inspection Required")

# ==============================
# FAILURE EXPLANATION ENGINE
# ==============================

st.subheader("AI Failure Analysis")

if temp_deviation > vib_deviation:
    st.write("Primary Risk Factor: Temperature deviation detected.")
elif vib_deviation > temp_deviation:
    st.write("Primary Risk Factor: Abnormal vibration pattern detected.")
else:
    st.write("Multiple parameters deviating from baseline.")

# ==============================
# ECONOMIC IMPACT ESTIMATOR
# ==============================

st.subheader("Economic Impact Estimation")

estimated_downtime_cost = (100 - risk_score) * 5000
st.write(f"Estimated Potential Downtime Cost: ₹{estimated_downtime_cost:,}")

# ==============================
# FUTURE FAILURE TREND
# ==============================

st.subheader("Failure Trend Forecast")

trend_prediction = "Low Risk"
if risk_score < 50:
    trend_prediction = "High probability of failure within next operational cycle"
elif risk_score < 70:
    trend_prediction = "Moderate risk if load increases further"

st.write(trend_prediction)

time.sleep(1)
st.rerun()
