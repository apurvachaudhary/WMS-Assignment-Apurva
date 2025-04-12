import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("WMS Sales Data Viewer")

uploaded_file = st.file_uploader("Upload cleaned sales CSV", type="csv")
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("Preview of Data:", df.head())

    if 'MSKU' in df.columns and 'Quantity' in df.columns:
        msku_summary = df.groupby('MSKU')['Quantity'].sum().reset_index()
        st.bar_chart(msku_summary.set_index('MSKU'))