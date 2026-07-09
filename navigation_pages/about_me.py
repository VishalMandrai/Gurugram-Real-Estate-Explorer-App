import streamlit as st

# ------------------------- Page layout functions -------------------------
def page_content():
    ## Title of Page:
    st.markdown(
        """<h1 style='text-align: center; color: white;'> 
        🏡 Gurugram Real Estate Explorer App
        </h1>""",
        unsafe_allow_html=True)
    
    ## Analytics Module heading in the box:
    st.markdown(
        """<div style="background-color:#EDDD68; padding:3px; 
        border-radius:5px; text-align:center;"></div>
        
        """, unsafe_allow_html=True)


## ------------------------------------------------------------------------------------------
## ------------------------------------------------------------------------------------------


def overview():
    ## Quick Overview:
    st.markdown("""
    <div style="line-height: 1.3;">
    <p style="color:#ffffff; font-size:22px; font-weight:50;font-family: calibri; margin:0;">
    The <strong>Gurugram Real Estate Explorer App</strong> is a comprehensive <strong>streamlit-based web application</strong> designed to help <strong>home buyers, real estate investors, developers, and policymakers</strong> explore the Gurugram property market in depth. The app combines interactive analytics, predictive modeling, and recommendation systems to provide actionable insights based on the latest property data.
    </p></div>
    """, unsafe_allow_html=True)
    
    ## User Warning:
    st.markdown("""
    <br>
    <div style="line-height: 1.3; background-color:#121111; padding:5px; 
        border-radius:5px; text-align:center;">
    <p style="color:#ffffff; font-size:20px; font-weight:50;font-family: calibri; margin:0;">
    <strong>NOTE:</strong> Although <strong>not a substitute for professional consulting</strong>, this tool utilizes the <strong>latest property data</strong> to provide intelligent, data-driven insights — powerful enough to support informed decision-making.
    <br>
    </p></div>
    """, unsafe_allow_html=True)
    
    ## Tech Stack Tags:
    st.markdown(
        """
        <br>
        <div style="background-color:#121111; padding:5px; 
        border-radius:5px; text-align:center;">
        <img src="https://img.shields.io/badge/Python-3.9+-blue?logo=python" alt="Python">
        <img src="https://img.shields.io/badge/Streamlit-App-red?logo=streamlit" alt="Streamlit">
        <img src="https://img.shields.io/badge/NumPy-Numerical%20Computing-orange?logo=numpy" alt="NumPy">
        <img src="https://img.shields.io/badge/Matplotlib-Data%20Visualization-yellow?logo=matplotlib" alt="Matplotlib">
        <img src="https://img.shields.io/badge/Seaborn-Statistical%20Plots-teal?logo=seaborn" alt="Seaborn">
        <img src="https://img.shields.io/badge/Plotly-Interactive%20Charts-lightblue?logo=plotly" alt="Plotly">
        <img src="https://img.shields.io/badge/Scikit--learn-ML%20Library-orange?logo=scikit-learn" alt="Scikit-learn">
        <img src="https://img.shields.io/badge/XGBoost-Model-green?logo=xgboost" alt="XGBoost">
        <img src="https://img.shields.io/badge/Folium-Interactive%20Maps-lightblue?logo=python" alt="Folium">
        <img src="https://img.shields.io/badge/OpenStreetMap-GeoData-green?logo=openstreetmap" alt="OpenStreetMap">
        </div
        """, unsafe_allow_html=True)


## ------------------------------------------------------------------------------------------
## ------------------------------------------------------------------------------------------


