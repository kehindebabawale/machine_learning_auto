#load library

from operator import index
import streamlit as st
import plotly.express as px
from pandas_profiling import ProfileReport
import pandas as pd
from streamlit_pandas_profiling import st_profile_report
import os


st.title("Exploratory Data Analysis")
st.image("EDA2.png")

st.write("Here we are going to summarise and explore the file uploaded data. Guess what?..you will be able to download the EDA report.")
st.write()

try:
    profile = st.button("Click to Profile")
    if profile:
        if st.session_state["my_input"] is not None:
            df = st.session_state["my_input"]
            profile_df = ProfileReport(df)
            st_profile_report(profile_df)
            EDA_report = profile_df.to_html()
            st.download_button(
                label="Download EDA report",
                data=EDA_report,
                file_name='EDA_report.html')
            st.success("proceed to modelling")
        else:
                st.error("Please Upload Dataset")
    else:
        st.write("Please Upload Dataset")
except:
    st.error("please upload data")
