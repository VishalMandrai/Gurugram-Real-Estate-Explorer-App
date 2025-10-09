import streamlit as st
from streamlit_folium import st_folium
import pandas as pd
import numpy as np
from io import BytesIO

from navigation_pages.graphs_and_plots import all_graphs_for_AM as myplots # Have all the graphing code!

# ------------------------- Page layout functions -------------------------
def page_content():
    ## Title of Page:
    st.markdown(
        "<h1 style='text-align: center; color: white;'>📊 Know Gurgram Real Estate</h1>",
        unsafe_allow_html=True)
    
    ## Analytics Module heading in the box:
    st.markdown(
        """<div style="background-color:#5AA2E6; padding:5px; 
        border-radius:5px; text-align:center;">
        <p style="color:#000000; font-size:44px; font-weight:600; margin:0; font-family: calibri">
        ANALYTICS MODULE </p>
        </div>
        """, unsafe_allow_html=True)
    st.markdown("<br>",unsafe_allow_html=True)

## ----------------------------------------------------------------------------------------

    
def About_flats_and_contribution():
    st.markdown(
        """
        <div style="background-color:#0B3C73; padding:5px; border-radius:8px; 
        text-align:left !important;">
        <p style="color:#000000; font-size:32px; font-weight:900; font-family: calibri; margin:0;">
        <span style="color: #ffffff;">Flat Types</span> & 
        <span style="color: #ffffff;">Distribution</span>
        </p>
        </div>
        """, unsafe_allow_html=True)
    
    st.plotly_chart(myplots.What_are_the_different_kinds_of_Flats_available_for_sale_in_Gurgaon(),
                    use_container_width=True) 

    st.markdown("""
    <style>
    .big-box-style {border-radius:5px; border:2px solid #FFFFFF; padding:5px 100px !important;
    font-size:27px !important; font-weight:600; font-family:calibri;}    
    </style>
    
    <div style="background-color:#080707; text-align:center;">
    <p style="color:#ffffff; margin:10px;">
    <span class="big-box-style">Distribution of different Flat Types</span>
    </p></div>
    """, unsafe_allow_html=True)
    st.pyplot(myplots.What_is_the_portion_of_each_Flat_type_in_the_overall_flat_market())

    ## Concuding comments:
    st.markdown("")
    st.markdown(
        """
        <style>
        .med-font {
            font-size:16px !important;
            color: #FFFFFF !important; 
            line-height: 1.2 !important;
            font-family: calibri !important;}
        </style>
        
        <div>
        <p class="med-font"><span style="font-size:28px; font-weight:bold; color:#50FAA0; font-family: calibri !important;"> Gurgaon’s Housing Market</span> is <b>largely family-driven</b>, with <b>3 BHK (46.2%) and 2 BHK (27.3%)</b> together forming <b>over 73% of total supply</b>. This underscores a <b>strong builder–buyer alignment</b> towards <b>mid-sized family apartments</b>.</p>
        <ul>
        <li class="med-font"><b>4 BHK units (11.2%) dominate</b> the <b>premium segment</b>, while</li>
        <li class="med-font"><b>Niche options</b> like <b>2.5 BHK and 3.5 BHK</b> serve <b>selective demand pockets</b>.</li>
        <li class="med-font">In contrast, <b>small units (1 BHK/1 RK)</b> remain <b>scarce</b>, showing <b>limited focus on students or transient professionals</b>.</li>
        <li class="med-font"><b>Ultra-luxury (6–7 BHK)</b> stays <b>confined to</b> a niche <b>HNI audience</b>.</li>
        </ul>
        </div>

        """,unsafe_allow_html=True)
    st.markdown("<br>",unsafe_allow_html=True)

## ----------------------------------------------------------------------------------------


