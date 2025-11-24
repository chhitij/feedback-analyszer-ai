import streamlit as st
import pandas as pd

def render_input_data_tab(reviews_df: pd.DataFrame, emails_df: pd.DataFrame, expected_df: pd.DataFrame):
    """
    Renders the Input Data tab showing raw CSV data
    
    Args:
        reviews_df: DataFrame containing app store reviews
        emails_df: DataFrame containing support emails
        expected_df: DataFrame containing expected classifications
    """
    st.subheader("📱 App Store Reviews")
    st.dataframe(reviews_df, use_container_width=True)
    
    st.subheader("📧 Support Emails")
    st.dataframe(emails_df, use_container_width=True)
    
    st.subheader("✅ Expected Classifications (Ground Truth)")
    st.dataframe(expected_df, use_container_width=True)
