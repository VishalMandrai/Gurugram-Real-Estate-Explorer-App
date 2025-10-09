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
def Age_of_Properties_across_the_Top_25_Sectors():
    ## Prepare data:
    top_25_sec = df['Sector'].value_counts().drop('-').head(25).index
    
    data = df[(df['Sector'].isin(top_25_sec)) & (df['Age_of_property_in_years'] != '-')]
    data = data.astype({'Age_of_property_in_years':'int16'})
    
    data_plot = data.groupby(by = 'Sector')[['Sector', 'Age_of_property_in_years',
                                            'Price_in_rupees']].agg({
                                                            'Age_of_property_in_years':['mean', 'median'],
                                                            'Price_in_rupees':'median'})
    
    data_plot.sort_values(by = ('Age_of_property_in_years', 'median'), inplace = True)
    
    data_med = data_plot['Age_of_property_in_years']['median']
    data_avg = data_plot['Age_of_property_in_years']['mean']
    data_price = data_plot['Price_in_rupees']['median']
    ## -----------------------------------------------------------------------------------
    ## Creating Plot:
    fig = plt.figure(figsize = (15,5), dpi = 600)
    ax = fig.add_subplot(1,1,1)
    ax.grid(axis = 'y', alpha = 0.8, zorder = 1, linestyle ='--')
        
    bar = ax.bar(height = data_med.values, x = data_med.index, color = '#A6E7FF',
                 label = 'Median Age of Property in Sector', zorder = 2)
    scatter1 = ax.scatter(x = data_avg.index , y = data_avg.values, color = '#6E5EF7',
                          label = 'Mean Age of Property in Sector', zorder = 3)
    
    ax.set_ylabel('Age of Property (in Years)', fontsize=16, fontweight='bold', labelpad=10,
                  color='white')
    ax.set_xlabel('Sectors', fontsize=16, fontweight='bold', labelpad=15, color='white')
    ax.set_xlim(-1,25)
    ax.set_xticks(list(range(25)))
    ax.set_xticklabels(pd.Series(data_plot.index).apply(lambda x: x.split()[-1]), rotation = 0,
                      color='white', fontsize=13)
    ax.tick_params(axis='y', labelsize=13, labelcolor='white')
    
    ## Creating Twin axis:
    ax1 = ax.twinx()
    scatter2 = ax1.scatter(data_price.index, data_price.values, 
                           label = 'Median Price of Property in Sector',
                           zorder = 4, marker = ',', color = '#D90000')
    ax1.set_ylabel('Median Price of Property (in ₹)', fontsize=16, fontweight='bold', 
                   labelpad=20, rotation=-90, color='white')
    
    ax1.set_ylim(0, 60000001)
    ax1.set_yticks(list(range(0, 60000001, 10000000)))
    ax1.set_yticklabels([str(round(i/(10000000) , 2)) + 'Cr' 
                         for i in list(range(0, 60000001, 10000000))], color='white', fontsize=13)
    
    ## Merging Labels of 3 plots:
    labels = [plot.get_label() for plot in [bar, scatter1, scatter2]]
    ax.legend([bar, scatter1, scatter2], labels, loc="upper center", fontsize=12, 
              frameon=True, fancybox=True, framealpha=1)
    
    fig.tight_layout()
    fig.patch.set_facecolor("#080707")   # figure background
    ax.set_facecolor("#080707")        # axes background
    
    return fig
    

## -------------------------------------------------------------------------------------------------
## Second set of Visz:

