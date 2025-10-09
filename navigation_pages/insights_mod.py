import streamlit as st
from streamlit_folium import st_folium
import pandas as pd
import numpy as np
from io import BytesIO

from navigation_pages.graphs_and_plots import all_graphs_for_IM as myplots # Have all the graphing code!


# ------------------------- Page layout functions -------------------------
def page_content():
    ## Title of Page:
    st.markdown(
        """<h1 style='text-align: center; color: white;'> 
        💡 Insights on Gurugram Real Estate
        </h1>""",
        unsafe_allow_html=True)
    
    ## Analytics Module heading in the box:
    st.markdown(
        """<div style="background-color:#EDDD68; padding:3px; 
        border-radius:5px; text-align:center;"></div>
        
        """, unsafe_allow_html=True)

def Insights_Age():
    st.markdown(
        """
        <div style="background-color:#FFFC82; padding:2px; border-radius:4px; 
        text-align:left !important;">
        <p style="color:#000000; font-size:30px; font-weight:600; margin:0;">
        <span style="font-size:28px; font-weight:bold; color:#7A360C; 
        font-family: calibri !important;">Age</span> 
        of Real Estate & Relation with 
        <span style="font-size:28px; font-weight:bold; color:#7A360C; 
        font-family: calibri !important;">Affordability</span></p> </div>
        <div><br></div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div style="line-height: 1.3;">
    <p style="color:#ffffff; font-size:18px; font-weight:50;font-family: calibri; margin:0;">
    In real estate, <b>Property Age</b> has a <b>direct impact on price dynamics</b>.
    </p>
    <ul>
      <li style="color:#ffffff; font-size:18px; font-weight:50;font-family: calibri; margin:0;"><b>Newer properties</b> generally <b>command</b> a <b>premium due to modern layouts</b>, better amenities, and lower maintenance costs.</li>
      <li style="color:#ffffff; font-size:18px; font-weight:50;font-family: calibri; margin:0;"><b>As Properties Age</b> beyond <b>8–12 years</b>, <b>prices</b> tend to <b>stabilize or even decline</b>, reflecting wear-and-tear, outdated designs, and higher upkeep.</li>
      <li style="color:#ffffff; font-size:18px; font-weight:50;font-family: calibri; margin:0;">However, <b>in prime locations</b>, <b>older properties can still retain or appreciate in value</b> due to land scarcity and location advantage, even if the building itself depreciates.</li>
    </ul>
    </div>

    <style>
    .big-box-style {background-color:#080707; padding:5px; border-radius:8px; border:2px solid #FFFFFF;
    color:#ffffff;}    
    </style>
    
    <div style="background-color:#080707; padding:8px; border-radius:12px; text-align:center;">
    <p style="color:#D6EAF8; font-size:23px; font-weight:600; margin:5px;">
    <span class = "big-box-style">Age of Property across Top 25 Sectors & Price Behavior</span>
    </p>
    </div>
    """, unsafe_allow_html=True)

    ## Ploting the graph:
    st.pyplot(myplots.Age_of_Properties_across_the_Top_25_Sectors())

    ## Some insightful statments:
    st.markdown("""
    <div style="line-height: 1.3;">
    <p style="color:#ffffff; font-size:20px; font-weight:50;font-family: calibri; margin:0;">
    <span style="font-size:34px; font-weight:bold; color:#50FAA0; font-family: calibri !important;">
    Property Age is NOT the Sole Determinant of Price</span> in Gurugram’s real estate market.</p>
    <ul>
      <li style="color:#ffffff; font-size:20px; font-weight:50;font-family: calibri; margin:0;"><b>While younger sectors</b> generally <b>indicate new development</b> and potential for appreciation, <b>prices are equally influenced by</b> - <b>sector location, infrastructure, and premium positioning</b>.</li>
      <li style="color:#ffffff; font-size:20px; font-weight:50;font-family: calibri; margin:0;"><b>For stakeholders</b>, balancing between <b>new growth corridors</b> and <b>established sectors</b> is key to making informed real estate decisions.</li>
    </ul>
    </div>
    <div><br></div>
    """, unsafe_allow_html=True)


