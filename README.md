# 📚 Book Recommender System

This is a machine learning-based Book Recommender System that uses **Collaborative Filtering** and **Popularity-based Ranking** to suggest books to users. It is built using **Python**, **Pandas**, **Scikit-learn**, and **Streamlit**.

## 🚀 Features

- 🔥 **Top 50 Most Popular Books** based on average rating and number of ratings
- 🎯 **Book Recommendation System** that suggests books similar to a selected one
  using cosine similarity
- 🧠 Collaborative Filtering using a user-book rating matrix
- 📊 Clean Streamlit UI with multiple pages
- 🖼️ Displays book covers, authors, and ratings in a neat card layout

## 📊 Tech Stack  

**Language:** Python 🐍  

**Libraries:**  
- `pandas`, `numpy` – Data manipulation  
- `scikit-learn` – Cosine similarity and preprocessing  
- `streamlit` – Web app development  
- `pickle` – Model serialization  

**Techniques Used:**  
- Popularity-based Recommendation  
- Collaborative Filtering  
- Cosine Similarity  



## 🧾 Project Structure
```
BOOK-RECOMMENDER-SYSTEM/
│
├── app.py                # Main entry point for Streamlit
├── b_r_s.ipynb           # Jupyter notebook for data processing and modeling
├── Books.csv             # Book metadata
├── Ratings.csv           # User ratings for books
├── Users.csv             # User demographic data
├── pt.pkl                # Pivot table for collaborative filtering
├── similarity.pkl        # Cosine similarity matrix
├── popularity_df.pkl     # Top 50 most popular books
├── requirements.txt      # Python dependencies
├── .gitignore            # Files to ignore in Git
├── pages/                # Streamlit multipage layout
│   ├── 1_📚_Top_50_Books.py            # Displays top 50 books
│   └── 2_🔍_Book_Recommendation.py     # Book recommendation UI
└── README.md             # Project documentation
```

## 🖥️ How to Run

- **Clone the Repository**  
```
git clone https://github.com/yourusername/BOOK-RECOMMENDER-SYSTEM.git
cd Book-Recommender-System
```
- **Install Dependencies**  
```
pip install -r requirements.txt
```
- **Launch Streamlit Web App**
```
streamlit run app.py
```

## 🧠 How It Works

**Data Processing**

- Merges books and ratings

- Filters users with over 200 ratings and books with at least 50 ratings

- Creates a pivot table of Book-Title vs User-ID

**Popularity-Based Recommender**

- Filters books with ≥250 ratings

- Calculates average ratings

- Displays top 50 highest-rated books

**Collaborative Filtering**

- Uses cosine similarity on pivot table

- Recommends 5 books similar to the selected title

- Book details (cover, title, author, ratings) are shown in a clean layout

**Deployment**

- Data is saved as .pkl files

- Streamlit provides an easy-to-use frontend

## 🧪 Example Usage

- Open the Streamlit app and:

- Go to 🔍 Book Recommendation Page

  - Choose a book like:
    `"The Da Vinci Code"`

  - Click Recommend

  - Output: 5 recommended books with cover images, author names, and titles.

- Or:

  - Go to 📚 Top 50 Books Page

  - Browse most popular books with images and average ratings.

## 📸 Screenshots

![Screenshot 2025-07-01 115054](https://github.com/user-attachments/assets/40b7691d-e826-482d-bf8b-2ea4f1c08489)
![Screenshot 2025-07-01 115119](https://github.com/user-attachments/assets/2de091f8-6d0c-4a2a-8bcc-ca64e3c0664e)
![Screenshot 2025-07-01 115144](https://github.com/user-attachments/assets/9c0e46c1-4cb8-44ca-9701-0d439ef84e4d)
![Screenshot 2025-07-01 115037](https://github.com/user-attachments/assets/20f20ae5-4afb-431c-9da9-f360470a3474)
![Screenshot 2025-07-01 114956](https://github.com/user-attachments/assets/4403e5fd-5c81-4a8c-a4b5-6c98ae2da7ed)
![Screenshot 2025-07-01 114908](https://github.com/user-attachments/assets/fe74e448-5da4-4ad2-8ae9-2f5e96e4fa8e)  

 
[Book Recommender System Demo](https://github.com/user-attachments/assets/cf2e69ee-90da-42cb-982c-f3ba7aab1393)



## 🤝 Contributing
Contributions, ideas, and suggestions are welcome!

Feel free to:

- Fork this repository

- Create a new feature branch

- Submit a pull request 🚀

⭐ If you found this project helpful, please consider giving it a star!

## 📄 License
This project is licensed under the MIT License.

## 🧑‍💻 Author  
**Anshuman Dash** 
 
[![GitHub](https://img.shields.io/badge/GitHub-Profile-black?logo=github)](https://github.com/ANSH5252) 

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?logo=linkedin)](https://www.linkedin.com/in/anshuman-dash-739793351/)
