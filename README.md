# 🧠 MannMitra: Mental Well-being Chatbot for Teenagers

MannMitra is a Python-based AI chatbot designed to provide emotional support, coping strategies, and immediate access to crisis resources for teenagers. By leveraging a machine learning-based sentiment analysis model, the chatbot engages in supportive dialogue and adapts responses based on detected emotional tone.

---

## 🚀 Features

- **🎯 Sentiment Analysis Powered by ML**  
  Utilizes a Logistic Regression model trained on the Kaggle dataset [`Sentiment_Analysis_for_Mental_Health.csv`](https://www.kaggle.com/datasets/suchintikasarkar/sentiment-analysis-for-mental-health) to classify user input as `positive`, `negative`, or `neutral`.

- **🧘 Contextual Coping Mechanisms**  
  Suggests evidence-based coping strategies like journaling, grounding techniques, and breathing exercises based on the user's emotional state.

- **📞 Crisis Redirection (India Specific)**  
  Detects signs of acute distress or suicidal ideation and instantly provides access to verified Indian helplines and emergency services.

- **💬 Informative & Supportive Chat**  
  Responds empathetically to general mental health questions and encourages emotional expression. Contains a disclaimer clarifying its supportive—not professional—nature.

- **🧩 Modular Code Design**  
  Clean and scalable structure divided into:
  - `main.py`: Handles interaction loop
  - `sentiment_analysis.py`: Predicts user sentiment
  - `coping_mechanisms.py`: Returns strategies or emergency contact info
  - `config.py`: Stores constants and configuration values

---

## 📁 Project Structure

```

chatbot\_project/
├── data/
│   └── Sentiment\_Analysis\_for\_Mental\_Health.csv
├── Sentiment\_Model\_Training.ipynb 
├── sentiment\_model.pkl
├── tfidf\_vectorizer.pkl
├── main.py
├── sentiment\_analysis.py
├── coping\_mechanisms.py
├── config.py
└── README.md

````

---

## ⚙️ Getting Started

### 1. Download the Dataset

- Visit the [Kaggle Dataset Link](https://www.kaggle.com/datasets/suchintikasarkar/sentiment-analysis-for-mental-health)
- Download `Sentiment_Analysis_for_Mental_Health.csv`
- Place it in the `data/` directory

---

### 2. Install Dependencies

Ensure you have Python 3.7+ installed, then run:

```bash
pip install pandas scikit-learn textblob jupyter notebook nltk
````

Also, download necessary NLTK corpora:

```bash
python -m nltk.downloader punkt
python -m nltk.downloader stopwords
python -m nltk.downloader vader_lexicon
```

---

### 3. Train the Sentiment Model

1. Start Jupyter Notebook:

```bash
jupyter notebook
```

2. Open `notebooks/Sentiment_Model_Training.ipynb`
3. Run all cells to:

   * Preprocess data
   * Train a logistic regression model
   * Save `sentiment_model.pkl` and `tfidf_vectorizer.pkl`

**Note:** Ensure column mapping is correct in preprocessing:

```python
df = df[['statement', 'status']].copy()
LABEL_MAPPING = {
    'depression': 'negative',
    'normal': 'neutral',
    'supportive': 'positive',
    ...
}
```

---

### 4. Run the Chatbot

```bash
python main.py
```

Type your message to chat. Type `exit` to end the session.

---

## ⚠️ Disclaimer

> This chatbot is not a substitute for professional help. It is for supportive and educational purposes only. If you or someone you know is in crisis, please seek help from a qualified mental health professional or contact emergency services.

---

## 📞 Crisis Resources (India)

* **AASRA (24/7, Mumbai):** +91-9820466726
* **Vandrevala Foundation Helpline (National):** +91-9999666555
* **KIRAN Mental Health Helpline (Govt of India):** 1800-599-0019
* **Emergency Numbers:**

  * Police: `112` or `100`
  * Ambulance: `102`

---

## 🌱 Future Enhancements

* Integrate SpaCy or Transformers for better intent recognition
* Add GUI using Tkinter or deploy with Streamlit
* Expand coping strategy library and personalization
* Implement user session memory and user authentication

---

Developed with the intention to support and empower teenagers struggling with mental health. Let's reduce stigma and make help more accessible.

```