def Sector_number():
    st.markdown(
        """
        <div style="background-color:#FFFC82; padding:2px; border-radius:4px; 
        text-align:left !important;">
        <p style="color:#000000; font-size:30px; font-weight:600; margin:0;">
        <span style="font-size:28px; font-weight:bold; color:#7A360C; 
        font-family: calibri !important;">Sector Number</span> — Order of
        <span style="font-size:28px; font-weight:bold; color:#7A360C; 
        font-family: calibri !important;">Development</span>
        & Relation with 
        <span style="font-size:28px; font-weight:bold; color:#7A360C; 
        font-family: calibri !important;">Affordability</span>
        </p> </div>
        <div><br></div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div style="line-height: 1.3;">
    <p style="color:#ffffff; font-size:24px; font-weight:50; font-family: calibri; margin:0;">
    <b>🗺️ NUMBERING OF SECTORS OF GURUGRAM :</b></p>
    
    <ul>
      <li style="color:#ffffff; font-size:18px; font-weight:50;font-family: calibri; margin:0;">
      The <b>numbering of Sectors</b> in Gurugram (formerly Gurgaon) is <b>NOT STRICTLY sequential based on</b> the <b>order of their creation</b>.
      </li>
      <li style="color:#ffffff; font-size:18px; font-weight:50;font-family: calibri; margin:0;">
      While <b>there's a general progression</b> from <b>older to newer sectors</b>, the <b>numbering doesn't perfectly reflect the exact timeline of development</b>.
      </li>
      <li><b>General Trend:</b>
        <ul>
          <li style="color:#ffffff; font-size:18px; font-weight:50;font-family: calibri; margin:0;">
          Older sectors like those in Old Gurgaon (e.g., sectors 1-23) were developed earlier, while
          </li>
          <li style="color:#ffffff; font-size:18px; font-weight:50;font-family: calibri; margin:0;">
          Newer sectors, such as those along the Dwarka Expressway and in New Gurgaon (e.g., sectors 76-95, 102-113), were developed later.
          </li>
        </ul>
        </li>
        
      <li style="color:#ffffff; font-size:18px; font-weight:50;font-family: calibri; margin:0;">
      <b>No Strict Sequence:</b> However, <b>there's not a strict one-to-one correlation between sector number and the year of development</b>. Some sectors might have been <b>developed out of sequence</b>, or with <b>gaps in numbering</b>.
      </li>
    </ul>
    
    </div>

    <style>
    .big-box-style {background-color:#080707; padding:5px; border-radius:8px; border:2px solid #FFFFFF;
    color:#ffffff;}    
    </style>
    
    <div style="background-color:#080707; padding:8px; border-radius:12px; text-align:center;">
    <p style="color:#D6EAF8; font-size:23px; font-weight:600; margin:5px;">
    <span class = "big-box-style">Sector Numbers & Pricing Trend</span>
    </p>
    </div>
    """, unsafe_allow_html=True)

    ## Ploting the graph:
    st.pyplot(myplots.trend_bw_sector_numbers_and_development_and__pricing())

    ## Some insightful statments:
    st.markdown("""
    <div style="line-height: 1.3;">
    <p style="color:#ffffff; font-size:20px; font-weight:50;font-family: calibri; margin:0;">
    <span style="font-size:34px; font-weight:bold; color:#50FAA0; font-family: calibri !important;">
    Sector Numbering has no <i>Statistical Correlation</i></span> with <b>Property Price Density</b> in Gurugram.</p>
    <ul>
      <li style="color:#ffffff; font-size:20px; font-weight:50;font-family: calibri; margin:0;">
      Pearson Correlation Test: <b>Corr. Coef. = -0.00389, p-value = 0.968</b>.
      </li>
      <li style="color:#ffffff; font-size:20px; font-weight:50;font-family: calibri; margin:0;">
      Instead, <b>price variations</b> are <b>driven by localized factors</b> such as <i>premium projects</i>, <i>infrastructure</i>, and <i>proximity to commercial hubs</i>.
      </li>
      <li style="color:#ffffff; font-size:20px; font-weight:50;font-family: calibri; margin:0;">
      <b>Stakeholders</b> must therefore <b>evaluate property investment</b> at a <b>micro-market (sector-specific) level</b>, rather than relying on <b>broad sector numbering</b> as a proxy for affordability or costliness.
      </li>
    </ul>
    </div>
    <div><br></div>
    """, unsafe_allow_html=True)



