# 📰 Fake News Detection Using Machine Learning

A Flask-based Fake News Detection web application that combines **Linear SVM**, **TF-IDF**, **Google News RSS**, and **Sentence Transformers** to classify news articles as **Real** or **Fake**.

## Features

* Machine Learning-based fake news detection
* Linear SVM classifier
* TF-IDF text vectorization
* Google News RSS source verification
* Semantic similarity using Sentence Transformers
* Confidence score
* Article statistics
* Related news articles
* Modern Flask web interface

## Technologies Used

* Python
* Flask
* Scikit-learn
* Pandas
* Sentence Transformers
* Feedparser
* HTML
* CSS
* JavaScript

## Project Structure

```text
fake-news-detection/
│── app.py
│── requirements.txt
│── README.md
│── templates/
│── static/
│── svm_model.pkl
│── vectorizer.pkl
```

## Installation

```bash
git clone https://github.com/sipanja/fake-news-detection.git

cd fake-news-detection

python -m venv venv

source venv/bin/activate
# Windows
venv\Scripts\activate

pip install -r requirements.txt
```

## Run

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

## Workflow

1. User enters a news article.
2. Text is preprocessed.
3. TF-IDF converts text into numerical features.
4. Linear SVM predicts Real/Fake.
5. Google News RSS searches for related articles.
6. Sentence Transformer measures semantic similarity.
7. Final verdict is displayed.

## Future Improvements

* BERT-based classifier
* NewsAPI integration
* PDF report generation
* User authentication
* Dashboard analytics

## License

MIT License
