import streamlit as st
import pandas as pd
import numpy as np
import json, pickle

## Global Variable to store Price Prediction Result:
response = None

## List of all Flats: ---------------------------------------------------------------------------------------------
Flat_type = ['1 BHK Flat', '2 BHK Flat', '2.5 BHK Flat', '3 BHK Flat', '3.5 BHK Flat', 
             '4 BHK Flat', '4.5 BHK Flat', '5 BHK Flat', '1 RK Flat']

## List of all Sector_Localities: ---------------------------------------------------------------------------------
# Sector_Locality = ['Sector 1', 'Sector 2', 'Sector 3', 'Sector 3A', 'Sector 4', 'Sector 5', 'Sector 6', 'Sector 7', 
#                   'Sector 9A', 'Sector 10A', 'Sector 11', 'Sector 12', 'Sector 14', 'Sector 15', 'Sector 22A', 
#                   ..... , 'Sector 112', 'Sector 113', 'DLF Phase 1', 'DLF Phase 2', 'DLF Phase 3', 'DLF Phase 4', 
#                   'DLF Phase 5', 'Dhunela', 'Gwal Pahari', 'Kadarpur', 'Manesar', 'Nurpur Jharsa', 'Palam Vihar', 
#                   'Palam Vihar Extension', 'Southern Peripheral Road', 'Sushant Lok Phase 1', 'Tulip Violet Society']

# These are the smaller Sector Localities of Gurugram!

## List of all Locality: ----------------------------------------------------------------------------------------
Locality_list = ['New Gurugram', 'Dwarka Expressway Belt', 'Golf Course Road & Extension', 'Old Gurgaon',
                 'Southern Peripheral Road (SPR) Belt', 'MG Road & Central Gurugram', 'Gwal Pahari', 
                 'Kadarpur', 'Dhunela']

## List of all Age Category: ------------------------------------------------------------------------------------
Age_Category_list = ['Newer Property (< 5 Years)', 'Mid Age Property (5 to 10 Years)', 
                     'Slightly Older (10 to 15 Years)', 'Older Property (> 15 Years)']    
                                            # Age_Category_list.split(" (")[0]

## List of all Floor Category: ----------------------------------------------------------------------------------
Floor_Category_list = ['Lower Floor', 'Middle Floor', 'Upper Floor']
                                            # Put a info tag with message that relative to building

## List of all Building Height Category: ------------------------------------------------------------------------
Building_Height_Category_list = ['Shorter Building (< 14 Floors)', 'Medium Building (14 t0 20 Floors)',
                                 'Taller Building ( > 20 FLoors)']
                                            # Building_Height_Category_list.split(" (")[0]

## List of all Furnishing Category: -----------------------------------------------------------------------------
Furnishing_list = ['Fully Furnished', 'Semi Furnished', 'Unfurnished']

#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------

def page_title_content():
    ## Title of Page:
    st.markdown(
        """<h1 style='text-align: center; color: white;'> 
        💰 PRICE PREDICTION MODEL
        </h1>""",  unsafe_allow_html=True)
    
    ## Analytics Module heading in the box:
    st.markdown( """<div style="background-color:#E6A51C; padding:3px; 
                    border-radius:5px; text-align:center;"></div>""", unsafe_allow_html=True)

## -------------------------------------------------------------------------------------------------------------

