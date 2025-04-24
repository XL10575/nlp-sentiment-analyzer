# xxl1323 Xiang Luo

import streamlit as st
from textblob import TextBlob
from nltk.stem.wordnet import WordNetLemmatizer
import re

def clean_and_lemmatize(text):
    # 1) Keep only letters and numbers
    text = re.sub(r"[^A-Za-z0-9]", " ", text)
    # 2) Remove possessives
    text = re.sub(r"\'s", " ", text)
    # 3) Replace links
    text = re.sub(r"http\S+", " link ", text)
    # 4) Remove standalone numbers
    text = re.sub(r"\b\d+(?:\.\d+)?\s+", "", text)
    # 5) Split into words
    words = text.split()
    # 6) Lemmatize each word
    lemmatizer = WordNetLemmatizer()
    lemmas = [lemmatizer.lemmatize(w) for w in words]
    return " ".join(lemmas)

def analyze_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity  # range [-1.0, +1.0]

def sentiment_label(score):
    if score > 0:
        return "Positive", ":blush:"
    elif score < 0:
        return "Negative", ":disappointed:"
    else:
        return "Neutral", ":confused:"

def main():
    st.title("📊 NLP Sentiment Analyzer")
    st.subheader("Enter some text below and click Analyze to get its sentiment")

    user_input = st.text_area("Your text here", height=200)

    if st.button("Analyze"):
        if not user_input.strip():
            st.warning("Please enter some text to analyze.")
            return

        # clean & lemmatize
        cleaned = clean_and_lemmatize(user_input)
        # sentiment
        score = analyze_sentiment(cleaned)
        label, emoji = sentiment_label(score)

        # display
        if label == "Positive":
            st.success(f"{emoji} Positive sentiment detected!")
        elif label == "Negative":
            st.warning(f"{emoji} Negative sentiment detected!")
        else:
            st.info(f"{emoji} Neutral sentiment detected!")

        st.write(f"**Polarity score:** {score:.3f}")

if __name__ == "__main__":
    main()