def trend_bw_sector_numbers_and_development_and__pricing():
    ## Preparing data for analysis:
    data = df[df['Sector'] != '-']
    sec_pricing = data.groupby(by='Sector')[['Avg_price_rupee_per_sqft']].agg({
        'Avg_price_rupee_per_sqft':'median'}).reset_index()
    
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
    
    sec_pricing['Sector Order'] = sec_pricing['Sector'].apply(sort_sec)
    sec_pricing = sec_pricing.sort_values(by = 'Sector Order').reset_index(drop=True)
    
    ## ------------------------------------------------------------------------------------------------
    ## Creating Plot: 
    fig = plt.figure(figsize = (20,5), dpi = 500)
    ax = fig.add_subplot(1,1,1)
    
    ax.plot(sec_pricing['Sector'].apply(lambda x: x.split()[-1]), 
            sec_pricing['Avg_price_rupee_per_sqft'], 
            linewidth=1.8, color='white', linestyle='--',
            label = 'Sector-wise Median Price Density (in ₹/Sq.ft)', 
            marker = 'o', markersize=7,  markerfacecolor='#99F2F7',markeredgecolor='white', 
            markeredgewidth = 1.1)
    
    ax.set_title(' ', fontsize=18, pad=20)
    ax.set_ylabel('Median Price Density (in ₹/Sq.ft)', fontsize=18, fontweight='bold', color='white')
    ax.set_xlabel('Sector Number', fontsize=25, fontweight='bold', color='white')
    
    ax.set_xlim(-1, sec_pricing.shape[0] + 1)
    ax.set_xticks(list(range(0, sec_pricing.shape[0])))
    ax.set_xticklabels(sec_pricing['Sector'].apply(lambda x: x.split()[-1]), rotation = 90, 
                       fontsize = 9, fontweight = 'bold', color='white')
    
    ax.set_ylim(0,68000)
    ax.set_yticks(list(range(0, 65001, 10000)))
    ax.set_yticklabels([f"₹{i}" for i in range(0, 65001, 10000)], fontsize = 14, color='white')
    
    ax.legend(fontsize=20, loc = 'upper right', frameon=True, fancybox=True, framealpha=1,
             edgecolor="#ffffff", facecolor='#080707', labelcolor="white")
   
    fig.tight_layout()
    fig.patch.set_facecolor("#080707")   # figure background
    ax.set_facecolor("#080707")          # axes background
    
    return fig


## -------------------------------------------------------------------------------------------------
## Third set of Visz:

def Price_Bucket_VS_Per_bedroom_Cost():
    ## Preparing data for Plot:
    # Binning "Property Prices" into fixed ranges
    bins = [0, 25e5, 50e5, 75e5, 1e7, 125e5, 150e5, 175e5, 2e7, 
            225e5, 250e5, 275e5, 3e7, 325e5, 350e5, 375e5, 4e7, 
            425e5, 450e5, 475e5, 5e7, 525e5, 550e5, 575e5, 6e7,
            625e5, 650e5, 675e5, 7e7, 8e7, 9e7, 10e7, float('inf')]
    
    labels = ['<25L','25L-50L', '50L-75L', '75L-1Cr', '1-1.25Cr', '1.25-1.5Cr', '1.5-1.75Cr', '1.75-2Cr', 
              '2-2.25Cr', '2.25-2.5Cr', '2.5-2.75Cr', '2.75-3Cr',
              '3-3.25Cr', '3.25-3.5Cr', '3.5-3.75Cr', '3.75-4Cr',
              '4-4.25Cr', '4.25-4.5Cr', '4.5-4.75Cr', '4.75-5Cr',
              '5-5.25Cr', '5.25-5.5Cr', '5.5-5.75Cr', '5.75-6Cr',
              '6-6.25Cr', '6.25-6.5Cr', '6.5-6.75Cr', '6.75-7Cr',
              '7-8Cr', '8-9Cr', '9-10Cr', '10Cr+']
    
    ## Creating a Column in DF with "Price_buckets" label:
    df['Price_buckets'] = pd.cut(df['Price_in_rupees'], bins = bins, labels = labels)
    
    ## Grouping data based on the Price Buckets formed above and finding mean and 
    ## median "Price/bedrooms" for each of the group:
    def func_bed(data):
        pri_per_bed = data['Price_in_rupees'] / data['Bedrooms']
        return pd.Series([pri_per_bed.size, pri_per_bed.min(), pri_per_bed.max(), pri_per_bed.mean(), 
                          pri_per_bed.median()],
                         index = pd.MultiIndex.from_tuples([('Price_per_bedrooms', 'tot_prop_listed'), 
                                                            ('Price_per_bedrooms', 'min'), 
                                                            ('Price_per_bedrooms', 'max'),
                                                            ('Price_per_bedrooms', 'mean'), 
                                                            ('Price_per_bedrooms', 'median')]))
    
    data = df.groupby(by = 'Price_buckets').apply(func_bed).reset_index()
    
    ## ------------------------------------------------------------------------------------------------
    ## Creating Plot: 
    fig = plt.figure(figsize = (12,4), dpi = 500)
    ax = fig.add_subplot(1,1,1)
    
    ax.bar(height = data[('Price_per_bedrooms', 'mean')], x = data['Price_buckets'], 
           color='#32A7FA', linewidth=1.4, edgecolor='#1E87D4', label = 'Average Cost per Bedroom')
    
    ax.plot(data['Price_buckets'], data[('Price_per_bedrooms', 'median')], 
            color='#C97300', linewidth=1.5, 
            label = 'Median Cost per Bedroom', marker = '*', markersize  = 9,  
            markerfacecolor='#FA0000', markeredgecolor='black', markeredgewidth = 0.3)
    
    ax.plot(data['Price_buckets'], data[('Price_per_bedrooms', 'min')], linewidth=0, 
            label = 'Minimum Cost per Bedroom', marker = '$-$', markersize  = 9,  
            markerfacecolor='black', markeredgecolor='black', markeredgewidth = 0.3)
    
    ax.set_ylabel('Per Bedroom Cost (in ₹)', fontsize=14, fontweight='bold', color='white')
    ax.set_xlabel('Price Buckets (in ₹)', fontsize=18, fontweight='bold', labelpad=8, color='white')
    
    ax.set_xlim(-1, 32)
    ax.set_xticks(list(range(0, 32)))
    ax.set_xticklabels(data['Price_buckets'], rotation = 45, fontsize = 8, fontweight = 'bold',
                      color='white')

    ax.set_ylim(0,5e7)
    ax.set_yticks(list(range(0, 50000001, 10000000)))
    ax.set_yticklabels([f"₹{i} Cr" for i in range(0, 6)], fontsize = 8, 
                       fontweight = 'bold', color='white')

    ax.legend(fontsize=12, loc = 'upper left', frameon=True, fancybox=True, framealpha=1,
             edgecolor="black", facecolor='white', labelcolor="black")
    
    fig.tight_layout()
    fig.patch.set_facecolor("#080707")   # figure background
    ax.set_facecolor("#080707")          # axes background

    return fig


