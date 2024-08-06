import streamlit as st
import pandas as pd

st.title('🤖 ML Linear Regression')

st.write('Machine Learning Model based on linear regression model')

df = pd.read_csv("Walmart_Sales.csv")