def About_price_density_distribution():
    st.markdown(
        """
        <br>
        <div style="background-color:#0B3C73; padding:5px; border-radius:8px; 
        text-align:left !important;">
        <p style="color:#000000; font-size:32px; font-weight:900; font-family: calibri; margin:0;">
        <span style="color: #ffffff;">Property Built-up Area</span> across 
        <span style="color: #ffffff;">Gurugram</span>
        </p>
        </div><br>
        """, unsafe_allow_html=True)

    ## Adding Data Cards:
    col1, col2, col3, col4, col5 = st.columns([1,1,1,1,1])
    
    # Smallest Prop by Size: 
    value = myplots.smallest_area_prop_det()
    col1.metric(label="Smallest Built-Up Area", value= value[0], 
                delta=f"Price: ₹ {value[3]}", delta_color="inverse", 
                help=f"Flat: {value[1]} - {value[2]}")

    # Largest Prop by size: 
    value = myplots.largest_area_prop_det()
    col2.metric(label="Largest Built-Up Area", value= value[0], 
                delta=f"Price: ₹ {value[3]}", delta_color="normal", 
                help=f"Flat: {value[1]} - {value[2]}")
    
    # Median Property Price in Gurugram:
    value = myplots.med_average_mod()
    col3.metric(label="Median Built-Up Area", value=value[0],
                help="Median Built-Up Area from all the properties listed")
    col4.metric(label="Average Built-Up Area", value=value[1], 
                help="Average Built-Up Area from all the properties listed")
    col5.metric(label="Most Frequent Size", value=value[2], 
                help="Most Frequent Size of all the properties listed!")
    
    ## Adding Flat vs Flat Size distribution plot:
    st.markdown("""
    <style>
    .big-box-style {border-radius:5px; border:2px solid #FFFFFF; padding:5px 100px !important;
    font-size:27px !important; font-weight:600; font-family:calibri;}    
    </style>
    
    <div style="background-color:#080707; text-align:center;">
    <p style="color:#ffffff; margin:10px;">
    <span class="big-box-style">Distribution of Built-up Area across Flat Types</span>
    </p></div>
    """, unsafe_allow_html=True)
    
    st.pyplot(myplots.What_is_the_Average_Builtup_Area_across_5_major_Flat_types())
    
    ## Concuding comments:
    st.markdown(
        """
        <style>
        .med-font {
            font-size:16px !important;
            color: #FFFFFF !important; 
            line-height: 1.2 !important;
            font-family: calibri !important;}
        </style>
        <div><br></div>
        <div>
        <p class="med-font"><span style="font-size:28px; font-weight:bold; color:#50FAA0; font-family: calibri !important;">Built-up Area </span> <b>rises with flat size</b>, but <b>variability is sharpest</b> in <b>4 BHKs<b>, revealing a <b>Dual Market</b> — <b>standardized mid-segment</b> (2–3 BHK) vs. <b>luxury</b> (3.5–4 BHK & above). Strategies must balance affordability with aspirational demand.</p> </div>
        <div><br></div>
        """,unsafe_allow_html=True)

## ----------------------------------------------------------------------------------------