## -------------------------------------------------------------------------------------------------
## Fourth set of Visz:

def Furnishing_Status_affects_Property_Pricing_and_Property_Price_Density():
    ## Preparing data:
    five_maj_ft = ["2 BHK Flat", "2.5 BHK Flat", "3 BHK Flat",  "3.5 BHK Flat", "4 BHK Flat"]
    data = df[(df['Furnishing'].isin(['Unfurnished', 'Semi Furnished'])) & (df['Flat'].isin(five_maj_ft))]
    data['Furnishing'] = data['Furnishing'].apply(lambda x: x if x == 'Unfurnished' else 'Furnished')
    
    ##----------------------------------------------------------------------------
    ## Creating Plot:
    fig = plt.figure(figsize=(15,5), dpi=600)
    ax1 = fig.add_subplot(1, 2, 1)
    ax2 = fig.add_subplot(1, 2, 2)
    bbox={'facecolor': '#080707', 'edgecolor': 'white', 'boxstyle': 'round, pad=0.2', 'linewidth': 1.2}
    
    sns.boxplot(data=data, y='Flat', x = 'Avg_price_rupee_per_sqft' , hue = 'Furnishing', ax=ax1,
                     palette="hot", order=data['Flat'].value_counts().index, 
                     hue_order=data['Furnishing'].value_counts().sort_index().index, linecolor='white',
                     linewidth=0.8, flierprops=dict(marker='o', markerfacecolor='orange', markersize=2.8, 
                                     markeredgecolor='orange', markeredgewidth = 0.4), 
                     boxprops=dict(edgecolor='white', linewidth=1))
    
    ax1.set_title("Furnishing Status VS Property Price Density (in ₹/Sq.ft)", 
                 fontsize = 16, fontweight='bold', bbox = bbox, pad = 10, color='white')
    ax1.set_xlabel("Price Density (in ₹/Sq.ft)", fontsize = 14, fontweight='bold', labelpad = 12, 
                   color='white')
    ax1.set_ylabel("Flat", fontsize = 14, fontweight='bold', color='white')
    
    ax1.set_xlim(0, 55000)
    ax1.set_xticks(list(range(0,55000, 10000)))
    ax1.set_xticklabels(['₹'+str(i)+'/Sq.ft' for i in range(0,55000, 10000)], fontsize=8, fontweight='bold',
                       color='white')
    ax1.set_yticks(list(range(5)))
    ax1.set_yticklabels([i[:-5] for i in data['Flat'].value_counts().index], fontsize=10, fontweight='bold', 
                        color='white')
    
    ## ------------------------------------------------------------------------------
    sns.boxplot(data=data, y='Flat', x = 'Price_in_rupees' , hue = 'Furnishing', ax = ax2,
                palette="hot", order=data['Flat'].value_counts().index, 
                hue_order=data['Furnishing'].value_counts().sort_index().index, linecolor='white',
                linewidth=0.8, flierprops=dict(marker='o', markerfacecolor='orange', markersize=2.8, 
                                     markeredgecolor='orange', markeredgewidth = 0.4), 
                boxprops=dict(edgecolor='white', linewidth=1))
    
    ax2.set_title("Furnishing Status VS Property Price (in ₹ Cr)", 
                 fontsize = 16, fontweight='bold', bbox = bbox, pad = 10, color='white')
    ax2.set_xlabel("Property Price (in ₹ Cr)", fontsize = 14, fontweight='bold', labelpad = 12, color='white')
    ax2.set_ylabel("Flat", fontsize = 14, fontweight='bold', color='white')
    
    ax2.set_xlim(0, 10e7)
    ax2.set_xticks(list(range(0,100000001, 10000000)))
    ax2.set_xticklabels(['₹'+str(int(i/10000000))+' Cr' for i in range(0,100000001, 10000000)], 
                       fontsize = 8, fontweight='bold', color='white')
    ax2.set_yticks(list(range(5)))
    ax2.set_yticklabels([i[:-5] for i in data['Flat'].value_counts().index], 
                       fontsize = 10, fontweight='bold', color='white')
    
    fig.tight_layout()
    fig.patch.set_facecolor("#080707")    # figure background
    ax1.set_facecolor("#080707")          # axes background
    ax2.set_facecolor("#080707")          # axes background
    
    ax1.legend(fontsize=12, loc = 'lower right', title_fontsize=12, fancybox=True, framealpha=1,
             edgecolor="white", facecolor='white', labelcolor="black", title="Furnishing Status")
    ax2.legend(fontsize=12, loc = 'lower right', title_fontsize=12, fancybox=True, framealpha=1,
             edgecolor="white", facecolor='white', labelcolor="black", title="Furnishing Status")
    
    return fig



