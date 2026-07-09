##                                    Streamlit App - Gurgaon Real Estate Explorer
## Importing necessary tools:
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from io import StringIO
import sys

## ------------------------------------------------------------------------------------------------------------
## Custom Transformer Class: saved in a module "Custom_transformer" to support "Prediction Model Pipeline" 

from sklearn.base import BaseEstimator, TransformerMixin         ## for creating Custom Transformer Class...

## Custom Transformer Class for Adding new feature to Data:       ## Used in Pipeline....
class Sector_Locality_PD_Adder(BaseEstimator, TransformerMixin):
    def __init__(self):
        self.PD_records = None

    def fit(self, X, y=None):
        X = X.copy()   
        ## We are creating Historical Median Price Density Records from Property data: 
        self.PD_records = X.groupby(by = 'Sector_Locality').agg({'Avg_price_rupee_per_sqft': 'median'
                                                                  }).to_dict()['Avg_price_rupee_per_sqft']
        return self

    def transform(self, X):
        X = X.copy()   
        values = X['Sector_Locality'].replace(self.PD_records)   ## Using saved records...

        ## Creating a new feature with name "Sector_Locality_Price_Density" in X:
        X.insert(4, "Sector_Locality_Price_Density", values, allow_duplicates = False)
        
        ## Removing "Avg_price_rupee_per_sqft" from X as it can potentially cause Data Leakage:
        X = X[['Flat', 'Sector_Locality', 'Locality', 'Built_up_area_in_sqft', 'Sector_Locality_Price_Density', 
               'Age_Category', 'Floor_Category', 'Building_Height_Category', 'Furnishing', 'Bedrooms', 'Bathrooms', 
               'Covered_parking', 'Open_parking', 'Balcony', 'Sector_Amenity_Score']]
        
        return X

    def fit_transform(self, X, y=None, **fit_params):
        self.fit(X, y, **fit_params)
        return self.transform(X)

## -----------------------------------------------------------------------------------------------------------------


## Setting Page Configuration:
st.set_page_config(page_title="Gurugram Real Estate", layout='wide', page_icon='🏡', 
                   initial_sidebar_state="expanded",
                   menu_items={                                ## customize Streamlit’s hamburger menu
                        'Get Help': 'https://docs.streamlit.io/',
                        'Report a bug': "https://github.com/streamlit/streamlit/issues",
                        'About': "# 🏡 Gurugram Real Estate Explorer App\nWeb-App built with Streamlit"})

st.markdown(    ## Changing width of Sidebar Window...
    """
    <style>
    /* (Optional) Move the main content a bit to fit correctly in some setups */
    div.block-container {padding-left: 3rem !important;
                         padding-right: 3rem !important;
    /* tweak if content overlaps or you want more space */ }
    </style>
    """, unsafe_allow_html=True )


st.markdown(    ## Reduce the top margin padding...
    """<style>
    /* Reduce the top space above the title/content */
    div.block-container {padding-top: 0.5rem;   /* default ~6rem, reduce it */}
    </style>
    """, unsafe_allow_html=True)


page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background: #080707;}
[data-testid="stHeader"] {
    background: rgba(0,0,0,0);  /* transparent header */}
