import streamlit as st
import os

# Set page config
st.set_page_config(page_title="Tools | Sifiso AI", layout="wide")

# Custom CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@600&family=Open+Sans&display=swap');

    body {
        font-family: 'Open Sans', sans-serif;
        color: #374151;
    }
    h1, h2, h3 {
        font-family: 'Montserrat', sans-serif;
    }
    .header {
        position: fixed;
        top: 0;
        width: 100%;
        background-color: #ffffff;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        z-index: 1000;
        padding: 1rem 2rem;
    }
    .header a {
        color: #374151;
        font-weight: 600;
        margin-left: 1.5rem;
        text-decoration: none;
    }
    .header a:hover {
        color: #D97706;
    }
    .logo {
        color: #D97706;
        font-size: 1.5rem;
        font-weight: bold;
    }
    .section {
        padding: 4rem 2rem;
        margin-top: 60px;
    }
    .card {
        background-color: #ffffff;
        border-radius: 0.5rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        padding: 1.5rem;
        margin-bottom: 1rem;
    }
    .footer {
        background-color: #D97706;
        color: #FEF3C7;
        padding: 1.5rem;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

def render_header():
    """Render the sticky header."""
    st.markdown("""
        <div class="header">
            <a href="/" class="logo">Sifiso AI</a>
            <a href="/learn">Learn</a>
            <a href="/community">Community</a>
            <a href="/tools">Tools</a>
            <a href="/about">About</a>
            <a href="/contact">Contact</a>
        </div>
    """, unsafe_allow_html=True)

def render_footer():
    """Render the footer."""
    st.markdown("""
        <div class="footer">
            <p>© 2025 Sifiso AI. All rights reserved.</p>
    """, unsafe_allow_html=True)
    cols = st.columns(4)
    socials = ["facebook.png", "twitter.png", "linkedin.png", "instagram.png"]
    for i, social in enumerate(socials):
        with cols[i]:
            st.image(os.path.join("images", social), width=24)
    st.markdown('</div>', unsafe_allow_html=True)

# Render header
render_header()

# Tools Section
st.markdown('<div class="section" id="tools">', unsafe_allow_html=True)
st.header("Startup Tools for AI Builders", anchor=False)
cols = st.columns(3)
tools = [
    {"title": "AI Code Editor", "desc": "Write, test, and debug AI code with smart suggestions and real-time error checking.", "image": "code_editor.jpg"},
    {"title": "Data Visualization Tool", "desc": "Create interactive charts and graphs to better understand your AI datasets.", "image": "data_viz.jpg"},
    {"title": "Model Training Dashboard", "desc": "Monitor and optimize your AI models with detailed training insights and metrics.", "image": "model_dashboard.jpg"}
]
for i, tool in enumerate(tools):
    with cols[i]:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.image(os.path.join("images", tool["image"]), width=120)
        st.subheader(tool["title"], anchor=False)
        st.write(tool["desc"])
        st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Render footer
render_footer()