## -------------------------------------------------------------------------------------------------
## Fifth set of Visz:

def Flat_Facing_Compass_and_treemap():
    ## Preparing Data
    data = df[df['Facing'] != '-']
    
    ## ------------------------------------------------------------------------------------------------
    ## Creating Plot:
    ## 1) Building TreeMap for "Facing" Feature:
    tmap = px.treemap(data, path=[px.Constant('Gurugram Flats'), 'Facing'], color='Facing',
                      values=pd.Series(np.ones(data.shape[0])).astype('int8'), color_continuous_scale='Blues')
    tmap.update_traces(textinfo="label+value+percent entry", 
                       hovertemplate='<b>%{label}</b><br>Count: %{value}<br><extra></extra>', 
                       textfont=dict(size=18, color="black", family="Calibri black"), 
                       textposition="middle center", tiling=dict(pad=2) )
    
    ## -----------------------------
    ## 2) Two-column canvas: left domain (treemap), right xy (image)
    fig = make_subplots(rows=1, cols=2, specs=[[{"type": "xy"}, {"type": "domain"}]], 
                        column_widths=[0.40, 0.60], horizontal_spacing=0)
    
    # Add treemap traces to the LEFT only
    for tr in tmap.data:
        fig.add_trace(tr, row=1, col=2)
    
    # ------------------------------------------------------------------------------------------------
    ## 3) Right panel: place image tied to x2/y2 axes
    image_path = "navigation_pages/graphs_and_plots/Facing_Directions.jpg"  # change to your file or URL
    
    # Determine true size to preserve aspect
    if image_path.lower().startswith(("http://", "https://")):
        # Provide real pixel size if known
        w, h = 1200, 900
        img_src = image_path
    else:
        img = Image.open(image_path)
        w, h = img.size
        img_src = img
    
    ## Draw the image exactly inside the right subplot
    fig.add_layout_image(dict(source=img_src, xref="x1", yref="y1", 
                               x=-75, y=-80,             
                               xanchor="left", yanchor="bottom",
                               sizex=w+150, sizey=h+150, sizing="stretch", layer="above"))
    
    ## Configure right axes so the image fills the panel and axes are invisible
    fig.update_xaxes(row=1, col=1, range=[0, w], showgrid=False, showticklabels=False, zeroline=False)
    fig.update_yaxes(row=1, col=1, range=[0, h], showgrid=False, showticklabels=False, zeroline=False,
                     scaleanchor="x1", scaleratio=1)

    ## Optional thin border for the image panel
    fig.add_shape( type="rect", xref="x2", yref="y2",
                  x0=0, y0=h, x1=w, y1=0, line=dict(color="black", width=1)   )

    ## -----------------------------
    ## 4) Global layout: single title, no panning
    fig.update_layout(template="plotly_white", height=420, margin=dict(l=5, r=5, t=25, b=20),
                      paper_bgcolor="#080707",    # outside area
                      dragmode=False)

    return fig


