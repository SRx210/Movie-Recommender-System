# Movie Recommendation System

A content-based movie recommendation web application built using **Python**, **Scikit-learn**, and **Streamlit**. It suggests top 5 similar movies based on a selected title using NLP and cosine similarity on movie metadata.

---

## Features

- Recommend top 5 movies based on content similarity
- Utilizes movie metadata like overview, genres, cast, crew, and keywords
- Implements NLP techniques (stemming, vectorization)
- Clean and interactive UI using **Streamlit**
- Fast model loading using **Pickle**
- Lightweight and easy to run locally

---

## Tech Stack

**Languages & Tools:**  
`Python`, `Pandas`, `NumPy`, `Scikit-learn`, `Pickle`, `Streamlit`, `CountVectorizer`

**Dataset:**  
[TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata) from Kaggle

---

## Installation

1. **Clone the repository**
```bash
git clone https://github.com/SRx210/Movie-Recommender-System.git
cd movie-recommender-system
````

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Run the app**

```bash
streamlit run app.py
```

---

## How It Works

1. **Preprocessing**:

   * Combined movie features: overview, genres, keywords, cast, crew
   * Cleaned and stemmed text data

2. **Vectorization**:

   * Transformed text using `CountVectorizer` (Bag-of-Words model)

3. **Similarity Calculation**:

   * Used `cosine_similarity` to find and recommend similar movies

4. **Deployment**:

   * Streamlit-based web interface
   * Pickle used for saving and loading models efficiently

---

## Author

**Sohan Raut**

* GitHub: [@SRx210](https://github.com/SRx210)
---
