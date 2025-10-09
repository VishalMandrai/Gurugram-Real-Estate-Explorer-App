import streamlit as st
import pandas as pd
import numpy as np


# --------------------------------------------- Page layout functions -----------------------------------------
def page_content():
    col0, col1, col2 = st.columns([0.5,3.7,5.8])
    with col1:
        st.image(image = "About me/my_prof_pic.png")
        
        st.markdown( """
        <div style="background-color:#EDDD68; padding:3px; width: 370px; 
        border-radius:5px; text-align:left;"></div>
        <br>
        <div style="font-size: 24px;"><p>
        <a href="https://www.linkedin.com/in/vishal-mandrai999/" target="_blank" style="
          text-decoration:none;
          background-color:#080707;
          border: 1.1px solid #ffffff;
          color:white;
          font-weight:600;
          padding:4px 8px;
          border-radius:6px;">
          in</a>
          &nbsp : &nbsp<a href="https://www.linkedin.com/in/vishal-mandrai999/" target="_blank"
          style="all:unset; cursor: pointer; font-family: calibiri;">
        vishalmandrai </a>        
        </p></div>

        <div style="font-size: 24px;">
        <a href="mailto:vishalm.nitt@gmail.com" style="
          text-decoration:none;
          background-color:#080707;
          border: 1.1px solid #ffffff;
          padding:4px 6px;
          border-radius:6px;
          color:#fff;
          font-weight:500;">
          ✉︎</a>
          &nbsp : &nbsp<a href="mailto:vishalm.nitt@gmail.com"
          style="all:unset; cursor: pointer; font-family: calibiri;">
        mailto:vishalmandrai </a>        
        </div>

        """,
        unsafe_allow_html=True)

    with col2:
        st.pdf("About me/Resume.pdf", height=850)    ## My resume....


## ------------------------------------------------------------------------------------------------------------

def main():
    page_content()
    

if __name__ == "__main__":
    main()










    