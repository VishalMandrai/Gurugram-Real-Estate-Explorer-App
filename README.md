# **🏙️ Gurugram Real Estate Explorer - App**

### 🔍 **An Interactive Data Science App that provides an Analytics Module, Insights Dashboard, Price Prediction Engine, and a Smart Flat Recommendation System to help explore the Gurugram Real Estate landscape with ease.**

![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit)
![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python)
![Plotly](https://img.shields.io/badge/Plotly-Interactive%20Charts-lightblue?logo=plotly)
![XGBoost](https://img.shields.io/badge/XGBoost-Model-green?logo=xgboost)
![License](https://img.shields.io/badge/License-MIT-orange)

---

## 📘 Overview

The **Gurugram Real Estate Explorer App** is an interactive data science web app built with **Streamlit**, offering an intuitive way to analyze, visualize, and predict **property prices** across **Gurugram’s residential sectors**.

It combines **data-driven insights**, **rich geospatial visualizations**, and **machine learning models** to help users explore the housing market — from local price densities to predictive analytics.

---

## 🚀 Key Features

### 🧭 **1. Interactive Data Exploration**

* Explore flats across **Gurgaon sectors and localities**
* Filter by **furnishing**, **parking**, **amenities**, and **seller type**
* Dynamic **boxplots, bar charts, and density plots** powered by Plotly

### 💰 **2. Price Density Analytics**

* Visualizes **Median Price Density (₹/sq.ft)** for each locality
* Understand **floor-rise premiums**, **builder effects**, and **neighborhood price clusters**
* Supports **sector-wise comparison** and **area segmentation**

### 🧠 **3. Machine Learning Price Prediction**

* Built and optimized using **XGBoost Regressor**
* Features include: `Area`, `Sector`, `Furnishing`, `EMI`, `Parking`, etc.
* Handles categorical + numerical data using a **custom feature engineering pipeline**
* Supports **real-time price predictions** in the app

### 🗺️ **4. Map-Based Visual Insights**

* Interactive **Folium + OpenStreetMap** visualization of listings
* Sector boundaries and property markers with tooltips for price and area

### 📊 **5. Business-Level Insights**

* Highlights **hot sectors**, **premium projects**, and **affordable zones**
* Detects **overpriced** or **underpriced** properties using density comparisons

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

## 🏗️ Project Structure

```
Gurugram_RealEstate_Explorer/
│
├── 📁 data/                     # Cleaned and processed datasets (hidden or private)
├── 📁 pages/                    # Multi-page Streamlit structure
│   ├── 1_🏙️_Overview.py
│   ├── 2_📊_Price_Density_Analysis.py
│   ├── 3_🧠_Price_Prediction.py
│   ├── 4_🗺️_Map_Explorer.py
│
├── 📁 models/                   # ML model and pipeline
│   ├── trained_xgb_model.pkl
│   ├── pipeline.pkl
│
├── app.py                       # Main entry point for Streamlit
├── requirements.txt             # Dependencies
├── README.md                    # You are here
└── .gitignore                   # To hide data and model files
```

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
streamlit run app.py
```

---

## 🔐 Data Privacy

The raw property dataset used in this project is **not included in the public repository** for privacy reasons.
If you wish to explore or contribute, please contact the maintainer for access or use mock data available in the `sample_data/` directory.

---

## 🧠 Model Insights

The ML pipeline uses **feature engineering** + **XGBoost optimization via Optuna**.
Key learnings:

* Price strongly depends on **locality density**, **floor-rise premium**, and **furnishing status**
* Incorporating **Median Price Density (MPD)** as a spatial feature improved performance significantly
* Achieved an **R² score of ~0.87** on test data

---

## 📸 Screenshots (optional placeholders)

| Home Page                | Analytics Page                     | Prediction Page                      |
| ------------------------ | ---------------------------------- | ------------------------------------ |
| ![Home](assets/home.png) | ![Analytics](assets/analytics.png) | ![Prediction](assets/prediction.png) |

---

## 📬 Contact

👤 **Vishal Mandrai**
📧 [vishal.mandrai@gmail.com](mailto:vishal.mandrai@gmail.com)
🔗 [LinkedIn](https://linkedin.com/in/vishalmandrai)
💻 [GitHub](https://github.com/vishalmandrai)

---

## 🏁 Future Enhancements

* ✅ Add live price updates from real estate APIs
* ✅ Integrate Google Maps and heatmaps
* 🔜 Time-series price trend analysis
* 🔜 Model explainability with SHAP

---

## 📝 License

This project is licensed under the [MIT License](LICENSE).

---

Would you like me to generate a **second version of this README with emoji-rich formatting and GitHub markdown styling (colored titles, badges, table design)** — optimized for visual impact on your GitHub profile?




