import streamlit as st
import pickle
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# ==== Load Saved Files ====
title_df = pickle.load(open("D:/ML PROJECTS/Netflix Content Analysis and Recommendation System/netflix_titles.pkl", "rb"))
cosine_sim = pickle.load(open("D:/ML PROJECTS/Netflix Content Analysis and Recommendation System/cosine_sim_matrix.pkl", "rb"))
tfidf_vectorizer = pickle.load(open("D:/ML PROJECTS/Netflix Content Analysis and Recommendation System/tfidf_vectorizer.pkl", "rb"))

# ==== Title Index Mapping ====
title_df = title_df.reset_index(drop=True)
title_to_index = pd.Series(title_df.index, index=title_df['title'].str.lower())

# ==== Streamlit Page Settings ====
st.set_page_config(page_title="Netflix Recommender", page_icon="🎬", layout="centered")
st.markdown(
    "<h1 style='text-align: center; color: crimson;'>🎬 Netflix Recommendation System</h1>",
    unsafe_allow_html=True
)
st.markdown("<hr>", unsafe_allow_html=True)

# ==== Input ====
user_input = st.text_input("🔍 Enter a Netflix Title:", placeholder="Try 'Breaking Bad' or 'Sherlock'")

def recommend(title):
    title_lower = title.lower()
    if title_lower not in title_to_index:
        return ["❌ Title not found. Please try another."]
    
    idx = title_to_index[title_lower]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:6]  # Top 5 excluding the same title
    recommended_titles = title_df['title'].iloc[[i[0] for i in sim_scores]].tolist()
    return recommended_titles

# ==== Results ====
if st.button("Get Recommendations 🚀"):
    if user_input.strip() == "":
        st.warning("⚠️ Please enter a title.")
    else:
        st.markdown("### 🎯 Top 5 Recommended Titles:")
        for i, rec in enumerate(recommend(user_input), 1):
            st.markdown(f"- {i}. **{rec}**")

# ==== Footer ====
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown(
    "<div style='text-align: center; color: gray;'>Built with ❤️ using Streamlit & Scikit-learn</div>",
    unsafe_allow_html=True
)
