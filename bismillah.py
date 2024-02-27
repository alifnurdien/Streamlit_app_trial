import streamlit as st
import pandas as pd 


#title of the app
st.title("Well Log Data Visualization")

#sidebar
st.sidebar.subheader("Visualization setting")

#setup file upload
uploaded_file = st.sidebar.file_uploader(
                        label ="Upload your Excel or CSV File",
                         type=['xlsx','csv'])

global df
if uploaded_file is not None:
    print(uploaded_file)
    print("Good")
    try:
        df = pd.read_excel(uploaded_file)
    except Exception as e:
        print(e)
        df = pd.read_csv(uploaded_file)

try:
    st.write(df)
except Exception as e:
    print(e)
    st.write("Please upload file to the application")