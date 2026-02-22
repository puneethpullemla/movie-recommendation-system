# 🎬 Movie Recommendation System

A Machine Learning web application that recommends movies based on similarity using content-based filtering and NLP techniques.

🚀 **Live App**:
https://movie-recommendation-system-bxnzcbx5gf3e4ryx5xpuua.streamlit.app/

---

## 📌 Project Overview

This system suggests movies similar to a given movie by analyzing features like genres, keywords, cast, director, and overview. It uses vectorization and cosine similarity to find the most relevant matches.

---

## 🧠 Features

* 🔍 Search any movie name
* 🎯 Top 5 similar movie recommendations
* 🖼️ Movie posters using TMDB API
* ⚡ Fast similarity-based results
* 🌐 Fully deployed web application

---

## 🛠️ Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn
* NLP (CountVectorizer)
* Streamlit
* TMDB API

---

## ⚙️ How It Works

1. Data preprocessing (merge movies & credits datasets)
2. Feature engineering (genres, keywords, cast, director, overview)
3. Text vectorization using CountVectorizer
4. Similarity computation using cosine similarity
5. Recommend top similar movies

---

## 📂 Project Structure

movie-recommendation-system/
│
├── app.py

├── movies.pkl
├── similarity.pkl (downloaded via Google Drive)
├── requirements.txt
└── README.md

---

## 🔐 Environment Variables

This project uses TMDB API to fetch movie posters.

### Local setup:

Create a folder `.streamlit` and inside it create `secrets.toml`:

TMDB_API_KEY = "your_api_key_here"

### Deployment:

Add the same key in Streamlit Cloud → **Secrets section**

---

## 🚀 Run Locally

git clone https://github.com/puneethpullemla/movie-recommendation-system.git
cd movie-recommendation-system

pip install -r requirements.txt
streamlit run app.py

---

## 📦 Deployment

Deployed using Streamlit Cloud:

1. Push code to GitHub
2. Connect repository to Streamlit Cloud
3. Add API key in Secrets
4. Deploy

---

## 📊 Future Improvements

* Hybrid recommendation system
* Trailer integration
* Ratings-based filtering
* Improved UI/UX
* Search auto-suggestions

---

## 🙌 Acknowledgements

* Dataset: TMDB 5000 Movies Dataset (Kaggle)
* API: TMDB (The Movie Database)

---

## 👨‍💻 Author

Puneeth Kumar

GitHub: https://github.com/puneethpullemla
LinkedIn: https://www.linkedin.com/in/puneethkumar7/

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
