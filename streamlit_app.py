import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title('🤖 ML Linear Regression')

st.write('Machine Learning Model based on linear regression model')

df = pd.read_csv("Walmart_Sales.csv")

with st.expander("Walmart Data"):
  st.write("Raw Data")
  df
