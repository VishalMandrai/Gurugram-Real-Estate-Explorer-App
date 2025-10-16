
<img width="878" height="115" alt="Github_readme_title_banner" src="https://github.com/user-attachments/assets/71c23815-cf94-4048-8ef9-90ef5f2c3657" href="https://gurugram-real-estate-explorer.streamlit.app/" />


#### 🔍 An Interactive Data Science App designed for **Homebuyers, Investors, Developers, and Policy makers** to explore the real estate dynamics of Gurugram with ease. Built on the latest data from leading housing platforms, this app serves both as a **market snapshot** and a **tool for in-depth analysis**.

> **NOTE:** Although not a substitute for professional consulting, this tool utilizes the **latest property data** to provide intelligent, data-driven insights — powerful enough to support informed decision-making.

![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit)
![NumPy](https://img.shields.io/badge/NumPy-Numerical%20Computing-orange?logo=numpy)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Data%20Visualization-yellow?logo=matplotlib)
![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20Plots-teal?logo=seaborn)
![Plotly](https://img.shields.io/badge/Plotly-Interactive%20Charts-lightblue?logo=plotly)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML%20Library-orange?logo=scikit-learn)
![XGBoost](https://img.shields.io/badge/XGBoost-Model-green?logo=xgboost)
![Folium](https://img.shields.io/badge/Folium-Interactive%20Maps-lightblue?logo=python)
![OpenStreetMap](https://img.shields.io/badge/OpenStreetMap-GeoData-green?logo=openstreetmap)



---

## **📘 OVERVIEW [🔗](https://gurugram-real-estate-explorer.streamlit.app/)**
The **Gurugram Real Estate Explorer App** is a comprehensive **Streamlit-based web application** designed to help **home buyers, real estate investors, developers, and policymakers** explore the Gurugram property market in depth. The app combines interactive analytics, predictive modeling, and recommendation systems to provide actionable insights based on the latest property data.


## **🚀 KEY FEATURES**

### **`I.` `🧭 Market Analytics & Insights:`**
  * **Dedicated Tabs:**
    * **Market Analytics:** Provides a broad overview of the Gurugram real estate market.
    * **Market Insights:** Highlights key price drivers and interesting trends across Gurugram.
  * **Interactive Visualizations** — Uses for interactive maps and plots. Map-based visualizations mark Sectors and Locality boundaries.
  * **Market Analytics Tab:**
    * Gives a **bird’s-eye view** of pricing, property specifications, sector-wise and locality-wise comparisons.
    * Helps identify patterns across flat types, building heights, furnishing status, parking availability, and more.
  * **Market Insights Tab:**
    * Explains **price drivers** and critical factors influencing property values.
    * Provides **crisp textual insights** alongside interactive charts for quick and informed reading.
    * Helps users, investors, and policy makers quickly understand key trends and make data-driven observations.
  * **Purpose:**
    * Allows users to **explore the Gurugram real estate market** from multiple angles — both visually and analytically.
    * Supports both **detailed research** and **quick market checks** through an intuitive dashboard.


### **`II.` `🗺️ Sector Explorer:`**
  * **Dedicated Tab:** Provides a focused interface to **explore individual Sectors** of Gurugram.
  * **Interactive Map:** Displays the selected sector with **sector amenities**, and **rough sector boundaries**.
  * **Property Overview:** Shows available properties in the sector with **types, pricing, and distribution**.
  * **Sector Segmentation:** Highlights the **Affordability Segment** of the sector using **Sector Median Price Density**.
  * **Wordcloud Insights:** Names **Societies and Active Developers** in the sector through intuitive wordcloud visualizations.
  * **Purpose:**
    * Helps users gather **key, actionable information** about a sector, including pricing trends, amenities, property types, and developers — all in one place for quick reference or detailed study.


### **`III.` `💰 Price Prediction:`**
  * **Robust Regression Model:** Predicts a **price range** for a property based on specifications provided by the user.
  * **Deployed Model:** Uses a **Bayesian-optimized XGBoost Regressor**, selected after rigorous testing against multiple models, including various **Linear models, Bagging, and Boosting models**.
  * **Model Performance:**
    * **Test R²:** **`0.92`**
    * **Train R²:** **`0.95`**
    * **MAE:** **`~ ₹30 Lakh`**
  * **Input Features:** Accepts key property specifications such as **flat type, built-up area, bedrooms, bathrooms, floor, locality, and amenity score**.
  * **Purpose:** Provides **reliable, data-driven price estimates**, assisting buyers, investors, and developers in assessing property values quickly and confidently.


### **`IV.` `📊 Society Recommendation Engine:`**
  * **Content-based Filtering:** Suggests the **Top 10 most Similar Societies** based on multiple factors.
  * **Key Considerations:**
    * **Property Pricing** (highest priority)
    * **Nearby Locations** (high priority)
    * **Societal Amenities** (lower priority)
  * **Weighted Recommendation:** Combines **three separate recommendation modules** into a single, unified engine using weighted priorities.
  * **Property Listings:** Displays available properties in the recommended societies, including **pricing, property type, and actionable links**.
  * **Robust & Manually Tested:** The engine was **manually tested** and found to be **reliable, practical, and useful** for home buyers, investors, and developers.
  * **Purpose:** Helps users quickly **discover similar societies**, compare properties, and make **data-driven location decisions**.

Built on the latest data from major housing platforms, the app serves both as a **quick market reference** and a **deep-dive analytical tool**, allowing users to study trends, compare localities, and make informed property-related decisions.

### **Live App Link:** [Gurugram Real Estate Explorer](https://gurugram-real-estate-explorer.streamlit.app/)


---


## **🧩 TECH STACK**

| ✨ Category             | 🤖 Tools / Libraries              |
| -------------------- | ------------------------------ |
| **Language**         | Python 3.9+                    |
| **Web Framework**    | Streamlit                      |
| **Visualization**    | Plotly, Folium, Matplotlib     |
| **Machine Learning** | XGBoost, Scikit-learn, Optuna  |
| **Data Processing**  | Pandas, NumPy                  |
| **Deployment**       | Streamlit Cloud / GitHub Pages |
| **Version Control**  | Git + GitHub                   |


---
<br>

## **⚙️ Installation & Setup**

### 🔸 Clone the repository

```bash
git clone https://github.com/VishalMandrai/Gurugram-Real-Estate-Explorer-App.git
cd Gurugram-Real-Estate-Explorer-App
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
<br>


## **🧠 Model Insights**

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

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
*/ # **🏙️ Gurugram Real Estate Explorer - App**  /*

Here’s a clear set of pointers you can add for the **Market Analytics & Insights** feature in your README:

---

### Market Analytics & Insights



---

If you want, I can also write similar **pointers for the Sector Explorer, Price Prediction, and Society Recommendation Engine** sections so all app features are described uniformly in your README. Do you want me to do that next?
 



---
---
