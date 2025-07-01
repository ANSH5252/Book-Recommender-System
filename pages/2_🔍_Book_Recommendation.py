import streamlit as st
import numpy as np
import pandas as pd
import pickle

pt = pd.read_pickle("pt.pkl")
similarity = pickle.load(open("similarity.pkl", "rb"))

books = pd.read_csv("books.csv")

st.title("🔍 Book Recommendation System")

book_name = st.selectbox("Choose a book", pt.index.tolist())

if st.button("Recommend"):
    index = np.where(pt.index == book_name)[0][0]
    similar_items = sorted(list(enumerate(similarity[index])), key=lambda x: x[1], reverse=True)[1:6]

    st.markdown("<h3 style='text-align: center;'>📖 Recommended Books</h3>", unsafe_allow_html=True)

    cols = st.columns(5)

    for col, (i, score) in zip(cols, similar_items):
        recommended_title = pt.index[i]
        book_data = books[books['Book-Title'] == recommended_title].drop_duplicates('Book-Title')

        if not book_data.empty:
            image_url = book_data.iloc[0]['Image-URL-M']
            author = book_data.iloc[0]['Book-Author']

            with col:
                st.image(image_url, use_container_width=True)
                st.markdown(f"<div style='text-align: center'><strong>{recommended_title}</strong></div>", unsafe_allow_html=True)
                st.markdown(f"<div style='text-align: center'><em>by {author}</em></div>", unsafe_allow_html=True)
        else:
            with col:
                st.markdown("📘 Book data not found.")