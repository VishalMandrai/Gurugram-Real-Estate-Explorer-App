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
import random
from shapely.geometry import MultiPoint, Polygon, mapping, Point
import alphashape
                                          
from PIL import Image
import warnings
warnings.filterwarnings("ignore")        ## Hides all warnings
## -------------------------------------------------------------------------------------------------

## Importing dataset to be used:
df = pd.read_csv('navigation_pages/graphs_and_plots/Housing_Listings_all_records_(numbers)_FINAL_Cleaned_FE.csv', 
                 index_col = 'Unnamed: 0')

## -------------------------------------------------------------------------------------------------
## First set of Visz:
def What_are_the_different_kinds_of_Flats_available_for_sale_in_Gurgaon():
    ## Creating a TreeMap:
    fig = px.treemap(df, path=[px.Constant('Gurugram'),'Flat'], 
                     values = pd.Series(np.ones(7143)).astype('int8'),
                     color = 'Flat' , color_continuous_scale='Viridis')
    
    fig.update_layout(autosize=True, height=380, margin=dict(l=10, r=10, t=40, b=10),
                      #title=dict(text="<b>🏙  FLAT TYPES & DISTRIBUTION</b>",
                      #           font=dict(size=28, color="white", family='Calibri'),
                      #           x = 0,  # center title
                      #           pad=dict(t=50, b=0, l=20, r=20)),
                      plot_bgcolor="#080707",  # area inside axes
                      paper_bgcolor="#080707"    # outside area
                     )
    
    fig.update_traces(textinfo="label",
                      hovertemplate='''<b>%{label}</b><br>Count: %{value}<br>City: %{parent}
                                      <extra></extra>''',
                      textfont=dict(size=22, color="black", family="Calibri black"),
                      textposition="middle center",
                      tiling=dict(pad=2),  # extra padding between boxes
                     )
    return fig


def What_is_the_portion_of_each_Flat_type_in_the_overall_flat_market():
    fig = plt.figure(figsize = (14, 3.5), dpi=500)
    ax1 = fig.add_subplot(1, 3, (1,2))
    ax2 = fig.add_subplot(1, 3, 3)
    bbox={'facecolor': 'lightblue', 'edgecolor': 'white', 'boxstyle': 'round, pad=0.2', 'linewidth': 1}
    
    top_6_data = df['Flat'].value_counts().sort_values(ascending = False).head(6)
    other_data = df['Flat'].value_counts().sort_values(ascending=False)[6:].sum()
    data_pie = pd.concat([top_6_data, pd.Series([other_data], index = ['Others →'])])
    
    wedges, texts, autotexts = ax1.pie(x = data_pie, labels = data_pie.index , autopct='%0.1f%%', 
                                       pctdistance=0.8, shadow=True, labeldistance = 1.12, radius=1.1,                                   
                                       wedgeprops ={'linewidth':1 , 'edgecolor':'black', 'width':0.5})
    for t in texts:
        t.set_fontsize(10)
        t.set_color('white')
        t.set_fontweight('bold')
    
    for at in autotexts:
        at.set_fontsize(8)
        at.set_fontweight('bold')
        at.set_color('white')
    
    
    other_flats = df['Flat'].value_counts().sort_values(ascending=False)[6:]
    bar = ax2.barh(other_flats.index , other_flats , color='#FFAA33')
    
    ax2.set_title('Other Flat Types', fontsize=12, fontweight='bold', color='white')
    ax2.set_yticks(list(range(0,6)))
    ax2.set_yticklabels(other_flats.index, fontsize=10, color='white', fontweight='bold')
    ax2.set_xlim(0, 100)
    ax2.set_xticks(list(range(0,101, 20)))
    ax2.set_xticklabels(list(range(0,101, 20)), fontsize=10, color='white', fontweight='bold')
    
    percent_of_total_flat = round((other_flats / (data_pie.sum())) * 100 , 2).apply(lambda x: str(x) + "%")
    ax2.bar_label(bar, labels = percent_of_total_flat, padding=2, fontsize=10, color='white',
                  fontweight='bold')
    
    #fig.suptitle("Distribution of each Flat Type" , fontweight = 'bold', fontsize = 20, 
    ##             color = '#000000', ha='center', x=0.56, y=1.05,)
    
    fig.patch.set_facecolor("#080707")   # figure background
    ax1.set_facecolor("#080707")        # axes background
    ax2.set_facecolor("#080707")        # axes background
    
    ## Change spine (axis line) colors
    #for border in ['bottom','left','top','right']:
    #    ax2.spines[border].set_color("white")       
    return fig

## ----------------------------------------------------------------------------------------------------
## 2nd set of Visz:

## Adding Data Cards:
def smallest_area_prop_det():
    data = df[df['Built_up_area_in_sqft'] == df['Built_up_area_in_sqft'].min()][[
        'Built_up_area_in_sqft','Flat','Address', 'Price']].values
    Area = str(data[0][0]) + " Sq.ft"
    Flat = data[0][1] 
    Address = data[0][2]
    Price = data[0][3]
    return Area, Flat, Address, Price

