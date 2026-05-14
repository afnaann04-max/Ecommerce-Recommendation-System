import streamlit as st
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Load dataset
df = pd.read_csv("dataset/amazon.csv")


# Create combined features
df['combined_features'] = (
    df['product_name'].astype(str) + ' ' +
    df['category'].astype(str) + ' ' +
    df['about_product'].astype(str)
)


# TF-IDF
vectorizer = TfidfVectorizer(stop_words='english')

feature_vectors = vectorizer.fit_transform(df['combined_features'])


# Similarity matrix
similarity = cosine_similarity(feature_vectors)


# Recommendation function
def recommend_products(product_name):

    matching_products = df[
        df['product_name'].str.contains(
            product_name,
            case=False,
            na=False
        )
    ]

    if matching_products.empty:
        return []

    product_index = matching_products.index[0]

    similarity_scores = list(
        enumerate(similarity[product_index])
    )

    sorted_products = sorted(
        similarity_scores,
        key=lambda x: x[1],
        reverse=True
    )

    recommended = []

    for product in sorted_products[1:6]:

        index = product[0]

        recommended.append({
            'name': df.iloc[index]['product_name'],
            'image': df.iloc[index]['img_link'],
            'rating': df.iloc[index]['rating']
        })

    return recommended


# Streamlit UI
st.title("🛒 Personalized Ecommerce Recommendation System")

st.write("Find similar Amazon products using AI")


# Search box
product_input = st.text_input(
    "Enter product name"
)


# Button
if st.button("Recommend"):

    recommendations = recommend_products(product_input)

    if recommendations:

        st.subheader("Recommended Products")

        for item in recommendations:

            st.image(item['image'], width=150)

            st.write(item['name'])

            st.write("⭐ Rating:", item['rating'])

            st.write("---")

    else:
        st.write("No matching products found")