# Movie Recommendation System

## Overview
This is a **Movie Recommendation System** that suggests the **top 5 movies** based on a user's preferred movie. The project utilizes **Machine Learning** techniques, including vectorization, to generate movie vectors and recommend similar films.

## Technologies Used
- **Python Libraries:**
  - `pandas` – for data manipulation
  - `numpy` – for numerical computations
  - `sklearn (scikit-learn)` – for machine learning model and vectorization
  - `pickle` – for saving and loading the trained model
- **Web Framework:**
  - `Streamlit` – for building the web interface and testing the model

## Features
- Takes a user's favorite movie as input
- Uses vectorization techniques to find similar movies
- Recommends the **top 5 most similar movies**
- Interactive UI using **Streamlit**

## Setup and Installation
### Prerequisites
Make sure you have **Python 3.9** installed along with the required dependencies.

### Installation Steps
1. **Download Jupyter Notebook** if not already installed.
2. **Install required libraries** using the following command:
   ```sh
   pip install pandas numpy scikit-learn pickle-mixin streamlit
   ```
3. **Run the .ipynb file (Jupyter Notbook)**
4. **This will create pickle files which is neccessary for the **app.py** to execute**
5. **Run the Streamlit app**
   ```sh
   streamlit run app.py
   ```

## Usage
1. Open the web app in your browser (usually at `http://localhost:8501/`).
2. Enter the name of a movie you like.
3. Get a list of **5 recommended movies** similar to your choice.

## Model Explanation
- **Vectorization:**
  - Converts movie descriptions into numerical vectors using **TF-IDF** or **CountVectorizer**.
- **Similarity Calculation:**
  - Uses **Cosine Similarity** to measure the closeness between movie vectors.
- **Recommendation:**
  - Finds the top 5 movies with the highest similarity scores.

---
### Author
[Sohan Raut]  
GitHub: [SRx210](https://github.com/SRx210)

