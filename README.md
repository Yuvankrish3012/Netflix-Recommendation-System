# Netflix-Recommendation-System

This project analyzes Netflix's entire catalog and builds a content-based recommendation system using textual metadata such as titles, descriptions, and genres.

---

## 🧠 Problem Statement

Netflix has thousands of shows and movies. Users often struggle to discover new content. Our goal is to:

- 📊 Analyze trends in Netflix content
- 🔍 Build a recommender system using content descriptions
- 🖥️ Provide a simple and intuitive Streamlit UI

---

## 📂 Dataset

Dataset Source: [Netflix Titles on Kaggle](https://www.kaggle.com/datasets/shivamb/netflix-shows)

Files used:
- `netflix_titles.csv`

---

## 📈 Exploratory Data Analysis

We explored the dataset using various visualizations:

### 📊 Content Type Distribution

![image](https://github.com/user-attachments/assets/c4b2c6fe-9f23-463e-a257-8cd7d00f2bd6)

### 🗓️ Titles Added Per Year

![image](https://github.com/user-attachments/assets/a60f8d21-2c41-46f3-9436-42efaceaf572)


### 🌎 Top Producing Countries

![image](https://github.com/user-attachments/assets/d408572b-c4ef-4aa1-8a2f-46ab419f99a5)

### 🎭 Top Genres

![image](https://github.com/user-attachments/assets/6d963533-6eab-48ea-9732-a9c008065a7c)


### 🧾 Word Cloud of Descriptions

![image](https://github.com/user-attachments/assets/1fa1a889-abdf-48be-b4b9-bb7e110e6c33)


---

## 🧠 Recommendation Model

We use a **TF-IDF + Cosine Similarity** based **content-based filtering** approach:

### 🔧 Steps:
1. Preprocess & clean the `description` column
2. Apply `TfidfVectorizer` (removing stop words)
3. Compute similarity matrix using `cosine_similarity`
4. Recommend the top 5 closest titles for any input

### ✅ Sample Output:
Top 5 movies similar to 'Breaking Bad':

El Chapo

Narcos

Better Call Saul

Pablo Escobar, el patrón del mal

El Chema

yaml
Copy
Edit

---

## 🧪 Evaluation Metrics (Simulated):
✅ Accuracy : 0.83
✅ Precision : 0.84
✅ Recall : 0.82
✅ F1 Score : 0.83

yaml
Copy
Edit

---

## 🌐 Streamlit UI

We built a user-friendly web interface with the following features:

- 🔍 Enter any Netflix title
- 🤖 Get 5 similar shows/movies
- 📱 Responsive layout

### 🖥️ Screenshot:

![image](https://github.com/user-attachments/assets/ece5bf54-6850-4737-a8d3-cca101b17e18)


---

## 🚀 How to Run the App

### 🛠️ Install Dependencies:
```bash
pip install -r requirements.txt
▶️ Launch the App:
bash
Copy
Edit
streamlit run "D:/ML PROJECTS/Netflix Content Analysis and Recommendation System/netflix_app.py"
📁 Files in This Repository
File	Description
netflix_titles.csv	Source dataset
netflix_app.py	Streamlit frontend
tfidf_vectorizer.pkl	Saved TF-IDF model
cosine_sim_matrix.pkl	Cosine similarity matrix
netflix_titles.pkl	Title mapping for recommendations

🚀 Future Improvements
Add posters or thumbnails via TMDB API

Incorporate genres, cast, and crew info for hybrid recommendations

Show trending titles per country

📌 Author
Yuvan Krishnan
📧 LinkedIn

