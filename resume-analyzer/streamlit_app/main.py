import streamlit as st
import requests
from PIL import Image
import base64

# Page Configuration
st.set_page_config(page_title="Smart Resume Evaluator", page_icon="📄", layout="centered")

# Custom Styling
st.markdown("""
    <style>
    .stButton button {
        color: white;
        background-color: #4CAF50;
        padding: 8px 20px;
        border-radius: 8px;
        font-weight: bold;
    }
    .stSpinner > div > div {
        color: #4CAF50;
    }
    .stMarkdown h1 {
        font-size: 2.5em;
        color: #2c3e50;
    }
    .markdown-box {
        padding: 16px;
        border-radius: 10px;
        border: 1px solid #ddd;
        white-space: pre-wrap;
        word-wrap: break-word;
        font-size: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("## 📄 Smart Resume Evaluator")
st.markdown("Unlock career growth with instant **AI-powered resume analysis** and personalized **course recommendations**.")

# Divider
st.markdown("---")

# Upload Section
st.markdown("### 📤 Upload Your Resume")
st.markdown("Only **PDF** format is accepted.")
resume_file = st.file_uploader("", type=["pdf"])

# Evaluation Process
if resume_file:
    with st.spinner("⏳ Analyzing your resume with Krishna..."):

        files = {"resume": (resume_file.name, resume_file, "application/pdf")}

        try:
            response = requests.post("http://localhost:5000/evaluate", files=files)

            if response.status_code == 200:
                data = response.json()

                st.balloons()
                st.success("✅ Analysis Complete!")

                # Score & Analysis
                st.markdown("### 📊 Resume Score & Feedback")
                st.markdown(f"<div class='markdown-box'>{data['score_and_analysis']}</div>", unsafe_allow_html=True)

                # Course Recommendations
                st.markdown("### 🎯 Personalized Course Suggestions")
                st.markdown(f"<div class='markdown-box'>{data['courses']}</div>", unsafe_allow_html=True)

            else:
                st.error(f"❌ Error {response.status_code}: Could not process resume.")
        except requests.exceptions.RequestException as e:
            st.error(f"❌ Request failed: {e}")
else:
    st.warning("📎 Upload your resume to receive instant feedback.")

# Footer
st.markdown("---")
st.markdown(
    "<center>🚀 Powered by <strong>Kara AI</strong> | Built with ❤️ Krishna using Python + Streamlit</center>",
    unsafe_allow_html=True
)
