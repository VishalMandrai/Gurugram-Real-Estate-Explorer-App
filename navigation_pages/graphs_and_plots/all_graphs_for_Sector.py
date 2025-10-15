## Importing necessary tools for Data Manipulation and Visualisation:
import pandas as pd                      ## Pandas for data manipulation
import numpy as np                       ## Numpy for mathematical computation
import matplotlib.pyplot as plt          ## pyplot module of Matplotlib for visualization

import seaborn as sns                    ## Seaborn for visualization
import plotly.graph_objects as go        ## Plotly for dynamic and interactive visualization
import plotly.express as px
from plotly.subplots import make_subplots

from wordcloud import WordCloud          ## For making Word Cloud

import osmnx as ox                        ## For Map work
import folium
from PIL import Image
import warnings
warnings.filterwarnings("ignore")        ## Hides all warnings

## -------------------------------------------------------------------------------------------------

## First Set of Visz: 
## Sector Map with Amenities:
def Gurgaon_sector_map_with_localities(name, coords, amenities):
    ## Extracting lats and Longs from Sector Coordinates:
    sec_latitude, sec_longitude = coords[1:-1].split(', ')
    
    if amenities[~ amenities['amenity'].isin(['Bench', 'Parking', 'Waste Basket'])].shape[0] > 12:
        amenities = amenities[~ amenities['amenity'].isin(['Bench', 'Parking', 'Waste Basket'])]
        
    
    ## Dictionary mapping Amenity Type to similar FontAwesome icons:
    place_icons = {
        "Fuel Station": ("fa", "gas-pump", "red"), "Hospital": ("fa", "hospital", "darkred"),
        "Bank": ("fa", "university", "blue"), "ATM": ("fa", "credit-card", "darkblue"),
        "Pharmacy": ("fa", "medkit", "gray"), "Fast Food": ("fa", "hamburger", "orange"),
        "Parking": ("fa", "parking", "black"), "Place of Worship": ("fa", "place-of-worship", "purple"),
        "Restaurant": ("fa", "utensils", "cadetblue"), "School": ("fa", "school", "lightblue"),
        "Cafe": ("fa", "coffee", "brown"), "Dentist": ("fa", "tooth", "pink"),
        "Bench": ("fa", "chair", "green"), "Waste Basket": ("fa", "trash", "darkgreen"),
        "Clinic": ("fa", "stethoscope", "lightred")      }
    ## -----------------------------------------------------------------------------------------
    ## Step 1: Create folium map, centered on selected "Sector":  
    m = folium.Map(location=[float(sec_latitude), float(sec_longitude)],# Map center on Sector itself...
                   zoom_start=14, no_touch=False , width='100%', height=590, 
                   dragging=True, zoom_control=True, scrollWheelZoom=False, 
                   doubleClickZoom=False, box_zoom=False, touchZoom=False, tiles='OpenStreetMap')
    
    
    ## Step 2: Marking Sector using on Map:
    folium.Marker(
            location=[float(sec_latitude) + 0.0009, float(sec_longitude)],     ## (lat, lon) as (y, x)
            popup= name + " Gurgram,\nHaryana, India",
            tooltip= name,
            icon=folium.Icon(color = 'green', icon="building", prefix="fa")
    ).add_to(m)

    
    folium.Marker(                               ## Annotating Sector Name...
        location= [float(sec_latitude), float(sec_longitude) - 0.003],
        icon=folium.DivIcon(html= f"""<div style="display: inline-block; white-space: nowrap;
                                    font-size: 15px;
                                    font-weight: bold; color: darkred;
                                    background-color: rgba(255,255,255,0.9);
                                    border: 2px solid black; border-radius: 4px;
                                    padding: 4px 4px; box-shadow: 2px 2px 5px rgba(0,0,0,0.3);">
                                    📍{name}
                                    </div>""")
    ).add_to(m)

    
    ## Step 3: Encircle the Sector:
    folium.Circle(location=[float(sec_latitude), float(sec_longitude)], 
                  radius=2700, color='green', fill=True, fill_opacity=0.1, weight=2.5,
                  dash_array="10, 10", fill_color='cyan'
                 ).add_to(m)

    
    ## Step 4: Mark all the Amenities:
    for amenity, amenity_name, position in amenities.values:      
        position = position[7:-1].split()
        if amenity_name is not np.nan:
            folium.Marker(
                location = [float(position[1]), float(position[0])], tooltip = amenity,
                popup = amenity_name, icon=folium.Icon(prefix=place_icons[amenity][0], 
                                               icon=place_icons[amenity][1], 
                                               color=place_icons[amenity][2])
            ).add_to(m)

        else:
            folium.Marker(
                location = [float(position[1]), float(position[0])], tooltip = amenity,
                icon=folium.Icon(prefix=place_icons[amenity][0], icon=place_icons[amenity][1], 
                                 color=place_icons[amenity][2])
            ).add_to(m)    

   
    ## Step 5: return the map
    return m


