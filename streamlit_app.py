import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

st.title('🤖 ML Linear Regression')

st.write('Machine Learning Model based on linear regression model')

data = pd.read_csv("Walmart_Sales.csv")

with st.expander("Walmart Data"):
  st.write("Raw Data")
  data

  st.write("Data Description")
  describe=data.describe()
  describe

  st.write("Null Data Count")
  data_null=data.isnull().sum()
  data_null
  
data = data.drop("Date",axis=1)

plt.figure(figsize=(12, 6))
sns.histplot(data['Weekly_Sales'], bins=20, kde=True)
plt.title('Distribution of Weekly Sales');