def largest_area_prop_det():
    data = df[df['Built_up_area_in_sqft'] == df['Built_up_area_in_sqft'].max()][[
        'Built_up_area_in_sqft','Flat','Address', 'Price']].values
    Area = str(data[0][0]) + " Sq.ft"
    Flat = data[0][1] 
    Address = data[0][2]
    Price = data[0][3]
    return Area, Flat, Address, Price

def med_average_mod():
    desc = df['Built_up_area_in_sqft'].describe()
    median = str(int(desc['50%'])) + " Sq.ft"
    average = str(int(desc['mean'])) + " Sq.ft"
    mode = str(df['Built_up_area_in_sqft'].mode().values[0]) + " Sq.ft"
    return median, average, mode


## Distribution of Built-up Area across 5 Major flats:
def What_is_the_Average_Builtup_Area_across_5_major_Flat_types():
    ## Preparing data for analysis:
    five_maj_ft = ["2 BHK Flat", "2.5 BHK Flat", "3 BHK Flat",  "3.5 BHK Flat", "4 BHK Flat"]
    data = df[df['Flat'].isin(five_maj_ft)].groupby(by = 'Flat')['Built_up_area_in_sqft'].mean()

    ## Creating Plot: --------------------------------------------------------------------------------
    fig = plt.figure(figsize = (13,4.5), dpi = 500)
    ax1 = fig.add_subplot(1,5,(1,2))
    ax2 = fig.add_subplot(1,5,(3,5))
    bbox={'facecolor': 'lightblue', 'edgecolor': 'white', 'boxstyle': 'round, pad=0.2', 'linewidth': 1}
    
    #fig.suptitle("5 Major Flat Type VS Built-up Area (in Sq.ft)" , 
    #              fontweight = 'bold', fontsize = 22, color = '#000000', ha='center', x=0.5, y=1.0)
    
    ## Graph 1: ---------------------------------------------------------------------------------------
    bar = ax1.bar(x = data.index, height = data.values, color='#45D971')
    ax1.scatter(x = data.index, y = data.values, color='red', label='Average Built-up area (in Sq.ft)')
    ax1.plot(data.index, data.values, color = "white")
    
    ax1.bar_label(bar, labels = np.round(data.values,1), padding=10, fontsize=10, color='white',
                  fontweight='bold')
    
    ax1.set_xlabel("Flat", fontsize=14, fontweight='bold', c='white', labelpad=8)
    ax1.set_ylabel("Built-up Area (in Sq.ft)", fontsize=14, fontweight='bold' , c='white')
    
    ax1.set_ylim(0 , data.values.max() + 300)
    ax1.set_yticks(range(0, int(data.values.max() + 600), 400))
    ax1.set_yticklabels(range(0, int(data.values.max() + 600), 400), fontweight = 'bold', 
                        color='white')
    
    ax1.set_xticks(range(len(data.index)))
    ax1.set_xticklabels([i[:-5] for i in data.index], fontsize=10, fontweight = 'bold', color='white')

    ax1.legend(loc='upper left')
    
    ## Graph 2: ---------------------------------------------------------------------------------------
    
    ax2 = sns.stripplot(x = df[df['Flat'].isin(five_maj_ft)]['Flat'], 
                        y = df[df['Flat'].isin(five_maj_ft)]['Built_up_area_in_sqft'], jitter = 0.4, 
                        size = 2.5, hue = df[df['Flat'].isin(five_maj_ft)]['Flat'], order=five_maj_ft,
                        palette = 'Dark2', edgecolor='white', linewidth=0.06)
    
    ax2.set_xlabel("Flat", fontsize=14, fontweight='bold', c='white', labelpad=8)
    ax2.set_ylabel("Built-up Area (in Sq.ft)", fontsize=14, fontweight='bold' , c='white', labelpad=12)
    
    ax2.set_yticks(range(0, 10200, 1400))
    ax2.set_yticklabels(range(0, 10200, 1400), fontweight = 'bold', color='white')
    
    ax2.set_xticks(range(len(five_maj_ft)))
    ax2.set_xticklabels([i[:-5] for i in five_maj_ft], fontsize=12, fontweight = 'bold', color='white')

    fig.patch.set_facecolor("#080707")   # figure background
    ax1.set_facecolor("#080707")        # axes background
    ax2.set_facecolor("#080707")        # axes background
    
    fig.tight_layout()
    
    return fig



