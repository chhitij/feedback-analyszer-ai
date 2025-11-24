import pandas as pd
import streamlit as st
import os

@st.cache_data
def load_data():
    """
    Loads feedback data from CSV files
    
    Returns:
        tuple: (reviews_df, emails_df, expected_df)
    """
    # Get project root directory (2 levels up from this file)
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../'))
    
    reviews = pd.read_csv(os.path.join(project_root, 'data/raw/app_store_reviews.csv'))
    emails = pd.read_csv(os.path.join(project_root, 'data/raw/support_emails.csv'))
    expected = pd.read_csv(os.path.join(project_root, 'data/raw/expected_classifications.csv'))
    
    return reviews, emails, expected