def features():
    st.markdown("""
        <div style="font-family: calibri; line-height: 1.3; margin-top: 25px;">

        <!-- Main Header -->
        <h2 style="font-size: 28px; color: #ffffff; border-bottom: 2px solid #edf2f7; padding-bottom: 12px; margin-top: 0; margin-bottom: 24px; font-weight: 700;">
            🚀 KEY FEATURES
        </h2>

        <!-- Feature Section -->
        <div style="margin-bottom: 20px;">
            <h3 style="font-size: 20px; color: #000000; margin-bottom: 15px; font-weight: 900;">
                <code style="background-color: #ebf8ff; color: #2d3748; padding: 4px 8px; border-radius: 4px; font-family: monospace; font-size: 22px; font-weight: 900; margin-right: 5px;">I.</code> 
                <code style="background-color: #f7fafc; color: #2d3748; padding: 4px 8px; border-radius: 4px; font-family: monospace; font-size: 22px; font-weight: 900;">🧭 Market Analytics & Insights:</code>
            </h3>
        <div style="color:#ffffff; font-size:20px; font-weight:50;font-family: calibri; margin: 0px;">
        <ul style="list-style-type: none; padding-left: 0; margin: 0;">
            <!-- Bullet Point 1 -->
            <li style="margin-bottom: 12px; position: relative; padding-left: 20px;">
                <span style="position: absolute; left: 0; color: #4299e1;">•</span>
                <strong>Dedicated Tabs:</strong>
                <ul style="list-style-type: none; padding-left: 0; margin-top: 6px; margin-bottom: 6px;">
                    <li style="margin-bottom: 4px; position: relative; padding-left: 15px;">
                        <span style="position: absolute; left: 0; color: #718096;">-</span>
                        <strong>Market Analytics:</strong> Provides a broad overview of the Gurugram real estate market.
                    </li>
                    <li style="margin-bottom: 4px; position: relative; padding-left: 15px;">
                        <span style="position: absolute; left: 0; color: #718096;">-</span>
                        <strong>Market Insights:</strong> Highlights key price drivers and interesting trends across Gurugram.
                    </li>
                </ul>
            </li>
            <!-- Bullet Point 2 -->
            <li style="margin-bottom: 12px; position: relative; padding-left: 20px;">
            <span style="position: absolute; left: 0; color: #4299e1;">•</span>
            <strong>Interactive Visualizations</strong> — Uses for interactive maps and plots. Map-based visualizations mark Sectors and Locality boundaries.
            </li>
            <!-- Bullet Point 3 -->
            <li style="margin-bottom: 12px; position: relative; padding-left: 20px;">
                <span style="position: absolute; left: 0; color: #4299e1;">•</span>
                <strong>Market Analytics Tab:</strong>
                <ul style="list-style-type: none; padding-left: 0; margin-top: 6px; margin-bottom: 6px;">
                    <li style="margin-bottom: 4px; position: relative; padding-left: 15px;">
                        <span style="position: absolute; left: 0; color: #718096;">-</span>
                        Gives a <strong>bird’s-eye view</strong> of pricing, property specifications, sector-wise and locality-wise comparisons.
                    </li>
                    <li style="margin-bottom: 4px; position: relative; padding-left: 15px;">
                        <span style="position: absolute; left: 0; color: #718096;">-</span>
                        Helps identify patterns across flat types, building heights, furnishing status, parking availability, and more.
                    </li>
                </ul>
            </li>
            <!-- Bullet Point 4 -->
            <li style="margin-bottom: 12px; position: relative; padding-left: 20px;">
                <span style="position: absolute; left: 0; color: #4299e1;">•</span>
                <strong>Market Insights Tab:</strong>
                <ul style="list-style-type: none; padding-left: 0; margin-top: 6px; margin-bottom: 6px;">
                    <li style="margin-bottom: 4px; position: relative; padding-left: 15px;">
                        <span style="position: absolute; left: 0; color: #718096;">-</span>
                        Explains <strong>price drivers</strong> and critical factors influencing property values.
                    </li>
                    <li style="margin-bottom: 4px; position: relative; padding-left: 15px;">
                        <span style="position: absolute; left: 0; color: #718096;">-</span>
                        Provides <strong>crisp textual insights</strong> alongside interactive charts for quick and informed reading.
                    </li>
                    <li style="margin-bottom: 4px; position: relative; padding-left: 15px;">
                        <span style="position: absolute; left: 0; color: #718096;">-</span>
                        Helps users, investors, and policy makers quickly understand key trends and make data-driven observations.
                    </li>
                </ul>
            </li>
            <!-- Bullet Point 5 -->
            <li style="margin-bottom: 12px; position: relative; padding-left: 20px;">
                <span style="position: absolute; left: 0; color: #4299e1;">•</span>
                <strong>Purpose:</strong>
                <ul style="list-style-type: none; padding-left: 0; margin-top: 6px; margin-bottom: 6px;">
                    <li style="margin-bottom: 4px; position: relative; padding-left: 15px;">
                        <span style="position: absolute; left: 0; color: #718096;">-</span>
                        Allows users to <strong>explore the Gurugram real estate market</strong> from multiple angles — both visually and analytically.
                    </li>
                    <li style="margin-bottom: 4px; position: relative; padding-left: 15px;">
                        <span style="position: absolute; left: 0; color: #718096;">-</span>
                        Supports both <strong>detailed research</strong> and <strong>quick market checks</strong> through an intuitive dashboard.
                    </li>
                </ul>
            </li>
        </ul>
        </div>
        </div>
        </div>
        """, unsafe_allow_html=True)
    
    
    st.markdown("""
    <div style="font-family: calibri; line-height: 1.2; margin-top: 25px;">
    <!-- Feature Section II -->
    <div style="margin-bottom: 20px;">
        <h3 style="font-size: 20px; color: #000000; margin-bottom: 15px; font-weight: 900;">
            <code style="background-color: #ebf8ff; color: #2d3748; padding: 4px 8px; border-radius: 4px; font-family: monospace; font-size: 22px; font-weight: 900; margin-right: 5px;">II.</code> 
            <code style="background-color: #f7fafc; color: #2d3748; padding: 4px 8px; border-radius: 4px; font-family: monospace; font-size: 22px; font-weight: 900;">🗺️ Sector Explorer:</code>
        </h3>
        <div style="color:#ffffff; font-size:20px; font-weight:50; font-family: calibri; margin: 0;">
            <ul style="list-style-type: none; padding-left: 0; margin: 0;">
                <!-- Bullet Point 1 -->
                <li style="margin-bottom: 12px; position: relative; padding-left: 20px;">
                    <span style="position: absolute; left: 0; color: #4299e1;">•</span>
                    <strong>Dedicated Tab:</strong> Provides a focused interface to <b>explore individual Sectors</b> of Gurugram.
                </li>
                <!-- Bullet Point 2 -->
                <li style="margin-bottom: 12px; position: relative; padding-left: 20px;">
                    <span style="position: absolute; left: 0; color: #4299e1;">•</span>
                    <strong>Interactive Map:</strong> Displays the selected sector with <b>sector amenities</b>, and <b>rough sector boundaries</b>.
                </li>
                <!-- Bullet Point 3 -->
                <li style="margin-bottom: 12px; position: relative; padding-left: 20px;">
                    <span style="position: absolute; left: 0; color: #4299e1;">•</span>
                    <strong>Property Overview:</strong> Shows available properties in the sector with <b>types, pricing, and distribution</b>.
                </li>
                <!-- Bullet Point 4 -->
                <li style="margin-bottom: 12px; position: relative; padding-left: 20px;">
                    <span style="position: absolute; left: 0; color: #4299e1;">•</span>
                    <strong>Sector Segmentation:</strong> Highlights the <b>Affordability Segment</b> of the sector using <b>Sector Median Price Density</b>.
                </li>
                <!-- Bullet Point 5 -->
                <li style="margin-bottom: 12px; position: relative; padding-left: 20px;">
                    <span style="position: absolute; left: 0; color: #4299e1;">•</span>
                    <strong>Wordcloud Insights:</strong> Names <b>Societies and Active Developers</b> in the sector through intuitive wordcloud visualizations.
                </li>
                <!-- Bullet Point 6 (With Nested Purpose Items) -->
                <li style="margin-bottom: 12px; position: relative; padding-left: 20px;">
                    <span style="position: absolute; left: 0; color: #4299e1;">•</span>
                    <strong>Purpose:</strong>
                    <ul style="list-style-type: none; padding-left: 0; margin-top: 6px; margin-bottom: 6px;">
                        <li style="margin-bottom: 4px; position: relative; padding-left: 15px;">
                            <span style="position: absolute; left: 0; color: #718096;">-</span>
                            Helps users gather <b>key, actionable information</b> about a sector, including pricing trends, amenities, property types, and developers — all in one place for quick reference or detailed study.
                        </li>
                    </ul>
                </li>
            </ul>
        </div>
    </div>
    </div>
    """, unsafe_allow_html=True)

    
    st.markdown("""
    <div style="font-family: calibri; line-height: 1.3; margin-top: 25px;">
    <!-- Feature Section III -->
    <div style="margin-bottom: 20px;">
        <h3 style="font-size: 20px; color: #000000; margin-bottom: 15px; font-weight: 900;">
            <code style="background-color: #ebf8ff; color: #2d3748; padding: 4px 8px; border-radius: 4px; font-family: monospace; font-size: 22px; font-weight: 900; margin-right: 5px;">III.</code> 
            <code style="background-color: #f7fafc; color: #2d3748; padding: 4px 8px; border-radius: 4px; font-family: monospace; font-size: 22px; font-weight: 900;">💰 Price Prediction:</code>
        </h3>
        <div style="color:#ffffff; font-size:20px; font-weight:50; font-family: calibri; margin: 0px;">
            <ul style="list-style-type: none; padding-left: 0; margin: 0;">
                <!-- Bullet Point 1 -->
                <li style="margin-bottom: 12px; position: relative; padding-left: 20px;">
                    <span style="position: absolute; left: 0; color: #4299e1;">•</span>
                    <strong>Robust Regression Model:</strong> Predicts a <b>price range</b> for a property based on specifications provided by the user.
                </li>
                <!-- Bullet Point 2 -->
                <li style="margin-bottom: 12px; position: relative; padding-left: 20px;">
                    <span style="position: absolute; left: 0; color: #4299e1;">•</span>
                    <strong>Deployed Model:</strong> Uses a <b>Bayesian-optimized XGBoost Regressor</b>, selected after rigorous testing against multiple models, including various <b>Linear models, Bagging, and Boosting models</b>.
                </li>
                <!-- Bullet Point 3 (With Nested Model Performance Metrics) -->
                <li style="margin-bottom: 12px; position: relative; padding-left: 20px;">
                    <span style="position: absolute; left: 0; color: #4299e1;">•</span>
                    <strong>Model Performance:</strong>
                    <ul style="list-style-type: none; padding-left: 0; margin-top: 6px; margin-bottom: 6px;">
                        <li style="margin-bottom: 4px; position: relative; padding-left: 15px;">
                            <span style="position: absolute; left: 0; color: #718096;">-</span>
                            <strong>Test R²:</strong> <code style="background-color: #ebf8ff; color: #2d3748; padding: 2px 6px; border-radius: 4px; font-family: monospace; font-size: 18px; font-weight: 900;">0.92</code>
                        </li>
                        <li style="margin-bottom: 4px; position: relative; padding-left: 15px;">
                            <span style="position: absolute; left: 0; color: #718096;">-</span>
                            <strong>Train R²:</strong> <code style="background-color: #ebf8ff; color: #2d3748; padding: 2px 6px; border-radius: 4px; font-family: monospace; font-size: 18px; font-weight: 900;">0.95</code>
                        </li>
                        <li style="margin-bottom: 4px; position: relative; padding-left: 15px;">
                            <span style="position: absolute; left: 0; color: #718096;">-</span>
                            <strong>MAE: </strong> &#126 <code style="background-color: #ebf8ff; color: #2d3748; padding: 2px 6px; border-radius: 4px; font-family: monospace; font-size: 18px; font-weight: 900;">₹30 Lakh</code>
                        </li>
                    </ul>
                </li>
                <!-- Bullet Point 4 -->
                <li style="margin-bottom: 12px; position: relative; padding-left: 20px;">
                    <span style="position: absolute; left: 0; color: #4299e1;">•</span>
                    <strong>Input Features:</strong> Accepts key property specifications such as <b>flat type, built-up area, bedrooms, bathrooms, floor, locality, and amenity score</b>.
                </li>
                <!-- Bullet Point 5 -->
                <li style="margin-bottom: 12px; position: relative; padding-left: 20px;">
                    <span style="position: absolute; left: 0; color: #4299e1;">•</span>
                    <strong>Purpose:</strong> Provides <b>reliable, data-driven price estimates</b>, assisting buyers, investors, and developers in assessing property values quickly and confidently.
                </li>
            </ul>
        </div>
    </div>
    </div>
    """, unsafe_allow_html=True)

    
    st.markdown("""
    <div style="font-family: calibri; line-height: 1.3; margin-top: 25px;">
    <!-- Feature Section IV -->
    <div style="margin-bottom: 20px;">
        <h3 style="font-size: 20px; color: #000000; margin-bottom: 15px; font-weight: 900;">
            <code style="background-color: #ebf8ff; color: #2d3748; padding: 4px 8px; border-radius: 4px; font-family: monospace; font-size: 22px; font-weight: 900; margin-right: 5px;">IV.</code> 
            <code style="background-color: #f7fafc; color: #2d3748; padding: 4px 8px; border-radius: 4px; font-family: monospace; font-size: 22px; font-weight: 900;">📊 Society Recommendation Engine:</code>
        </h3>
        <div style="color:#ffffff; font-size:20px; font-weight:50; font-family: calibri; margin: 0px;">
            <ul style="list-style-type: none; padding-left: 0; margin: 0;">
                <!-- Bullet Point 1 -->
                <li style="margin-bottom: 12px; position: relative; padding-left: 20px;">
                    <span style="position: absolute; left: 0; color: #4299e1;">•</span>
                    <strong>Content-based Filtering:</strong> Suggests the <strong>Top 10 most Similar Societies</strong> based on multiple factors.
                </li>
                <!-- Bullet Point 2 (With Nested Key Considerations) -->
                <li style="margin-bottom: 12px; position: relative; padding-left: 20px;">
                    <span style="position: absolute; left: 0; color: #4299e1;">•</span>
                    <strong>Key Considerations:</strong>
                    <ul style="list-style-type: none; padding-left: 0; margin-top: 6px; margin-bottom: 6px;">
                        <li style="margin-bottom: 4px; position: relative; padding-left: 15px;">
                            <span style="position: absolute; left: 0; color: #718096;">-</span>
                            <strong>Property Pricing</strong> (highest priority)
                        </li>
                        <li style="margin-bottom: 4px; position: relative; padding-left: 15px;">
                            <span style="position: absolute; left: 0; color: #718096;">-</span>
                            <strong>Nearby Locations</strong> (high priority)
                        </li>
                        <li style="margin-bottom: 4px; position: relative; padding-left: 15px;">
                            <span style="position: absolute; left: 0; color: #718096;">-</span>
                            <strong>Societal Amenities</strong> (lower priority)
                        </li>
                    </ul>
                </li>
                <!-- Bullet Point 3 -->
                <li style="margin-bottom: 12px; position: relative; padding-left: 20px;">
                    <span style="position: absolute; left: 0; color: #4299e1;">•</span>
                    <strong>Weighted Recommendation:</strong> Combines <strong>three separate recommendation modules</strong> into a single, unified engine using weighted priorities.
                </li>
                <!-- Bullet Point 4 -->
                <li style="margin-bottom: 12px; position: relative; padding-left: 20px;">
                    <span style="position: absolute; left: 0; color: #4299e1;">•</span>
                    <strong>Property Listings:</strong> Displays available properties in the recommended societies, including <strong>pricing, property type, and actionable links</strong>.
                </li>
                <!-- Bullet Point 5 -->
                <li style="margin-bottom: 12px; position: relative; padding-left: 20px;">
                    <span style="position: absolute; left: 0; color: #4299e1;">•</span>
                    <strong>Robust & Manually Tested:</strong> The engine was <strong>manually tested</strong> and found to be <strong>reliable, practical, and useful</strong> for home buyers, investors, and developers.
                </li>
                <!-- Bullet Point 6 -->
                <li style="margin-bottom: 12px; position: relative; padding-left: 20px;">
                    <span style="position: absolute; left: 0; color: #4299e1;">•</span>
                    <strong>Purpose:</strong> Helps users quickly <strong>discover similar societies</strong>, compare properties, and make <strong>data-driven location decisions</strong>.
                </li>
            </ul>
        </div>
    </div>
    <!-- Summary Paragraph Footer -->
    <div style="color: #ffffff; font-size: 20px; font-weight: 50; line-height: 1.4; margin-top: 25px; border-top: 1px solid rgba(237, 242, 247, 0.2); padding-top: 15px;">
        Built on the latest data from major housing platforms, the app serves both as a <strong>quick market reference</strong> and a <strong>deep-dive analytical tool</strong>, allowing users to study trends, compare localities, and make informed property-related decisions.
    </div>

    </div>
    """, unsafe_allow_html=True)


