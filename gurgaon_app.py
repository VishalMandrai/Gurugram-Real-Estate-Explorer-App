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


# ----------------------------------------------- Page layout functions -------------------------------------------
def home_page():
    ## Title of Page: 
    st.markdown(
        "<h1 style='text-align: center; color: white;'>🏡 Gurugram Real Estate Explorer</h1>",
        unsafe_allow_html=True)
    
    ## About the project:
    st.markdown(
        """
        <div style="background-color:rgba(61, 213, 109, 0.2); padding:12px; 
        border-radius:8px; text-align:center;">
        <p style="color:#D6EAF8; font-size:20px; font-weight:600; margin:0;">
        This platform brings together an <b>Analytics Module</b>, <b>Insights Dashboard</b>, <b>Price Prediction engine</b>, and a Smart <b>Flat Recommendation System</b> to help you explore properties with ease.</p>
        </div>
        """, unsafe_allow_html=True)
    st.markdown("")

    
    ## Project for:------------------------------------------------------------------------------------------------
    st.markdown(
        """
        <div style="background-color:#16324F; padding:5px; border-radius:8px; text-align:center;">
        <p style="color:#ffffff; font-size:30px; font-weight:600; margin:0;">
        ALL IN ONE APP FOR
        </p></div>
        """, unsafe_allow_html=True)
    
    st.markdown("")

    col1, col2, col3, col4 = st.columns(4)    ## Creating 4 side-by-side sections...
    for section, app_user in zip([col1, col2, col3, col4], 
                                 ['BUYERS', 'DEVELOPERS', 'INVESTORS','POLICY MAKERS']):
        with section:  ## Now we'll use context manager ('with') to access these sections
            st.markdown(
            f"""
            <div style="background-color:#EB9642; padding:5px; border-radius:8px; text-align:center;">
            <p style="color:#000000; font-size:24px; font-weight:600; margin:0; 
            font-weight:bold;">{app_user}</p>
            </div>
            """, unsafe_allow_html=True)


    
    ## Project Introductory Content: ----------------------------------------------------------------------------
    col1, col2 = st.columns([7,3])
    with col1:
        st.markdown(
            """
            <style>
            .big-font {
                font-size:20px !important;
                font-weight:100 !important;
                color: #FFFFFF !important; 
                line-height: 1.28 !important;
                font-family: calibri !important;}
            
            .med-font {
                font-size:20px !important;
                font-weight:80 !important;
                color: #FFFFFF !important; 
                line-height: 1.28 !important;
                font-family: calibri !important;}
            </style>
            
            <div class="big-font">
            <br><span style="font-size:28px; font-weight:bold; color:#50FAA0; font-family: calibri !important;">Gurugram</span> is <b>no longer</b> just a satellite extension to Delhi — it has become a 
                <b>fully-fledged real estate powerhouse</b> driven by: 
                <ul>
                    <li class="med-font"><b>Robust Public Infrastructure</b></li>
                    <li class="med-font"><b>Evolving Demand</b></li>
                    <li class="med-font"><b>Strategic Policy Shifts</b></li>
                </ul>
            </div>
            
            <p class="med-font">
            Over the past few years the city has witnessed <b>major connectivity feats</b> such as the <b>operationalization of Dwarka Expressway</b>, <b>expansions in metro links</b>, and <b>renewed focus on expressways and corridors</b> that bind Gurugram more tightly to <b>Delhi/NCR</b> 28nd the IGI Airport</b>. These <b>developments have reshaped</b> the geography of <b>demand</b>, <b>pushing property values sharply</b> along key corridors while opening up peripheral sectors for medium-to-long-term growth. </p>
            """, unsafe_allow_html=True)

    ## Features: --------------------------------------------------------------------------------------------------
    with col2:
        st.markdown("<br><br>", unsafe_allow_html=True)
        for feature, link in zip(['PRICE PREDICTION MODEL', 'RECOMMENDATION ENGINE', 'MARKET DASHBOARDS'],
                                ["price_pred", "rec_mod", "insights_mod"]):
            st.markdown(
            f"""
            <div style="background-color:#659FD6; padding:5px; border-radius:8px; text-align:center;">
            <p style="color:#000000; font-size:24px; font-weight:600; margin:0; 
            font-weight:bold;">
            <a href="/{link}" target="_self" style="all:unset; cursor: pointer;">{feature}</a></p>
            </div>
            <div><br></div>
            """, unsafe_allow_html=True)

    ## Rest of the content continues...
    st.markdown(
        """
        <style>
        .big-font {
            font-size:20px !important;
            font-weight:100 !important;
            color: #FFFFFF !important; 
            line-height: 1.28 !important;
            font-family: calibri !important;}
        
        .med-font {
            font-size:20px !important;
            font-weight:80 !important;
            color: #FFFFFF !important; 
            line-height: 1.28 !important;
            font-family: calibri !important;}
        </style>
        
        <div>
        <p class="med-font">For <span style="font-size:28px; font-weight:bold; color:#27F5EB; font-family: calibri !important;">HOME BUYERS</span>, <b>affordability has become a moving target</b>. Homes in newly connected sectors that offer value are pushing up prices even in mid-segments. <b>Buyers now expect more:</b> </p>
        <ul>
        <li class="med-font"><b>Wellness Amenities</b>,</li>
        <li class="med-font"><b>Green/open Spaces</b>, and</li>
        <li class="med-font"><b>Mixed-use Townships</b>.</li>
        </ul>
        <p class="med-font"><b>Smart homes</b> are <b>no longer luxury add-ons</b> but baseline requirements. <b>Projects that combine lifestyle, access, and legal certainty</b> (thanks to regulations like RERA) are <b>winning trust</b>. </p>
        </div>

        <div>
        <p class="med-font"><span style="font-size:28px; font-weight:bold; color:#DAF527; font-family: calibri !important;">DEVELOPERS</span> are <b>navigating both opportunity and risk</b>.</p>
        <ul>
        <li class="med-font">On one hand, well-located land, favourable policies, and strong demand in luxury, premium, and mid-housing segments offer <b>high capital appreciation</b>, especially in posh zones.</li>
        <li class="med-font"> On the other hand, rising input costs, stricter regulatory oversight, and growing expectations for sustainability and public infrastructure place <b>pressure on margins and timelines</b>.</li>
        </ul>
        <p class="med-font"><b>To succeed</b>, developers need to <b>shift towards</b> — <b>integrated townships</b>, <b>mixed use projects</b>, and <b>more transparent project disclosures</b>.</p>
        </div>

        <div>
        <p class="med-font">
        <span style="font-size:28px; font-weight:bold; color:#F0C781; font-family: calibri !important;">INVESTORS</span> see Gurugram as a <b>fertile ground for</b> both <b>Income Yield</b> and <b>Capital Appreciation</b>. <b>Rental demand</b> remains strong <b>driven by</b> &mdash; <i><b>Corporates</b></i>, <i><b>Millennials</b></i>, and <i><b>NRIs</b></i>, especially for premium apartments and office-spaces. Recent trends show that property prices along strategic corridors (e.g. Dwarka Expressway) have nearly doubled in recent years, with projections of <b>further growth of ~15-20%</b> in near term, <b>depending on infrastructure rollout</b>. </p>
        
        <p class="med-font">But <b>risks include</b> <b>over-supply in certain sectors</b>, <b>regulatory delays</b>, and <b>affordability bottlenecks</b> which <i><b>might slow absorption rates</b></i>.</p>
        </div>

        <div>
        <p class="med-font">For <span style="font-size:28px; font-weight:bold; color:#418EFA; font-family: calibri !important;">POLICY MAKERS</span>, Gurugram <b>offers a template of <i>high growth</i></b>, but <b>also a mandate to guide that growth <i>sustainably and equitably</i></b>. Key levers include &mdash;</p>
        <ul>
        <li class="med-font"><b>Regulating Policy Charges</b> like EDC to balance revenue for infrastructure with affordable access;</li>
        <li class="med-font"><b>Ensuring</b> that <b>connectivity infrastructure keeps pace with new launches</b>;</li>
        <li class="med-font"><b>Enforcing transparency and quality</b> via <b>legislation</b> (e.g. RERA, building norms, environmental rules);</li>
        <li class="med-font"><b>Planning</b> for inclusive housing so growth is not limited to only luxury/premium segments.</li>
        </ul>
        
        <p class="med-font"><b>With thoughtful policy alignment</b>, Gurugram can continue to be a leading city in <b>India’s real estate ecosystem</b> &mdash; one that appeals to all stakeholders.</p>
        </div>
        
        """,unsafe_allow_html=True)


