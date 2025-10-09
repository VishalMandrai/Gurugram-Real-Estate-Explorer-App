import streamlit as st
import pandas as pd
import numpy as np
from io import BytesIO

from navigation_pages.graphs_and_plots import all_graphs_for_Sector as myplots  
                                                                              # Have all graphing code!

## Importing dataset to be used:
## 1. Main Dataframe with all properties data for analysis:
df = pd.read_csv('navigation_pages/graphs_and_plots/Housing_Listings_all_records_(numbers)_FINAL_Cleaned_FE.csv', 
                 index_col='Unnamed: 0')
data = df[df['Sector'] != '-']

## 2. Sector Geo Data:
geo_sec = pd.read_csv('navigation_pages/graphs_and_plots/sector_geo_centroid_data.csv', index_col='Unnamed: 0')
geo_sec['Locality'] = geo_sec['Locality'].replace({'Southern Peripheral Road (SPR) Belt' : 
                                                   'Southern Peripheral Road Belt'})

## 3. Gurugram Amenity Geo Data:
sec_amenity = pd.read_csv('navigation_pages/graphs_and_plots/Amenity_with_Closest_Sectors_data.csv', index_col='Unnamed: 0')

renamer = {
        "fuel": "Fuel Station", "hospital": "Hospital", "bank": "Bank", "atm": "ATM",
        "pharmacy": "Pharmacy", "fast_food": "Fast Food", "parking": "Parking", 
        "place_of_worship": "Place of Worship", "restaurant": "Restaurant", "school": "School", 
        "cafe": "Cafe", "dentist": "Dentist", "bench": "Bench", "waste_basket": "Waste Basket",
        "clinic":"Clinic"}
sec_amenity['amenity'] = sec_amenity['amenity'].replace(renamer)

## --------------------------------------------------------------------------------------------------

## Sorting all the Sectors numerically:
def sort_sec(sector):
        x = sector.split()[-1]
        if x[-1].isdigit():
            return int(x)
        elif x[-1] == 'A':
            return int(x[0:-1]) + 0.1
        elif x[-1] == 'B':
            return int(x[0:-1]) + 0.2
        elif x[-1] == 'C':
            return int(x[0:-1]) + 0.3
        elif x[-1] == 'D':
            return int(x[0:-1]) + 0.4

sectors = pd.Series(data['Sector'].unique())
sector_order = sectors.apply(sort_sec)

## Sorted List of all the Sectors:
sector_list = pd.concat([sectors, sector_order], axis=1).sort_values(by=1)[0].values
del sectors, sector_order    ## To free unnecessary space...

## ----------------------------------------------------------------------------------------------
## ----------------------------------------------------------------------------------------------

def page_content():
    ## Title of Page:
    st.markdown(
        """<h1 style='text-align: center; color: white;'> 
        📍 Sectors of Gurugram - Know Everything!
        </h1>""",
        unsafe_allow_html=True)
    
    ## Analytics Module heading in the box:
    st.markdown(
        """<div style="background-color:#6DFF66; padding:3px; 
        border-radius:5px; text-align:center;"></div>
        
        """, unsafe_allow_html=True)


## -----------------------------------------------------------------------------------------------

def About_builtup_area_distribution(data):
    st.markdown("""
    <div style="background-color:#6BFF72; padding:1px; border-radius:4px; 
    text-align:left;">
    <p style="color:#000000; font-size:30px; font-weight:600; margin:0;">
    <span style="font-size:30px; font-weight:bold; color:#5C250B; 
    font-family: calibri !important;">Built-up Area</span> & 
    <span style="font-size:30px; font-weight:bold; color:#5C250B; 
    font-family: calibri !important;">Flats</span>
    </p> </div>
    <div><br></div>
    """, unsafe_allow_html=True)


    ## Adding Data Cards:
    col1, col2, col3, col4, col5 = st.columns([1,1,1,1,1])
    
    # Smallest Prop by Size: 
    value = myplots.smallest_area_prop_det(data)
    col1.metric(label="Smallest Built-Up Area", value= value[0], 
                delta=f"Price: ₹ {value[3]}", delta_color="inverse", 
                help=f"Flat: {value[1]} - {value[2]}")

    # Largest Prop by size: 
    value = myplots.largest_area_prop_det(data)
    col2.metric(label="Largest Built-Up Area", value= value[0], 
                delta=f"Price: ₹ {value[3]}", delta_color="normal", 
                help=f"Flat: {value[1]} - {value[2]}")
    
    # Median Property Price in Gurugram:
    value = myplots.med_average_mod(data)
    col3.metric(label="Median Built-Up Area", value=value[0],
                help="Median Built-Up Area from all the properties listed")
    col4.metric(label="Average Built-Up Area", value=value[1], 
                help="Average Built-Up Area from all the properties listed")
    col5.metric(label="Most Frequent Size", value=value[2], 
                help="Most Frequent Size of all the properties listed!")
    
    ## Adding Flat vs Flat Size distribution plot:
    st.markdown("""
    <style>
    .big-box-style {background-color:#080707; padding:5px; border-radius:8px; 
    border:2px solid #FFFFFF; color:#ffffff;}    
    </style>
    <div><br></div>
    <div style="background-color:#080707; padding:5px; border-radius:12px; text-align:center;">
    <p style="color:#D6EAF8; font-size:23px; font-weight:600; margin:2px;">
    <span class = "big-box-style">Built-Up Area across Flats</span>
    </p></div>
    """, unsafe_allow_html=True)
    st.pyplot(myplots.What_is_the_Average_Builtup_Area_across_5_major_Flat_types(data))