## Vaastu Stats Dataset:
def Vaastu_data():
    pref_directions = ["North-East facing", "East facing", "North facing"]
    data = df[df['Facing'] != '-']
    
    data = data['Facing'].apply(lambda x: 'Vaastu Compliant' 
                                if x in pref_directions 
                                else "Non-Compliant").value_counts()
    
    data = pd.DataFrame(data.values, index = data.index , columns = ['Property Count'])
    data['Percentage'] = round((data['Property Count'] / data['Property Count'].sum()) * 100, 
                               2).astype('str') + " %"
    
    ## Preparing data for Vaastu Property Pricing Stats: ------------------------------
    pref_directions = ["North-East facing", "East facing", "North facing"]
    data_stats = df[df["Facing"] != '-']
    data_stats['Vaastu'] = data_stats['Facing'].apply(lambda x: 'Vaastu Compliant' 
                                                      if x in pref_directions
                                                      else "Non-Compliant")
    
    ## Grouping data based on "Vaastu Compliance" and finding mean and median 
    ## "Property Price" for each group:
    def func_bed(data_stats):
        pro_pri = data_stats['Price_in_rupees']
        return pd.Series([pro_pri.min(), pro_pri.max(), pro_pri.mean(), pro_pri.median()],
                         index = [('Minium Price'), ('Maximum Price'), ('Average Price'), 
                                  ('Median Price')])
    
    data_stats = data_stats.groupby(by = 'Vaastu').apply(func_bed)
    
    for i in [('Minium Price'), ('Maximum Price'), ('Average Price'), ('Median Price')]:
        data_stats[i] = '₹ ' + round(data_stats[i] / 1e7 , 2).astype('str') + " Cr"
    
    data_stats = pd.merge(data, data_stats, left_index = True, right_index = True)
    
    return data_stats


## -------------------------------------------------------------------------------------------------
## Last set of Visz:

def Distribution_of_Floor_Number_and_Building_Height():
    ## Preparinf data for Analysis:
    df['Floor_number'].replace({'Ground Floor' : '0'}, inplace = True)
    data = df[df['Floor'] != '-'].astype({'Floor_number': 'int32', 'Building_height': 'int32'})
    
    ## --------------------------------------------------------------------------------------------
    ## Creating Plots:
    fig = plt.figure(figsize = (14,4), dpi = 500)
    ax1 = fig.add_subplot(1,2,1)
    ax2 = fig.add_subplot(1,2,2)
    
    ## Plotting KDE plots in ax1:
    ax1.axvline(data['Building_height'].max(), linestyle = '--', color='white', linewidth = 1.4, alpha=0.6,
               label = 'Building Height Range')
    ax1.axvline(data['Building_height'].min(), linestyle = '--', color='white', linewidth = 1.4, alpha=0.6)
    
    ax1.axvline(data['Floor_number'].max(), linestyle = '--', color='green', linewidth = 1.4, alpha=0.8,
                label = 'Floor Number Range')
    ax1.axvline(data['Floor_number'].min(), linestyle = '--', color='green', linewidth = 1.4, alpha=0.8)
    
    sns.kdeplot(data = data, x = 'Floor_number',ax = ax1, label =  "Floor Number", color = 'blue',
               linewidth = 2)
    sns.kdeplot(data = data, x = 'Building_height',ax = ax1, label =  "Building Height", color = '#FFC39E',
               linewidth = 2)
    
    ax1.set_xlabel("Floor Number / Building Height", fontsize = 14, fontweight = 'bold', labelpad = 12,
                   color='white')
    ax1.set_ylabel("Density", fontsize = 14, fontweight = 'bold', color='white')

    ax1.tick_params(axis='y', labelsize=10, labelcolor='white')
    ax1.set_xlim(-4, 76)
    ax1.set_xticks(list(range(0, 76, 5)))
    ax1.set_xticklabels(list(range(0, 76, 5)), fontsize = 10, fontweight = 'bold', color='white')
    
    ax1.legend()
    
    ## Plotting Hist Plot on ax2:
    sns.histplot(data=data, x='Floor_number',ax=ax2, label="Floor Number", color='blue', alpha=1,
                 bins = 45)
    sns.histplot(data=data, x='Building_height',ax=ax2, label="Building Height", color='#FFC39E', alpha=0.3,
                 bins = 45)
    
    ax2.set_xlabel("Floor Number / Building Height", fontsize = 14, fontweight = 'bold', 
                   labelpad = 14, color='white')
    ax2.set_ylabel("Property Count", fontsize = 14, fontweight = 'bold', color='white')

    ax2.tick_params(axis='y', labelsize=10, labelcolor='white')
    ax2.set_xlim(-1, 71)
    ax2.set_xticks(list(range(0, 71, 5)))
    ax2.set_xticklabels(list(range(0, 71, 5)), fontsize = 10, fontweight = 'bold', color='white')
    
    fig.tight_layout()
    fig.patch.set_facecolor("#080707")    # figure background
    ax1.set_facecolor("#080707")          # axes background
    ax2.set_facecolor("#080707")          # axes background
    
    ax1.legend(fontsize=10, loc = 'upper center', fancybox=True, framealpha=1,
             edgecolor="white", facecolor='#080707', labelcolor="white")
    ax2.legend(fontsize=12, loc = 'upper right', fancybox=True, framealpha=1,
             edgecolor="white", facecolor='#080707', labelcolor="white")
    
    return fig