## ----------------------------------------------------------------------------------------------------
## 3rd set of Visz:
def What_all_Sectors_have_Flats_available_for_Sale():
    ## Preparing data for analysis:
    data = df[df['Sector'] != '-']
    data = pd.DataFrame(data["Sector"].value_counts()).reset_index()
    
    ## Creating plot: ---------------------------------------------------------------------
    fig = plt.figure(figsize = (12, 4), dpi = 500)
    ax = fig.add_subplot(1,1,1)
    
    wc = WordCloud(width=3800, height=1000, background_color="#080707",
                   colormap="prism",             # color palette
                   contour_color="black",          # outline color
                   contour_width=10,                # outline thickness
                   max_words=800,                  # limit words
                   max_font_size=180,               # largest word size
                   min_font_size=40,               # smallest word size
                   prefer_horizontal=0.75,          # orientation of words
                   random_state=32)
    wc.generate_from_frequencies(data.set_index("Sector")["count"].to_dict())
    
    ax.imshow(wc, interpolation="bilinear")
    ax.axis("off")
    fig.patch.set_facecolor("#080707")
    fig.tight_layout()

    return fig

## Sector Map with Localities:
def Gurgaon_sector_map_localities():
    ## Using already collected Geo Spatial data: 
    sec_location = pd.read_csv('navigation_pages/graphs_and_plots/sector_geo_centroid_data.csv', index_col = 'Unnamed: 0')
    sec_location['latitude'] = sec_location['Location_(lat_long)'].apply(lambda x: x[1:-1].split(', ')[0])
    sec_location['longitude'] = sec_location['Location_(lat_long)'].apply(lambda x: x[1:-1].split(', ')[1])

    ## Create and Plot Convex Hull of Localities:
    def enclosing_polygons_map(m, geo_data, localities_w_colors):
        """
        Build convex-hull polygon around input (lat, lon) points
        and render them on a Folium map.
        Returns (folium.Map).
        """
        localities_polygons = []
        
        for locality in localities_w_colors.keys():
            sec_geo_coords = geo_data[geo_data['Locality'] == locality][[
                'latitude','longitude']].astype({'latitude':'float', 'longitude':'float'}).values
    
            if len(sec_geo_coords) < 3:
                raise ValueError("At least 3 points are required to form a polygon")
    
            ## Create Convex hull (guaranteed to enclose all points):
            lon_lat_points = [(lon, lat) for lat, lon in sec_geo_coords]
            hull = MultiPoint(lon_lat_points).convex_hull       # shapely Polygon or LineString
            if hull.geom_type != "Polygon":
                ## Handle collinear or 2-point edge cases
                hull = hull.buffer(1e-9)

            localities_polygons.append(tuple([locality, hull]))

        ## List of Geo-Polygons of Localities of Gurugram:
        localities = localities_polygons
        
        ## Removing the area of "New Gurugram" from "Old Gurgaon":
        intersection = localities[5][1].intersection(localities[3][1])
        revised_old_gurgaon = localities[5][1].difference(intersection)

        ## Removing overlapping regions of "MG Road" and "Golf Course areas":
        intersection = localities[1][1].intersection(localities[4][1])
        revised_mg_road = localities[1][1].difference(intersection)
        revised_golf_course = localities[4][1].difference(intersection)
        
        ## Upadting the List:
        localities[5] = ('Old Gurgaon', revised_old_gurgaon)
        #localities[1] = ('MG Road & Central Gurugram', revised_mg_road)
        #localities[4] = ('Golf Course Road & Extension', revised_golf_course)
                
        ## Style and Add Polygons (GeoJSON expects [lon, lat] order)
        def add_poly(geom, name, color, fill_color, opacity=0.9, fill_opacity=0.20):
            gj = folium.GeoJson(
                data=mapping(geom),
                name=name,
                style_function=lambda feat: {"color": color,"weight": 3,"opacity": opacity,
                                             "fillColor": fill_color,
                                             "fillOpacity": fill_opacity})
            folium.Popup(name).add_to(gj)
            gj.add_to(m)               

        for locality, shape in localities:
            add_poly(shape, locality, color=localities_w_colors[locality], 
                     fill_color=localities_w_colors[locality])

            
    ## -------------------------------------------------------------------------------------
    ## Plotting all the Sectors on Map - using scrapped Geo Centroids:
    sectors_list = sec_location[['Sector', 'Location_(lat_long)', 'Locality']].values
    sec_local_color = {'Dwarka Expressway Belt':'cadetblue',
                       'MG Road & Central Gurugram':'blue',
                       'Southern Peripheral Road (SPR) Belt':'darkblue', 
                       'New Gurugram':'gray', 
                       'Golf Course Road & Extension':'red', 'Old Gurgaon':'green'}
    
    ## Step 1: Create folium map centered on "Sector 10A":
    map_center = sec_location[sec_location['Sector'] == 'Sector 10A']      ## Map center...
    
    m = folium.Map(location=[float(map_center['latitude'].iloc[0]) - 0.01, 
                             float(map_center['longitude'].iloc[0]) - 0.004], 
                   zoom_start=11.5, no_touch=False , width='100%', height=690, 
                   dragging=False, zoom_control=False, scrollWheelZoom=False, 
                   doubleClickZoom=False, box_zoom=False, touchZoom=False, tiles='OpenStreetMap')
    
    
    ## Step 2: Marking Sectors using Geo Coordinates on Map:
    for sector, point, locality in sectors_list: 
        location_name = sector + ", Gurugram, Haryana, India"
        point = point[1:-1].split(', ')
    
        # Step 3: Add a marker
        folium.Marker(
            location=[point[0], point[1]],  ## (lat, lon) as (y, x)
            popup=location_name + '\n(' + locality + ')',
            tooltip=location_name + '\n(' + locality + ')',
            icon=folium.Icon(color = sec_local_color[locality], icon="info-sign")).add_to(m)
     
    ## Step 3: Adding borders around Localities: 
    enclosing_polygons_map(m, sec_location, localities_w_colors = sec_local_color)
    
    
    ## Step 4: Adding Gurugram boundary:
    gdf = ox.geocode_to_gdf("Gurugram, Haryana, India")
    
    city_boundary = folium.GeoJson(gdf.geometry.__geo_interface__, name="Gurgaon Boundary",
                                   style_function=lambda x: {"color": "black", "weight": 3, 
                                                             "fill": False},)
    folium.Popup("Gurgaon Boundary").add_to(city_boundary)
    city_boundary.add_to(m)
    
    ## Step 4: Save or show the map
    return m


