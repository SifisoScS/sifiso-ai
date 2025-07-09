import streamlit as st
import os
from streamlit import runtime

# Set page config - MUST be first command
st.set_page_config(
    page_title="Sifiso AI | Learn AI in Your Language",
    layout="wide",
    initial_sidebar_state="collapsed"  # Completely removes the sidebar
)

# Custom CSS with color-themed buttons
st.markdown("""
    <style>
    /* Completely remove the sidebar */
    section[data-testid="stSidebar"] {
        display: none !important;
    }
    
    /* Adjust main content area */
    .main .block-container {
        padding-top: 5rem;
        max-width: 100% !important;
        padding-left: 2rem;
        padding-right: 2rem;
    }
    
    /* SA-inspired color variables */
    :root {
        --sa-yellow: #FFCD00;
        --sa-green: #007749;
        --sa-red: #DE3831;
        --sa-blue: #002395;
        --sa-black: #000000;
        --sa-white: #FFFFFF;
    }
    
    /* Sticky header with SA flag colors */
    .header {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        background: linear-gradient(90deg, 
            var(--sa-black) 0%, 
            var(--sa-yellow) 33%, 
            var(--sa-green) 66%, 
            var(--sa-red) 100%);
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        z-index: 1000;
        padding: 1rem 2rem;
        display: flex;
        align-items: center;
    }
    
    /* Navigation buttons - each with different SA colors */
    div.stButton > button:first-child {
        border-radius: 0.5rem !important;
        font-weight: 600 !important;
        padding: 0.5rem 1rem !important;
        transition: all 0.3s !important;
        margin: 0 0.25rem !important;
    }
    
    /* Home button - black theme */
    div.stButton > button:first-child[kind="secondary"]:nth-child(1) {
        background-color: var(--sa-black) !important;
        color: var(--sa-white) !important;
        border: 1px solid var(--sa-white) !important;
    }
    
    /* Get Started button - yellow theme */
    div.stButton > button:first-child[kind="primary"] {
        background-color: var(--sa-yellow) !important;
        color: var(--sa-black) !important;
        border: none !important;
        border-radius: 1.5rem !important;
        padding: 0.75rem 1.5rem !important;
    }
    
    /* Learn button - green theme */
    div.stButton > button:first-child[kind="secondary"]:nth-child(3) {
        background-color: var(--sa-green) !important;
        color: var(--sa-white) !important;
        border: 1px solid var(--sa-green) !important;
    }
    
    /* Community button - red theme */
    div.stButton > button:first-child[kind="secondary"]:nth-child(4) {
        background-color: var(--sa-red) !important;
        color: var(--sa-white) !important;
        border: 1px solid var(--sa-red) !important;
    }
    
    /* About button - blue theme */
    div.stButton > button:first-child[kind="secondary"]:nth-child(5) {
        background-color: var(--sa-blue) !important;
        color: var(--sa-white) !important;
        border: 1px solid var(--sa-blue) !important;
    }
    
    /* Contact button - white theme */
    div.stButton > button:first-child[kind="secondary"]:nth-child(6) {
        background-color: var(--sa-white) !important;
        color: var(--sa-black) !important;
        border: 1px solid var(--sa-white) !important;
    }
    
    /* Hover effects for all buttons */
    div.stButton > button:first-child:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        opacity: 0.9;
    }
    
    /* Logo styling */
    .logo {
        color: var(--sa-yellow);
        font-size: 1.5rem;
        font-weight: bold;
        margin-right: 2rem;
    }
    
    /* Hero section */
    .hero {
        background: linear-gradient(to bottom right, #F59E0B, #D97706, #F97316);
        color: white;
        text-align: center;
        padding: 6rem 2rem;
        margin-top: 0;
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
    
    /* Footer with SA colors */
    .footer {
        background: linear-gradient(135deg, 
            var(--sa-black) 0%, 
            var(--sa-yellow) 25%, 
            var(--sa-green) 50%, 
            var(--sa-red) 75%, 
            var(--sa-blue) 100%);
        color: var(--sa-white);
        padding: 1.5rem;
        text-align: center;
        margin-top: 2rem;
    }
    
    /* Mobile responsiveness */
    @media (max-width: 768px) {
        .header {
            padding: 0.8rem 1rem;
        }
        div.stButton > button:first-child {
            padding: 0.4rem 0.8rem !important;
            font-size: 0.8rem !important;
            margin: 0 0.1rem !important;
        }
        .hero {
            padding: 4rem 1rem;
            min-height: 40vh;
        }
        .hero h1 {
            font-size: 2.2rem;
        }
    }
    </style>
""", unsafe_allow_html=True)

def render_header():
    """Render the sticky header with color-themed navigation buttons."""
    st.markdown("""
        <div class="header">
            <span class="logo">Sifiso AI</span>
        </div>
    """, unsafe_allow_html=True)
    
    # Navigation buttons with color themes
    cols = st.columns([1,1,1,1,1,1])
    nav_items = [
        ("Home", "Home", "secondary"),
        ("Get Started", "get_started", "primary"),  # Special yellow button
        ("Learn", "Learn", "secondary"),
        ("Community", "Community", "secondary"),
        ("Tools", "Tools", "secondary"),
        ("Contact", "Contact", "secondary")
    ]
    
    for i, (name, page, btn_type) in enumerate(nav_items):
        with cols[i]:
            if st.button(name, key=f"nav_{name.lower()}", type=btn_type):
                if page == "Home":
                    st.switch_page("app.py")
                else:
                    st.switch_page(f"pages/{page.lower()}.py")

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
    <div class="hero">
        <div class="hero-content">
            <h1>Welcome to Sifiso AI</h1>
            <h2>Desire to Learn, Power to Build</h2>
            <p>Learn AI and digital skills in your language: From Mdantsane to eThekwini & from eThekwini to Soweto. Unlock your potential with community-powered AI tutoring and startup tools.</p>
        </div>
    </div>
""", unsafe_allow_html=True)

# Render footer
render_footer()