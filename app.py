# File: app.py
# Run with: streamlit run app.py

import streamlit as st
import os
import base64
from main import process_pdf, generate_answer

# Function to add full-screen background and set all text to white
def add_custom_styles(image_path):
    with open(image_path, "rb") as img_file:
        encoded_string = base64.b64encode(img_file.read()).decode()
    css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{encoded_string}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
        color: white;
    }}
    html, body, [class*="css"] {{
        color: white;
    }}
    .stTextInput label,
    .stFileUploader label {{
        color: white !important;
    }}
    div[data-testid="stSuccess"] {{
        background-color: #28a745 !important;
        color: white !important;
        border-radius: 6px;
        font-weight: bold;
    }}
    div[data-testid="stSuccess"] * {{
        color: white !important;
    }}
    .stTextInput > div > div > input,
    .stFileUploader > div {{
        color: black !important;
        background-color: white !important;
        border-radius: 5px;
        padding: 5px;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)


# Add custom styles
add_custom_styles("bg.jpg")  # Update path if needed

# Title and subtitle
st.markdown(
    "<h1 style='color: white; font-weight: bold;'>📄 RAG-based Research Q&A System</h1>",
    unsafe_allow_html=True
)
st.markdown(
    "<p style='color: white;'>Upload a research paper (PDF) and ask questions about it using RAG + Ollama</p>",
    unsafe_allow_html=True
)

# File uploader
uploaded_file = st.file_uploader("Upload PDF", type="pdf")

# Display success and input question
if uploaded_file:
    file_path = os.path.join("temp_docs", uploaded_file.name)
    os.makedirs("temp_docs", exist_ok=True)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("PDF uploaded and processed successfully!")

    # Question input
    question = st.text_input("Ask a question about the paper")

    vectordb = process_pdf(file_path)

    if question:
        with st.spinner("Generating answer..."):
            answer = generate_answer(vectordb, question)
        
        st.markdown("<p style='color: white;'>### 📌 Answer:</p>",
        unsafe_allow_html=True)
        st.write(answer)
else:
    st.info("Please upload a research paper to get started.")