## Clustering Sectors based on Affordability & Amenity Score:
def Can_we_luster_Sectors_based_on_Sector_Affordability_and_Sector_level_Amenities():
    ## Preparing data:
    data = df[df["Sector"] != '-']
    data = data.groupby(by='Sector')[['Avg_price_rupee_per_sqft', 
                                      'Sector_Amenity_Score']].agg({'Avg_price_rupee_per_sqft':'median',
                                                                  'Sector_Amenity_Score':'median'})
    ## Using Segementation Criterions:
    q1 = 8500
    q2 = 12500
    q3 = 17000
    
    ## Creating plot: -----------------------------------------------------------------------------------
    fig = go.Figure()
    
    # Add colored rectangles (layered in order)
    fig.add_shape(type="rect", x0=2500,  x1=q1, y0=5, y1=15, fillcolor="green", opacity=0.4, line=dict(width=0))
    fig.add_shape(type="rect", x0=2500,  x1=q1, y0=-2, y1=5, fillcolor="salmon", opacity=0.4,line=dict(width=0))
    
    fig.add_shape(type="rect", x0=q1, x1=q2, y0=5, y1=15, fillcolor="orange", opacity=0.4, line=dict(width=0))
    fig.add_shape(type="rect", x0=q1, x1=q2, y0=-2, y1=5, fillcolor="red", opacity=0.4, line=dict(width=0))
    
    fig.add_shape(type="rect", x0=q2, x1=q3, y0=5, y1=15, fillcolor="yellow", opacity=0.4, line=dict(width=0))
    fig.add_shape(type="rect", x0=q2, x1=q3, y0=-2, y1=5, fillcolor="purple", opacity=0.4, line=dict(width=0))
    
    fig.add_shape(type="rect", x0=q3, x1=25000, y0=5, y1=15, fillcolor="violet", opacity=0.4, line=dict(width=0))
    fig.add_shape(type="rect", x0=q3, x1=25000, y0=-2, y1=5, fillcolor="blue", opacity=0.4, line=dict(width=0))
    
    ## Scatter Plot:
    fig.add_trace(go.Scatter(x = data['Avg_price_rupee_per_sqft'], y = data['Sector_Amenity_Score'], 
                             mode='markers', marker=dict(color='black', size = 7), text=data.index,
                            customdata = data.values,  # pass extra data
                            hovertemplate=("<b>%{text}</b><br>"
                                           "Median Price(in ₹/Sq.ft): %{customdata[0]:,.0f}<br>"
                                           "Sector Amenity Score: %{customdata[1]:.2f}<br><extra></extra>")))
    
    ## Adding Vertical lines creating compartments of Sector Segments:
    fig.add_vline(x=q1, line=dict(color="violet", dash="dash"))
    fig.add_vline(x=q2, line=dict(color="green", dash="dash"))
    fig.add_vline(x=q3, line=dict(color="red", dash="dash"))
    fig.add_hline(y=5, line=dict(color="blue", dash="dash"))
    
    
    ## Annoting Sector Segments:
    for cate, x_pos in zip(['AFFORDABLE', 'MID-RANGE', 'EXPENSIVE', 'LUXURY'], [5500, 10500, 14750, 21000]):
        fig.add_annotation(
            x=x_pos, y=13, text=cate,         # text content
            showarrow=False,                  # arrow pointing
            font=dict(
                size=13, color="crimson",    # font customization
                family="Arial Black"),
            bgcolor="lightyellow",           # background color
            bordercolor="black",             # border around text
            borderwidth=1, borderpad=2       # padding inside box
        )
    
    ## Update layout:
    fig.update_layout(autosize=True, margin=dict(l=10, r=10, t=5, b=10), height=360,
                      xaxis_range=[2500, 25000], yaxis_range=[-2, 15], 
                      plot_bgcolor='white', # area inside axes
                      paper_bgcolor="#080707",    # outside area
                      xaxis = dict(title = dict(text="Median Property Price Density (in ₹/Sq.ft)",
                                               font=dict(size=22, color="white", family='Calibri'))),
                      yaxis = dict(title = dict(text="Sector Amenity Score",
                                               font=dict(size=22, color="white", family='Calibri'))))
    
    fig.update_xaxes(tickvals = np.arange(2500, 25000, 2000), ticktext = np.arange(2500, 25000, 2000))
    fig.update_yaxes(tickvals = np.arange(-2, 12, 2), ticktext = [' '] + list(np.arange(0, 12, 2)))

    return fig

