import streamlit as st
from PIL import Image
from utils.ocr import extract_text_from_image
from utils.text_preprocessing import clean_text
import joblib
import pytesseract
import tensorflow as tf
import numpy as np
import pickle
import base64
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.initializers import Orthogonal  # ✅ Fix initializer issue
from utils.se_detector import detect_social_engineering
from utils.preprocess import process_text

# Streamlit page config
st.set_page_config(page_title="Fake News Detector", layout="centered")

# Set path for Tesseract OCR (adjust path if different)
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\ASUS\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

# ✅ Set custom background image (local file)
def set_background(image_path):
    with open(image_path, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
            background-position: center;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Set local background image (must exist in same folder)
set_background("background 1.jpg")

# ✅ Load LSTM model safely
@st.cache_resource
def load_model():
    return tf.keras.models.load_model(
        "model.keras",
        custom_objects={"Orthogonal": Orthogonal},  # Fix initializer
        safe_mode=False                             # Allow flexible deserialization
    )

# Load tokenizer
@st.cache_resource
def load_tokenizer():
    with open("tokenizer.pickle", "rb") as handle:
        return pickle.load(handle)

# Constants
model = load_model()
tokenizer = load_tokenizer()
max_len = 100

# Title
st.title("📰 Fake News & Social Engineering Detection Bot")

# Upload Image
uploaded_image = st.file_uploader("📸 Upload News Screenshot (Optional)", type=["jpg", "jpeg", "png"])

# Text input
st.markdown("### ✍️ Or Enter News Content Below:")
input_text = st.text_area("Paste the news text here:", height=200)

# OCR or text input
text = None
if uploaded_image:
    st.image(uploaded_image, caption="Uploaded Screenshot", use_container_width=True)
    with st.spinner("🔎 Extracting text from image..."):
        text = extract_text_from_image(Image.open(uploaded_image))
elif input_text.strip():
    text = input_text.strip()

# Preprocess for model
def preprocess_text(text):
    sequences = tokenizer.texts_to_sequences([text])
    return pad_sequences(sequences, maxlen=max_len)

# Prediction workflow
if text:
    clear_text = process_text(text)
    matched_patterns = detect_social_engineering(clear_text)

    if st.button("🔍 Detect"):
        st.subheader("📝 Processed Text:")
        st.write(clear_text)

        if len(clear_text.split()) < 5:
            st.warning("⚠️ Text is too short or unclear for accurate prediction.")
        else:
            processed = preprocess_text(clear_text)
            prediction = model.predict(processed)[0][0]

            # Display prediction with confidence
            st.subheader("📊 Prediction Result:")

            if prediction >= 0.7:
                st.error(f"🔴 Fake News Detected (Confidence: {prediction:.2f})")
            elif prediction >= 0.5:
                st.warning(f"🟠 Possibly Fake News (Confidence: {prediction:.2f})")
            else:
                st.success(f"🟢 Real News (Confidence: {1 - prediction:.2f})")

            # Social Engineering Detection
            if matched_patterns:
                st.subheader("🧠 Social Engineering Detected:")
                for reason in matched_patterns:
                    st.warning(f"⚠️ {reason}")
            else:
                st.info("✅ No social engineering patterns detected.")
else:
    st.info("📎 Please upload an image or enter news text to start detection.")

# Footer
st.markdown("---")
st.caption("Built with ❤️ using LSTM, Streamlit, and OCR")
