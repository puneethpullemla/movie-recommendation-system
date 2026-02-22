import streamlit as st
import pickle
import difflib
import requests

# Page config
st.set_page_config(
    page_title="Movie Recommender",
    page_icon="🎬",
    layout="wide"
)

# Load data
movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Fetch poster
def fetch_poster(movie_id):
    api_key = st.secrets["TMDB_API_KEY"]
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
    
    data = requests.get(url).json()
    poster_path = data.get('poster_path')
    
    if poster_path:
        return "https://image.tmdb.org/t/p/w500/" + poster_path
    else:
        return "https://via.placeholder.com/500x750?text=No+Image"

# Recommend function
def recommend(movie):
    movie_list = movies['title'].values
    find_close_match = difflib.get_close_matches(movie, movie_list)
    
    if not find_close_match:
        return [], []
    
    close_match = find_close_match[0]
    
    index = movies[movies['title'] == close_match]['index'].values[0]
    distances = similarity[index]
    
    movies_list = sorted(list(enumerate(distances)), key=lambda x: x[1], reverse=True)[1:6]
    
    recommended_movies = []
    recommended_posters = []
    
    for i in movies_list:
        movie_id = movies.iloc[i[0]]['id']
        recommended_movies.append(movies.iloc[i[0]]['title'])
        recommended_posters.append(fetch_poster(movie_id))
        
    return recommended_movies, recommended_posters

# ---------- UI DESIGN ----------

st.markdown(
    """
    <h1 style='text-align: center; color: #ff4b4b;'>🎬 Movie Recommendation System</h1>
    <p style='text-align: center;'>Find movies similar to your taste 🍿</p>
    """,
    unsafe_allow_html=True
)

st.write("")

# Input
selected_movie = st.text_input("🔍 Enter your favourite movie")

# Button
if st.button('Recommend 🎯'):
    if selected_movie.strip() == "":
        st.warning("Please enter a movie name")
    else:
        with st.spinner("Finding best movies for you..."):
            names, posters = recommend(selected_movie)
        
        if names:
            st.success("Top Recommendations 👇")
            
            col1, col2, col3, col4, col5 = st.columns(5)
            
            for idx, col in enumerate([col1, col2, col3, col4, col5]):
                with col:
                    st.image(posters[idx])
                    st.markdown(f"**{names[idx]}**")
        else:
            st.error("Movie not found! Try another name.")

# Footer
st.markdown(
    """
    <hr>
    <p style='text-align: center;'>Built with ❤️ using Streamlit</p>
    """,
    unsafe_allow_html=True
)