## App Starts from here: ----------------------------------------------------------------------------------------

def main():
    ## Session State container for the app:
    if 'app_state' not in st.session_state:
        st.session_state['app_state'] = {}
    state = st.session_state['app_state']

    ## Sidebar Navigation:
    pages = {"MENU" : 
                   [st.Page(home_page, title="🏗️ Home")],
             "Analytic Dashboards":
                    [st.Page("navigation_pages/analytic_mod.py", 
                            title="📊 Know the Market"),
                    st.Page("navigation_pages/insights_mod.py", title="💡 Insights Dashboard"),
                    st.Page("navigation_pages/know_sector.py", title="📍 Know the Sector")],
             "ML Models":
                    [st.Page("navigation_pages/price_pred.py", title="💰 Price Prediction Model"),
                    st.Page("navigation_pages/rec_mod.py", title="🎯 Recommendation Engine")],
             
             "MORE": [st.Page("navigation_pages/about_me.py", title="ℹ️ About Me")]}
    
    pg = st.navigation(pages)
    pg.run()

    ## Optional quick help & links:
    with st.sidebar:
        st.markdown( """
        <br>
        <div style="font-size: 18px;"><p>
        <a href="https://www.linkedin.com/in/vishal-mandrai999/" target="_blank" style="
          text-decoration:none;
          background-color:#080707;
          border: 1.1px solid #ffffff;
          color:white;
          font-weight:400;
          padding:4px 8px;
          border-radius:6px;">
          in</a> : <a href="https://www.linkedin.com/in/vishal-mandrai999/" target="_blank"
          style="all:unset; cursor: pointer; font-family: calibiri;">
        vishalmandrai </a>        
        </p></div>

        <div style="font-size: 18px;">
        <a href="mailto:vishalm.nitt@gmail.com" style="
          text-decoration:none;
          background-color:#080707;
          border: 1.1px solid #ffffff;
          padding:4px 6px;
          border-radius:6px;
          color:#fff;
          font-weight:400;">
          ✉︎</a> : <a href="mailto:vishalm.nitt@gmail.com"
          style="all:unset; cursor: pointer; font-family: calibiri;">
        mailto:vishalmandrai </a>        
        </div>
        """, unsafe_allow_html=True)

    
    #st.sidebar.info("Add some info about using the App properly!")



if __name__ == '__main__':
    main()


