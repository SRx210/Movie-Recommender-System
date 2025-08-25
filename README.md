# 🎬 Movie Recommender System

## 📌 Overview

This project is a **content-based Movie Recommender System** built using **Python**, **Pandas**, and **Scikit-learn**.
It recommends movies similar to a given movie by analyzing metadata such as genres, keywords, cast, and crew from the **TMDB 5000 Movie Dataset**.

---

## 📂 Dataset

The project uses the following datasets (available on Kaggle’s TMDB 5000 Movie Dataset):

* `tmdb_5000_movies.csv`
* `tmdb_5000_credits.csv`

---

## ⚙️ Features

* Data cleaning and preprocessing of movie and credits datasets
* Merging datasets to form a single DataFrame
* Feature extraction (genres, keywords, cast, crew, overview)
* Text preprocessing using **NLTK / Python string methods**
* Vectorization using **CountVectorizer (Bag of Words)**
* Similarity calculation using **Cosine Similarity**
* Function to recommend top-N similar movies

---

## 🛠️ Technologies Used

* **Python** 🐍
* **Pandas** – Data handling
* **NumPy** – Numerical operations
* **Scikit-learn** – Vectorization & similarity computation

---

## 🚀 How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/<your-username>/Movie-Recommender-System.git
   cd Movie-Recommender-System
   ```
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
3. Run the Jupyter Notebook:

   ```bash
   jupyter notebook Untitled-1.ipynb
   ```

---

## 📊 Example Output

```python
recommend("Avatar")
```

➡️ Suggested Movies:

* Guardians of the Galaxy
* Star Wars: The Force Awakens
* Star Trek
* John Carter
* The Avengers

---

## 📌 Future Improvements

* Deploy model using **Streamlit / Flask**
* Add **collaborative filtering** for user-based recommendations
* Optimize performance with **TF-IDF** instead of simple CountVectorizer

---

## 👨‍💻 Author

Developed by **Sohan Raut** ✨

---
