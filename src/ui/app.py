import streamlit as st
import sys
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

# Import UI components
from src.ui.components.sidebar import render_sidebar
from src.ui.utils.data_loader import load_data
from src.ui.tabs.dashboard_tab import render_dashboard_tab
from src.ui.tabs.input_data_tab import render_input_data_tab
from src.ui.tabs.results_tab import render_results_tab

# Page configuration
st.set_page_config(page_title="Feedback Analyzer AI", layout="wide")

# Header
st.title("🤖 Intelligent Feedback Analysis System")
st.markdown("Multi-Agent System for processing user feedback and generating actionable tickets.")

# Render sidebar
render_sidebar()

# Load data
try:
    reviews_df, emails_df, expected_df = load_data()
except FileNotFoundError:
    st.error("📁 Data files not found. Please run `python generate_mock_data.py` first.")
    st.stop()

# Create tabs
tab1, tab2, tab3 = st.tabs(["📊 Dashboard & Control", "📝 Input Data", "✅ Analysis Results"])

# Render tabs
with tab1:
    render_dashboard_tab(reviews_df, emails_df)

with tab2:
    render_input_data_tab(reviews_df, emails_df, expected_df)

with tab3:
    render_results_tab()