## Dataframe of Sector Amenities:
def Top_Sector_amenities(data_sec_amenity):
    data_sec_amenity = data_sec_amenity[~ data_sec_amenity['name'].isnull()][['amenity', 'name']]

    data = pd.DataFrame()
    for amenity in ['Hospital', 'School', 'Bank', 'Restaurant']:
        data = pd.concat([data, data_sec_amenity[data_sec_amenity['amenity'] == amenity]], axis=0, 
                         ignore_index=True)
    if data.shape[0] >= 7:
        data.columns = ['Amenity', 'Name']
        return data
    else:
        data = pd.concat([data, 
                          data_sec_amenity[~ data_sec_amenity['amenity'].isin(['Hospital','School', 
                                                                               'Bank','Restaurant'])]],
                         axis=0, ignore_index=True)
        data.columns = ['Amenity', 'Name']
        return data


## ----------------------------------------------------------------------------------------------------
## 2nd set of Visz:

## Adding Data Cards:
def smallest_area_prop_det(data):
    data = data[data['Built_up_area_in_sqft'] == data['Built_up_area_in_sqft'].min()][[
        'Built_up_area_in_sqft','Flat','Address', 'Price']].values
    Area = str(data[0][0]) + " Sq.ft"
    Flat = data[0][1] 
    Address = data[0][2]
    Price = data[0][3]
    return Area, Flat, Address, Price

def largest_area_prop_det(data):
    data = data[data['Built_up_area_in_sqft'] == data['Built_up_area_in_sqft'].max()][[
        'Built_up_area_in_sqft','Flat','Address', 'Price']].values
    Area = str(data[0][0]) + " Sq.ft"
    Flat = data[0][1] 
    Address = data[0][2]
    Price = data[0][3]
    return Area, Flat, Address, Price

def med_average_mod(data):
    desc = data['Built_up_area_in_sqft'].describe()
    median = str(int(desc['50%'])) + " Sq.ft"
    average = str(int(desc['mean'])) + " Sq.ft"
    mode = str(data['Built_up_area_in_sqft'].mode().values[0]) + " Sq.ft"
    return median, average, mode


## Distribution of Built-up Area across 5 Major flats:
def What_is_the_Average_Builtup_Area_across_5_major_Flat_types(data):
    ## Preparing data for analysis:
    five_maj_ft = ["2 BHK Flat", "2.5 BHK Flat", "3 BHK Flat",  "3.5 BHK Flat", "4 BHK Flat"]
    data_1 = data[data['Flat'].isin(five_maj_ft)].groupby(by = 'Flat')['Built_up_area_in_sqft'].mean()

    ## Creating Plot: --------------------------------------------------------------------------------
    fig = plt.figure(figsize = (13,4), dpi = 500)
    ax1 = fig.add_subplot(1,5,(1,2))
    ax2 = fig.add_subplot(1,5,(3,5))
    
    ## Graph 1: --------------------------------------------------------------------------------
    bar = ax1.bar(x = data_1.index, height = data_1.values, color='#91FA99')
    ax1.scatter(x = data_1.index, y = data_1.values, color='red', 
                label='Average Built-up area (in Sq.ft)')
    ax1.plot(data_1.index, data_1.values, color = "white")
    
    ax1.bar_label(bar, labels = np.round(data_1.values,1), padding=10, fontsize=10, color='white',
                  fontweight='bold')
    
    ax1.set_xlabel("Flat", fontsize=14, fontweight='bold', c='white', labelpad=8)
    ax1.set_ylabel("Built-up Area (in Sq.ft)", fontsize=14, fontweight='bold' , c='white')
    
    ax1.set_ylim(0 , data_1.values.max() + 300)
    ax1.set_yticks(range(0, int(data_1.values.max() + 600), 400))
    ax1.set_yticklabels(range(0, int(data_1.values.max() + 600), 400), fontweight = 'bold', 
                        color='white')
    
    ax1.set_xticks(range(len(data_1.index)))
    ax1.set_xticklabels([i[:-5] for i in data_1.index], fontsize=10, fontweight = 'bold', 
                        color='white')

    ax1.legend(loc='upper left')
    
    ## Graph 2: ---------------------------------------------------------------------------------
    ax2 = sns.stripplot(x = data[data['Flat'].isin(five_maj_ft)]['Flat'], 
                        y = data[data['Flat'].isin(five_maj_ft)]['Built_up_area_in_sqft'], 
                        jitter = 0.4, size = 4.5, hue = data[data['Flat'].isin(five_maj_ft)]['Flat'], 
                        palette = 'Dark2', edgecolor='white', linewidth=0.06)
    
    ax2.set_xlabel("Flat", fontsize=14, fontweight='bold', c='white', labelpad=8)
    ax2.set_ylabel("Built-up Area (in Sq.ft)", fontsize=14, fontweight='bold' , 
                   c='white', labelpad=12)
    
    ax2.set_yticks(range(0, 10200, 1400))
    ax2.set_yticklabels(range(0, 10200, 1400), fontweight = 'bold', color='white')
    
    ax2.set_xticks(range(len(data_1.index)))
    ax2.set_xticklabels([i[:-5] for i in data_1.index], fontsize=12, fontweight = 'bold', 
                        color='white')

    fig.patch.set_facecolor("#080707")   # figure background
    ax1.set_facecolor("#080707")        # axes background
    ax2.set_facecolor("#080707")        # axes background
    
    fig.tight_layout()
    
    return fig


