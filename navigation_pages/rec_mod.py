# ------------------------------------------- Recommendation Engine Page ----------------------------------------
import streamlit as st
import pandas as pd
import numpy as np

## Global Variable for easy transitioning:
Recommend_flag = None             ## flag to transition to Recommendation based on inputs....

Locality_list = ['New Gurugram', 'Dwarka Expressway Belt', 'Golf Course Road & Extension', 'Old Gurgaon',
                 'Southern Peripheral Road (SPR) Belt', 'MG Road & Central Gurugram', 'Gwal Pahari', 'Kadarpur', 
                 'Dhunela']

df = pd.read_csv("navigation_pages/model/recommendation_engine/" + 
                 "Gurgaon_housing_data_of_top_300_soc_for_recommendation.csv", index_col = ["Unnamed: 0"])


## Similarity Matrices to be used for recommendation:
pricing = pd.read_csv("navigation_pages/model/recommendation_engine/" + 
                      "REC_1_Pricing_similarity_matrix.csv", index_col = 'Society_Loc')
facilities = pd.read_csv("navigation_pages/model/recommendation_engine/" + 
                         "REC_2_Facility_similarity_matrix.csv", index_col = 'Society_Loc')
locations = pd.read_csv("navigation_pages/model/recommendation_engine/" + 
                        "REC_3_Locations_similarity_matrix.csv", index_col = 'Society_Loc')

#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------

def page_title_content():
    ## Title of Page:
    st.markdown(
        """<h1 style='text-align: center; color: white;'> 
        🎯 PROPERTY RECOMMENDATION ENGINE
        </h1>""",  unsafe_allow_html=True)
    
    ## Analytics Module heading in the box:
    st.markdown( """<div style="background-color:#F2CBA2; padding:3px; 
                    border-radius:5px; text-align:center;"></div>""", unsafe_allow_html=True)

## -------------------------------------------------------------------------------------------------------------

def form_fill_for_recommendation():
    ## Selectbox for "Broader Locality" and "Society_Loc":
    Locality, Society, Rec_button = st.columns([3,5,2])
    with Locality:
        st.markdown("""
        <div style="background-color:#F2CBA2; padding:1px; border-radius:4px; 
        text-align:center;">
        <p style="color:#000000; font-size:30px; font-weight:700; margin:0;"> 
        Choose the
        <span style="font-size:28px; font-weight:bold; color:#5C250B; font-family: calibri !important;">
        LOCALITY</span></p>
        </div>

        <div><p style="font-size:0.2px;"><br></p></div>

        <style>
        div[data-baseweb="select"] > div {
            background-color: #000000; color: white;  border-radius: 5px; padding:-5px 10px;
            font-size: 20px; font-weight: 600; font-family: calibri;                            }
        </style>
        """, unsafe_allow_html=True)
    
        Locality = st.selectbox("", Locality_list, placeholder="Choose the Locality", index=int(1),
                                label_visibility="collapsed")


    with Society:
        st.markdown("""
        <div style="background-color:#F2CBA2; padding:1px; border-radius:4px; 
        text-align:center;">
        <p style="color:#000000; font-size:30px; font-weight:700; margin:0;"> 
        Choose the
        <span style="font-size:28px; font-weight:bold; color:#5C250B; font-family: calibri !important;">
        SOCIETY</span></p>
        </div>

        <div><p style="font-size:0.2px;"><br></p></div>
        """, unsafe_allow_html=True)
        ## Loading the Mapped Sector Locality records:    
        Society_list = df[df['Locality'] == Locality]['Society_Loc'].unique()
        Society_list = sorted(Society_list)

        Society_Loc = st.selectbox("", Society_list, placeholder="Choose the Society", index=int(22),
                                    label_visibility="collapsed")
    
    
    ## Button on click makes recommendation based on selection:
    with Rec_button:
        ## Styling the Streamlit Button:
        css = """
        <style>
        /* Target the native Streamlit button */
        div.stButton > button:first-child {
          background: linear-gradient(90deg,#ff7a18,#af002d); /* gradient */
          color: #fff;
          font-weight: 800 !important;
          font-size: 35px !important;
          padding: 10px 20px;
          border-radius: 5px;
          border: 2px solid rgba(255,255,255,0.15);
          box-shadow: 0 8px 20px rgba(0,0,0,0.18);
          cursor: pointer;
        }
        
        /* Add an icon-like pseudo-element (unicode) */
        div.stButton > button:first-child::before {
          content: "✨";
          margin-right: 5px;
          font-size: 25px;
        }
        </style>
        """
        st.markdown(css, unsafe_allow_html=True)
            
        if st.button("Recommend Societies!"):
            global Recommend_flag
            Recommend_flag = True


    ## Note: How socities are recommended? - Based on Pricing Similarity, Nearby Locations, and Facilities.
    st.markdown(
            """
            <style>
            .big-box-style1 {background-color:gba(61, 213, 109, 0.2); padding:7px; border-radius:8px; 
            border:1.2px solid #FFFFFF; color:#ffffff;}    
            </style>
            <div style="background-color:rgba(61, 213, 109, 0.2); padding:12px; 
            border-radius:8px; text-align:left;">
            <p style="color:#D6EAF8; font-size:20px; font-weight:600; margin:0;">
            Socities are recommended on the basis of 3 criteria :
            <span class="big-box-style1">I. Property Pricing Similarity</span> 
            <span class="big-box-style1">II. Nearby Locations</span> and 
            <span class="big-box-style1">III. Similar Facilities</span>
            </p></div>
            """, unsafe_allow_html=True)


    ## Transitioning to recommend similar Societies and show selected Society info:
    if Recommend_flag == True:
        Society_info_and_recommendations(Society_Loc)    
            

    
