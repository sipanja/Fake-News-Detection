from flask import Flask, render_template, request
import pickle
import re
import feedparser
from urllib.parse import quote_plus

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# Load model and vectorizer
model = pickle.load(open("svm_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# Load semantic model
encoder = SentenceTransformer("all-MiniLM-L6-v2")


# Text cleaning
def clean_text(text):
    text = text.lower()
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    return text


# Fake News Verification
def verify_news(news):

    # ML prediction
    news_vector = vectorizer.transform([clean_text(news)])
    prediction = model.predict(news_vector)[0]

    # Search Google News
    headline = news.split(".")[0]

    query = quote_plus(headline)

    url = f"https://news.google.com/rss/search?q={query}"

    feed = feedparser.parse(url)

    # No sources found
    if len(feed.entries) == 0:
        if prediction == 1:
            return "✅ REAL NEWS"
        else:
            return "❌ FAKE NEWS"

    # Top 5 titles
    titles = [article.title for article in feed.entries[:5]]

    # Semantic similarity
    input_embedding = encoder.encode([headline])

    title_embeddings = encoder.encode(titles)

    similarities = cosine_similarity(
        input_embedding,
        title_embeddings
    )[0]

    avg_similarity = similarities.mean()
    max_similarity = similarities.max()

    # Final decision
    if max_similarity >= 0.90:
        return "✅ REAL NEWS"

    elif avg_similarity >= 0.80:
        return "✅ REAL NEWS"

    elif prediction == 1 and avg_similarity >= 0.60:
        return "✅ REAL NEWS"

    else:
        return "❌ FAKE NEWS"


# Home page
@app.route("/")
def home():
    return render_template("index.html")


# Prediction
@app.route("/predict", methods=["POST"])
def predict():

    news = request.form["news"]

    # Statistics
    word_count = len(news.split())
    char_count = len(news)
    sentence_count = len(re.split(r'[.!?]+', news)) - 1

    # ML Prediction
    news_vector = vectorizer.transform([clean_text(news)])
    prediction = model.predict(news_vector)[0]

    ml_prediction = "REAL NEWS" if prediction == 1 else "FAKE NEWS"

    # Google News Search
    headline = news.split(".")[0]

    query = quote_plus(headline)

    url = f"https://news.google.com/rss/search?q={query}"

    feed = feedparser.parse(url)

    sources_found = len(feed.entries)

    related_articles = []

    for article in feed.entries[:5]:

        related_articles.append({
            "title": article.title,
            "link": article.link
        })

    confidence = 0

    if sources_found > 0:

        titles = [article.title for article in feed.entries[:5]]

        input_embedding = encoder.encode([headline])

        title_embeddings = encoder.encode(titles)

        similarities = cosine_similarity(
            input_embedding,
            title_embeddings
        )[0]

        confidence = round(float(max(similarities)) * 100, 2)

    # Final Verdict

    if confidence >= 90:

        final_prediction = "✅ REAL NEWS"

        analysis = "Multiple highly similar articles found."

    elif prediction == 1:

        final_prediction = "✅ REAL NEWS"

        analysis = "ML model predicts article as genuine."

    else:

        final_prediction = "❌ FAKE NEWS"

        analysis = "No reliable supporting sources found."

    return render_template(
        "index.html",
        prediction=final_prediction,
        confidence=confidence,
        ml_prediction=ml_prediction,
        sources_found=sources_found,
        word_count=word_count,
        char_count=char_count,
        sentence_count=sentence_count,
        analysis=analysis,
        related_articles=related_articles
    )


if __name__ == "__main__":
    app.run(debug=True)
