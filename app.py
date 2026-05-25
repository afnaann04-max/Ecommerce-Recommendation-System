import streamlit as st
import pandas as pd
import base64

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------
st.set_page_config(
    page_title="IntelliCart AI",
    page_icon="🛒",
    layout="wide"
)


# ---------------------------------------------------
# BACKGROUND IMAGE FUNCTION
# ---------------------------------------------------
def add_bg_from_local(image_file):

    with open(image_file, "rb") as image:
        encoded = base64.b64encode(image.read()).decode()

    st.markdown(
        f"""
        <style>

        /* MAIN BACKGROUND */
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}

        /* DARK OVERLAY */
        .stApp::before {{
            content: "";
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0,0,0,0.55);
            z-index: -1;
        }}

        /* SIDEBAR */
        section[data-testid="stSidebar"] {{
            background: rgba(255,255,255,0.08);
            backdrop-filter: blur(20px);
            border-right: 1px solid rgba(255,255,255,0.10);
        }}

        /* HEADER */
        header[data-testid="stHeader"] {{
            background: transparent;
        }}

        /* TEXT COLORS */
        h1, h2, h3, h4, h5, h6, p, label {{
            color: white !important;
        }}

        /* ================================= */
        /* TRANSPARENT BLUR SEARCH BAR */
        /* ================================= */

        div[data-baseweb="input"] {{
            background-color: rgba(255,255,255,0.05) !important;
            backdrop-filter: blur(25px);
            border-radius: 18px !important;
            border: 1px solid rgba(255,255,255,0.20) !important;
            box-shadow: none !important;
        }}

        /* REMOVE INNER WHITE BACKGROUND */
        div[data-baseweb="base-input"] {{
            background: transparent !important;
        }}

        /* INPUT TEXT */
        div[data-baseweb="input"] input {{
            background: transparent !important;
            color: black !important;
            font-size: 16px !important;
            font-weight: 600 !important;
        }}

        /* PLACEHOLDER */
        div[data-baseweb="input"] input::placeholder {{
            color: rgba(0,0,0,0.6) !important;
        }}

        /* SEARCH BAR FOCUS */
        div[data-baseweb="input"]:focus-within {{
            border: 1px solid rgba(0,191,255,0.7) !important;
            box-shadow: 0 0 15px rgba(0,191,255,0.35);
        }}

        /* BUTTON */
        .stButton button {{
            width: 100%;
            height: 3em;
            border-radius: 18px;
            background: rgba(0,191,255,0.22);
            backdrop-filter: blur(20px);
            color: white;
            font-size: 18px;
            font-weight: bold;
            border: 1px solid rgba(255,255,255,0.15);
            transition: 0.3s;
        }}

        .stButton button:hover {{
            background: rgba(0,191,255,0.40);
            border: 1px solid rgba(255,255,255,0.30);
            transform: scale(1.02);
        }}

        /* PRODUCT CARD */
        .product-card {{
            background: rgba(255,255,255,0.08);
            backdrop-filter: blur(18px);
            border-radius: 20px;
            padding: 15px;
            border: 1px solid rgba(255,255,255,0.12);
            margin-bottom: 20px;
            transition: 0.3s;
        }}

        .product-card:hover {{
            transform: translateY(-5px);
            border: 1px solid rgba(0,191,255,0.5);
        }}

        /* SCROLLBAR */
        ::-webkit-scrollbar {{
            width: 10px;
        }}

        ::-webkit-scrollbar-track {{
            background: rgba(255,255,255,0.05);
        }}

        ::-webkit-scrollbar-thumb {{
            background: rgba(255,255,255,0.20);
            border-radius: 10px;
        }}

        </style>
        """,
        unsafe_allow_html=True
    )


# ---------------------------------------------------
# ADD BACKGROUND IMAGE
# ---------------------------------------------------
add_bg_from_local("images/bg.jpg")


# ---------------------------------------------------
# LOAD DATASET
# ---------------------------------------------------
df = pd.read_csv("dataset/amazon.csv")


# ---------------------------------------------------
# CREATE COMBINED FEATURES
# ---------------------------------------------------
df['combined_features'] = (
    df['product_name'].astype(str) + ' ' +
    df['category'].astype(str) + ' ' +
    df['about_product'].astype(str)
)


# ---------------------------------------------------
# TF-IDF
# ---------------------------------------------------
vectorizer = TfidfVectorizer(stop_words='english')

feature_vectors = vectorizer.fit_transform(
    df['combined_features']
)


# ---------------------------------------------------
# COSINE SIMILARITY
# ---------------------------------------------------
similarity = cosine_similarity(feature_vectors)


# ---------------------------------------------------
# RECOMMENDATION FUNCTION
# ---------------------------------------------------
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
            'rating': df.iloc[index]['rating'],
            'link': df.iloc[index]['product_link']
        })

    return recommended


# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------
st.sidebar.title("🛍️ IntelliCart AI")

st.sidebar.markdown("---")

st.sidebar.markdown("### Features")
st.sidebar.markdown("✔ Smart Product Recommendation")
st.sidebar.markdown("✔ Machine Learning Powered")
st.sidebar.markdown("✔ Amazon Product Dataset")
st.sidebar.markdown("✔ Real-time Similarity Search")

st.sidebar.markdown("---")

st.sidebar.markdown(
    """
    <p style='color:white; font-size:14px;'>
    Built using Streamlit, Scikit-learn,
    TF-IDF and Cosine Similarity.
    </p>
    """,
    unsafe_allow_html=True
)


# ---------------------------------------------------
# PROFESSIONAL TITLE
# ---------------------------------------------------
st.markdown(
    """
    <h1 style='
        text-align: center;
        font-size: 58px;
        font-weight: 800;
        color: white;
        letter-spacing: 2px;
        margin-bottom: 10px;
        text-shadow: 0 0 20px rgba(0,191,255,0.7);
    '>
        ✨ IntelliCart AI
    </h1>

    <p style='
        text-align: center;
        font-size: 22px;
        color: rgba(255,255,255,0.85);
        margin-top: -10px;
        margin-bottom: 40px;
        letter-spacing: 1px;
    '>
        Smart Ecommerce Recommendation Engine
    </p>
    """,
    unsafe_allow_html=True
)


# ---------------------------------------------------
# SEARCH INPUT
# ---------------------------------------------------
product_input = st.text_input(
    "",
    placeholder="🔍 Search products like Samsung, Boat, HP..."
)


# ---------------------------------------------------
# RECOMMEND BUTTON
# ---------------------------------------------------
if st.button("Recommend Products"):

    recommendations = recommend_products(product_input)

    if recommendations:

        st.subheader("Recommended Products")

        cols = st.columns(5)

        for idx, item in enumerate(recommendations):

            with cols[idx]:

                st.image(item['image'], width=180)

                st.markdown(
                    f"""
                    <div class="product-card">

                    <p style='color:white; font-size:14px;'>
                    {item['name'][:120]}...
                    </p>

                    <p style='color:yellow; font-weight:bold;'>
                    ⭐ Rating: {item['rating']}
                    </p>

                    </div>
                    """,
                    unsafe_allow_html=True
                )

                st.markdown(
                    f"[🛒 View Product]({item['link']})"
                )

    else:
        st.error("No matching products found")