## -------------------------------------------------------------------------------------------------------------
    
def Society_info_and_recommendations(Society_Loc):
    ## Creating 2 sections to show society pricing info and List of Recommended Socities:
    society_info, recommended_societies = st.columns([6.8,3.2])
    
    with society_info:
        ## Putting Society name as heading:
        st.markdown("""
            <style> .big-box-style {background-color:#000000; padding:8px 25px; border-radius:8px; 
            border:2px solid #FFFFFF; color:#ffffff;} 
            </style>""" + """
            <div style="background-color:#080707; padding:1px; border-radius:12px; text-align:center;"><br>
            <p style="color:#ffffff; font-size:24px; font-weight:800; margin:5px;">
            <span class = "big-box-style">{}</span>
            </p></div> 
            <div><br></div>""".format(Society_Loc.split(", ")[0]), unsafe_allow_html=True)

        ## Showing Society Pricing Data:
        def pricing_info_scrapper(society):   # Function to get Property Priicng data in the selected Society...
            ## Fitering only Society data:
            data = df[df['Society_Loc'] == society]
        
            result = data.groupby(by = ['Flat']).agg({'Built_up_area_in_sqft': ["min", "max"], 
                                                      'Avg_price_rupee_per_sqft': ["min", "max"], 
                                                      'Price_in_rupees': ["min", "max"]})
            ## Writing the Column indices:
            col_ind_tuples = [("Built-up Area", "Min"), ("Built-up Area", "Max"), 
                              ("Price Density", "Min"), ("Price Density", "Max"),
                              ("Prop. Price", "Min"), ("Prop. Price", "Max")]
            
            result.columns = pd.MultiIndex.from_tuples(col_ind_tuples)

            ## Editing the data for readability:
            result[("Built-up Area", "Min")] = result[("Built-up Area", "Min")].astype('str') + " Sq.ft"
            result[("Built-up Area", "Max")] = result[("Built-up Area", "Max")].astype('str') + " Sq.ft"
        
            result[("Price Density", "Min")] = "₹ " + result[("Price Density", "Min")].astype('str') + " /Sq.ft"
            result[("Price Density", "Max")] = "₹ " + result[("Price Density", "Max")].astype('str') + " /Sq.ft"
            
            result[("Prop. Price", "Min")] = "₹ " + round(result[("Prop. Price", "Min")]/1e7, 2).astype('str') + " Cr."
            result[("Prop. Price", "Max")] = "₹ " + round(result[("Prop. Price", "Max")]/1e7, 2).astype('str') + " Cr."
    
            return result


        st.dataframe(pricing_info_scrapper(Society_Loc), width=5000) # Outputing the DF of Pricing Info of Society...

    ## ----------------------------------------------------------------------------------------------------------
    with recommended_societies:
        ## Putting a heading for Recommended socities:
        st.markdown("""
            <style> .big-box-style {background-color:#000000; padding:8px 12px; border-radius:8px; 
            border:2px solid #FFFFFF; color:#ffffff;} 
            </style>""" + """
            <div style="background-color:#080707; padding:1px; border-radius:12px; text-align:center;"><br>
            <p style="color:#ffffff; font-size:24px; font-weight:800; margin:5px;">
            <span class = "big-box-style">Top 10 Recommended Societies</span>
            </p></div> 
            <div><br></div>""", unsafe_allow_html=True)    
        
        st.dataframe(recommend_society(Society_Loc), width=5000, height=250)   
                                                            # Outputing the list of top 10 similar Societies...
        
    
    st.divider()
    ## Transitioning to recommend similar Societies and show selected Society info:
    Show_property_listings(recommend_society(Society_Loc))    


