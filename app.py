import streamlit as st
import pickle
import pandas as pd

# Load the data and similarity matrix
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Convert dict to DataFrame
new_df = pd.DataFrame(movies_dict)

def recommend(movie):
    movie_index = new_df[new_df['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(new_df.iloc[i[0]].title)
    return recommended_movies

st.set_page_config(page_title="Movie Recommender", page_icon="🎬", layout="centered")

st.title('🎬 Movie Recommender System')
st.markdown("##### Get personalized movie recommendations based on your selection!")

selected_movie = st.selectbox(
    '🎥 **Choose a movie:**',
    new_df['title'].values
)

if st.button('Recommend'):
    recommendations = recommend(selected_movie)
    st.markdown("### ⭐ Top 5 Recommended Movies:")
    cols = st.columns(5)
    for idx, movie in enumerate(recommendations):
        st.markdown(f"**{movie}**")