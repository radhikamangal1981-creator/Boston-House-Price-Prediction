import streamlit as st
import joblib
import numpy as np

st.set_page_config(page_title="Boston House Price Predictor", page_icon="🏠")

@st.cache_resource
def load_model():
    return joblib.load("house_model.pkl")

model = load_model()

st.title("🏠 Boston House Price Predictor")
st.write("Multiple Linear Regression model (R² ≈ 0.63) trained on the Boston Housing dataset.")

with st.form("house_form"):
    rm = st.number_input("Average number of rooms (RM)", min_value=3.0, max_value=9.0, value=6.0, step=0.1)
    lstat = st.number_input("% lower-status population (LSTAT)", min_value=1.0, max_value=40.0, value=12.0, step=0.5)
    ptratio = st.number_input("Pupil-teacher ratio (PTRATIO)", min_value=12.0, max_value=22.0, value=18.0, step=0.1)
    submitted = st.form_submit_button("Predict price")

if submitted:
    features = np.array([[rm, lstat, ptratio]])
    prediction = model.predict(features)[0]
    st.success(f"Estimated median home value: ${prediction * 1000:,.0f}")
    st.caption("Prices in this dataset are from the 1970s, so treat results as a demo.")