## -------------------------------------------------------------------------------------------------------------
## Below 2 functions will return the WC for Locations around Socit
def Show_property_listings(data):
    ## Putting a heading for List of Suggested Properties in Recommended Societies:
    st.markdown("""
        <style> .big-box-style {background-color:#000000; padding:8px 12px; border-radius:8px; 
        border:2px solid #FFFFFF; color:#ffffff;} 
        </style>""" + """
        <div style="background-color:#080707; padding:1px; border-radius:12px; text-align:center;"><br>
        <p style="color:#ffffff; font-size:24px; font-weight:800; margin:5px;">
        <span class = "big-box-style">Property Listings in Top 10 Recommended Societies</span>
        </p></div> 
        <div><br></div>""", unsafe_allow_html=True)    

    props = df[df['Society_Loc'].isin(data.iloc[:,0].values[0:5])]
    props = props[['Flat', 'Society', 'Sector_Locality', 'Locality', 'Built_Up_Area', 'Avg_Price', 'Price',
                   'Floor', 'Facing', 'Brokerage', 'EMI', 'Link']]
    if props.shape[0] < 50:
        props = props.sample(props.shape[0], random_state = 25).sort_values(by = ['Flat']).reset_index(drop=True)
    else:
        props = props.sample(50, random_state = 25).sort_values(by = ['Flat']).reset_index(drop=True)


    ## Outputing a DF of Properties in the Recommended Societies:
    config = {
        'Flat' : "🏠 Flat Type",
        'Society': "🏙️ Society", 
        'Sector_Locality': "Area of Gurugram", 
        'Locality': "Locality of Gurugram", 
        'Built_Up_Area': "📐 Built-up Area (in Sq.ft)", 
        'Avg_Price': "Price density (in ₹/Sq.ft)", 
        'Price': "💰 Price (in ₹)",
        'Floor': "Floor", 
        'Facing': "Flat Facing", 
        'Brokerage': "Brokerage (in ₹)", 
        'EMI': "EMI (in ₹)", 
        'Link': st.column_config.LinkColumn("🔗 Link")
    }

    st.dataframe(props, column_config = config)

    st.divider()

## -------------------------------------------------------------------------------------------------------------

## Function to recommend Top 10 similar Societies:
def recommend_society(society_name):
    ## Using imported Similarity matrices:
    sim_matrix = (35 * pricing) + (5 * facilities) + (15 * locations) #set the weights as per the preference
    
    societies = sim_matrix[society_name].sort_values(ascending = False).iloc[1:11].index
    return pd.DataFrame(societies.values, index = range(1,11), columns = ['Most Similar Societies'])

## -------------------------------------------------------------------------------------------------------------

def main():
    ## Page's Introductory Content:
    page_title_content()

    ## Form to take input from user and then Provide Recommendations:
    form_fill_for_recommendation()



if __name__ == "__main__":
    main()