def About_sectors():
    st.markdown(
        """
        <br>
        <div style="background-color:#0B3C73; padding:5px; border-radius:8px; 
        text-align:left !important;">
        <p style="color:#000000; font-size:32px; font-weight:900; font-family: calibri; margin:0;">
        <span style="color: #ffffff;">Sectors</span> of Gurugram
        </p></div>
        <br>
        """, unsafe_allow_html=True)
    
    st.pyplot(myplots.What_all_Sectors_have_Flats_available_for_Sale())

    ## Create 2 sections, first one takes 60% space and other 40% space:
    col1, col2 = st.columns([3,7])
    with col1:
        st.markdown("""
        <style>
        .bullet-font {color:#FFFFFF; font-size:20px; font-weight:200; margin:2px;
        line-height: 1.4 !important; font-family: calibri !important;}
        </style>
        
        <div style="background-color:#080707; padding:8px; border-radius:12px; text-align:center;">
        <p style="color:#D6EAF8; font-size:23px; font-weight:400; margin:5px;"><br></p>
        </div>

        <div>
        <p style="color:#FFFFFF; font-size:20px; font-weight:200; margin:2px; line-height: 1.2; 
        font-family: calibri !important;">
        Gurugram’s Real Estate is spread across distinct Sectors and Belts, each with its own character, affordability, and demand drivers. From heritage clusters to ultra-modern corridors, these Sectors cater to diverse buyers, investors, and developers.
        </p>
         <div style="text-align:center;">
         <p style="color:#FFFFFF; font-size:22px; font-weight:800; margin:2px;"> 
         MAJOR LOCALITIES </p></div>
        
        <ul>
        <li><span style="color:#50FAA0; font-weight:800;">
        Old Gurgaon </span> – Affordable housing, older infrastructure.</li> 
        <li><span style="color:#718FAD; font-weight:800;">
        Dwarka Expressway Belt </span> – Rapidly growing, mid-to-premium demand.</li>
        <li><span style="color:#23D9D9; font-weight:800;">
        MG Road & Central Gurugram </span> – Prime commercial hub, high property costs.</li>
        <li><span style="color:#FF0021; font-weight:800;">
        Golf Course Road & Extension </span> – Luxury segment, top HNI demand.</li>
        <li><span style="color:#003CFF; font-weight:800;">
        Southern Peripheral Road (SPR) Belt </span> – Emerging mid-high market, rising traction.</li>
        <li><span style="color:#7D7D7D; font-weight:800;">
        New Gurugram </span> – Affordable to mid-segment, strong long-term potential.</li> 
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:    ## Plotting Gurgaon sector map...
        st.markdown("""
        <div style="background-color:#080707; padding:8px; border-radius:12px; text-align:center;">
        <p style="color:#D6EAF8; font-size:23px; font-weight:600; margin:5px;">
            Gurugram Map - Sectors & Localities
        </p>
        </div>
        """, unsafe_allow_html=True)
  
        @st.cache_data
        def map_to_html(_m):
            bytes_io = BytesIO()
            _m.save(bytes_io, close_file=False)
            return bytes_io.getvalue().decode()
            
        map_html = map_to_html(myplots.Gurgaon_sector_map_localities())
        st.components.v1.html(map_html, height=600)
    
    ## Sector Segmentation based on - "Affordability" & "Amenity Score" -------------------------
    st.markdown("""
    <style>
    .big-box-style1 {background-color:#080707; padding:5px; border-radius:8px; border:2px solid #FFFFFF;
    color:#ffffff; font-size:23px;}    
    </style>
    
    <div style="background-color:#080707; padding:8px; border-radius:12px; text-align:center;">
    <p style="color:#ffffff; font-size:23px; font-weight:600; margin:5px;">
        Sector Segmentation on 
        <span class = "big-box-style1">Affordability</span> & 
        <span class = "big-box-style1">Sector Amenity Score</span>
    </p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([65,35])
    with col1:
        st.plotly_chart(
            myplots.Can_we_luster_Sectors_based_on_Sector_Affordability_and_Sector_level_Amenities(),
            use_container_width=True, config=dict(displaylogo=False, 
                                                  modeBarButtonsToRemove=["pan2d","zoom2d",                                                "select2d","lasso2d","zoomIn2d","zoomOut2d","autoScale2d",
                                "resetScale2d","toImage"])) 

    with col2:
        st.markdown("""
        <style>
        .small-box-style {background-color:#080707; padding:1.5px; border-radius:4px; 
        border:1px solid #FFFFFF; color:#ffffff;}
        </style>

        <div style="text-align:center;"><br>
        <p style="color:#FFFFFF; font-size:22px; font-weight:800; margin:2px;">
        Sector Segmentation</p></div>

        <div>
        <p style="color:#FFFFFF; font-size:18px; font-weight:200; margin:2px; line-height: 1.2; 
        font-family: calibri !important;">
        Sector Segmentation based on Market Research and Data observed:
        </p></div>
        <ul>
            <li><span class="small-box-style">AFFORDABLE</span>: Less than ₹8,500/Sq.ft</li>
            <li><span class="small-box-style">MID-RANGE</span>: ₹8,500/Sq.ft to ₹12,500/Sq.ft</li>
            <li><span class="small-box-style">EXPENSIVE</span>: ₹12,500/Sq.ft and ₹17,000/Sq.ft</li>
            <li><span class="small-box-style">LUXURY</span>: More than ₹17,000/Sq.ft</li>
        </ul>

        <div>
        <p style="color:#FFFFFF; font-size:18px; font-weight:200; margin:2px; line-height: 1.2; 
        font-family: calibri !important;">
        NOTE: This Segmentation is done based on Median Price Density of Properties of the Sector.
        </p></div>
        
         """, unsafe_allow_html=True)

    ## Some comments on above plot:
    st.markdown(
        """
        <style>
        .med-font {font-size:20px !important; color: #FFFFFF !important; line-height: 1.2 !important;
        font-family: calibri !important;}
        .big-font {font-size:18px !important; color: #FFFFFF !important; line-height: 1.4 !important;
        font-family: calibri !important;}
        </style>
        
        <div class="med-font">
        <p class="big-font"><span style="font-size:28px; font-weight:bold; color:#50FAA0; font-family: calibri !important;">🎯 Sector Amenity vs Affordability — </span> The analysis highlights that <b>price alone does not guarantee livability</b>.</p>
        <ul>
          <li class="med-font">Gurugram shows a mix of sectors where <b>affordability aligns with good amenities</b> and others where <b>premium prices are not fully backed by livability factors</b>.</li>
          <li class="med-font">For buyers and investors, this underscores the importance of evaluating both <b>price density and amenity score together</b>, rather <b>than relying solely on cost</b>.</li>
        </ul>
        </div>
        <div><br></div>
        """,unsafe_allow_html=True)
    

    ## Affordability of Properties across Localities: --------------------------------------------
    st.markdown("""
    <style>
    .big-box-style {background-color:#080707; padding:5px; border-radius:8px; border:2px solid #FFFFFF;
    color:#ffffff;}    
    </style>
    
    <div style="background-color:#080707; padding:8px; border-radius:12px; text-align:center;">
    <p style="color:#D6EAF8; font-size:23px; font-weight:600; margin:5px;">
    <span class = "big-box-style">Affordability of Properties across Localities of Gurugram</span>
    </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.plotly_chart(
            myplots.Distribution_of_Property_Cost_across_6_Major_Localities(),
            use_container_width=True, config=dict(displaylogo=False, 
                                                  modeBarButtonsToRemove=["pan2d","zoom2d",                                                "select2d","lasso2d","zoomIn2d","zoomOut2d","autoScale2d",
                                "resetScale2d","toImage"])) 

    
    ## Adding an Insights Dataframe based on MArket Research and Concluding Comments:
    col1, col2 = st.columns([4,6])
    with col1:
        ## Some comments on above plot:
        st.markdown(
            """
            <style>
            .med-font {font-size:16px !important; font-weight:50; color: #FFFFFF !important; 
            line-height: 1.1 !important; font-family: calibri !important;}
            </style>
            
            <div class="med-font">
            <p class="med-font"><span style="font-size:28px; font-weight:bold; color:#50FAA0; font-family: calibri !important;">✅ Locality-wise Affordability</span><br> The analysis shows a <b>clear segmentation in Gurugram’s housing market</b>:</p>
            <ul>
              <li class="med-font"><b>Golf Course Road &amp; MG Road</b> remain the <b>luxury strongholds</b>, with <b>consistently high price densities</b>.</li>
              <li class="med-font"><b>Dwarka Expressway and New Gurugram</b> are the <b>fastest-growing, high-supply markets</b>, driving <b>affordable-to-mid segment growth</b>.</li>
              <li class="med-font"><b>Old Gurugram</b> caters to <b>budget housing</b>, while <b>SPR Belt</b> is <b>emerging as a premium corridor</b>.</li>
            </ul>
            <p class="med-font">This <b>segmentation highlights</b> Gurugram’s <b><em>Dual Housing Landscape</em></b> — <em>luxury zones for elite buyers and expanding affordable hubs for the wider population</em>.</p>
            </div>
    
            <div><br></div>
            """,unsafe_allow_html=True)
    
    
    ## Render the Styled DataFrame from all_graphs module...
    col2.write(myplots.local_insights_df_func(), unsafe_allow_html=True)


    ## Distribution of Flats across Localities:
    st.markdown("""
    <style>
    .big-box-style {background-color:#080707; padding:5px; border-radius:8px; border:2px solid #FFFFFF;
    color:#ffffff;}    
    </style>
    
    <div style="background-color:#080707; padding:8px; border-radius:12px; text-align:center;">
    <p style="color:#D6EAF8; font-size:23px; font-weight:600; margin:5px;">
    <span class = "big-box-style">
    Distribution of 5 Major Flat Types across 6 Localities of Gurugram</span>
    </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.pyplot(myplots.Distribution_of_5_Major_Flat_Types_across_6_Localities_of_Gurugram())

    ## Some comments on above plot:
    st.markdown(
        """
        <style>
        .med-font {font-size:18px !important; color: #FFFFFF !important; line-height: 1.1 !important;
        font-family: calibri !important;}
        .big-font {font-size:18px !important; color: #FFFFFF !important; line-height: 1.4 !important;
        font-family: calibri !important;}
        </style>
        
        <div class="med-font">
        <p class="big-font"><span style="font-size:28px; font-weight:bold; color:#50FAA0; font-family: calibri !important;">🔍 Flat distribution across Localities — </span> The analysis highlights that <b>3 BHK flats form the backbone of Gurugram’s residential market</b>, cutting across all localities.</p>
        <ul>
          <li class="med-font"><b>New Gurugram and Dwarka Expressway Belt</b> are the <b>fastest-growing hubs</b>, <b>offering both affordability (2 BHKs) and family-centric homes (3 BHKs)</b>.</li>
          <li class="med-font">On the other hand, <b>Golf Course Road &amp; Extension</b> continue to <b>represent Gurugram’s luxury segment</b> with a higher share of <b>4 BHK and premium configurations</b>.</li>
        </ul>
        <p class="med-font">This <b>distribution underscores Gurugram’s dual role</b> as both an <b>affordable housing hub</b> for mid-income families and a <b>luxury destination</b> for elite buyers.</p>
        </div>

        <div><br></div>
        """,unsafe_allow_html=True)

## ----------------------------------------------------------------------------------------

def About_prop_prices():
    st.markdown(
        """
        <br>
        <div style="background-color:#0B3C73; padding:5px; border-radius:8px; 
        text-align:left !important;">
        <p style="color:#000000; font-size:32px; font-weight:900; font-family: calibri; margin:0;">
        <span style="color: #ffffff;">Affordability</span> of  
        <span style="color: #ffffff;">Gurugram</span> Real Estate
        </p></div>
        <br>
        """, unsafe_allow_html=True)

    ## Adding Data Cards:
    col1, col2, col3, col4, col5 = st.columns([1,1,1,1,1])
    
    # Cheapest Prop: 
    value = myplots.cheapest_prop_det()
    col1.metric(label="Cheapest Property", value= value[0], 
                delta=f"Price: ₹ {value[2]}", delta_color="inverse", help=f"Address: {value[1]}")

    # Most Expensive Prop: 
    value = myplots.most_expensive_prop_det()
    col2.metric(label="Most Expensive Property", value= value[0], 
                delta=f"Price: ₹ {value[2]}", delta_color="normal", help=f"Address: {value[1]}")
    
    # Median Property Price in Gurugram:
    value = myplots.med_average_tot_listings()
    col3.metric(label="Median Property Price", value=f"₹ {value[0]}", 
                delta="",delta_color="normal", help="Median Price from all the properties listed")
    col4.metric(label="Average Property Price", value=f"₹ {value[1]}", 
                delta="",delta_color="normal", help="Average Price from all the properties listed")
    col5.metric(label="Total Active Listings", value=value[2], 
                delta="",delta_color="normal", help="Total Units Available for Sale!")


    ## Putting Heading for Plot:
    st.markdown("""
        <style>
        .big-box-style {background-color:#080707; padding:5px; border-radius:8px; 
        border:2px solid #FFFFFF; color:#ffffff;}    
        </style>
        <div><br></div>
        <div style="background-color:#080707; padding:8px; border-radius:12px; text-align:center;">
        <p style="color:#D6EAF8; font-size:23px; font-weight:600; margin:5px;">
        <span class = "big-box-style">Distribution of Properties across Different Price Buckets</span>
        </p>
        </div>
        """, unsafe_allow_html=True)
    
    st.plotly_chart(
            myplots.Price_Buckets_VS_Number_of_Property_listings_cate1(),
            use_container_width=True, config=dict(displaylogo=False, 
                                                  modeBarButtonsToRemove=["pan2d","zoom2d",                                                "select2d","lasso2d","zoomIn2d","zoomOut2d","autoScale2d",
                                "resetScale2d","toImage"])) 

    st.plotly_chart(
            myplots.Price_Buckets_VS_Number_of_Property_listings_cate2(),
            use_container_width=True, config=dict(displaylogo=False, 
                                                  modeBarButtonsToRemove=["pan2d","zoom2d",                                                "select2d","lasso2d","zoomIn2d","zoomOut2d","autoScale2d",
                                "resetScale2d","toImage"])) 
    

    ## Some comments on above plot:
    st.markdown(
        """
        <div style="line-height: 1.2 !important;">
        <p>
        <span style="font-size:28px; font-weight:bold; color:#50FAA0; font-family: calibri !important;">🎯 Property Affordability in Gurugram — </span>
        <span style="font-size:18px; font-weight:bold; font-family: calibri !important;"><b>Gurgaon property market</b> is <b>heavily skewed toward</b> <b><i>affordable to moderate housing (≤ ₹2 Cr)</i></b>, reflecting broader demand patterns of the city.</span>
        </p>
        <ul>
          <li style="font-size:18px; font-weight:bold; font-family: calibri !important;">
          <b>While luxury and ultra-luxury properties exist</b>, they form a <b>niche market</b> with <b>limited buyers</b>.</li>
          <li style="font-size:18px; font-weight:bold; font-family: calibri !important;">
          For sustainable growth, <b>stakeholders should focus</b> on strengthening the <b>affordable and mid-segment housing</b> while <b>maintaining a premium edge</b> in <b>select high-demand sectors</b>.</li>
        </ul>
        </div>
       
        <div><br></div>
        """,unsafe_allow_html=True)
    
## ----------------------------------------------------------------------------------------


def redirecting_to_insights_page():
    st.markdown(
    """
    <div style="background-color:#E0DD5C; padding:5px; border-radius:8px; 
    text-align:left !important;">
    <a href="/insights_mod" target="_self" title="Click me!" 
    style="text-decoration:none; color:#000000; font-size:30px; font-weight:600; margin:0;">
        💡 Check out Some Insights on Gurugram Real Estate - CLICK HERE!
    </a></div>
    """, unsafe_allow_html=True)


## App Starts from here: ------------------------------------------------------------------------
def main():
    ## Introductory heading and content:
    page_content()

    ## First set of Visz:
    About_flats_and_contribution()

    ## Second set of Visz:
    About_price_density_distribution()

    ## Third set of Visz:  
    About_sectors()

    ## Fourth and last set of Visz:
    About_prop_prices() 

    ## Dnne with Analytics...
    ## Link to direct to Insights Page:
    redirecting_to_insights_page()

    
if __name__ == '__main__':
    main()

## ----------------------------------------------------------------------------------

