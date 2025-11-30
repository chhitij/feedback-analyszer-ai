import streamlit as st
import pandas as pd
import time
import os
import plotly.express as px
from src.main_crew import FeedbackCrew, save_results_to_csv

def render_dashboard_tab(reviews_df: pd.DataFrame, emails_df: pd.DataFrame):
    """
    Renders the Dashboard & Control tab with statistics and analysis controls
    
    Args:
        reviews_df: DataFrame containing app store reviews
        emails_df: DataFrame containing support emails
    """
    # Statistics Display
    col1, col2, col3 = st.columns(3)
    col1.metric("📱 Total Reviews", len(reviews_df))
    col2.metric("📧 Total Emails", len(emails_df))
    col3.metric("📊 Total Items", len(reviews_df) + len(emails_df))

    st.markdown("---")
    st.subheader("🎮 System Control")
    
    # Only show start button if API key is configured
    if not st.session_state.get('api_key_set', False):
        st.warning("⚠️ Please configure your API key in the sidebar to start analysis.")
    else:
        if st.button("🚀 Start Analysis Agent Crew", type="primary", use_container_width=True):
            with st.spinner("🤖 Agents are working... This may take a minute..."):
                # Create a placeholder for logs
                log_placeholder = st.empty()
                progress_bar = st.progress(0)
                
                try:
                    log_placeholder.text("⚙️ Initializing Crew...")
                    progress_bar.progress(10)
                    time.sleep(0.5)
                    
                    log_placeholder.text("📖 Reading CSV files...")
                    progress_bar.progress(30)
                    
                    # Get absolute paths to data files
                    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../'))
                    reviews_path = os.path.join(project_root, 'data/raw/app_store_reviews.csv')
                    emails_path = os.path.join(project_root, 'data/raw/support_emails.csv')
                    
                    crew = FeedbackCrew()
                    log_placeholder.text("🔄 Running agent analysis...")
                    progress_bar.progress(50)
                    
                    result = crew.run(reviews_path, emails_path)
                    
                    log_placeholder.text("💾 Processing complete! Saving results...")
                    progress_bar.progress(80)
                    
                    output_path, result_df = save_results_to_csv(result)
                    progress_bar.progress(100)
                    
                    if result_df is not None and not result_df.empty:
                        st.success(f"✅ Analysis Complete! Tickets saved to `{output_path}`")
                        st.session_state['results'] = result_df
                        log_placeholder.empty()
                        progress_bar.empty()
                    else:
                        st.warning("⚠️ Analysis completed but no structured results. Check raw output:")
                        # Display raw result
                        if hasattr(result, 'raw'):
                            st.text_area("Raw Output", result.raw, height=300)
                        else:
                            st.text_area("Raw Output", str(result), height=300)
                        
                except Exception as e:
                    import traceback
                    st.error(f"❌ An error occurred: {str(e)}")
                    st.code(traceback.format_exc(), language="python")
                    progress_bar.empty()
                    log_placeholder.empty()

    # Display results if available
    if 'results' in st.session_state:
        st.markdown("---")
        st.subheader("📊 Latest Analysis Results")
        st.dataframe(st.session_state['results'], use_container_width=True)
        
        # Simple charts
        if 'category' in st.session_state['results'].columns:
            col1, col2 = st.columns(2)
            with col1:
                fig = px.pie(st.session_state['results'], names='category', title='Feedback Categories')
                st.plotly_chart(fig, use_container_width=True)
            
            with col2:
                if 'priority' in st.session_state['results'].columns:
                    fig2 = px.bar(st.session_state['results'], x='priority', title='Priority Distribution')
                    st.plotly_chart(fig2, use_container_width=True)
