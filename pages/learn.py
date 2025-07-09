import streamlit as st
import os

# Set page config
st.set_page_config(
    page_title="Sifiso AI - Learn",
    page_icon="🇿🇦",
    layout="wide"
)

# Custom CSS with learning-focused styling
st.markdown("""
    <style>
    :root {
        --sa-yellow: #FFCD00;
        --sa-green: #007749;
        --sa-blue: #002395;
    }
    
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@700&family=Poppins:wght@400;600&display=swap');
    
    .course-header {
        font-family: 'Montserrat', sans-serif;
        color: var(--sa-green);
        border-left: 5px solid var(--sa-yellow);
        padding-left: 1rem;
        margin: 2rem 0 1rem;
    }
    
    .language-badge {
        background: var(--sa-blue);
        color: white;
        padding: 0.25rem 0.75rem;
        border-radius: 1rem;
        font-size: 0.8rem;
        display: inline-block;
        margin-right: 0.5rem;
    }
    
    .module-card {
        border-radius: 10px;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
        background: #f8f9fa;
        transition: transform 0.3s;
    }
    
    .module-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)

# Language selector
selected_lang = st.selectbox(
    "🌍 Choose your language",
    ["English", "isiZulu", "Afrikaans", "Sesotho"],
    key="lang_selector"
)

# Main header
st.markdown("""
    <h1 style='color:#007749; font-family:Montserrat; text-align:center;'>
        AI Education for South African Builders
    </h1>
    <p style='text-align:center; margin-bottom:2rem;'>
        Practical skills taught in contextually relevant ways
    </p>
""", unsafe_allow_html=True)

# Core Learning Tracks
st.markdown('<h2 class="course-header">Foundational Tracks</h2>', unsafe_allow_html=True)

# Track 1: AI Basics
with st.expander("🤖 AI Fundamentals for Everyone", expanded=True):
    cols = st.columns([1,3])
    with cols[0]:
        st.image("images/ai_basics.jpg", use_container_width=True)
    with cols[1]:
        st.markdown("""
        ### Understanding Artificial Intelligence
        - How AI works in everyday life
        - Basic terminology explained
        - Local applications in SA townships
        
        <div style="margin-top:1rem;">
            <span class="language-badge">English</span>
            <span class="language-badge">isiZulu</span>
            <span class="language-badge">Afrikaans</span>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("Start This Track", key="ai_basics"):
            st.switch_page("pages/ai_fundamentals.py")

# Track 2: Practical Coding
with st.expander("💻 Python for Problem Solving"):
    cols = st.columns([1,3])
    with cols[0]:
        st.image("images/python_coding.jpg", use_container_width=True)
    with cols[1]:
        st.markdown("""
        ### Coding Skills for Local Challenges
        - Automating township business tasks
        - Analyzing local economic data
        - Building simple AI models
        
        <div style="margin-top:1rem;">
            <span class="language-badge">English</span>
            <span class="language-badge">isiXhosa</span>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("Start This Track", key="python_coding"):
            st.switch_page("pages/python_basics.py")

# Footer
st.markdown("""
<div style="margin-top:3rem; padding:1.5rem; background:#00774920; border-radius:8px; text-align:center;">
    <p>Need help choosing a learning path? <a href="/contact" style="color:#007749; font-weight:bold;">Contact our education advisors</a></p>
</div>
""", unsafe_allow_html=True)