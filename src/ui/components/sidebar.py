import streamlit as st
import os

def render_sidebar():
    """
    Renders the sidebar with API key configuration
    """
    st.sidebar.header("🔐 Configuration")

    # Initialize session state for API key if not exists
    if 'api_key_set' not in st.session_state:
        st.session_state['api_key_set'] = False

    # Check if API key exists in .env file
    env_api_key = os.getenv("OPENAI_API_KEY", "")

    # API Key Input Section
    if not st.session_state['api_key_set'] and not env_api_key:
        st.sidebar.warning("⚠️ API Key Required")
        api_key_input = st.sidebar.text_input(
            "Enter OpenAI API Key", 
            type="password",
            help="Your API key will be stored only for this session"
        )
        
        if st.sidebar.button("🔓 Set API Key"):
            if api_key_input:
                os.environ["OPENAI_API_KEY"] = api_key_input
                st.session_state['api_key_set'] = True
                st.sidebar.success("✅ API Key configured!")
                st.rerun()
            else:
                st.sidebar.error("Please enter a valid API key")
        
        st.sidebar.info("""
        **Alternative:** Add to `.env` file:
        ```
        OPENAI_API_KEY="your-key-here"
        ```
        """)
        
    elif env_api_key:
        # API key loaded from .env
        os.environ["OPENAI_API_KEY"] = env_api_key
        st.session_state['api_key_set'] = True
        st.sidebar.success("✅ API Key loaded from .env")
        
    else:
        # API key already set in session
        st.sidebar.success("✅ API Key is configured")

    # Show reset button if API key is set
    if st.session_state['api_key_set']:
        if st.sidebar.button("🔄 Reset API Key"):
            del st.session_state['api_key_set']
            os.environ.pop("OPENAI_API_KEY", None)
            st.rerun()

    st.sidebar.markdown("---")
    st.sidebar.info(f"**Model:** {os.getenv('OPENAI_MODEL_NAME', 'gpt-4o-mini')}")