def form_to_fill():
    ## Selectbox for Locality and Sector_Locality:
    Locality, Sec_Locality = st.columns([5,5])
    with Locality:
        st.markdown("""
        <div style="background-color:#FAC552; padding:1px; border-radius:4px; 
        text-align:center;">
        <p style="color:#000000; font-size:30px; font-weight:700; margin:0;"> 
        Choose the
        <span style="font-size:28px; font-weight:bold; color:#5C250B; font-family: calibri !important;">
        BROADER LOCALITY</span></p>
        </div>

        <div><p style="font-size:0.2px;"><br></p></div>

        <style>
        div[data-baseweb="select"] > div {
            background-color: #000000; color: white;  border-radius: 5px; padding:0px 0px;
            font-size: 20px; font-weight: 600; font-family: calibri;                            }
        </style>
        """, unsafe_allow_html=True)
    
        Locality = st.selectbox("", Locality_list, placeholder="Choose the Locality", index=int(1),
                                label_visibility="collapsed")


    with Sec_Locality:
        st.markdown("""
        <div style="background-color:#FAC552; padding:1px; border-radius:4px; 
        text-align:center;">
        <p style="color:#000000; font-size:25px; font-weight:700; margin:0;"> 
        Choose the
        <span style="font-size:28px; font-weight:bold; color:#5C250B; font-family: calibri !important;">
        AREA</span></p>
        </div>

        <div><p style="font-size:0.2px;"><br></p></div>

        <style>
        div[data-baseweb="select"] > div {
            background-color: #000000; color: white;  border-radius: 5px; padding:0px 0px;
            font-size: 20px; font-weight: 600; font-family: calibri;                            }
        </style>
        """, unsafe_allow_html=True)
        ## Loading the Mapped Sector Locality records:
        with open("navigation_pages/model/Locality_&_Sector_Loc_sorted.json", "r") as file:
            Sec_Locality_records = json.load(file)

        Sec_Locality = st.selectbox("", Sec_Locality_records[Locality], placeholder="Choose the Area", index=int(0),
                                    label_visibility="collapsed")
    
    
    
    ## Flat Type, Built-Up Area, Bedrooms and Bathrooms: -----------------------------------------------------------
    st.divider()
    col1, col2, col3, col4 = st.columns([1,1,1,1])

    with col1:   # Selectboc for Flat Type.... 
        st.markdown("""
        <div style="background-color:#FAC552; padding:1px; border-radius:4px; 
        text-align:center;">
        <p style="color:#000000; font-size:25px; font-weight:700; margin:0;"> 
        Flat Type
        <span style="font-size:28px; font-weight:bold; color:#5C250B; font-family: calibri !important;">
        </span></p>
        </div>
        
        <div><p style="font-size:0.2px;"><br></p></div>
        """, unsafe_allow_html=True)
        Flat = st.selectbox("", Flat_type, placeholder="Choose Flat Type", index=int(3),
                            label_visibility="collapsed")
        
    with col2:   # Number Input Box for Built-up Area.... 
        st.markdown("""
        <div style="background-color:#FAC552; padding:1px; border-radius:4px; 
        text-align:center;">
        <p style="color:#000000; font-size:25px; font-weight:700; margin:0;"> 
        Built-up Area
        <span style="font-size:28px; font-weight:bold; color:#5C250B; font-family: calibri !important;">
        </span></p>
        </div>

        <div><p style="font-size:0.2px;"><br></p></div>
        
        <style>
        .stNumberInput div[data-baseweb="input"] > div {
            background-color: #000000; /* Light blue background */
            border: 1px solid #ffffff; /* Light blue border */
            border-radius: 4px; }
    
        .stNumberInput label {
            font-size:0.1px !important;
            color: #333333;}
        </style>
        """, unsafe_allow_html=True)
        
        Area = st.number_input("", min_value=180, max_value=10000, value=1000, step=50, format=None, 
                               placeholder=None, disabled=False, label_visibility="collapsed")
        
        Area = np.log1p(Area)    # Applying Log transformation on Built-up Area...  

    with col3:     # Number Input Box for Bedroom Count.... 
        st.markdown("""
        <div style="background-color:#FAC552; padding:1px; border-radius:4px; 
        text-align:center;">
        <p style="color:#000000; font-size:25px; font-weight:700; margin:0;"> 
        Bedrooms
        <span style="font-size:28px; font-weight:bold; color:#5C250B; font-family: calibri !important;">
        </span></p>
        </div>

        <div><p style="font-size:0.2px;"><br></p></div>
        """, unsafe_allow_html=True)
        
        Bedrooms = st.number_input("", min_value=1, max_value=5, value=3, step=1, format=None, 
                               placeholder=None, disabled=False, label_visibility="collapsed")
        

    with col4:     # Number Input Box for Bathroom Count.... 
        st.markdown("""
        <div style="background-color:#FAC552; padding:1px; border-radius:4px; 
        text-align:center;">
        <p style="color:#000000; font-size:25px; font-weight:700; margin:0;"> 
        Bathrooms
        <span style="font-size:28px; font-weight:bold; color:#5C250B; font-family: calibri !important;">
        </span></p>
        </div>

        <div><p style="font-size:0.2px;"><br></p></div>
        """, unsafe_allow_html=True)
        
        Bathrooms = st.number_input("", min_value=1, max_value=6, value=3, step=1, format=None, 
                                    placeholder=None, disabled=False, label_visibility="collapsed")



    ## Age, Floor, Building Height and Furnishing: -----------------------------------------------------------
    st.divider()
    col1, col2, col3, col4 = st.columns([1,1,1,1])
    
    with col1:     # Radio Button Selection for Age Category....
        st.markdown("""
        <div style="background-color:#FAC552; padding:1px; border-radius:4px; 
        text-align:center;">
        <p style="color:#000000; font-size:25px; font-weight:700; margin:0;"> 
        Age
        <span style="font-size:28px; font-weight:bold; color:#5C250B; font-family: calibri !important;">
        </span></p>
        </div>

        <div><p style="font-size:0.2px;"><br></p></div>
        """, unsafe_allow_html=True)
        Age_category = st.radio('', Age_Category_list, label_visibility="collapsed")

        Age_category = Age_category.split(" (")[0]


    with col2:     # Check Box for Floor Category....
        st.markdown("""
        <div style="background-color:#FAC552; padding:1px; border-radius:4px; 
        text-align:center;">
        <p style="color:#000000; font-size:25px; font-weight:700; margin:0;"> 
        Floor
        <span style="font-size:28px; font-weight:bold; color:#5C250B; font-family: calibri !important;">
        </span></p>
        </div>

        <div><p style="font-size:0.2px;"><br></p></div>
        """, unsafe_allow_html=True)
        Floor_category = st.radio('', Floor_Category_list, label_visibility="collapsed")


    with col3:     # Check Box for Building Height Category....
        st.markdown("""
        <div style="background-color:#FAC552; padding:1px; border-radius:4px; 
        text-align:center;">
        <p style="color:#000000; font-size:25px; font-weight:700; margin:0;"> 
        Building Height
        <span style="font-size:28px; font-weight:bold; color:#5C250B; font-family: calibri !important;">
        </span></p>
        </div>

        <div><p style="font-size:0.2px;"><br></p></div>
        """, unsafe_allow_html=True)
        Building_height_category = st.radio('', Building_Height_Category_list, label_visibility="collapsed")
        
        Building_height_category = Building_height_category.split(" (")[0]


    with col4:     # Check Box for Funishing Category....
        st.markdown("""
        <div style="background-color:#FAC552; padding:1px; border-radius:4px; 
        text-align:center;">
        <p style="color:#000000; font-size:25px; font-weight:700; margin:0;"> 
        Furnishing Status
        <span style="font-size:28px; font-weight:bold; color:#5C250B; font-family: calibri !important;">
        </span></p>
        </div>

        <div><p style="font-size:0.2px;"><br></p></div>
        """, unsafe_allow_html=True)
        Furnishing_category = st.radio('', Furnishing_list, label_visibility="collapsed")


    ## Covered_parking, Open_parking, Balcony & Sector_Amenity_Score: ----------------------------------------
    st.divider()
    col1, col2, col3, col4 = st.columns([1,1,1,1])

    with col1:     # Number Input Box for Covered Parking Count.... 
        st.markdown("""
        <div style="background-color:#FAC552; padding:1px; border-radius:4px; 
        text-align:center;">
        <p style="color:#000000; font-size:25px; font-weight:700; margin:0; padding:0px 0px;"> 
        Covered Parking Space</p>
        </div>

        <div><p style="font-size:0.2px;"><br></p></div>
        """, unsafe_allow_html=True)
        
        Covered_parking = st.number_input("", min_value=0, max_value=6, value=1, step=1, format=None, 
                                          placeholder=None, disabled=False, label_visibility="collapsed")

    with col2:     # Number Input Box for Open Parking Count.... 
        st.markdown("""
        <div style="background-color:#FAC552; padding:1px; border-radius:4px; 
        text-align:center;">
        <p style="color:#000000; font-size:25px; font-weight:700; margin:0; padding:0px 0px;"> 
        Open Parking Space</p>
        </div>

        <div><p style="font-size:0.2px;"><br></p></div>
        """, unsafe_allow_html=True)
        
        Open_parking = st.number_input("", min_value=0, max_value=4, value=1, step=1, format=None, 
                                          placeholder=None, disabled=False, label_visibility="collapsed")


    with col3:     # Number Input Box for Open Parking Count.... 
        st.markdown("""
        <div style="background-color:#FAC552; padding:1px; border-radius:4px; 
        text-align:center;">
        <p style="color:#000000; font-size:25px; font-weight:700; margin:0; padding:0px 0px;">
        Balcony</p>
        </div>

        <div><p style="font-size:0.2px;"><br></p></div>
        """, unsafe_allow_html=True)
        
        Balcony = st.number_input("", min_value=0, max_value=6, value=2, step=1, format=None, 
                                  placeholder=None, disabled=False, label_visibility="collapsed")


    with col4:     # Number Input Box for Open Parking Count.... 
        st.markdown("""
        <div style="background-color:#FAC552; padding:1px; border-radius:4px; 
        text-align:center;">
        <p style="color:#000000; font-size:25px; font-weight:700; margin:0; padding:0px 0px;">
        Area Amenity Score</p>
        </div>

        <div><p style="font-size:0.2px;"><br></p></div>
        """, unsafe_allow_html=True)
        
        Score = st.slider("", min_value=0.0, max_value=10.0, value=8.5, step=0.01, format=None, 
                          disabled=False, label_visibility="collapsed")


    st.divider()
    
    ## Time to predict:
    Col_names = ['Flat', 'Sector_Locality', 'Locality', 'Built_up_area_in_sqft',
                 'Age_Category', 'Floor_Category', 'Building_Height_Category',
                 'Furnishing', 'Bedrooms', 'Bathrooms', 'Covered_parking',
                 'Open_parking', 'Balcony', 'Sector_Amenity_Score']
    
    values = [[Flat, Sec_Locality, Locality, Area, Age_category, Floor_category, Building_height_category,
              Furnishing_category, Bedrooms, Bathrooms, Covered_parking, Open_parking, Balcony, Score]]

    # Creating DF:
    rec = pd.DataFrame(values, columns = Col_names)

    Prediction(rec)    ## Calling Prediction Function....

