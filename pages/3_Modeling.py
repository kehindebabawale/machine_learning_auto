from operator import index
import streamlit as st
import plotly.express as px
from pycaret.regression import *
from pycaret.classification import * 
import pandas as pd
import os


df = st.session_state["my_input"]
# page setup
st.image("background.png")
st.title("Data Modeling")
try:
    with st.sidebar:
        st.title("Modeling")
        st.image("modeling.png")
        choice = st.radio("Navigation", ["Run Modelling", "Download"])
        st.write("Wait let find the best model for the dataset, but befor that you will help to pick the target feature you are interested in...")
#try:
    if st.session_state["my_input"] is not None:
        if choice == "Run Modelling": 
            st.write('Grab a popcorn sachet, let do the magic.....this might take some minutes, depends on data size.')
            
            features_target = st.selectbox('Choose the Target Column', df.columns) 
            if st.button('Run Modelling'):

                setup(df, target=features_target, silent=True)
                setup_df = pull()
                st.write("Features summaries")
                st.dataframe(setup_df)
                best_model = compare_models()
                st.write("model's results, Note best model top the list.")
                compare_df = pull()
                st.dataframe(compare_df)
                save_model(best_model, 'best_model')
                    
            
        if choice == "Download": 
            
            with open('best_model.pkl', 'rb') as f: 
                st.download_button('Download Model', f, file_name="best_model.pkl")
except: 
    st.error("Chill...upload data first \N{smiling face with sunglasses}") 