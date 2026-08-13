# 🛒 IntelliCart AI

## Personalized Ecommerce Recommendation System

IntelliCart AI is a **Machine Learning-based personalized ecommerce recommendation system** that recommends similar and relevant products based on product information such as product name, category, and description.

The project uses **Content-Based Filtering**, **TF-IDF Vectorization**, and **Cosine Similarity** to identify products that are similar to the product searched by the user.

🔗 **Live Demo:** https://ecommerce-recommendation-system-2lfkz6mtkkhdnwe5rrzzqs.streamlit.app/

---

## 📌 Project Overview

Online shopping platforms contain thousands of products, making it difficult for users to find products that match their interests.

IntelliCart AI solves this problem by analyzing product information and recommending similar products to the user.

### Example

If a user searches for:

> Samsung Smartphone

The system analyzes the product's information and recommends other products with similar characteristics.

---

## 🎯 Objectives

* Build a personalized ecommerce recommendation system.
* Recommend relevant products based on product similarity.
* Apply Machine Learning and Natural Language Processing techniques.
* Use product descriptions and categories as recommendation features.
* Develop an interactive web application using Streamlit.
* Provide product images, ratings, and product links.
* Deploy the application online for real-time demonstration.

---

## ✨ Features

* 🔍 Smart product search
* 🤖 Machine Learning-based recommendations
* 🛍️ Content-Based Filtering
* 📊 TF-IDF Vectorization
* 🔗 Cosine Similarity
* ⭐ Product ratings
* 🖼️ Product images
* 🛒 Amazon product links
* 🎨 Modern glassmorphism user interface
* 🌐 Live Streamlit deployment

---

## 🧠 Recommendation Method

The system uses **Content-Based Filtering**.

Instead of comparing different users, the system compares the characteristics of products.

The following product information is combined:

* Product Name
* Category
* Product Description

This combined information is converted into numerical vectors using **TF-IDF**.

The similarity between products is then calculated using **Cosine Similarity**.

### Recommendation Workflow

```text
User searches for a product
          ↓
Product information is retrieved
          ↓
Product name + category + description
          ↓
TF-IDF Vectorization
          ↓
Cosine Similarity
          ↓
Similarity scores calculated
          ↓
Top similar products selected
          ↓
Recommended products displayed
```

---

## 🛠️ Technologies Used

| Technology        | Purpose                        |
| ----------------- | ------------------------------ |
| Python            | Main programming language      |
| Pandas            | Data processing                |
| NumPy             | Numerical operations           |
| Scikit-learn      | Machine Learning               |
| TF-IDF            | Text feature extraction        |
| Cosine Similarity | Product similarity calculation |
| Streamlit         | Web application                |
| Git               | Version control                |
| GitHub            | Source code management         |

---

## 📂 Dataset

The project uses an **Amazon Sales Dataset obtained from Kaggle**.

Important columns used by the system include:

* `product_name`
* `category`
* `about_product`
* `rating`
* `img_link`
* `product_link`

### Dataset Usage

The following columns are combined to create the recommendation features:

```text
product_name
category
about_product
```

The system uses these features to determine product similarity.

---

## 🔄 Machine Learning Workflow

### 1. Data Collection

The Amazon sales/product dataset was collected from Kaggle.

### 2. Data Preprocessing

Product information is converted to string format and combined into a single feature.

### 3. Feature Engineering

The following information is combined:

```text
Product Name + Category + Product Description
```

### 4. TF-IDF Vectorization

TF-IDF converts textual product information into numerical vectors.

### 5. Similarity Calculation

Cosine Similarity compares the vectors of different products.

### 6. Recommendation

The products with the highest similarity scores are selected as recommendations.

### 7. Web Application

The recommendation system is integrated into a Streamlit interface.

---

## 🖥️ Application Interface

The application provides a modern ecommerce-style interface with:

* AI-powered branding
* Search bar
* Glassmorphism design
* Blurred sidebar
* Product recommendation cards
* Product images
* Product ratings
* Amazon product links

---

## 📁 Project Structure

```text
Personalized-Ecommerce-recommendation-system/
│
├── dataset/
│   └── amazon.csv
│
├── images/
│   └── bg.jpg
│
├── app.py
├── model.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/afnaann04-max/Personalized-Ecommerce-recommendation-system.git
```

### 2. Navigate to the project folder

```bash
cd Personalized-Ecommerce-recommendation-system
```

### 3. Install required libraries

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit application

```bash
streamlit run app.py
```

The application will normally open at:

```text
http://localhost:8501
```

---

## 🚀 Live Demo

Try the deployed application:

**IntelliCart AI:**
https://ecommerce-recommendation-system-2lfkz6mtkkhdnwe5rrzzqs.streamlit.app/

---

## 📊 Sample Recommendation Process

```text
Input:
Samsung

        ↓

Search Dataset

        ↓

Extract Product Information

        ↓

TF-IDF Vectorization

        ↓

Cosine Similarity

        ↓

Top 5 Similar Products

        ↓

Display Recommendations
```

---

## 🔮 Future Enhancements

The current system uses content-based recommendations. Future versions can include:

* 👤 User login and profiles
* 🧠 Collaborative Filtering
* 🔀 Hybrid Recommendation System
* 📈 User purchase history
* ⭐ Personalized recommendations based on ratings
* 💬 AI shopping assistant/chatbot
* 🎤 Voice-based product search
* 🔄 Real-time recommendations
* 📱 Mobile application
* 🗄️ Database integration
* 📊 Recommendation performance evaluation

---

## ⚠️ Current Limitations

* The current system primarily uses product-content similarity.
* It does not yet use individual user purchase history.
* Recommendations depend on the quality of product descriptions and categories.
* The dataset is relatively small compared with real-world ecommerce platforms.

---

## 🎓 Learning Outcomes

Through this project, I gained practical experience in:

* Python programming
* Data preprocessing
* Natural Language Processing
* Feature engineering
* TF-IDF vectorization
* Cosine similarity
* Recommendation systems
* Machine Learning
* Streamlit application development
* Git and GitHub
* Web application deployment

---

## 👩‍💻 Developer

**Afnan KC**

BSc Mathematics & Physics
Data Science / AI Trainee

---

## 📜 Project Type

**Machine Learning / Data Science Project**

**Domain:** Ecommerce & Recommendation Systems

**Status:** Completed and Deployed 🚀

---

## ⭐ Acknowledgement

Dataset used in this project was obtained from **Kaggle** and is used for educational and project-development purposes.

---

## 📬 Feedback

Suggestions and feedback are welcome. Feel free to explore the project and try the live application.

⭐ If you find this project interesting, consider giving the repository a star!

