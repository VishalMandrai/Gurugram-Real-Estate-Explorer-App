# **🏙️ Gurugram Real Estate Explorer - App** [🔗](https://gurugram-real-estate-explorer.streamlit.app/)
<img width="878" height="115" alt="Github_readme_title_banner" src="https://github.com/user-attachments/assets/71c23815-cf94-4048-8ef9-90ef5f2c3657" href="https://gurugram-real-estate-explorer.streamlit.app/" />


### 🔍 **An Interactive Data Science App that provides an Analytics Module, Insights Dashboard, Price Prediction Engine, and a Smart Flat Recommendation System to help explore the Gurugram Real Estate landscape with ease.**

![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit)
![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python)
![Plotly](https://img.shields.io/badge/Plotly-Interactive%20Charts-lightblue?logo=plotly)
![XGBoost](https://img.shields.io/badge/XGBoost-Model-green?logo=xgboost)

---

## 📘 Overview

The **Gurugram Real Estate Explorer App** is an interactive data science web app built with **Streamlit**, offering an intuitive way to analyze, visualize, and predict **property prices** across **Gurugram’s residential sectors**.

It combines **data-driven insights**, **rich geospatial visualizations**, and **machine learning models** to help users explore the housing market — from local price densities to predictive analytics.

---

## 🚀 Key Features

### 🧭 **1. Interactive Data Exploration**
* Explore flats across **Gurgaon sectors and localities**
* Filter by **furnishing**, **parking** and **amenities**
* Dynamic **boxplots, bar charts, and density plots** powered by Plotly

### 💰 **2. Price Density Analytics**
* Visualizes **Median Price Density (₹/sq.ft)** for each locality
* Understand **floor-rise premiums**, **builder effects**, and **neighborhood price clusters**
* Supports **sector-wise comparison** and **area segmentation**

### 🧠 **3. Machine Learning Price Prediction**
* Built and optimized using **XGBoost Regressor**
* Features include: `Area`, `Sector`, `Furnishing`, `Parking`, etc.
* Handles categorical + numerical data using a **custom feature engineering pipeline**
* Supports **real-time price predictions** in the app.

### 🗺️ **4. Map-Based Visual Insights**
* Interactive **Folium + OpenStreetMap** visualization of listings
* Sector and amenity markers with tooltips for each sector

### 📊 **5. Business-Level Insights**
* Highlights **hot sectors**, **premium projects**, and **affordable zones**

---

## 🧩 Tech Stack

| Category             | Tools / Libraries              |
| -------------------- | ------------------------------ |
| **Language**         | Python 3.9+                    |
| **Web Framework**    | Streamlit                      |
| **Visualization**    | Plotly, Folium, Matplotlib     |
| **Machine Learning** | XGBoost, Scikit-learn, Optuna  |
| **Data Processing**  | Pandas, NumPy                  |
| **Deployment**       | Streamlit Cloud / GitHub Pages |
| **Version Control**  | Git + GitHub                   |


---

## ⚙️ Installation & Setup

### 🔸 Clone the repository

```bash
git clone https://github.com/yourusername/Gurugram-RealEstate-Explorer.git
cd Gurugram-RealEstate-Explorer
```

### 🔸 Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate   # (Linux/Mac)
venv\Scripts\activate      # (Windows)
```

### 🔸 Install dependencies

```bash
pip install -r requirements.txt
```

### 🔸 Run the Streamlit app

```bash
streamlit run gurgaon_app.py
```

---

## 🧠 Model Insights

The ML pipeline uses **feature engineering** + **XGBoost optimization via Optuna**.
Key learnings:

* Price strongly depends on **locality density**, **floor-rise premium**, and **furnishing status**
* Incorporating **Median Price Density (MPD)** as a spatial feature improved performance significantly
* Achieved an **R² score of ~0.90** on test data

---

## **📸 Application Screenshots**

### **`Home Page`**
<img width="1918" height="829" alt="image" src="https://github.com/user-attachments/assets/8701d978-07bd-4158-b418-6cf69d1cad1e" /> 

### **`Analytics Page`**
<img width="1919" height="807" alt="image" src="https://github.com/user-attachments/assets/2b2e585c-1be5-453e-8c0a-2a00bae768ed" /> 

### **`Prediction Page`**
<img width="1919" height="787" alt="image" src="https://github.com/user-attachments/assets/0c5ce13a-61a6-4ee2-ba24-3a9301c27c99" /> |

---

## 📬 Contact

👤 **Vishal Mandrai**
📧 [vishalm.nitt@gmail.com](mailto:vishalm.nitt@gmail.com)
🔗 [LinkedIn](https://linkedin.com/in/vishal-mandrai999/)
💻 [GitHub](https://github.com/vishalmandrai)

---
---