## Localitiy wise Price Distribution:
def Distribution_of_Property_Cost_across_6_Major_Localities():
    sec_location = pd.read_csv('navigation_pages/graphs_and_plots/sector_geo_centroid_data.csv', index_col = 'Unnamed: 0')

    ## Preparing data for analysis:
    data_local = pd.merge(sec_location, df, how='inner', on='Sector')
    data_local = data_local[data_local['Sector'] != '-']
    
    ## Aggregation
    def func_pri(data):
        pro_pri = data['Avg_price_rupee_per_sqft']
        return pd.Series([pro_pri.size, pro_pri.min(), pro_pri.max(), pro_pri.mean(), pro_pri.median()],
             index=pd.MultiIndex.from_tuples([('Price', 'tot_prop_listed'),('Price', 'min'),('Price', 'max'),
                 ('Price', 'mean'),('Price', 'median')]))
    
    data_local = data_local.groupby(by='Locality').apply(func_pri).astype({('Price','tot_prop_listed'):'int32'})
    data = data_local.sort_index().reset_index()
    
    # Custom x-tick labels
    tick_names = [f'Dwarka Expressway<br>Belt',f'Golf Course<br>Road & Extension',
                  f'MG Road &<br>Central Gurugram',f'New Gurugram',f'Old Gurgaon',
                  f'Southern Peripheral<br>Road (SPR) Belt']
    
    # Create Plotly figure
    fig = go.Figure()
    
    # Average line
    fig.add_trace(go.Scatter(
        x=data['Locality'], y=data[('Price','mean')],
        mode='lines+markers',
        name='Average Property Cost',
        line=dict(color='black', dash='dash', width=1.5),
        marker=dict(symbol='star', size=10, color='skyblue', line=dict(color='black', width=1)),
        hovertemplate="<b>Locality:</b> %{x}<br>"
                  "<b>Average Price Density:</b> ₹ %{y:.0f}/Sq.ft<extra></extra>"    ))
    
    # Median line
    fig.add_trace(go.Scatter(
        x=data['Locality'], y=data[('Price','median')],
        mode='lines+markers',
        name='Median Property Cost',
        line=dict(color='orange', dash='solid', width=1.5),
        marker=dict(symbol='diamond', size=10, color='green', line=dict(color='black', width=1)),
        hovertemplate="<b>Locality:</b> %{x}<br>"
                  "<b>Median Price Density:</b> ₹ %{y:.0f}/Sq.ft<extra></extra>"))
    
    # Minimum line
    fig.add_trace(go.Scatter(
        x=data['Locality'], y=data[('Price','min')],
        mode='lines+markers',
        name='Minimum Property Cost',
        line=dict(color='grey', width=1.5),
        marker=dict(symbol='cross', size=10, color='red', line=dict(color='black', width=1)),
        hovertemplate="<b>Locality:</b> %{x}<br>"
                  "<b>Minium Price Density:</b> ₹ %{y:.0f}/Sq.ft<extra></extra>"))
    
    # Annotate property counts
    for prop_count, locality in zip(data[('Price','tot_prop_listed')], data['Locality']):
        fig.add_annotation(
            x=locality, y=0,
            text=f"Total Listings<br>{prop_count}",
            showarrow=False,
            font=dict(size=16, color='black', family="Calibri", weight="bold"),
            align="center",
            bgcolor="lightgreen",
            bordercolor="black",
            borderwidth=0.6
        )
    
    # Layout formatting
    fig.update_layout(
        #title=dict(
        #    text="Locality VS Aggregated Property Price Density (in ₹/Sq.ft)",
        #    x=0.5, xanchor="center",
        #    font=dict(size=20, color="black", family="Arial Black")
        #),
        xaxis=dict(
            title="Locality",
            tickmode='array',
            tickvals=list(range(len(tick_names))),
            ticktext=tick_names,
            #titlefont=dict(size=24, color='white',family="Calibri"),
            tickfont=dict(size=16, color='white',family="Calibri"), showgrid=False,
        ),
        yaxis=dict(
            title="Price Density (in ₹/Sq.ft)",
            title_standoff=20, ticklabelposition="outside left",
            range=[-2500, 20200],
            tickmode='array',
            tickvals=[f"{i}  " for i in range(0,20001,2500)],
            #titlefont=dict(size=24, color='white',family="Calibri"),
            tickfont=dict(size=16, color='white',family="Calibri"),
            showgrid=False, gridcolor="black", gridwidth=0,
            minor=dict(showgrid=False, gridcolor="black", gridwidth=0), zeroline=False
        ),
        legend=dict(
            font=dict(size=16, color='black', family='Calibri'),
            bgcolor="rgba(255,255,255,255)",
            bordercolor="black",
            borderwidth=1,
            x=0.98, y=0.98, xanchor="right", yanchor="top"
        ),
        plot_bgcolor="#F5F2F2",   # area inside axes
        paper_bgcolor="#080707",    # outside area
        autosize=True, height=460,
        margin=dict(l=50,r=50,t=20,b=20))
    
    return fig