## -----------------------------------------------------------------------------------------------

def About_prop_prices(data):
    st.markdown("""
    <div style="background-color:#6BFF72; padding:1px; border-radius:4px; 
    text-align:left;">
    <p style="color:#000000; font-size:30px; font-weight:600; margin:0;">
    <span style="font-size:30px; font-weight:bold; color:#5C250B; 
    font-family: calibri !important;">Property Price </span> & 
    <span style="font-size:30px; font-weight:bold; color:#5C250B; 
    font-family: calibri !important;">Price Density Distribution</span> across
    <span style="font-size:30px; font-weight:bold; color:#5C250B; 
    font-family: calibri !important;">Sector</span>
    </p> </div>
    <div><br></div>
    """, unsafe_allow_html=True)

    ## Adding Data Cards:
    col1, col2, col3, col4, col5 = st.columns([1,1,1,1,1])
    
    # Cheapest Prop: 
    value = myplots.cheapest_prop_det(data)
    col1.metric(label="Cheapest Property", value= value[0], 
                delta=f"Price: ₹ {value[2]}", delta_color="inverse", help=f"Address: {value[1]}")

    # Most Expensive Prop: 
    value = myplots.most_expensive_prop_det(data)
    col2.metric(label="Most Expensive Property", value= value[0], 
                delta=f"Price: ₹ {value[2]}", delta_color="normal", help=f"Address: {value[1]}")
    
    # Median Property Price in Gurugram:
    value = myplots.med_average_tot_listings(data)
    col3.metric(label="Median Property Price", value=f"₹ {value[0]}", 
                delta="",delta_color="normal", help="Median Price from all the properties listed")
    col4.metric(label="Average Property Price", value=f"₹ {value[1]}", 
                delta="",delta_color="normal", help="Average Price from all the properties listed")
    col5.metric(label="Sector Segment", value=value[2][0], 
                delta=value[2][1], delta_color="normal", 
                help="Based on Median Price Density in Sector")

    ## Price DEnsity Distribution:
    st.markdown("""
    <style>
    .big-box-style {background-color:#080707; padding:5px; border-radius:8px; border:2px solid #FFFFFF;
    color:#ffffff;}    
    </style>
    
    <div style="background-color:#080707; padding:8px; border-radius:12px; text-align:center;">
    <p style="color:#D6EAF8; font-size:23px; font-weight:600; margin:5px;">
    <span class = "big-box-style">Price Density Distribution across Flats</span>
    </p></div>
    """, unsafe_allow_html=True)
    
    st.pyplot(myplots.Price_density_across_flats(data))

## ----------------------------------------------------------------------------------------------

def Seller_builders_and_socities(data):
    st.markdown("""
    <div style="background-color:#6BFF72; padding:1px; border-radius:4px; 
    text-align:left;">
    <p style="color:#000000; font-size:30px; font-weight:600; margin:0;">
    <span style="font-size:30px; font-weight:bold; color:#5C250B; 
    font-family: calibri !important;">Sellers</span>, 
    <span style="font-size:30px; font-weight:bold; color:#5C250B; 
    font-family: calibri !important;">Builders</span> & 
    <span style="font-size:30px; font-weight:bold; color:#5C250B; 
    font-family: calibri !important;">Socities</span> of Sector
    </p> </div>
    <div style="color:#000000; font-size:5px;"><br></div>
    """, unsafe_allow_html=True)

    st.pyplot(myplots.Wordclouds_developers_and_socities(data))

## ----------------------------------------------------------------------------------------------


