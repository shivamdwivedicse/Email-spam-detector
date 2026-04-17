# 📧 Email Spam Detector

A Machine Learning project that classifies emails/SMS messages as **Spam** or **Ham (Not Spam)** using NLP techniques and Naive Bayes classification — achieving **98.02% accuracy**.

---

## 🚀 Live Demo
> 🔗 Live Demo — *Coming Soon (Deploying on Streamlit Cloud)*
---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Core language |
| Pandas & NumPy | Data manipulation |
| NLTK | NLP preprocessing |
| Scikit-learn | ML models & vectorization |
| Matplotlib & Seaborn | Visualization |
| Streamlit | Web UI |
| Pickle | Model saving |

---

## 🔧 NLP Preprocessing Pipeline

1. ✅ Lowercasing
2. ✅ Punctuation removal
3. ✅ Number removal
4. ✅ URL removal
5. ✅ Emoji removal
6. ✅ Special character removal
7. ✅ Stopword removal (NLTK)
8. ✅ Tokenization

---

## 🤖 Models Trained

| Model | Vectorizer | Accuracy |
|-------|-----------|----------|
| **Multinomial Naive Bayes** | **Bag of Words** | **98.02% 🏆** |
| Multinomial Naive Bayes | TF-IDF | 96.86% |
| Logistic Regression | Bag of Words | 97.66% |
| Logistic Regression | TF-IDF | 95.06% |

---

## 📈 Best Model — Classification Report
precision    recall  f1-score   support

 Ham (0)       0.98      0.99      0.99       965
Spam (1)       0.96      0.89      0.92       150

accuracy                           0.98      1115
macro avg       0.97      0.94      0.96      1115
weighted avg       0.98      0.98      0.98      1115
---

## 📁 Project Structure
email-spam-detector/
│
├── app.py                  # Streamlit UI
├── spam.ipynb     # Main notebook
├── mail.csv                # Dataset
├── model_1.pkl             # Saved Naive Bayes model
├── vectorizer.pkl          # Saved CountVectorizer
└── README.md
---

## ▶️ How to Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/yourusername/email-spam-detector.git

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the Streamlit app
streamlit run app.py
