import streamlit as st
import pandas as pd

def render_results_tab():
    """
    Renders the Analysis Results tab showing generated tickets and download options
    """
    if 'results' in st.session_state:
        st.subheader("🎫 Generated Tickets")
        st.dataframe(st.session_state['results'], use_container_width=True)
        
        # Statistics
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Tickets", len(st.session_state['results']))
        with col2:
            if 'category' in st.session_state['results'].columns:
                bugs = len(st.session_state['results'][st.session_state['results']['category'] == 'Bug'])
                st.metric("🐛 Bugs", bugs)
        with col3:
            if 'priority' in st.session_state['results'].columns:
                high_priority = len(st.session_state['results'][st.session_state['results']['priority'] == 'High'])
                st.metric("⚠️ High Priority", high_priority)
        
        st.markdown("---")
        st.subheader("📥 Download Results")
        csv = st.session_state['results'].to_csv(index=False).encode('utf-8')
        st.download_button(
            "⬇️ Download Tickets CSV",
            csv,
            "generated_tickets.csv",
            "text/csv",
            key='download-csv',
            use_container_width=True
        )
    else:
        st.info("ℹ️ Run the analysis in the Dashboard tab to see results here.")