## Floor Number & Price Trend:
def Floor_Number_affects_Property_Pricing():
    ## Preparinf data for Analysis:
    df['Floor_number'].replace({'Ground Floor' : '0'}, inplace = True)
    data = df[df['Floor'] != '-'].astype({'Floor_number': 'int32', 'Building_height': 'int32'})
    
    ## Grouping data based on Floor Number and finding mean and median "Property Price Per Sqft" 
    ## for each of the group:
    def func_bed(data):
        pro_pri = data['Avg_price_rupee_per_sqft']
        return pd.Series([pro_pri.size, pro_pri.min(), pro_pri.max(), pro_pri.mean(), pro_pri.median()],
             index = pd.MultiIndex.from_tuples([('Price', 'tot_prop_listed'), ('Price', 'min'), 
                                                ('Price', 'max'), ('Price', 'mean'), ('Price', 'median')]))
    
    data = data.groupby(by = 'Floor_number').apply(func_bed).astype({('Price', 'tot_prop_listed'):'int32'})
    data = data.reset_index()
    
    ## Selecting Floors with atleast 35 listings:
    data = data[data[('Price', 'tot_prop_listed')] > 35]
    
    ## ------------------------------------------------------------------------------------------------
    ## Creating Plot: 
    fig = plt.figure(figsize = (14,4.8), dpi = 550)
    ax = fig.add_subplot(1,1,1)
    
    ax.plot(data['Floor_number'].astype(str), data[('Price', 'mean')], linewidth=1.9, color='white', 
            linestyle='--',
            label = 'Average Cost Per Sq.ft', marker = '*', markersize  = 8,  markerfacecolor='#4EBAD9',
            markeredgecolor='white', markeredgewidth = 0.35)
    
    ax.plot(data['Floor_number'].astype(str), data[('Price', 'median')], color='orange', linestyle='--',
            linewidth=1.5, label = 'Median Cost Per Sq.ft', marker = 'p', markersize  = 8, 
            markerfacecolor='#5DE35E',markeredgecolor='white', markeredgewidth = 0.35)
    
    ax.plot(data['Floor_number'].astype(str), data[('Price', 'min')], linewidth=1.9, color='lightgrey', linestyle='--',
            label = 'Minimum Cost Per Sq.ft', marker = '$⧩$', markersize  = 8,  markerfacecolor='red',
            markeredgecolor='white', markeredgewidth = 0.35)
    
    
    ax.set_ylabel('Price Density (in ₹/Sq.ft)', fontsize=16, fontweight='bold', color='white', labelpad=12)
    ax.set_xlabel('Floor Number', fontsize=18, fontweight='bold', labelpad = 10, color='white')
    
    ax.set_xlim(-1, 24)
    ax.set_xticks(list(range(0, 24)))
    ax.set_xticklabels(data['Floor_number'].astype(str), fontsize = 12, fontweight = 'bold', color='white')
    
    ax.set_ylim(0,20000)
    ax.set_yticks(list(range(0, 20001, 2000)))
    ax.set_yticklabels(list(range(0, 20001, 2000)), fontsize = 10, fontweight = 'bold', color='white')
    
    fig.tight_layout()
    fig.patch.set_facecolor("#080707")    # figure background
    ax.set_facecolor("#080707")          # axes background
    
    ax.legend(fontsize=13, loc = 'upper left', fancybox=True, framealpha=1,
             edgecolor="white", facecolor='#080707', labelcolor="white")

    
    return fig