## ------------------------------------------------------------------------------------------
## ------------------------------------------------------------------------------------------


def end_line():
    ## User Warning:
    st.markdown("""
    <div style="color: #ffffff; font-size: 20px; font-weight: 50; line-height: 1.4; margin-top: 25px; border-top: 1px solid rgba(237, 242, 247, 0.2); padding-top: 15px;">
    </div>
    <br>
    <br>
    <div style="line-height: 1.3; background-color:#f2f2f2; padding:5px; 
        border-radius:5px; text-align:center;">
    <p style="color:#000000; font-size:22px; font-weight:400; font-family: calibri; margin:0;">
    <em><b>Gurugram Explorer App</b> is a passion project. If it sparked an idea, you found a bug, or just want to talk real estate and AI — reach out.</em>
    <br>
    </p></div>
    
        
    """, unsafe_allow_html=True)
    

## ------------------------------------------------------------------------------------------
## ------------------------------------------------------------------------------------------

    
def socials_buttons():
    st.markdown(
    """
    <div style="display: flex; flex-wrap: wrap; gap: 14px; justify-content: center; margin-top: 45px;">
        <!-- GitHub Button -->
        <a href="https://github.com/VishalMandrai/Gurugram-Real-Estate-Explorer-App" target="_blank" rel="noopener" aria-label="GitHub"
           style="background: #121111; border: 1px solid #FBF3EA; color: #FBF3EA; 
                  display: inline-flex; align-items: center; justify-content: center; gap: 10px; 
                  padding: 13px 20px; border-radius: 5px; font-family: calibri, sans-serif; 
                  font-size: 22px; letter-spacing: 0.1em; 
                  font-weight: 800; text-decoration: none; transition: all 0.3s ease;">
            <svg width="30" height="30" viewBox="0 0 23 23" fill="#ffffff" aria-hidden="true" style="flex-shrink: 0;">
                <path d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466 -.908-.62.069-.608.069-.608 1.003.07 1.531 1.032 1.531 1.032.892 1.53 2.341 1.088 2.91.832 .092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688 -.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0 1 12 6.844 a9.59 9.59 0 0 1 2.504.337c1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651 .64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.02 10.02 0 0 0 22 12.017 C22 6.484 17.522 2 12 2Z" />
            </svg>
            <span style="margin-left: 2px;">GitHub</span>
        </a>
        <!-- LinkedIn Button -->
        <a href="https://www.linkedin.com/in/vishal-mandrai999/" target="_blank" rel="noopener" aria-label="LinkedIn"
           style="background: #121111; border: 1px solid #FBF3EA; color: #FBF3EA; 
                  display: inline-flex; align-items: center; justify-content: center; gap: 10px; 
                  padding: 13px 20px; border-radius: 5px; font-family: calibri, sans-serif; 
                  font-size: 22px; letter-spacing: 0.1em; 
                  font-weight: 800; text-decoration: none; transition: all 0.3s ease;">
            <svg width="30" height="30" viewBox="0 0 24 24" fill="#25A3E8" aria-hidden="true" style="flex-shrink: 0;">
                <path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286ZM5.337 7.433a2.062 2.062 0 0 1-2.063-2.065 2.064 2.064 0 1 1 2.063 2.065Zm1.782 13.019H3.555V9h3.564v11.452ZM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003Z"/>
            </svg>
            <span style="margin-left: 2px;">LinkedIn</span>
        </a>
        <!-- X / Twitter Button -->
        <a href="https://x.com/vishman__" target="_blank" rel="noopener" aria-label="X / Twitter"
           style="background: #121111; border: 1px solid #FBF3EA; color: #FBF3EA; 
                  display: inline-flex; align-items: center; justify-content: center; gap: 10px; 
                  padding: 13px 20px; border-radius: 5px; font-family: calibri, sans-serif; 
                  font-size: 22px; letter-spacing: 0.1em; 
                  font-weight: 800; text-decoration: none; transition: all 0.3s ease;">
            <svg width="30" height="30" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true" style="flex-shrink: 0;">
                <path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-4.714-6.231-5.401 6.231H2.746 l7.73-8.835L1.254 2.25H8.08l4.713 6.231 5.45-6.231Zm-1.161 17.52h1.833L7.084 4.126 H5.117L17.083 19.77Z"/>
            </svg>
            <span style="margin-left: 2px;">X · Twitter</span>
        </a>
        <!-- Portfolio Button -->
        <a href="https://www.vishalm.online" target="_blank" rel="noopener" aria-label="Portfolio website"
           style="background: #121111; border: 1px solid #FBF3EA; color: #FBF3EA; 
                  display: inline-flex; align-items: center; justify-content: center; gap: 10px; 
                  padding: 13px 20px; border-radius: 5px; font-family: calibri, sans-serif; 
                  font-size: 22px; letter-spacing: 0.1em; 
                  font-weight: 800; text-decoration: none; transition: all 0.3s ease;">
            <svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="#D9FA6E" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="flex-shrink: 0;">
                <circle cx="12" cy="12" r="10"/>
                <line x1="2" y1="12" x2="22" y2="12"/>
                <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/>
            </svg>
            <span style="margin-left: 2px;">Portfolio</span>
        </a>
        <!-- Mail Button -->
        <a href="mailto:your.vishalm.nitt@gmail.com" aria-label="Email"
           style="background: #121111; border: 1px solid #FBF3EA ; color: #FBF3EA; 
                  display: inline-flex; align-items: center; justify-content: center; gap: 10px; 
                  padding: 13px 20px; border-radius: 5px; font-family: calibri, sans-serif; 
                  font-size: 22px; letter-spacing: 0.1em; 
                  font-weight: 800; text-decoration: none; transition: all 0.3s ease;">
            <svg width="30" height="30" viewBox="0 0 24 24" fill="#BF2626" stroke="#E8CFCF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="flex-shrink: 0;">
                <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/>
                <polyline points="22,6 12,13 2,6"/>
            </svg>
            <span style="margin-left: 2px;">Mail</span>
        </a>
    </div>
    """, 
    unsafe_allow_html=True
)

