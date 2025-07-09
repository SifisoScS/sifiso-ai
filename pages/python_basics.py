import streamlit as st

# Set page config
st.set_page_config(
    page_title="Python Basics | Sifiso AI",
    page_icon="🇿🇦",
    layout="wide"
)

# CSS styling
st.markdown("""
    <style>
    .module-header {
        color: #007749;
        border-bottom: 2px solid #FFCD00;
        padding-bottom: 0.3rem;
        margin-top: 1.5rem;
    }
    .local-example {
        background: #F0FDF4;
        border-left: 4px solid #007749;
        padding: 1rem;
        margin: 1rem 0;
        border-radius: 0 8px 8px 0;
    }
    .concept-list {
        margin-bottom: 1.5rem;
    }
    </style>
""", unsafe_allow_html=True)

# Main header
st.markdown("""
    <h1 style='color:#007749; border-bottom: 3px solid #FFCD00; padding-bottom: 0.5rem;'>
        Python for South African Problem Solvers
    </h1>
    <p style='font-size:1.1rem;'>
        Learn coding fundamentals using examples from township businesses and local challenges
    </p>
""", unsafe_allow_html=True)

# --- Module 1 ---
st.markdown('<h2 class="module-header">📌 Module 1: Python Essentials</h2>', unsafe_allow_html=True)

st.markdown("""
    <div class="concept-list">
        <h4>Localized Learning:</h4>
        <ul>
            <li><strong>Variables</strong> → Tracking spaza shop inventory</li>
            <li><strong>Loops</strong> → Analyzing taxi route data</li>
            <li><strong>Functions</strong> → Calculating township energy usage</li>
        </ul>
    </div>
""", unsafe_allow_html=True)

# --- Module 2 ---
st.markdown('<h2 class="module-header">📊 Module 2: Data Handling</h2>', unsafe_allow_html=True)

st.markdown("""
    <div class="concept-list">
        <h4>Local Datasets:</h4>
        <ul>
            <li>Working with SA census data</li>
            <li>Analyzing township electricity usage</li>
            <li>Processing agricultural yield records</li>
        </ul>
    </div>
    
    <div class='local-example'>
        <h4>🛒 Township Business Case</h4>
        <p>Analyze weekly sales from a spaza shop CSV:</p>
        ```python
        import pandas as pd
        sales = pd.read_csv('spaza_sales.csv')
        top_products = sales.sort_values('units', ascending=False)
        ```
    </div>
""", unsafe_allow_html=True)

# --- Module 3 ---
st.markdown('<h2 class="module-header">🤖 Module 3: AI Preparation</h2>', unsafe_allow_html=True)

st.markdown("""
    <div class="concept-list">
        <h4>Local AI Foundations:</h4>
        <ul>
            <li>Cleaning municipal service data</li>
            <li>Preparing agricultural images for ML</li>
            <li>Structuring township business records</li>
        </ul>
    </div>
    
    <div class='local-example'>
        <h4>🌾 Farming Application</h4>
        <p>Prepare crop data for disease detection:</p>
        ```python
        # Sample maize disease images
        from PIL import Image
        img = Image.open('maize_leaf.jpg')
        ```
    </div>
""", unsafe_allow_html=True)

# Practical exercise
st.markdown("""
<div style='background:#FFFBEB; padding:1.5rem; border-radius:8px; margin-top:2rem;'>
    <h3 style='color:#007749;'>🏘️ Township Mini-Project</h3>
    <p>Create a stock management system for a spaza shop:</p>
    <ol>
        <li>Track incoming/outgoing products</li>
        <li>Calculate daily profits</li>
        <li>Identify fast-moving goods</li>
    </ol>
</div>
""", unsafe_allow_html=True)