def link_directing_to_price_pred_model():
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
    
        <div><br></div><div><br></div>
        
        <div style = "display: flex; justify-content: center; align-items: center;">
        <button class="btn-tooltip" 
        style="background-color:#C0EBB5; color:#ffffff; border:4px solid #ffffff; border-radius:6px; 
        padding:8px 300px; font-size:26px; font-weight:800; cursor:pointer;"
        data-tooltip="This button takes you to try our Price Prediction Model!" >
        <a href="/price_pred" target="_self" style="color:#000000;">
        Price Prediction Model - CLICK HERE!
        </a>
        </button></div>
        """, unsafe_allow_html=True )


def main():
    ## Introductory heading and content:
    page_content()

    ## Create 2 Sections: 
    ## 1. Select Sector from the drop down box + Some basic info about the selected Sector.
    ## 2. Plot that Sector on Map with all surrounding Amenities.

    about_sector, map_work = st.columns([4,6])
    with about_sector:
        st.markdown("""
        <div style="background-color:#6BFF72; padding:1px; border-radius:4px; 
        text-align:center;">
        <p style="color:#000000; font-size:30px; font-weight:600; margin:0;"> 
        Choose the
        <span style="font-size:28px; font-weight:bold; color:#5C250B; font-family: calibri !important;">
        SECTOR</span></p>
        </div>

        <div><p style="font-size:0.5px;"><br></p></div>
     
        <style>
        div[data-baseweb="select"] > div {
            background-color: #000000; color: white;  border-radius: 5px; padding:0px 0px;
            font-size: 20px; font-weight: 600; font-family: calibri;                            }
        </style>
        """, unsafe_allow_html=True)
    
        default_sec = np.where(sector_list == 'Sector 65')[0][0] # Selecting "Sector 65" as default...
        sector = st.selectbox("", sector_list, placeholder="Choose the Sector", index=int(default_sec),
                             label_visibility="collapsed")

        ## Now, Filtering data as per the Selected "Sector": ---------------------------------------
        data_sec = data[data['Sector'] == sector]                  
        data_geo_sec = geo_sec[geo_sec['Sector'] == sector]          ## Sector Centroid & Locality

        def sec_checker(row):                   # Filtering Amenities in the Sector for "Map work"...
            sectors = row['Closest_Sectors']
            lis_sects = sectors[2:-3].split(", (")[0::2]
            
            ## check if the Sector is found in the list: 
            if f"'{sector}'" in lis_sects:
                return True
            else:
                return False
        
        data_sec_amenity = sec_amenity[sec_amenity.apply(sec_checker, axis = 1)][['amenity', 
                                                                                  'name', 'point']]

        ## -----------------------------------------------------------------------------------------

        ## Basic Info about "Sector": (1) locality, (2) Number of Listings & (3) Sector Amenity Score
        ## (1) Locality of Sector
        st.markdown("""
        <style> .big-box-style {background-color:#080707; padding:8px 12px; border-radius:8px; 
        border:2px solid #FFFFFF; color:#ffffff;} </style>""" + """
        <div style="background-color:#080707; padding:1px; border-radius:12px; text-align:center;">
        <p style="color:#D6EAF8; font-size:20px; font-weight:600; margin:5px;">
        <span class = "big-box-style">Locality: {}</span>
        </p></div> <div><br></div>""".format(data_geo_sec['Locality'].iloc[0]), 
                    unsafe_allow_html=True)
        
        ## (2) Number of Listings & (3) Sector Amenity Score
        card1, card2 = st.columns([5,5])
        ## Number of Property Listings: 
        tot_listings = data_sec.shape[0]
        card1.metric(label="Total Property Listings", value= tot_listings, 
                    delta=f"Out of {df.shape[0]}", delta_color="normal", 
                    help=f"Total Number of Properties Listed up for Sale in {sector}.")
    
        ## Sector Amenity Score: 
        amenity_score = data_sec['Sector_Amenity_Score'].unique()[0]
        card2.metric(label="Sector Amenity Score", value= amenity_score, delta="Out of 10", 
                     delta_color="normal", help=f"Sector Amenity Score of {sector} out of 10.")

        ## Adding DF of Top Amenities of Sector:
        st.dataframe(myplots.Top_Sector_amenities(data_sec_amenity), height=300, hide_index=False)


    ## 2nd Part: ----------------------------------------------------------------------------------
    with map_work:
        def map_to_html(_m):
            bytes_io = BytesIO()
            _m.save(bytes_io, close_file=False)
            return bytes_io.getvalue().decode()
            
        map_html = map_to_html(
            myplots.Gurgaon_sector_map_with_localities(sector, 
                                                       data_geo_sec['Location_(lat_long)'].iloc[0], 
                                                       data_sec_amenity))
        st.components.v1.html(map_html, height=600)

    ## -------------------------------------------------------------------------------------------

    ## Sector level data about Built-up Area and Distribution:
    About_builtup_area_distribution(data_sec)


    ## Sector level property Price distribution and Trends:
    About_prop_prices(data_sec)

    ## Analysis about Seller/Builders & Societies:
    Seller_builders_and_socities(data_sec)

    ## Finally!! Directing to Price Prediction Model:
    link_directing_to_price_pred_model()

    

if __name__ == "__main__":
    main()