# --------------------------------------------- Page layout functions -----------------------------------------
# def page_content():
#     col0, col1, col2 = st.columns([0.5,3.7,5.8])
#     with col1:
#         st.image(image = "about_me/my_prof_pic.png")
        
#         st.markdown( """
#         <div style="background-color:#EDDD68; padding:3px; width: 370px; 
#         border-radius:5px; text-align:left;"></div>
#         <br>
#         <div style="font-size: 24px;"><p>
#         <a href="https://www.linkedin.com/in/vishal-mandrai999/" target="_blank" style="
#           text-decoration:none;
#           background-color:#080707;
#           border: 1.1px solid #ffffff;
#           color:white;
#           font-weight:600;
#           padding:4px 8px;
#           border-radius:6px;">
#           in</a>
#           &nbsp : &nbsp<a href="https://www.linkedin.com/in/vishal-mandrai999/" target="_blank"
#           style="all:unset; cursor: pointer; font-family: calibiri;">
#         vishalmandrai </a>        
#         </p></div>

#         <div style="font-size: 24px;">
#         <a href="mailto:vishalm.nitt@gmail.com" style="
#           text-decoration:none;
#           background-color:#080707;
#           border: 1.1px solid #ffffff;
#           padding:4px 6px;
#           border-radius:6px;
#           color:#fff;
#           font-weight:500;">
#           ✉︎</a>
#           &nbsp : &nbsp<a href="mailto:vishalm.nitt@gmail.com"
#           style="all:unset; cursor: pointer; font-family: calibiri;">
#         mailto:vishalmandrai </a>        
#         </div>

#         """,
#         unsafe_allow_html=True)

#     with col2:
#         st.pdf("about_me/Resume.pdf", height=850)    ## My resume....


## ------------------------------------------------------------------------------------------
## ------------------------------------------------------------------------------------------


def main():
    page_content()
    
    overview()
    
    features()

    end_line()

    socials_buttons()

if __name__ == "__main__":
    main()