## Creating an Insights DataFrame along with Plot comments:
import re

def local_insights_df_func():
    # --- Data from Market Research and Collected Samples ---
    data = {"Corridor / Sector Cluster": ["Dwarka Expressway", "MG Road", "Golf Course Extension Road",
                                          "Premium Sectors (42, 54–56)", "New Gurugram (Sectors 81–95)", 
                                          "Mid-range Sectors (49–57)", "SPR Corridor"],
            "Price Range (₹/Sq.ft)": ["~10,700 (Q1 2024)","~23,400","~16,250","14,000 – 25,000",
                                      "5,000 – 10,000","5,000 – 8,000","18,000 (mid-2024)"],
            "Growth Trend": ["+27% YoY", "+50% YoY", "+27% YoY", "High-end sustained demand", 
                             "Emerging growth corridors", "Stable mid-segment zones", "+120% over five years"]
           }
    
    local_insights_df = pd.DataFrame(data)
    
    # --- helper: extract approximate numeric price for styling ---
    def approx_price_num(s: str) -> float:
        # extract all numbers from the string and compute mean (handles ranges and single values)
        nums = re.findall(r"[0-9]{1,3}(?:,[0-9]{3})*|[0-9]+", s)
        if not nums:
            return float("nan")
        # remove commas and convert
        vals = [int(n.replace(",", "")) for n in nums]
        return float(sum(vals)) / len(vals)
    
    price_numeric = local_insights_df["Price Range (₹/Sq.ft)"].apply(approx_price_num)
    
    # --- prepare a display copy (we can add icons/arrow unicode) ---
    display = local_insights_df.copy()
    
    # Add arrow icons for growth where useful
    def growth_display(s: str) -> str:
        s = str(s)
        if re.match(r"^\s*\+\d", s):  # starts with +number
            return "▲ " + s.strip()
        if re.match(r"^\s*-\d", s):  # starts with -number
            return "▼ " + s.strip()
        # other descriptive texts keep as-is (shorten if lengthy)
        return s
    
    display["Growth Trend"] = display["Growth Trend"].apply(growth_display)
    
    # Optionally prepend emoji to corridor names for visual flair
    emoji_map = {
        "Dwarka Expressway": "🚧",
        "MG Road": "🏙️",
        "Golf Course Extension Road": "⛳",
        "Premium Sectors (42, 54–56)": "💎",
        "New Gurugram (Sectors 81–95)": "🌱",
        "Mid-range Sectors (49–57)": "🏘️",
        "SPR Corridor": "🚄"
    }
    display["Corridor / Sector Cluster"] = display["Corridor / Sector Cluster"].apply(
        lambda x: f"{emoji_map.get(x, '')} {x}"
    )
    
    # --- styling functions ---
    def row_style(row):
        """
        Return a list of styles (strings) for each cell in the row.
        We'll style Price Range cell background based on price_numeric,
        and Growth Trend color based on arrow/keyword.
        """
        styles = [""] * len(row.index)
        idx = row.name  # index of the row in df/display
    
        # Style the Price cell based on price_numeric buckets
        p = price_numeric.iloc[idx]
        if pd.isna(p):
            price_style = ""
        elif p >= 20000:         # very high: dark red background, white text
            price_style = "background: linear-gradient(90deg, #b30000, #ff4d4d); color: red; font-weight:600;"
        elif p >= 14000:         # high: orange
            price_style = "background:linear-gradient(90deg,#ff8800,#ffd699); color: #F5F227; font-weight:600;"
        elif p >= 8000:         # mid: yellowish
            price_style = "background:linear-gradient(90deg,#ffd966,#fff2cc); color: #35A80A;"
        else:                   # lower: light green
            price_style = "background:linear-gradient(90deg,#c6f7d0,#f0fff7); color: #ffffff;"
        # assign to the 'Price Range' column position
        col_price_pos = list(row.index).index("Price Range (₹/Sq.ft)")
        styles[col_price_pos] = price_style
    
        # Style Growth Trend: green for upward, red for downward, blue for positive text
        gt = str(display.loc[idx, "Growth Trend"])
        col_growth_pos = list(row.index).index("Growth Trend")
        if gt.startswith("▲"):
            styles[col_growth_pos] = "color: #27F535; font-weight:850;"  # green
        elif gt.startswith("▼"):
            styles[col_growth_pos] = "color: #d93025; font-weight:700;"  # red
        elif "High" in gt or "Emerging" in gt or "growth" in gt.lower():
            styles[col_growth_pos] = "color:#27BBF5; font-weight:800;"  # blue-ish
        else:
            styles[col_growth_pos] = "color: #ffffff;"
    
        # Make the corridor column bold and slightly larger
        col_corr_pos = list(row.index).index("Corridor / Sector Cluster")
        styles[col_corr_pos] = (styles[col_corr_pos] + 
                                "font-weight:800; font-size:14px; padding:6px 8px;")
    
        return styles
    
    # create styler
    styler = display.style
    
    # Apply row-wise styling
    styler = styler.apply(row_style, axis=1)
    
    # Style the header
    styler = styler.set_table_styles([
        {"selector": "th", "props": [("background-color", "#16324F"),
                                     ("color", "white"),
                                     ("font-size", "18px"),
                                     ("padding", "8px")]},
        {"selector": "caption", "props": [("caption-side", "bottom")]}
    ])
    
    
    # set table attributes for full-width + nicer fonts
    styler = styler.set_table_attributes('class="styled-table" style="width:100%; font-family: calibri;"')
    
    return styler