## -------------------------------------------------------------------------------------------------------

def Prediction(data):
    global response      # Gobal declaration to alter the value within function....

    model_path = 'navigation_pages/model/XGBoost_model_pipeline.pkl'
   
    with open(model_path, 'rb') as file:                  ## Loading the Model Pipeline....
        modelXGBR = pickle.load(file)

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

    ## Click button to get the Predicted Price:
    col1,col2,col3, col4, col5 = st.columns([1,1,1,1,1])
    with col3:
        if st.button("Predict Price!"):
            response = np.expm1(modelXGBR.predict(data))          ## Result from Model....
    
    if response != None:
        Display_prediction(int(response[0]), data)     # Calling function to display results....

    
## -------------------------------------------------------------------------------------------------------------

def Display_prediction(prediction, data):
    flat = data['Flat'].values[0]
    area = data['Sector_Locality'].values[0]
    locality = data['Locality'].values[0]

    ## Our Model's Test MAE is ₹ 22 Lacs. So let's output a range of price instead of an absolute number.
    lower_pred = prediction - 22e5
    upper_pred = prediction + 22e5
    
    def edit_price(price):                            ## to edit the Price in readable string format
        if len(str(price)) > 7:
            return "₹ " + str(round(price/1e7, 2)) + " Cr"
        else:
            return "₹ " + str(round(price/1e5, 2)) + " Lacs"

    lower_pred = edit_price(lower_pred)
    prediction = edit_price(prediction)
    upper_pred = edit_price(upper_pred)


    ## Outputing Prediction Results:
    st.markdown("""
        <style> .big-box-style {background-color:#ffffff; padding:8px 12px; border-radius:8px; 
        border:2px solid #FFFFFF; color:#000000;} 
        </style>""" + """
        <div style="background-color:#080707; padding:0px; border-radius:12px; text-align:center;"><br>
        <p style="color:#ffffff; font-size:28px; font-weight:800; line-height: 2.3; margin:0px;">
        <span class = "big-box-style">{}</span> in 
        <span class = "big-box-style">{}</span> of 
        <span class = "big-box-style">{}</span> with specified specs <br>
        would cost between 
        </p></div>""".format(flat, area, locality), unsafe_allow_html=True)

    show_price_range(lower_pred, upper_pred)   ## Function to show Price Range on a line....


