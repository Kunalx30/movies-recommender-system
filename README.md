# 🎬 Movie Recommender System

A content-based **Movie Recommendation System** built using **Python**, **Pandas**, **Scikit-learn**, and **Streamlit**.  
The application recommends movies similar to a selected title by computing **cosine similarity** between movie feature vectors.

## 👉 Live App URL:
https://movies-recommender-system-43ptgfn6gnpryffgxa8mzc.streamlit.app/
---

## 🚀 Features
- Content-based movie recommendations  
- Cosine similarity–based matching  
- Interactive web interface using **Streamlit**  
- Fast and simple user experience  
- Handles large ML artifacts using **Git LFS**

---

## 🛠️ Tech Stack
- **Python**
- **Pandas, NumPy**
- **Scikit-learn**
- **Streamlit**
- **Git & Git LFS**

---

## ⚙️ How It Works
1. Movie metadata is processed and converted into numerical feature vectors  
2. Cosine similarity is calculated between all movies  
3. When a user selects a movie, the system recommends the top similar movies  
4. Results are displayed through a Streamlit web interface  

---

## 📁 Project Structure

movies-recommender-system/
│
├── app.py
├── movie_dict.pkl
├── similarity.pkl
├── requirements.txt
├── setup.sh
├── .gitignore


---

## 🧠 Large File Handling
> ⚠️ The `similarity.pkl` file is large and is managed using **Git Large File Storage (Git LFS)** to comply with GitHub file size limits.

---

## ▶️ How to Run Locally
### 1. Clone the repository:

git clone https://github.com/Kunalx30/movies-recommender-system.git

### 2. Navigate to the project directory:
cd movies-recommender-system

### 3. Install dependencies:
pip install -r requirements.txt

### 4. Run the Streamlit app:
streamlit run app.py


## 🌐 Deployment
The application is deployed using Streamlit Cloud and can be accessed directly through a web browser.

## 📌 Use Cases

Learning recommendation systems
ML & Data Science portfolio project
Understanding similarity-based filtering

Built and deployed a content-based Movie Recommendation System using Python, Scikit-learn, and Streamlit. Managed large ML artifacts using Git LFS and deployed the application on Streamlit Cloud.

---

## 🤝 Author

### Kunal
### B.Tech CSE | Data Analyst Aspirant

---

### ⭐ Acknowledgement
 Inspired by real-world recommendation systems used by streaming platforms.
