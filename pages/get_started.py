import streamlit as st
import os

# Set page config with SA flag icon
st.set_page_config(
    page_title="Sifiso AI - Start Your Journey",
    page_icon="🇿🇦",
    layout="wide"
)

# Custom CSS with SA design elements
st.markdown("""
    <style>
    :root {
        --sa-yellow: #FFCD00;
        --sa-green: #007749;
        --sa-red: #DE3831;
        --sa-blue: #002395;
        --sa-black: #000000;
    }
    
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@700&family=Poppins:wght@400;600&display=swap');
    
    .main-title {
        font-family: 'Montserrat', sans-serif;
        color: var(--sa-green);
        text-align: center;
        margin-bottom: 2rem;
        font-size: 2.5rem;
    }
    
    .pathway-card {
        border-radius: 15px;
        padding: 1.5rem;
        height: 100%;
        transition: transform 0.3s;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        border: 1px solid #eee;
    }
    
    .pathway-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 6px 12px rgba(0,0,0,0.15);
    }
    
    .card-title {
        color: var(--sa-blue);
        font-weight: 700;
        margin: 1rem 0 0.5rem;
    }
    
    .card-button {
        background: var(--sa-green) !important;
        color: white !important;
        border: none !important;
    }
    
    .card-button:hover {
        background: var(--sa-yellow) !important;
        color: var(--sa-black) !important;
    }
    </style>
""", unsafe_allow_html=True)

# Main content
st.markdown('<h1 class="main-title">Kickstart Your AI Journey</h1>', unsafe_allow_html=True)
st.markdown("""
    <p style='text-align:center; font-size:1.1rem; margin-bottom:3rem;'>
    Choose your pathway to AI mastery, tailored for South African builders
    </p>
""", unsafe_allow_html=True)

# Pathway cards
cols = st.columns(3)
pathways = [
    {
        "title": "Learn AI",
        "icon": "📚",
        "desc": "Courses in your language from township classrooms to online",
        "image": "learn_path.jpg",
        "action": "Start Learning",
        "target": "learn.py"
    },
    {
        "title": "Join Community",
        "icon": "👥",
        "desc": "Connect with mentors and peers in your area",
        "image": "community_path.jpg",
        "action": "Find Your Tribe",
        "target": "community.py"
    },
    {
        "title": "Build Solutions",
        "icon": "🛠️",
        "desc": "Tools for SA-specific AI projects",
        "image": "tools_path.jpg",
        "action": "Start Building",
        "target": "tools.py"
    }
]

for i, pathway in enumerate(pathways):
    with cols[i]:
        # Card container
        st.markdown(f"""
            <div class="pathway-card">
                <div style="text-align:center;">
                    <img src="{os.path.join('images', pathway['image'])}" 
                         style="width:100%; border-radius:10px; height:180px; object-fit:cover;">
                    <h3 class="card-title">{pathway['icon']} {pathway['title']}</h3>
                    <p>{pathway['desc']}</p>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        # Centered button
        st.markdown("""
            <div style="display:flex; justify-content:center; margin-top:1rem;">
        """, unsafe_allow_html=True)
        
        if st.button(pathway['action'], key=f"btn_{i}"):
            # Revert to using full relative path for st.switch_page
            st.switch_page(f"pages/{pathway['target']}")
        
        st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("""
    <div style="margin-top:4rem; padding:2rem; background:#007749; color:white; text-align:center; border-radius:8px;">
        <h3>Need help choosing?</h3>
        <p>Our team is ready to guide you on your AI journey</p>
    </div>
""", unsafe_allow_html=True)