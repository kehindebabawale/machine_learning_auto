from operator import index
import streamlit as st
#import plotly.express as px
#from pycaret.regression import setup, compare_models, pull, save_model, load_model
import pandas_profiling
import pandas as pd
from streamlit_pandas_profiling import st_profile_report
import os 


st.image("data.png")
st.title("Dataset Uploading")
#
# choice = st.radio("Navigation", ["Upload","Profiling","Modelling", "Download"])
st.info("please upload training dataset.")
if "my_input" not in st.session_state:
    st.session_state["my_input"] = ""
file = st.file_uploader("Upload Your Dataset")
if file:
    df = pd.read_csv(file, index_col=None)
    df.to_csv('dataset.csv', index=None)
    st.dataframe(df)
    submit = st.button("Submit")
    if submit:
        if file is not None:
            st.session_state["my_input"]= df
            st.success("Sucessfully uploaded")
            st.write("Proceed to EDA")
        else:
            st.error("please select file to upload")
            

        