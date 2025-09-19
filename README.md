📰 Fake News & Social Engineering Detection Bot

This project is a Streamlit web application that detects Fake News and potential Social Engineering attempts using:

An LSTM deep learning model (model.keras)

OCR (Optical Character Recognition) for extracting text from uploaded news screenshots

Text preprocessing & NLP techniques

Social Engineering pattern detection

It provides real-time predictions with confidence levels and alerts users about possible manipulation attempts.

🚀 Features

📸 Image Upload: Upload screenshots of news articles.

🔎 OCR Integration: Extracts text automatically from images using Tesseract OCR.

✍️ Manual Input: Directly enter or paste news text.

🤖 Fake News Detection: Classifies text as:

🔴 Fake News (Confidence ≥ 70%)

🟠 Possibly Fake News (Confidence ≥ 50%)

🟢 Real News (Confidence < 50%)

🧠 Social Engineering Detection: Flags suspicious linguistic patterns.

🎨 Custom Background Support (background 1.jpg).

📂 Project Structure
.
├── app.py                # Main Streamlit app
├── model.keras           # Trained LSTM model
├── tokenizer.pickle      # Tokenizer for text sequences
├── requirements.txt      # Dependencies
├── background 1.jpg      # App background image
└── utils/                # Utility scripts (OCR, preprocessing, SE detection)

⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/your-username/fake-news-detector.git
cd fake-news-detector

2️⃣ Create Virtual Environment (Optional but Recommended)
python -m venv venv
source venv/bin/activate   # For Linux/Mac
venv\Scripts\activate      # For Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Install & Configure Tesseract OCR

Download from: Tesseract OCR

Update the path in app.py:

pytesseract.pytesseract.tesseract_cmd = r'C:\Path\to\tesseract.exe'

5️⃣ Run the Application
streamlit run app.py

🖼️ Usage

Launch the app in your browser (usually http://localhost:8501/).

Upload a news screenshot or paste news text.

Click "🔍 Detect" to analyze.

View results:

Processed text

Fake/Real classification with confidence

Social engineering pattern detection

📦 Dependencies

From requirements.txt:

streamlit

pytesseract

Pillow

nltk

scikit-learn

joblib

Additionally:

tensorflow / keras (required for LSTM model)

numpy

base64

🧠 Model Details

Architecture: LSTM neural network

Tokenizer: Pretrained and saved as tokenizer.pickle

Max Sequence Length: 100 tokens

Prediction Thresholds:

≥ 0.7 → Fake News

≥ 0.5 → Possibly Fake News

< 0.5 → Real News

✨ Future Improvements

Add support for multi-language OCR.

Improve confidence calibration.

Expand dataset for better generalization.

Deploy app on Streamlit Cloud / Heroku / AWS.

👨‍💻 Author

Developed with ❤️ using Streamlit, LSTM, and OCR.