## Building Height Category & Price Trend:
def Do_higher_floors_in_taller_buildings_command_Premium_Pricing():
    ## Preparing data for Analysis:
    df['Floor_number'].replace({'Ground Floor' : '0'}, inplace = True)
    data = df[df['Floor'] != '-'].astype({'Floor_number': 'int32', 'Building_height': 'int32'})
    
    ## Lets Categorise Buildings based on their Total Floor Heights:
    thresh_1 = np.percentile(data['Building_height'], 33.33).astype('int32')   ## i.e., 14
    thresh_2 = np.percentile(data['Building_height'], 66.66).astype('int32')   ## i.e., 20
    
    def building_categorizer(height, thresh_1, thresh_2):
        if height <= thresh_1:
            return "Shorter Building"                    ## Height between 1 to 14
        elif height > thresh_1 and height <= thresh_2:
            return "Medium Building"                     ## Height between 14 to 20
        else:
            return "Taller Building"                     ## Height greater than 20
    
    data['Building_cate'] = data['Building_height'].apply(building_categorizer, thresh_1=thresh_1, 
                                                          thresh_2=thresh_2)
    
    ## Now, lets categorize Floor of a Building based on the position of Floor in the building:
    def floor_categorizer(data):
        height = data['Building_height']
        floor = data['Floor_number']
        
        if floor <= (1/3) * height:
            return 'Lower Floor'                                 ## Floor in lower 1/3rd part
        elif floor > (1/3) * height and floor <= (2/3) * height:
            return 'Middle Floor'                                ## Floor in middle 1/3rd part
        else:
            return 'Upper Floor'                                 ## Floor in upper 1/3rd part
    
    data['Floor_cate'] = data[['Floor_number', 'Building_height']].apply(floor_categorizer, axis=1)
    
    ## Now we just need to Groo by data based on Building Category and Floor Category and 
    ## get Aggregated Cost Per Sqft:
    
    def func_floo(data):
        pro_pri = data['Avg_price_rupee_per_sqft']
        return pd.Series([pro_pri.size, pro_pri.min(), pro_pri.max(), pro_pri.mean(), pro_pri.median()],
             index = pd.MultiIndex.from_tuples([('Price', 'tot_prop_listed'), ('Price', 'min'), 
                                                ('Price', 'max'), ('Price', 'mean'), ('Price', 'median')]))
    
    data = data.groupby(by=['Building_cate', 'Floor_cate']).apply(func_floo).astype({('Price', 
                                                                               'tot_prop_listed'):'int32'})
    data = data.reset_index()
    
    ## ------------------------------------------------------------------------------------------------
    ## Creating Plot: 
    fig = plt.figure(figsize = (14,4.8), dpi = 550)
    ax1 = fig.add_subplot(1,3,1)
    ax2 = fig.add_subplot(1,3,2)
    ax3 = fig.add_subplot(1,3,3)
    
    axes = [ax1, ax2, ax3]   ##Creating a list of all axes objects...
    
    building_categories = ['Shorter Building', 'Medium Building', 'Taller Building']
    building_labels = ['Shorter Building\n(1 to 14 Floors)', 'Medium Building\n(14 to 20 Floors)', 
                           'Taller Building\n(> 20 Floors)']
    
    for ax, building_category, building_label in zip(axes, building_categories, building_labels):
        temp = data[data['Building_cate'] == building_category]
        
        ax.plot(temp['Floor_cate'], temp[('Price', 'mean')], linewidth=1.8, color='white', 
                linestyle='--', label='Average Cost Per Sq.ft', marker='d', markersize=8,  
                markerfacecolor='#36E1F7', markeredgecolor='white', markeredgewidth = 0.01)
        
        ax.plot(temp['Floor_cate'], temp[('Price', 'median')], color='orange', linestyle='--',
                linewidth=1.8, label = 'Median Cost Per Sq.ft', marker = 'o', markersize  = 8, 
                markerfacecolor='#22D631',markeredgecolor='white', markeredgewidth = 0.01)
        
        ax.plot(temp['Floor_cate'], temp[('Price', 'min')], linewidth=1.8, color='lightgrey', 
                linestyle='--', label='Minimum Cost Per Sq.ft', marker='v', markersize=8,  
                markerfacecolor='red',markeredgecolor='white', markeredgewidth = 0.01)
    
        ax.set_ylabel('Price Density (in ₹/Sq.ft)', fontsize=14, fontweight='bold', color='white',
                     labelpad=12)
        ax.set_xlabel(building_label, fontsize=14, fontweight='bold', labelpad = 12, color='white')
        
        ax.set_xlim(-1, 3)
        ax.set_xticks(list(range(0, 3)))
        ax.set_xticklabels([i.split()[0] + '\n' + i.split()[1] for i in temp['Floor_cate'].values], 
                           fontsize = 12, fontweight = 'bold', color='white')
        
        ax.set_ylim(0,18500)
        ax.set_yticks(list(range(0, 18001, 2000)))

        for spline in ['top', 'bottom', 'left', 'right']:
            ax.spines[spline].set_color('#CFCFCF')

    
    ax1.set_yticklabels(list(range(0, 18001, 2000)), fontsize = 10, color='white')    
    ax2.get_yaxis().set_visible(False)
    ax3.get_yaxis().set_visible(False)
    
    fig.tight_layout()
    fig.patch.set_facecolor("#080707")    # figure background
    ax1.set_facecolor("#080707")          # axes background
    ax2.set_facecolor("#080707")          # axes background
    ax3.set_facecolor("#080707")          # axes background
    
    ax1.legend(fontsize=12, loc = 'upper left', fancybox=True, framealpha=1,
             edgecolor="white", facecolor='#080707', labelcolor="white")

    
    return fig


## -------------------------------------------------------------------------------------------------
## -------------------------------------------------------------------------------------------------
## -------------------------------------------------------------------------------------------------
## -------------------------------------------------------------------------------------------------
## -------------------------------------------------------------------------------------------------
## -------------------------------------------------------------------------------------------------





