import streamlit as st

# Set page config
st.set_page_config(
    page_title="AI Fundamentals | Sifiso AI",
    page_icon="🇿🇦",
    layout="wide"
)

# CSS for consistent styling
st.markdown("""
    <style>
    .case-study {
        background: #EFF6FF;
        border-radius: 8px;
        padding: 1rem;
        margin: 1rem 0;
    }
    .vernacular {
        color: #007749;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# Language selection
lang = st.radio("Select language:", 
               ["English", "isiZulu", "Afrikaans"],
               horizontal=True,
               label_visibility="collapsed")

# Content based on language selection
if lang == "isiZulu":
    st.title("I-AI Eyisisekelo Yamalunga Omphakathi")
    st.markdown("*Ukuqonda ubuhlakani bokwenziwa ngokomfanekiso ngezibonelo zaseNingizimu Afrika*")
    
    concepts = {
        "heading": "Indlela I-AI Esebenza Ngayo",
        "points": [
            "Ukufunda okusekelwe kudatha",
            "Amamodeli wokubikezela",
            "Ukuhlukanisa izithombe zezitshalo"
        ],
        "example": {
            "heading": "Isibonelo: Ukubona izifo zezitshalo",
            "text": "I-AI isebenzisa izithombe zamaqabunga ukukhomba izifo"
        }
    }
elif lang == "Afrikaans":
    st.title("AI Grondbeginsels vir Suid-Afrikaanse Gemeenskappe")
    st.markdown("**Begrip van kunsmatige intelligensie deur plaaslike voorbeelde*")
    
    concepts = {
        "heading": "Hoe AI Werk",
        "points": [
            "Data-aangedrewe leer",
            "Voorspellingsmodelle",
            "Plant siekte herkenning"
        ],
        "example": {
            "heading": "Voorbeeld: Gewas Siekte Identifikasie",
            "text": "AI gebruik blaar foto's om siektes te identifiseer"
        }
    }
else:  # English default
    st.title("AI Fundamentals for South African Communities")
    st.markdown("*Understanding artificial intelligence through local examples*")
    
    concepts = {
        "heading": "How AI Works",
        "points": [
            "Data-driven learning",
            "Prediction models",
            "Crop disease detection"
        ],
        "example": {
            "heading": "Example: Crop Disease Detection",
            "text": "AI uses leaf images to identify crop diseases"
        }
    }

# Main content tabs
tab1, tab2 = st.tabs(["Concepts", "Local Applications"])

with tab1:
    st.markdown(f"### {concepts['heading']}")
    for point in concepts['points']:
        st.markdown(f"- {point}")
    
    st.markdown(f"""
    <div class='case-study'>
        <h4>{concepts['example']['heading']}</h4>
        <p>{concepts['example']['text']}</p>
    </div>
    """, unsafe_allow_html=True)

with tab2:
    st.markdown("### South African Use Cases")
    
    st.markdown("""
    <div class='case-study'>
        <h4>🛒 Spaza Shop Optimization</h4>
        <p>Predicting which products will sell fast in different townships</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='case-study'>
        <h4>🚌 Public Transport Routing</h4>
        <p>Optimizing minibus taxi routes using traffic patterns</p>
    </div>
    """, unsafe_allow_html=True)

# Progress tracker (consistent across languages)
st.progress(0.3, text=f"{'Inkqubela yenkqubo' if lang == 'isiZulu' else 'Vordering' if lang == 'Afrikaans' else 'Course Progress'}: 30%")