## Distribution of Flats across localities: 
def Distribution_of_5_Major_Flat_Types_across_6_Localities_of_Gurugram():
    sec_location = pd.read_csv('navigation_pages/graphs_and_plots/sector_geo_centroid_data.csv', 
                               index_col = 'Unnamed: 0')
    
    ## Preparing data for analysis:
    data_local = pd.merge(sec_location, df, how='inner', on='Sector')
    five_maj_ft = ["2 BHK Flat", "2.5 BHK Flat", "3 BHK Flat",  "3.5 BHK Flat", "4 BHK Flat"]
    
    ## Only keeping records with Flat from 5 Major Flat types:
    data_local = data_local[data_local['Flat'].isin(five_maj_ft)]
    
    ## grouping data based on Locality and Flat, and counting total records in each group:
    grouped_data = data_local.groupby(by = ['Locality', 'Flat'])[['Locality','Flat']].apply(lambda x: x.shape[0])
    grouped_data = grouped_data.reset_index(drop=False).rename(columns = {0:'Num_listings'})
    
    ## Creating plot : ---------------------------------------------------------------
    fig = plt.figure(figsize = (15,5), dpi = 500)
    ax = fig.add_subplot(1,1,1)
    
    #fig.suptitle("Distribution of 5 Major Flat Types across 6 Localities of Gurugram" ,
    #             fontweight = 'bold', fontsize = 24, color = 'white', ha='center', x=0.53, y=0.95,
    #             bbox={'facecolor': 'black', 'edgecolor': 'white', 'boxstyle': 'round, pad=0.3', 
    #                   'linewidth': 1})
    
    ax = sns.barplot(data = grouped_data, x = 'Locality', y = 'Num_listings', hue = 'Flat', palette='Dark2')
        
    # Matplotlib customizations
    ax.set_xlabel("Locality", fontsize=16, color='white', labelpad=10, fontweight='bold')
    ax.set_ylabel("Number of Property Listings", fontsize=16, color='white', labelpad=14, fontweight='bold')
    
    # Customize ticks
    ax.set_yticks(np.arange(0, 1401, 200))
    ax.set_yticklabels(np.arange(0, 1401, 200), fontsize=14, color='white', fontweight='bold')
    
    ax.set_xticks(list(range(6)))
    local_names = ['Dwarka Expressway\nBelt', 'Golf Course\nRoad & Extension',
                   'MG Road &\nCentral Gurugram', 'New Gurugram', 'Old Gurgaon',
                   'Southern Peripheral\nRoad (SPR) Belt']
    ax.set_xticklabels(local_names, fontsize=12, fontweight='bold', color='white')
        
    fig.patch.set_facecolor("#080707")   # figure background
    ax.set_facecolor("#080707")        # axes background
    ax.legend(fontsize=14, title='Flat', title_fontsize=14, facecolor="#ffffff",
             frameon=True, fancybox=True)
    
    fig.tight_layout()
    
    return fig

## ----------------------------------------------------------------------------------------------------
## 4th and last set of Visz:

## Adding Data Cards:
def cheapest_prop_det():
    data = df[df['Price_in_rupees'] == df['Price_in_rupees'].min()][['Flat', 'Address', 'Price']].values
    Flat = data[0][0] 
    Address = data[0][1][:data[0][1].index(", S") + 1] + '\n' + data[0][1][data[0][1].index(", S") + 2 : ]
    Price = data[0][2]
    return Flat, Address, Price

