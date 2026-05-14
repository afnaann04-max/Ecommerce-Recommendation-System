import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv("dataset/amazon.csv")

print(df.head())

df['combined_features'] = (
    df['product_name'].astype(str) + ' ' +
    df['category'].astype(str) + ' ' +
    df['about_product'].astype(str)
)

print(df['combined_features'].head())

vectorizer = TfidfVectorizer(stop_words='english')

feature_vectors = vectorizer.fit_transform(df['combined_features'])

similarity = cosine_similarity(feature_vectors)

print(similarity.shape)

def recommend_products(product_name):

    # Find matching products
    matching_products = df[df['product_name'].str.contains(product_name, case=False)]

    if matching_products.empty:
        print("Product not found")
        return

    # Get first matching product
    product_index = matching_products.index[0]

    # Similarity scores
    similarity_scores = list(enumerate(similarity[product_index]))

    # Sort products
    sorted_products = sorted(
        similarity_scores,
        key=lambda x: x[1],
        reverse=True
    )

    print("\nRecommended Products:\n")

    # Top 5 recommendations
    for product in sorted_products[1:6]:

        index = product[0]

        print(df.iloc[index]['product_name'])

recommend_products('Samsung')
recommend_products("Wayona")