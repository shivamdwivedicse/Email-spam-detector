import streamlit as st
import pickle
import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# download (safe for first run)
nltk.download('punkt')
nltk.download('stopwords')

stop_words = set(stopwords.words("english"))

# load model and vectorizer
model = pickle.load(open("model_1.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# ---------- PREPROCESSING (EXACT SAME AS YOUR NOTEBOOK) ----------

def clean_text(text):
    # lowercase
    text = text.lower()
    
    # remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    # remove numbers
    text = ''.join([i for i in text if not i.isdigit()])
    
    # remove urls
    text = re.sub(r'https?://\S+|www\.\S+', '', text)
    
    # remove emojis
    text = re.sub(r'[^\x00-\x7F]+', '', text)
    
    # remove special chars
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    
    # tokenize + remove stopwords
    words = word_tokenize(text)
    words = [w for w in words if w not in stop_words]
    
    return " ".join(words)

# ---------- UI ----------

st.set_page_config(page_title="Spam Detector", page_icon="📧")

st.title("📧 Email Spam Detector")
st.write("Enter your message below 👇")

user_input = st.text_area("Message")

if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("Please enter a message")
    else:
        cleaned = clean_text(user_input)
        vector = vectorizer.transform([cleaned])
        prediction = model.predict(vector)[0]

        if prediction == 1:
            st.error("🚨 Spam Mail")
        else:
            st.success("✅ Not spam Mail")