## ----------------------------------------------------------------------------------------------------
## 3rd set of Visz:

## Adding Data Cards:
def cheapest_prop_det(data):
    data = data[data['Price_in_rupees'] == data['Price_in_rupees'].min()][['Flat', 
                                                                           'Address', 'Price']].values
    Flat = data[0][0] 
    Address = data[0][1] #[:data[0][1].index(", S") + 1] + '\n' + data[0][1][data[0][1].index(", S") + 2 : ]
    Price = data[0][2]
    return Flat, Address, Price

def most_expensive_prop_det(data):
    data = data[data['Price_in_rupees'] == data['Price_in_rupees'].max()][['Flat', 
                                                                           'Address', 'Price']].values
    Flat = data[0][0] 
    Address = data[0][1] #[:data[0][1].index(", S") + 1] + '\n' + data[0][1][data[0][1].index(", S") + 2 : ]
    Price = data[0][2]
    return Flat, Address, Price

def med_average_tot_listings(data):
    desc = data['Price_in_rupees'].describe()
    median = str(round(desc['50%'] / 1e7 , 2)) + " Cr"
    average = str(round(desc['mean'] / 1e7 , 2)) + " Cr"
    tot_listings = int(desc['count'])
    sector_segment = data['Avg_price_rupee_per_sqft'].median()
    
    if sector_segment < 8500:
        sector_segment = ["Affordable", '< ₹ 8,500/Sq.ft']
    elif sector_segment >= 8500 and sector_segment < 12500:
        sector_segment = ["Mid-Range", '₹ 8,500/Sq.ft to ₹ 12,500/Sq.ft']
    elif sector_segment >= 12500 and sector_segment < 17000:
        sector_segment = ["Expensive", '₹ 12,500/Sq.ft to ₹ 17,000/Sq.ft']
    else:
        sector_segment = ["Luxury", '> ₹ 17,000/Sq.ft']
        
    return median, average, sector_segment
    
    


