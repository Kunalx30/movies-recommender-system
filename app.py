import pandas as pd
import streamlit as st
import pickle
import requests
import time

# -------------------- PAGE CONFIG --------------------
st.set_page_config(
    page_title="Movie Recommender",
    page_icon="🎬",
    layout="wide"
)

# -------------------- CUSTOM CSS --------------------
st.markdown("""
<style>

/* ---------- GLOBAL BACKGROUND ---------- */
body {
    background: radial-gradient(
        circle at top,
        #1b2735 0%,
        #090a0f 45%,
        #000000 100%
    );
    color: #e5e5e5;
}

/* Remove Streamlit white padding */
.main {
    background-color: transparent;
}

/* ---------- HERO SECTION ---------- */
.hero {
    text-align: center;
    padding: 90px 20px 50px;
}

.hero h1 {
    font-size: 68px;
    font-weight: 900;
    letter-spacing: 1px;
    margin-bottom: 12px;
}

.hero span {
    background: linear-gradient(90deg, #f5c518, #ff8c00);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero p {
    font-size: 18px;
    color: #b0b3b8;
    max-width: 720px;
    margin: auto;
}

/* ---------- SEARCH BOX ---------- */
div[data-baseweb="select"] > div {
    background: linear-gradient(145deg, #0f1117, #151922);
    border-radius: 14px;
    border: 1px solid rgba(255,255,255,0.08);
    color: white;
}

/* ---------- BUTTON ---------- */
button {
    background: linear-gradient(135deg, #f5c518, #ff8c00) !important;
    color: black !important;
    font-weight: 700 !important;
    border-radius: 14px !important;
    height: 52px !important;
    transition: all 0.3s ease;
}

button:hover {
    transform: scale(1.05);
    box-shadow: 0 0 25px rgba(245,197,24,0.6);
}

/* ---------- MOVIE CARD ---------- */
.movie-card {
    background: linear-gradient(
        180deg,
        rgba(255,255,255,0.08),
        rgba(255,255,255,0.02)
    );
    border-radius: 18px;
    padding: 12px;
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255,255,255,0.06);
    box-shadow: 0 15px 35px rgba(0,0,0,0.6);
    transition: all 0.35s ease;
}

.movie-card:hover {
    transform: translateY(-10px) scale(1.04);
    box-shadow: 0 25px 60px rgba(0,0,0,0.9);
}

/* ---------- MOVIE TITLE ---------- */
.movie-title {
    text-align: center;
    font-weight: 600;
    color: #f1f1f1;
    margin-top: 10px;
}

/* ---------- FOOTER ---------- */
footer {
    margin-top: 90px;
    text-align: center;
    color: #8b8b8b;
    font-size: 14px;
    opacity: 0.8;
}

</style>
""", unsafe_allow_html=True)


# -------------------- LOAD MODEL --------------------
movies_dict = pickle.load(open("movie_dict.pkl", "rb"))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open("similarity.pkl", "rb"))

# -------------------- FUNCTIONS --------------------
def fetch_poster(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8"
        response = requests.get(url, timeout=5)
        data = response.json()
        if data.get("poster_path"):
            return "https://image.tmdb.org/t/p/w500/" + data["poster_path"]
    except:
        pass
    return "https://via.placeholder.com/300x450?text=No+Poster"


def recommend(movie):
    movie_index = movies[movies["title"] == movie].index[0]
    distances = similarity[movie_index]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    results = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        results.append({
            "title": movies.iloc[i[0]].title,
            "poster": fetch_poster(movie_id)
        })
    return results

# -------------------- HERO SECTION --------------------
st.markdown("""
<div class="hero">
    <h1>Movie <span>Recommender</span></h1>
    <p>
        Discover your next favorite film with our intelligent recommendation system.
        Enter a movie you love and let AI find your perfect match.
    </p>
</div>
""", unsafe_allow_html=True)

# -------------------- SEARCH INPUT --------------------
selected_movie = st.selectbox(
    "",
    movies["title"].values,
    index=None,
    placeholder="🔍 Enter a movie title you love..."
)

# -------------------- BUTTON --------------------
col_btn = st.columns([1,2,1])
with col_btn[1]:
    recommend_btn = st.button("✨ Get Recommendations", use_container_width=True)

# -------------------- RECOMMENDATION LOGIC --------------------
if recommend_btn and selected_movie:
    with st.spinner("Finding your perfect match 🎬"):
        time.sleep(1.2)
        recommendations = recommend(selected_movie)

    st.markdown(
        f"<h3 style='text-align:center;margin-top:40px;'>Recommendations based on \"{selected_movie}\"</h3>",
        unsafe_allow_html=True
    )

    cols = st.columns(5)
    for idx, col in enumerate(cols):
        with col:
            st.markdown("<div class='movie-card'>", unsafe_allow_html=True)
            st.image(recommendations[idx]["poster"], use_container_width=True)
            st.markdown(
                f"<div class='movie-title'>{recommendations[idx]['title']}</div>",
                unsafe_allow_html=True
            )
            st.markdown("</div>", unsafe_allow_html=True)

# -------------------- FOOTER --------------------
st.markdown("""
<footer>
    Powered by Machine Learning • Built By Kunal❤️
</footer>
""", unsafe_allow_html=True)



# streamlit run C:\CWH-DS\Projects\Project_02\Movies_recommender_system\app.py