## -------------------------------------------------------------------------------------------------------------

def show_price_range(lower_pred, upper_pred):
    st.markdown("""
    <style>
    /* Container */
    .dot-line-wrapper {
      width: 100%;
      max-width: 600px;
      margin: 40px auto;
      position: relative;
      padding: 40px 0px 20px; /* space for labels above */
      box-sizing: border-box;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial;
    }
    
    /* The horizontal line */
    .dot-line {
      position: relative;
      height: 4px;
      background: linear-gradient(90deg,#dfe7f5, #bfcff0);
      border-radius: 20px;
      margin-top: 35px; /* leaves space for labels above */
    }
    
    /* Generic dot */
    .dot {
      position: absolute;
      width: 14px;
      height: 14px;
      border-radius: 50%;
      background: linear-gradient(180deg,#2b7be9,#195bbb);
      box-shadow: 0 4px 10px rgba(25,91,187,0.28);
      transform: translateX(-50%) translateY(-50%);
      top: 65%; /* sits centered on the line */
      z-index: 3;
    }
    
    /* label box above each dot */
    .dot-label {
      position: absolute;
      transform: translateX(-50%);
      top: 0; /* sits above the line */
      z-index: 4;
      padding: 4px 20px;
      border-radius: 8px;
      background: #000000;
      border: 2.5px solid #fff;
      box-shadow: 0 6px 18px rgba(12,40,80,0.06);
      font-size: 25px;
      font-weight: 700;
      font-family: calibiri;
      white-space: nowrap;
    }
    
    /* small arrow/triangle pointing down from label to dot */
    .dot-label::after {
      content: "";
      position: absolute;
      left: 50%;
      transform: translateX(-50%);
      top: 100%;
      width: 0;
      height: 0;
      border-left: 7px solid transparent;
      border-right: 7px solid transparent;
      border-top: 8px solid white; /* arrow color = label bg */
      filter: drop-shadow(0 2px 2px rgba(12,40,80,0.04));
      z-index: 4;
    }
    
    /* subtle connecting stem to align arrow over the dot */
    .dot-label::before {
      content: "";
      position: absolute;
      left: 50%;
      transform: translateX(-50%);
      top: calc(100% - 1px);
      width: 2px;
      height: 8px;
      background: transparent;
      z-index: 3;
    }
    
    /* positions for the three dots (customize %, as needed) */
    .dot.dot-mid    { left: 50%; }   /* middle dot */
    .dot.dot-end-1  { left: 0%; }   /* first of the two at end */
    .dot.dot-end-2  { left: 100%; }   /* second of the two at end (adjacent) */
    
    /* corresponding label positions (same left values) */
    .label-mid      { left: 50%; }
    .label-end-1    { left: 0%; }
    .label-end-2    { left: 100%; }
    
    /* responsive tweaks */
    @media (max-width: 520px) {
      .dot-line-wrapper { padding: 32px 8px 12px; max-width: 95%; }
      .dot { width: 12px; height: 12px; }
      .dot-label { font-size: 12px; padding: 5px 8px; border-radius: 6px; }
      .dot-label::after { border-left: 6px solid transparent; border-right: 6px solid transparent; border-top: 6px solid white; }
      .dot.dot-end-1 { left: 76%; }
      .dot.dot-end-2 { left: 86%; }
      .label-end-1 { left: 76%; }
      .label-end-2 { left: 86%; }
    }
    </style>""" + """
    
    <div class="dot-line-wrapper">
      <div class="dot-line"></div>
    
      <!-- Left End + label -->
      <div class="dot dot-end-1" aria-hidden="true"></div>
      <div class="dot-label label-end-1">{}</div>
      
      <!-- Right End + label -->
      <div class="dot dot-end-2" aria-hidden="true"></div>
      <div class="dot-label label-end-2">{}</div>
    </div>
    """.format(lower_pred, upper_pred), unsafe_allow_html=True)


## -------------------------------------------------------------------------------------------------------------

def main():                      ## Function from where execution starts....
    ## Page's Intro Content:
    page_title_content()

    ## Information Form for Prediction input:
    form_to_fill()



if __name__ == '__main__':
    main()