def Per_bedroom_trend():
    st.markdown(
        """
        <div style="background-color:#FFFC82; padding:2px; border-radius:4px; 
        text-align:left !important;">
        <p style="color:#000000; font-size:30px; font-weight:600; margin:0;">
        <span style="font-size:28px; font-weight:bold; color:#7A360C; 
        font-family: calibri !important;">Per Bedroom Cost</span> 
        across
        <span style="font-size:28px; font-weight:bold; color:#7A360C; 
        font-family: calibri !important;">Price Buckets</span></p> 
        </div>
        <div><br></div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div style="line-height: 1.3;">
    <p style="color:#ffffff; font-size:18px; font-weight:50;font-family: calibri; margin:0;">
    <b>Per Bedroom Cost</b> is a useful metric <b>to standardize property pricing across configurations</b>.</p>
    <ul>
      <li style="color:#ffffff; font-size:18px; font-weight:50;font-family: calibri; margin:0;">
      It <b>reveals whether larger units</b> (3–4 BHK) are <b>priced at a premium per room</b> compared to smaller ones, or
      </li>
      <li style="color:#ffffff; font-size:18px; font-weight:50;font-family: calibri; margin:0;">
      <b>whether developers offer cost efficiency</b> with <b>added bedrooms</b>.
      </li>
      <li style="color:#ffffff; font-size:18px; font-weight:50;font-family: calibri; margin:0;">
      <b>For Buyers</b>, it <b>helps gauge value-for-money</b>, while
      </li>
      <li style="color:#ffffff; font-size:18px; font-weight:50;font-family: calibri; margin:0;">
      <b>For Investors and Developers</b>, it <b>signals demand patterns</b>, affordability thresholds, and <b>pricing strategies within the market</b>.
      </li>
    </ul>
    </div>

    <style>
    .big-box-style {background-color:#080707; padding:5px; border-radius:8px; border:2px solid #FFFFFF;
    color:#ffffff;}    
    </style>
    
    <div style="background-color:#080707; padding:8px; border-radius:12px; text-align:center;">
    <p style="color:#D6EAF8; font-size:23px; font-weight:600; margin:5px;">
    <span class = "big-box-style">Per Bedroom Cost Trend across Price Buckets</span>
    </p> </div>
    """, unsafe_allow_html=True)

    ## Ploting the graph:
    st.pyplot(myplots.Price_Bucket_VS_Per_bedroom_Cost())

    ## Some insightful statments:
    st.markdown("""
    <div style="line-height: 1.3;">
    <p style="color:#ffffff; font-size:20px; font-weight:50;font-family: calibri; margin:0;">
    <span style="font-size:34px; font-weight:bold; color:#50FAA0; font-family: calibri !important;">
    Per Bedroom Cost efficiency DECLINES as Property Price rises.</span>
    <br><b>Per Bedroom Cost rises steadily</b> with <b>Overall Property Value</b> but <b>accelerates disproportionately in the luxury segment</b>.</p>
    
    <ul>
      <li style="color:#ffffff; font-size:20px; font-weight:50;font-family: calibri; margin:0;">
      While <b>affordable and mid-market ranges maintain value efficiency</b>,
      </li>
      <li style="color:#ffffff; font-size:20px; font-weight:50;font-family: calibri; margin:0;">
      <b>Ultra-luxury properties</b> command a <b>significant brand/location premium per room</b>.
      </li>
      <li style="color:#ffffff; font-size:20px; font-weight:50;font-family: calibri; margin:0;">
      <b>This underlines</b> the <b><i>segmented nature of Gurugram’s market</i></b>, where affordability, premium demand, and luxury exclusivity <b>coexist</b>, each requiring distinct buyer targeting and pricing strategies.
      </li>
    </ul>
    
    </div>
    <div><br></div>
    """, unsafe_allow_html=True)