def Price_density_across_flats(data):
    ## Preparing data for analysis:
    five_maj_ft = ["2 BHK Flat", "2.5 BHK Flat", "3 BHK Flat",  "3.5 BHK Flat", "4 BHK Flat"]
    data = data[data['Flat'].isin(five_maj_ft)]

    ## Creating Plot: --------------------------------------------------------------------------------
    fig = plt.figure(figsize = (12,4), dpi = 500)
    ax = fig.add_subplot(1,1,1)

    ax = sns.swarmplot(y = data[data['Flat'].isin(five_maj_ft)]['Flat'], 
                       x = data[data['Flat'].isin(five_maj_ft)]['Avg_price_rupee_per_sqft'], 
                       size = 3.8, hue = data[data['Flat'].isin(five_maj_ft)]['Flat'].sort_values(), 
                       legend='full', hue_order = five_maj_ft, palette = 'Set2', edgecolor='white', 
                       linewidth=0.05, order = five_maj_ft)
    
    ax.set_ylabel("Flat", fontsize=15, fontweight='bold', c='white', labelpad=8)
    ax.set_xlabel("Property Price Density (in ₹/Sq.ft)", fontsize=15, fontweight='bold' , c='white', 
                  labelpad=12)

    x_max = data['Avg_price_rupee_per_sqft'].max()
    x_min = int(data['Avg_price_rupee_per_sqft'].min() - 1000)
    
    if str(x_min)[-3:] != "000":
        x_min = int(str(x_min)[:-3] + "000")
        
    ax.set_xlim(x_min, int(x_max + 2000))
    ax.set_xticks(range(x_min, int(x_max + 2000), 5000))
    ax.set_xticklabels([str(i)[:-3] + ',' + str(i)[-3:] if i != 0 else i 
                        for i in range(x_min, int(x_max + 2000), 5000)], fontweight = 'bold', 
                       color='white')
    
    ax.set_yticks(range(len(five_maj_ft)))
    ax.set_yticklabels([i[:-5] for i in five_maj_ft], fontsize=12, fontweight = 'bold', 
                       color='white')
    
    ax.legend(fontsize=12, loc = 'upper right', fancybox=True, framealpha=1,
              edgecolor="white", facecolor='#080707', labelcolor="white")
    
    fig.tight_layout()
    fig.patch.set_facecolor("#080707")   # figure background
    ax.set_facecolor("#080707")        # axes background
    
    return fig


## ------------------------------------------------------------------------------------------------
## 4th Set of Visz:
## Wordcloud of the Developers and Socities of the Sector:
def Wordclouds_developers_and_socities(data):
    ## Preparing data for analysis:
    data = data[(data["Seller_Builder"] != '-') & (data["Society"] != '-')]
    sector = data['Sector'].unique()[0]
    data_developers = pd.DataFrame(data["Seller_Builder"].value_counts()).reset_index()
    data_socities = pd.DataFrame(data["Society"].value_counts()).reset_index()
    
    ## Creating plot: --------------------------------------------------------------------------------
    fig = plt.figure(figsize = (9, 6), dpi = 500)
    ax1 = fig.add_subplot(1,2,1)
    ax2 = fig.add_subplot(1,2,2)
    bbox={'facecolor': 'black', 'edgecolor': 'white', 'boxstyle': 'round, pad=0.2', 'linewidth': 1}
    
    ## Developers: -------------------------------------------------------------------------------------
    wc1 = WordCloud(width=2000, height=550, background_color="#080707",
                   colormap="prism",             # color palette
                   contour_color="black",          # outline color
                   contour_width=10,                # outline thickness
                   max_words=500,                  # limit words
                   max_font_size=120,               # largest word size
                   min_font_size=50,               # smallest word size
                   prefer_horizontal=1, random_state=32)

    wc1.generate_from_frequencies(data_developers.set_index("Seller_Builder")["count"].to_dict())
    
    ax1.imshow(wc1, interpolation="bilinear")
    ax1.set_title(f'DEVELOPERS OF SECTOR {sector.split()[1]}', fontsize=15, fontweight='bold', 
                  color='white', fontfamily='Calibri', bbox=bbox, pad=8)
    
    ## Socities: -------------------------------------------------------------------------------------
    wc2 = WordCloud(width=2000, height=550, background_color="#080707",
                   colormap="prism",             # color palette
                   contour_color="black",          # outline color
                   contour_width=10,                # outline thickness
                   max_words=500,                  # limit words
                   max_font_size=120,               # largest word size
                   min_font_size=50,               # smallest word size
                   prefer_horizontal=1, random_state=35)
                    
    wc2.generate_from_frequencies(data_socities.set_index("Society")["count"].to_dict())
    ax2.imshow(wc2, interpolation="bilinear")
    ax2.set_title(f'SOCITIES OF SECTOR {sector.split()[1]}', fontsize=15, fontweight='bold', 
                  color='white', fontfamily='Calibri', bbox=bbox, pad=8)

    ax1.set_xticks(range(0))
    ax1.set_yticks(range(0))
    ax2.set_xticks(range(0))
    ax2.set_yticks(range(0))
    
    for spline in ['top', 'bottom', 'left', 'right']:
            ax1.spines[spline].set_color('#242323')
            ax1.spines[spline].set_linewidth(0.5)
            ax2.spines[spline].set_color('#242323')
            ax2.spines[spline].set_linewidth(0.5)
        
        
    fig.patch.set_facecolor("#080707")   # figure background
    fig.tight_layout()
    return fig


## ------------------------------------------------------------------------------------------------
## ------------------------------------------------------------------------------------------------








