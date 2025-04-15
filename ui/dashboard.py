# ui/dashboard.py

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from main_agent import RAGLLMAgent
import streamlit as st
from main_agent import RAGLLMAgent

st.set_page_config(page_title="🩺 AI Healthcare Assistant", layout="wide")

st.title("🧠 Healthcare Diagnostic Agent")
st.markdown(
    "This tool uses **LangChain + DeepSeek R3.1.5** (via Ollama) to provide AI-assisted clinical recommendations based on patient symptoms and history."
)

st.divider()

with st.sidebar:
    st.header("📋 Patient Info")
    name = st.text_input("Patient Name", value="Anonymous")
    age = st.number_input("Age", min_value=0, max_value=120, value=30)
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    history = st.text_area("Medical History", height=150)
    symptoms = st.text_area("Current Symptoms (comma-separated)", height=100)
    run_button = st.button("Run Diagnostic")

if run_button:
    st.subheader("🧪 Diagnostic Summary")

    if not symptoms.strip():
        st.warning("Please enter at least one symptom.")
    else:
        agent = RAGLLMAgent()

        try:
            with st.spinner("Retrieving and analyzing clinical data..."):
                symptom_list = [s.strip() for s in symptoms.split(",") if s.strip()]
                patient_summary = f"{age}-year-old {gender.lower()} with history: {history}"
                result = agent.run(symptom_list, patient_summary)

            st.markdown(result)
        except Exception as e:
            st.error(f"Something went wrong: {e}")