def most_expensive_prop_det():
    data = df[df['Price_in_rupees'] == df['Price_in_rupees'].max()][['Flat', 'Address', 'Price']].values
    Flat = data[0][0] 
    Address = data[0][1][:data[0][1].index(", S") + 1] + '\n' + data[0][1][data[0][1].index(", S") + 2 : ]
    Price = data[0][2]
    return Flat, Address, Price

def med_average_tot_listings():
    desc = df['Price_in_rupees'].describe()
    median = str(round(desc['50%'] / 1e7 , 2)) + " Cr"
    average = str(round(desc['mean'] / 1e7 , 2)) + " Cr"
    tot_listings = int(desc['count'])
    return median, average, tot_listings
    
    

## Price buckets distribution:
def Price_Buckets_VS_Number_of_Property_listings_cate1():
    # Price range: 0 to 5 cr
    prices = df[df['Price_in_rupees'] <= (5e7)]['Price_in_rupees']     
    counts, bin_edges = np.histogram(prices, bins=50)
    
    # Custom bin labels
    bins = [f"₹{bin_edges[i]/1e7:.2f} Cr - ₹{bin_edges[i+1]/1e7:.2f} Cr" 
            for i in range(len(bin_edges)-1)]
    
    # Create bar chart
    fig = go.Figure(go.Bar(
        x=list(range(50)),   # numeric positions
        y=counts,
        marker=dict(color='#40E0D0', line=dict(color='black', width=1)),
        name='Total Property Count in Price Bucket',
        text=counts,                   # counts displayed on bars
        textposition="inside",         # show count inside bar
        hovertemplate="<b>Price Bucket:</b> %{customdata}<br><b>Property Count:</b> %{y}<extra></extra>",
        customdata=bins                # pass bin labels for hover
    ))
    
    # Add bin labels as annotations above bars (like in Matplotlib)
    for i, (height, label) in enumerate(zip(counts, bins)):
        fig.add_annotation(
            x=i, y=height+80,
            text=label,
            showarrow=False,
            textangle=-90,
            font=dict(size=12, color="black", family="Calibri", weight="bold"),
            align="left"
        )
    
    # Layout
    fig.update_layout(
        yaxis=dict(title="Total Property Count", range=[0, 630],
                   titlefont=dict(size=25, family="Calibri", color='white'),
                   tickfont=dict(size=18, color='white',family="Calibri"),
                   showgrid=False, gridcolor="white", gridwidth=0,
                   minor=dict(showgrid=False, gridcolor="white", gridwidth=0), zeroline=False),
        
        xaxis=dict(showticklabels=False, range=[-1, 50]),
        
        legend=dict(font=dict(size=18)), plot_bgcolor="#F5F2F2", autosize=True, height=440,
        paper_bgcolor="#080707",    # outside area
        margin=dict(l=10,r=10,t=0,b=20)
    )
    
    return fig


def Price_Buckets_VS_Number_of_Property_listings_cate2():
    ## Properties with Prices: > 5cr
    prices_rest = df[df['Price_in_rupees'] > (5e7)]['Price_in_rupees']     
    counts_rest, bin_edges_rest = np.histogram(prices_rest, bins = 50)
    
    bins_rest = ["₹" + str(round(bin_edges_rest[i] / 1e7 , 3)) + " Cr - " + 
                 "₹" + str(round(bin_edges_rest[i+1] / 1e7 , 3)) + " Cr" 
                 for i in range(len(bin_edges_rest) - 1)]
    
    ## Creating Series then DF for Plotly Treemap:
    bin_ser = pd.Series()
    for i, count in zip(range(50), counts_rest):
        bin_ser = pd.concat([bin_ser, pd.Series([bins_rest[i]] * count)])
    
    data = pd.DataFrame(bin_ser, columns = ['Price Range'])
    
    ## -----------------------------------------------------------------------------------------
    ## Creating a TreeMap:
    fig = px.treemap(data, path=[px.Constant('Property Price Buckets'),'Price Range'], 
                     values = pd.Series(np.ones(bin_ser.size)).astype('int8'),
                     color = 'Price Range' , color_continuous_scale='Plasma')
    
    fig.update_layout(autosize=True, margin=dict(l=0, r=0, t=25, b=10),
                      paper_bgcolor='#080707')
    
    fig.update_traces(textinfo="label+value",
        hovertemplate='<b>Price Bucket: %{label}</b><br>Prop. Count: %{value}<br><extra></extra>',
                      textfont=dict(size=18, color="black", family="Calibri black"),
                      textposition="middle center",
                      tiling=dict(pad=2))

    return fig

## -------------------------------------------------------------------------------------------------
## -------------------------------------------------------------------------------------------------
## -------------------------------------------------------------------------------------------------