[data-testid="stSidebar"] {
    background-color: rgba(1,1,1,1); /* optional: white semi-transparent sidebar */
} </style>
"""

st.markdown(page_bg, unsafe_allow_html=True)   ## Changing BG color and styling...



## App Starts from here: ----------------------------------------------------------------------------------------

def main():
    ## Session State container for the app:
    if 'app_state' not in st.session_state:
        st.session_state['app_state'] = {}
    state = st.session_state['app_state']

    ## Sidebar Navigation:
    pages = {"MENU" : 
                   [st.Page("navigation_pages/home_page.py", 
                            title="🏗️ Home")],
             "Analytic Dashboards":
                    [st.Page("navigation_pages/analytic_mod.py", 
                            title="📊 Know the Market"),
                    st.Page("navigation_pages/insights_mod.py", title="💡 Insights Dashboard"),
                    st.Page("navigation_pages/know_sector.py", title="📍 Know the Sector")],
             "ML Models":
                    [st.Page("navigation_pages/price_pred.py", title="💰 Price Prediction Model"),
                    st.Page("navigation_pages/rec_mod.py", title="🎯 Recommendation Engine")],
             
             "MORE": [st.Page("navigation_pages/about_me.py", title="ℹ️ About")]}
    
    pg = st.navigation(pages)
    pg.run()

    ## Optional quick help & links:
    with st.sidebar:
        st.markdown(
        """
        <div style="display: flex; flex-wrap: wrap; gap: 10px; justify-content: center; margin-top: 5px;">
            <!-- Mail Button -->
            <a href="mailto:your.vishalm.nitt@gmail.com" aria-label="Email"
            style="background: #121111; border: 1px solid #FBF3EA ; color: #FBF3EA; 
                    display: inline-flex; align-items: center; justify-content: center; gap: 10px; 
                    padding: 5px 10px; border-radius: 5px; font-family: calibri, sans-serif; 
                    font-size: 16px; letter-spacing: 0.1em; 
                    font-weight: 800; text-decoration: none; transition: all 0.3s ease;">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="#BF2626" stroke="#E8CFCF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="flex-shrink: 0;">
                    <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/>
                    <polyline points="22,6 12,13 2,6"/>
                </svg>
            </a>
            <!-- GitHub Button -->
            <a href="https://github.com/VishalMandrai" target="_blank" rel="noopener" aria-label="GitHub"
            style="background: #121111; border: 1px solid #FBF3EA; color: #FBF3EA; 
                    display: inline-flex; align-items: center; justify-content: center; gap: 2px; 
                    padding: 5px 10px; border-radius: 5px; font-family: calibri, sans-serif; 
                    font-size: 16px; letter-spacing: 0.1em; 
                    font-weight: 800; text-decoration: none; transition: all 0.3s ease;">
                <svg width="22" height="22" viewBox="0 0 23 23" fill="#ffffff" aria-hidden="true" style="flex-shrink: 0;">
                    <path d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466 -.908-.62.069-.608.069-.608 1.003.07 1.531 1.032 1.531 1.032.892 1.53 2.341 1.088 2.91.832 .092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688 -.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0 1 12 6.844 a9.59 9.59 0 0 1 2.504.337c1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651 .64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.02 10.02 0 0 0 22 12.017 C22 6.484 17.522 2 12 2Z" />
                </svg>
            </a>
            <!-- LinkedIn Button -->
            <a href="https://www.linkedin.com/in/vishal-mandrai999/" target="_blank" rel="noopener" aria-label="LinkedIn"
            style="background: #121111; border: 1px solid #FBF3EA; color: #FBF3EA; 
                    display: inline-flex; align-items: center; justify-content: center; gap: 10px; 
                    padding: 5px 10px; border-radius: 5px; font-family: calibri, sans-serif; 
                    font-size: 16px; letter-spacing: 0.1em; 
                    font-weight: 800; text-decoration: none; transition: all 0.3s ease;">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="#25A3E8" aria-hidden="true" style="flex-shrink: 0;">
                    <path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286ZM5.337 7.433a2.062 2.062 0 0 1-2.063-2.065 2.064 2.064 0 1 1 2.063 2.065Zm1.782 13.019H3.555V9h3.564v11.452ZM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003Z"/>
                </svg>
            </a>
            <!-- X / Twitter Button -->
            <a href="https://x.com/vishman__" target="_blank" rel="noopener" aria-label="X / Twitter"
            style="background: #121111; border: 1px solid #FBF3EA; color: #FBF3EA; 
                    display: inline-flex; align-items: center; justify-content: center; gap: 10px; 
                    padding: 5px 10px; border-radius: 5px; font-family: calibri, sans-serif; 
                    font-size: 16px; letter-spacing: 0.1em; 
                    font-weight: 800; text-decoration: none; transition: all 0.3s ease;">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true" style="flex-shrink: 0;">
                    <path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-4.714-6.231-5.401 6.231H2.746 l7.73-8.835L1.254 2.25H8.08l4.713 6.231 5.45-6.231Zm-1.161 17.52h1.833L7.084 4.126 H5.117L17.083 19.77Z"/>
                </svg>
            </a>
            <!-- Portfolio Button -->
            <a href="https://www.vishalm.online" target="_blank" rel="noopener" aria-label="Portfolio website"
            style="background: #121111; border: 1px solid #FBF3EA; color: #FBF3EA; 
                    display: inline-flex; align-items: center; justify-content: center; gap: 10px; 
                    padding: 5px 10px; border-radius: 5px; font-family: calibri, sans-serif; 
                    font-size: 16px; letter-spacing: 0.1em; 
                    font-weight: 800; text-decoration: none; transition: all 0.3s ease;">
                <span style="margin-left: 2px;">My Website</span>
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#D9FA6E" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="flex-shrink: 0;">
                    <circle cx="12" cy="12" r="10"/>
                    <line x1="2" y1="12" x2="22" y2="12"/>
                    <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/>
                </svg>
            </a>
        </div>
        """, 
        unsafe_allow_html=True
    )
     
    
    #st.sidebar.info("Add some info about using the App properly!")



if __name__ == '__main__':
    main()