def Furnishing_and_affordability():
    st.markdown(
        """
        <div style="background-color:#FFFC82; padding:2px; border-radius:4px; 
        text-align:left !important;">
        <p style="color:#000000; font-size:30px; font-weight:600; margin:0;">
        Property
        <span style="font-size:28px; font-weight:bold; color:#7A360C; 
        font-family: calibri !important;">Furnishing Status</span> 
        & Relation with 
        <span style="font-size:28px; font-weight:bold; color:#7A360C; 
        font-family: calibri !important;">Affordability</span></p> 
        </div>
        <div><br></div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div style="line-height: 1.3;">
    <p style="color:#ffffff; font-size:18px; font-weight:50;font-family: calibri; margin:0;">
    <b>Furnishing</b> typically <b>adds a Price Premium</b> to real estate.</p>
    <ul>
      <li style="color:#ffffff; font-size:18px; font-weight:50;font-family: calibri; margin:0;">
      <b>Ready-to-move units</b> with modular kitchens, wardrobes, and appliances <b>reduce upfront costs for buyers</b>.
      </li>
      <li style="color:#ffffff; font-size:18px; font-weight:50;font-family: calibri; margin:0;">
      <b>Fully-furnished homes</b> often <b>attract young professionals, NRIs, and rental investors</b>, signaling convenience and faster occupancy.
      </li>
      <li style="color:#ffffff; font-size:18px; font-weight:50;font-family: calibri; margin:0;">
      <b>However</b>, the <b>Premium is NOT always proportional to resale value</b>.
      </li>
      <li style="color:#ffffff; font-size:18px; font-weight:50;font-family: calibri; margin:0;">
      Since <b>furnishing reflects personal taste</b> and <b>may depreciate faster</b> than the property itself.
      </li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

    ## Ploting the graph:
    st.pyplot(myplots.Furnishing_Status_affects_Property_Pricing_and_Property_Price_Density())

    ## Some insightful statments:
    st.markdown("""
    <div style="line-height: 1.2;">
    <p style="color:#ffffff; font-size:20px; font-weight:50;font-family: calibri; margin:0;">
    <span style="font-size:34px; font-weight:bold; color:#50FAA0; font-family: calibri !important;">
    Furnishing clearly influences both Property Price and Price Density.
    </span></p>
    <ul>
      <li style="color:#ffffff; font-size:20px; font-weight:50;font-family: calibri; margin:0;">
      <b>Fully furnished</b> units <b>command</b> the <b>high premiums</b>,</li>
      <li style="color:#ffffff; font-size:20px; font-weight:50;font-family: calibri; margin:0;">
      <b>Semi-furnished</b> dominate as the <b>mainstream choice</b>, while</li>
      <li style="color:#ffffff; font-size:20px; font-weight:50;font-family: calibri; margin:0;">
      <b>Unfurnished</b> remain the <b>affordable and customizable option</b>.</li>
    </ul>
    
    <p style="color:#ffffff; font-size:20px; font-weight:50;font-family: calibri; margin:0;">
    The <b>Premium Effect is STRONGER in larger flats</b>, underscoring the <b>role of furnishing</b> as a <b><i>luxury differentiator</i></b> in the real estate market.</p>
    </div>
    <div><br></div>
    """, unsafe_allow_html=True)


def Facing_Vaastu():
    st.markdown(
        """
        <div style="background-color:#FFFC82; padding:2px; border-radius:4px; 
        text-align:left !important;">
        <p style="color:#000000; font-size:30px; font-weight:600; margin:0;">
        <span style="font-size:28px; font-weight:bold; color:#7A360C; 
        font-family: calibri !important;">Facing Direction</span> 
        of Property, 
        <span style="font-size:28px; font-weight:bold; color:#7A360C; 
        font-family: calibri !important;">Vaastu Compliance</span> & 
        <span style="font-size:28px; font-weight:bold; color:#7A360C; 
        font-family: calibri !important;">Price Behavior</span>
        </p> 
        </div>
        <div><br></div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div style="line-height: 1.3;">
    <p style="color:#ffffff; font-size:18px; font-weight:50;font-family: calibri; margin:0;">
    In India, <b>Property Facing</b> strongly <b>influences buyer behavior</b>, often linked to <b>Vaastu Shastra</b> and <b>cultural beliefs</b>.</p>
    <ul>
      <li style="color:#ffffff; font-size:18px; font-weight:50;font-family: calibri; margin:0;">
      <b>East- and North-facing homes</b> are <b>considered auspicious</b> and usually <b>command a price premium</b>, while</li>
      <li style="color:#ffffff; font-size:18px; font-weight:50;font-family: calibri; margin:0;">
      <b>South-facing</b> units <b>may face resistance</b>, affecting demand and pricing.</li>
      <p style="color:#ffffff; font-size:18px; font-weight:50;font-family: calibri; margin:0;"><b>For many buyers</b>, especially in North India, <b>Vaastu compliance outweighs design</b> or <b>location trade-offs</b>, making facing a <b>subtle but significant factor</b> in both marketability and <b>cost premium</b>.</p>
    </ul>
    </div>

    <style>
    .big-box-style {background-color:#080707; padding:5px; border-radius:8px; border:2px solid #FFFFFF;
    color:#ffffff;}    
    </style>
    
    <div style="background-color:#080707; padding:8px; border-radius:12px; text-align:center;">
    <p style="color:#D6EAF8; font-size:23px; font-weight:600; margin:5px;">
    <span class = "big-box-style">Property Facing Distribution of Gurugram</span>
    </p>
    </div>
    """, unsafe_allow_html=True)

    ## Ploting the graph:
    # st.pyplot(myplots.Furnishing_Status_affects_Property_Pricing_and_Property_Price_Density())
    st.plotly_chart(
            myplots.Flat_Facing_Compass_and_treemap(),
            use_container_width=True, config=dict(displaylogo=False, 
                                                  modeBarButtonsToRemove=["pan2d","zoom2d",                                                "select2d","lasso2d","zoomIn2d","zoomOut2d","autoScale2d",
                                "resetScale2d","toImage"]))

    st.markdown("""
    <div><br></div>
    """, unsafe_allow_html=True)
    
    ## Some Insight from data and Dataset to support it:
    col1, col2 = st.columns([65,35])
    col1.markdown("""
    <div style="line-height: 1;">
    <p style="color:#ffffff; font-size:20px; font-weight:50;font-family: calibri; margin:0;">
    <span style="font-size:34px; font-weight:bold; color:#50FAA0; font-family: calibri !important;">
    Gurugram Properties shows a Strong Skew</span> 
    <b>toward North-East and East-facing flats</b> (together ~ 61%), <b>aligning with</b> 
    <span style="font-size:34px; font-weight:bold; color:#50FAA0; font-family: calibri !important;">
    Vastu Compliance</span> and higher market demand.
    </p> <br>
    </div>
    <div style="line-height: 1.2;">
    <ul>
      <li style="color:#ffffff; font-size:20px; font-weight:50;font-family: calibri; margin:0;">
      🙏 <b>Vaastu Shastra</b> (or <span style="font-size:18px;">वास्तुविद्या</span> ) is a <b>traditional Indian architectural system</b> that <b>links directions, layout, and energy flow</b>. It’s similar in spirit to Feng Shui in Chinese culture.</li>
      <li style="color:#ffffff; font-size:20px; font-weight:50;font-family: calibri; margin:0;">
      ➡️ In Vaastu, the <b>facing direction of property</b> is <b>considered important</b> because each direction is associated with a <b>ruling element and deity</b>.</li>
    </ul>

    </div>

    """, unsafe_allow_html=True)

    col2.dataframe(myplots.Vaastu_data().T)
    

def Floor_Building_features():
    st.markdown(
        """
        <div style="background-color:#FFFC82; padding:2px; border-radius:4px; 
        text-align:left !important;">
        <p style="color:#000000; font-size:30px; font-weight:600; margin:0;">
        <span style="font-size:28px; font-weight:bold; color:#7A360C; 
        font-family: calibri !important;">Floor</span> 
        Number, 
        <span style="font-size:28px; font-weight:bold; color:#7A360C; 
        font-family: calibri !important;">Building Height</span> & 
        <span style="font-size:28px; font-weight:bold; color:#7A360C; 
        font-family: calibri !important;">Price Trend</span>
        </p> 
        </div>
        <div><br></div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div style="line-height: 1.3;">
    <p style="color:#ffffff; font-size:18px; font-weight:50;font-family: calibri; margin:0;">
    In real estate, <b>Floor Number</b> and <b>Building Height</b> directly <b>influence Pricing</b>.
    </p>
    <ul>
      <li style="color:#ffffff; font-size:18px; font-weight:50;font-family: calibri; margin:0;">
      <b>In high-rise markets</b> like Gurugram, <b>mid-to-upper floors</b> often <b>command a premium</b>.</li>
      <li style="color:#ffffff; font-size:18px; font-weight:50;font-family: calibri; margin:0;">
      This premium is mainly <b>due to better views, ventilation</b>, and <b>reduced noise</b>.</li>
      <li style="color:#ffffff; font-size:18px; font-weight:50;font-family: calibri; margin:0;">
      <b>Higher towers</b> also <b>signal modern amenities</b> and <b>exclusivity</b>, adding to <b>property value</b>.</li>
      <li style="color:#ffffff; font-size:18px; font-weight:50;font-family: calibri; margin:0;">
      However, <b>very high floors may face buyer hesitation</b> (e.g., evacuation concerns, longer wait times for lifts).</li>
    </ul>
    <p style="color:#ffffff; font-size:18px; font-weight:50;font-family: calibri; margin:0;">
    So the <b>premium generally peaks in</b> the <b>mid-upper range</b> rather than the absolute top.
    </p>
    </div><div><br></div>

    <style>
    .big-box-style {background-color:#080707; padding:5px; border-radius:8px; border:2px solid #FFFFFF;
    color:#ffffff;}    
    </style>
    
    <div style="background-color:#080707; padding:8px; border-radius:12px; text-align:center;">
    <p style="color:#D6EAF8; font-size:23px; font-weight:600; margin:5px;">
    <span class = "big-box-style">Distribution of Floor Number and Building Height in Gurugram</span>
    </p>
    </div>
    """, unsafe_allow_html=True)

    ## Ploting the graph:
    st.pyplot(myplots.Distribution_of_Floor_Number_and_Building_Height())

    
    ## Some concluding insights:
    st.markdown("""
    <div><br></div>
    
    <div style="line-height: 1.3;">
    <p style="color:#ffffff; font-size:20px; font-weight:50;font-family: calibri; margin:0;">
    <span style="font-size:34px; font-weight:bold; color:#50FAA0; font-family: calibri !important;">
    Gurugram’s Real Estate Landscape</span> <b>is</b> 
    <span style="font-size:34px; font-weight:bold; color:#50FAA0; font-family: calibri !important;">
    Mid-rise Dominated</span>.</p>
    <ul>
      <li style="color:#ffffff; font-size:20px; font-weight:50;font-family: calibri; margin:0;">
      <b>Most offerings concentrated</b> on <b>4th–12th floor</b> in <b>10–25 floor towers</b>.</li>
      <li style="color:#ffffff; font-size:20px; font-weight:50;font-family: calibri; margin:0;">
      While <b>Super high-rise developments exist</b>, they <b>form</b> a <b>small, luxury-driven niche</b>.</li>

      <p style="color:#ffffff; font-size:20px; font-weight:50;font-family: calibri; margin:0;">
    This <b>indicates</b> that <b>floor preference</b> is <b>practical and mid-level centric</b>, while <b>Ultra-high-rise supply</b> is <b>targeted at</b> exclusive, <b>high-income groups</b>.</p>
    </ul>
    </div>

    <style>
    .big-box-style {background-color:#080707; padding:5px; border-radius:8px; border:2px solid #FFFFFF;
    color:#ffffff;}    
    </style>
    
    <div style="background-color:#080707; padding:8px; border-radius:12px; text-align:center;">
    <p style="color:#D6EAF8; font-size:23px; font-weight:600; margin:5px;">
    <span class = "big-box-style">
    Floor Number & Price Trend in Gurugram</span></p>
    </div>
    """, unsafe_allow_html=True)

    st.pyplot(myplots.Floor_Number_affects_Property_Pricing())

    ## Quick concluding statement for above graph:
    st.markdown("""
    <div style="line-height: 1.2;">
    <p style="color:#ffffff; font-size:20px; font-weight:50;font-family: calibri; margin:0;">
    There exist a <b>direct and significant positive correlation</b> between <b>Floor Number and Property Price Density</b>.</p>
    <ul>
      <li style="color:#ffffff; font-size:20px; font-weight:50;font-family: calibri; margin:0;">
      <b>Higher floors</b> command <b>clear premiums</b>, with <b>median costs rising</b> from <b>~₹11K/Sq.ft</b>,</li>
      <li style="color:#ffffff; font-size:20px; font-weight:50;font-family: calibri; margin:0;">
      At <b>lower floors</b> to <b>nearly ₹19K/Sq.ft</b> at <b>premium levels</b>.</li>

      <p style="color:#ffffff; font-size:20px; font-weight:50;font-family: calibri; margin:0;">
    This <b>validates</b> the <b>Floor-rise Pricing Model</b> widely <b>adopted</b> in Gurugram’s real estate market.</p>
    </ul>
    </div>

    <style>
    .big-box-style {background-color:#080707; padding:5px; border-radius:8px; border:2px solid #FFFFFF;
    color:#ffffff;}    
    </style>
    
    <div style="background-color:#080707; padding:8px; border-radius:12px; text-align:center;">
    <p style="color:#D6EAF8; font-size:23px; font-weight:600; margin:5px;">
    <span class = "big-box-style">
    Building Heigth Category, Relative Floor Position & Price Trend in Gurugram</span></p>
    </div>
    """, unsafe_allow_html=True)

    st.pyplot(myplots.Do_higher_floors_in_taller_buildings_command_Premium_Pricing())
    

    
    ## Some insightful statments:
    st.markdown("""
    <div style="line-height: 1.2;">
    <p><span style="font-size:34px; font-weight:bold; color:#50FAA0; font-family: calibri !important;">
    Floor-rise Premium is strongly correlated with Building Height.</span></p>
    <ul>
      <li style="color:#ffffff; font-size:20px; font-weight:50;font-family: calibri; margin:0;">
      In <b>Shorter buildings</b>, <b>pricing</b> is <b>almost uniform across floors</b>.</li>
      <li style="color:#ffffff; font-size:20px; font-weight:50;font-family: calibri; margin:0;">
      In <b>Medium-rise projects</b>, a <b>modest premium emerges</b>, while</li>
      <li style="color:#ffffff; font-size:20px; font-weight:50;font-family: calibri; margin:0;">
      In <b>Taller towers</b>, <b>upper floors command a significant premium</b> (₹1.5K–2K/Sq.ft higher).</li>
    </ul>
    <p style="color:#ffffff; font-size:20px; font-weight:50;font-family: calibri; margin:0;">
      This <b>reinforces</b> that <b>Floor-rise Pricing</b> is <b>a key differentiator</b> in <b>luxury high-rise developments</b>, while being <b>less relevant in shorter projects</b>.</p>
    </div>
    """, unsafe_allow_html=True)

## ----------------------------------------------------------------------------------------------


def link_directing_to_sectors_page():
    st.markdown(
        """
        <style>
        .btn-tooltip {
          --btn-bg: #16324F;
          --btn-color: #D6EAF8;
          --btn-padding: 10px 18px;
          --btn-radius: 10px;
          --btn-font-size: 16px;
          --btn-weight: 700;
          --tooltip-bg: rgba(20, 20, 20, 0.95);
          --tooltip-color: #fff;
          --tooltip-font-size: 13px;
          --tooltip-padding: 8px 10px;
          --tooltip-radius: 6px;
          --tooltip-offset: 10px;
          position: relative;
          display: inline-block;
          background: var(--btn-bg);
          color: var(--btn-color);
          padding: var(--btn-padding);
          border-radius: var(--btn-radius);
          border: none;
          font-size: var(--btn-font-size);
          font-weight: var(--btn-weight);
          cursor: pointer;
          transition: transform .08s ease;
        }
    
        .btn-tooltip:hover { transform: translateY(-2px); }
    
        .btn-tooltip::after {
          content: attr(data-tooltip);
          position: absolute;
          left: 50%;
          transform: translateX(-50%);
          bottom: calc(100% + var(--tooltip-offset));
          white-space: pre-wrap;
          background: var(--tooltip-bg);
          color: var(--tooltip-color);
          font-size: var(--tooltip-font-size);
          padding: var(--tooltip-padding);
          border-radius: var(--tooltip-radius);
          box-shadow: 0 6px 18px rgba(0,0,0,0.35);
          opacity: 0;
          pointer-events: none;
          transition: opacity .18s ease, bottom .12s ease;
          z-index: 999;
          min-width: 140px;
          max-width: 360px;
          text-align: center; }
    
        .btn-tooltip:hover::after { opacity: 1; bottom: calc(100% + (var(--tooltip-offset) - 6px)); }
    
        .btn-tooltip::before {content: ''; position: absolute; left: 50%; transform: translateX(-50%);
          bottom: calc(100% + var(--tooltip-offset) - 6px); border-width: 6px; border-style: solid;
          border-color: var(--tooltip-bg) transparent transparent transparent; opacity: 0;
          transition: opacity .18s ease, bottom .12s ease; z-index: 999; }
    
        .btn-tooltip:hover::before {opacity: 1; bottom: calc(100% + (var(--tooltip-offset) - 12px));}
        </style>
    
        <div><br></div><div><br></div><div><br></div>
        
        <div style = "display: flex; justify-content: center; align-items: center;">
        <button class="btn-tooltip" 
        style="background-color:#5AE667; color:#ffffff; border:4px solid #ffffff; border-radius:6px; 
        padding:8px 200px; font-size:28px; font-weight:800; cursor:pointer;"
        data-tooltip="This button takes you to Know the Sector Page" >
        <a href="/know_sector" target="_self" style="color:#000000;">
        Want to Know About any "Sector" - CLICK HERE!
        </a>
        </button></div>
        """, unsafe_allow_html=True )




## App Starts from here: ------------------------------------------------------------------------
def main():
    ## Introductory heading and content:
    page_content()

    ## Property Age Insights:
    Insights_Age()

    ## Sector Number Insight:
    Sector_number()

    ## Per Bedroom Cost Insight:
    Per_bedroom_trend()

    ## Furnishinh Status and Affordability:
    Furnishing_and_affordability()

    ## Property Facing & Vaastu:
    Facing_Vaastu()

    ## Floor Feature, Building Height & Pricing:
    Floor_Building_features()

    ## FINALLY!!! Directing to Sectors Page:
    link_directing_to_sectors_page()
        

if __name__ == '__main__':
    main()

