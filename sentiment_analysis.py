import joblib
import re
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from textblob import TextBlob # Fallback option

# --- Global variables for the loaded model and vectorizer ---
sentiment_model = None
tfidf_vectorizer = None

# --- Paths to your saved model files ---
MODEL_PATH = 'sentiment_model.pkl'
VECTORIZER_PATH = 'tfidf_vectorizer.pkl'

def preprocess_text(text):
    """Basic text preprocessing: lowercasing, removing punctuation, stop words."""
    if not isinstance(text, str):
        return ""
    text = text.lower()
    text = re.sub(f'[{re.escape(string.punctuation)}]', '', text)
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word not in stop_words]
    return " ".join(filtered_tokens)

def load_sentiment_model():
    """
    Loads the pre-trained sentiment model and TF-IDF vectorizer.
    """
    global sentiment_model, tfidf_vectorizer
    try:
        sentiment_model = joblib.load(MODEL_PATH)
        tfidf_vectorizer = joblib.load(VECTORIZER_PATH)
        print("Machine Learning sentiment model and vectorizer loaded successfully.")
        return True
    except FileNotFoundError:
        print(f"Warning: Model files '{MODEL_PATH}' or '{VECTORIZER_PATH}' not found.")
        print("Please ensure you have run the Jupyter Notebook (notebooks/Sentiment_Model_Training.ipynb) to train and save the model.")
        print("Falling back to TextBlob for sentiment analysis.")
        return False
    except Exception as e:
        print(f"Error loading sentiment model: {e}")
        print("Falling back to TextBlob for sentiment analysis.")
        return False

# --- Attempt to load the model on module import ---
if not load_sentiment_model():
    print("Consider running 'python -m nltk.downloader punkt stopwords' if TextBlob errors persist.")

def analyze_sentiment_ml(text):
    """
    Analyzes sentiment using the loaded ML model.
    Returns 'negative', 'neutral', or 'positive'.
    """
    if sentiment_model is None or tfidf_vectorizer is None:
        return analyze_sentiment_textblob(text) # Fallback if ML model isn't loaded

    cleaned_text = preprocess_text(text)
    # Ensure the input to transform is a list containing the cleaned text
    text_vec = tfidf_vectorizer.transform([cleaned_text])
    prediction = sentiment_model.predict(text_vec)[0]
    return prediction

def analyze_sentiment_textblob(text):
    """
    Analyzes the sentiment of the given text using TextBlob (fallback).
    Returns 'negative', 'neutral', 'positive' based on polarity.
    """
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity <= -0.05: # Common threshold for negative
        return 'negative'
    elif polarity >= 0.05: # Common threshold for positive
        return 'positive'
    else: # Neutral
        return 'neutral'

def analyze_sentiment(text):
    """
    Main function to determine sentiment. Tries ML model first, falls back to TextBlob if not available.
    Returns a dictionary with 'category' (string) and 'compound' (float for logic thresholds).
    """
    sentiment_category = analyze_sentiment_ml(text)

    # Map categories to a compound-like score for main.py's existing logic.
    # These values are arbitrary placeholders to allow the main.py's thresholds to work.
    compound_score = 0
    if sentiment_category == 'negative':
        # Assign a negative value that's within the range main.py expects for 'negative' sentiment
        compound_score = -0.5
    elif sentiment_category == 'positive':
        # Assign a positive value that's within the range main.py expects for 'positive' sentiment
        compound_score = 0.5
    # If neutral, compound_score remains 0

    return {
        'category': sentiment_category,
        'compound': compound_score
    }

if __name__ == "__main__":
    print("--- Testing Sentiment Analysis (ML Model or TextBlob Fallback) ---")
    test_phrases = [
        "I feel terrible today, nothing is going right.",
        "I'm so happy and excited for the weekend!",
        "Just doing my homework.",
        "I want to end my life.", # Should be caught by crisis keywords in main.py, but sentiment should also be strong negative
        "This is confusing but interesting.",
        "My friends always make me feel good."
    ]
    for phrase in test_phrases:
        result = analyze_sentiment(phrase)
        print(f"Phrase: '{phrase}' -> Category: {result['category']}, Compound (for logic): {result['compound']}")