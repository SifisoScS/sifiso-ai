import streamlit as st
import os

# Set page config
st.set_page_config(page_title="Sifiso AI | Learn AI in Your Language", layout="wide")

# Custom CSS for Tailwind-like styling
st.markdown("""
    <style>
    /* Font imports */
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@600&family=Open+Sans&display=swap');

    body {
        font-family: 'Open Sans', sans-serif;
        color: #374151; /* text-gray-800 */
    }
    h1, h2, h3 {
        font-family: 'Montserrat', sans-serif;
    }
    /* Sticky header */
    .header {
        position: fixed;
        top: 0;
        width: 100%;
        background-color: #ffffff; /* bg-white */
        box-shadow: 0 2px 4px rgba(0,0,0,0.1); /* shadow */
        z-index: 1000;
        padding: 1rem 2rem;
    }
    .header a {
        color: #374151; /* text-gray-700 */
        font-weight: 600;
        margin-left: 1.5rem;
        text-decoration: none;
    }
    .header a:hover {
        color: #D97706; /* hover:text-yellow-600 */
    }
    .logo {
        color: #D97706; /* text-yellow-600 */
        font-size: 1.5rem;
        font-weight: bold;
    }
    /* Section styling */
    .section {
        padding: 4rem 2rem;
    }
    .hero {
        background: linear-gradient(to bottom right, #F59E0B, #D97706, #F97316); /* from-amber-400 to-orange-500 */
        color: white;
        text-align: center;
        padding: 4rem 2rem;
        margin-top: 60px; /* Offset for fixed header */
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        min-height: 50vh;
    }
    .hero-content {
        max-width: 600px;
        margin: 0 auto;
    }
    .hero h1 {
        font-size: 3rem;
        font-weight: 600;
        margin-bottom: 1.5rem;
    }
    .hero h2 {
        font-size: 1.5rem;
        font-weight: 400;
        margin-bottom: 1rem;
    }
    .hero p {
        font-size: 1.125rem;
        margin-bottom: 2rem;
    }
    .hero button {
        background-color: #ffffff; /* bg-white */
        color: #D97706; /* text-yellow-700 */
        font-weight: 600;
        padding: 0.75rem 1.5rem;
        border-radius: 1.5rem;
        border: none;
        cursor: pointer;
        transition: background-color 0.3s;
    }
    .hero button:hover {
        background-color: #FEF3C7; /* hover:bg-yellow-100 */
    }
    .footer {
        background-color: #D97706; /* bg-yellow-600 */
        color: #FEF3C7; /* text-yellow-100 */
        padding: 1.5rem;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

def render_header():
    """Render the sticky header for all pages."""
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
    """Render the footer for all pages."""
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

# Hero Section
st.markdown("""
    <div class="hero" id="hero">
        <div class="hero-content">
            <h1>Welcome to Sifiso AI</h1>
            <h2>Desire to Learn, Power to Build</h2>
            <p>Learn AI and digital skills in your language: From Mdantsane to eThekwini & from eThekwini to Soweto. Unlock your potential with community-powered AI tutoring and startup tools.</p>
            <button id="get-started-btn">Get Started</button>
        </div>
    </div>
""", unsafe_allow_html=True)

# Handle Get Started button click
if st.session_state.get("get_started_clicked", False):
    st.switch_page("./pages/get_started.py")

# JavaScript to set session state on button click
st.markdown("""
    <script>
    document.getElementById("get-started-btn").addEventListener("click", function() {
        fetch("/?get_started_clicked=true", {method: "POST"}).then(() => {
            window.location.href = "/get_started";
        });
    });
    </script>
""", unsafe_allow_html=True)

# Render footer
render_footer()