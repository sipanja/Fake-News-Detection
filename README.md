# 📰 Fake News Detection Using Machine Learning

A Flask-based Fake News Detection web application that combines **Linear SVM**, **TF-IDF**, **Google News RSS**, and **Sentence Transformers** to classify news articles as **Real** or **Fake**.
# 📰 Fake News Detection System

<p align="center">

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Backend-000000?style=for-the-badge&logo=flask&logoColor=white)
![Machine Learning](https://img.shields.io/badge/Machine-Learning-orange?style=for-the-badge)
![Linear SVM](https://img.shields.io/badge/Linear-SVM-blue?style=for-the-badge)
![TF-IDF](https://img.shields.io/badge/TF--IDF-Vectorizer-success?style=for-the-badge)
![Google News RSS](https://img.shields.io/badge/Google_News-RSS-red?style=for-the-badge&logo=google)
![Sentence Transformers](https://img.shields.io/badge/Sentence-Transformers-purple?style=for-the-badge)
![HTML5](https://img.shields.io/badge/HTML5-Frontend-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![MIT License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)

</p>
<p align="center">

![GitHub stars](https://img.shields.io/github/stars/sipanja/Fake-News-Detection?style=for-the-badge)
![GitHub forks](https://img.shields.io/github/forks/sipanja/Fake-News-Detection?style=for-the-badge)
![GitHub issues](https://img.shields.io/github/issues/sipanja/Fake-News-Detection?style=for-the-badge)
![GitHub last commit](https://img.shields.io/github/last-commit/sipanja/Fake-News-Detection?style=for-the-badge)

</p>
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
