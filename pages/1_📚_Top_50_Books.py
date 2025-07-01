import streamlit as st
import pandas as pd

popularity_df = pd.read_pickle("popularity_df.pkl")

st.title("📚 Top 50 Best Rated Books")
st.markdown("These are the most popular books with at least 250 ratings.")

popularity_df = popularity_df.drop_duplicates("Book-Title").head(50)

for i in range(0, len(popularity_df), 5):
    row = popularity_df.iloc[i:i+5]
    cols = st.columns(5)
    
    for idx, (col, (_, book)) in enumerate(zip(cols, row.iterrows())):
        with col:
            st.image(book['Image-URL-M'], use_container_width=True)
            st.markdown(f"**{book['Book-Title']}**")
            st.markdown(f"*by {book['Book-Author']}*")
            st.markdown(f"⭐ {round(book['Avg_Rating'], 2)} | 👤 {book['No_of_Ratings']} ratings")