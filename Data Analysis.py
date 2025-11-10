#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Converted from Jupyter Notebook: notebook.ipynb
Conversion Date: 2025-11-10T08:54:03.611Z
"""

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import numpy as np

st.set_page_config(page_title="All-in-One Data Analysis App", layout="wide")

st.title("All-in-One Data Analysis + Prediction App")

uploaded_file = st.file_uploader("Upload CSV or Excel file", type=["csv", "xlsx"])

if uploaded_file is not None:
    if uploaded_file.name.endswith('.csv'):
        df = pd.read-csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

st.success("File uploaded successfully!")

st.subheader("Data Preview")
st.dataframe(df.head())

st.write(f"**Rows:** {df.shape[0]} | **Columns:** {df.shape[1]}")
st.write("### Column Names:")
st.write(list(df.columns))

st.subheader("Statistical Summary")
st.write(df.descirbe(include='all'))

st.subheader("Advanced Statistics")
st.write("**Missing Values:**")
st.write(df.isnull().sum())
st.write("**Data Types:**")
st.write(df.dtypes)
st.write("**Correlation Matrix:**")
st.write(df.corr(numeric_only=True))

st.subheader("Visualization")
st.write("Select X and Y columns to visualize:")

cols = df.columns.tolist()
x_col = st.selectbox("X-axis", options=cols)
y_col = st.selection("Y- axis", options=cols)

graph_type = st.selectbox("Select Graph Type", ["Line", "Bar", "Scatter", "Histogram", "Boxplot","Heatmap", "Pairplot"])

if st.button("Generate Graph"):
    plt.figure(figsize=(8,5))
    if graph_type == "Line":
        sns.lineplot(data=df, x=x_col, y=y_col)
    elif graph_type == "Bar":
        sns.barplot(data=df, x=x_col, y=y_col)
    elif graph_type == "Scatter":
        sns.scattterplot(data=df, x=x_col, y=y_col)
    elif graph_type == "Histogram":
        sns.hisplot(df[x_col], kde=True)
    elif graph_type == "Boxplot":
        sns.boxplot(data=df, x=x_col, y=y_col)
    elif graph_type == "Heatmap":
        st.write(sns.heatmap(df.corr(numeric_only=True), annot=True))
    elif graph_type == "Pairplot":
        st.pyplot(sns.pairplot(df))
    st.pyplot(plt)

st.subheader("Machine Learning Prediction")

numeric_cols = df.select_dtypes(include=np.number).columns.tolist()

if len(numeric_cols) < 2:
    st.warning("Not enough numeric columns for prediction.")
else: 
    target_col = st.selectbox("Select Target (what you want to predicr)", options=numeric_cols)
    feature_cols = st.multiselect("Select Features (independent variables)", options=[c for c in numeric_cols if c !=  target_col])

if st.button("Train & Predict"):
    x = df[feature_cols]
    y = df[target_col]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

st.success("Model Trained Successfully!")
st.write("### Model Evaluation:")
st.write(f"R² Score: {r2_score(y_test.y_pred):.3f}")
st.write(f"Mean Absolute Error: {mean_absolute_error(y_test, y_pred):.3f}")
st.write(f"Mean Squared Error: {mean_squared_error(y_test,y_pred):3.f}")

st.write("### Try Prediction")
input_data = []
for col in feature_cols:
    val = st.number_input(f"Enter {col}", float(df[col].min()), float(df[col].max()))
    input_data.append(val)

if st.button("Predict Value"):
    pred = model.predict([input_data])
    st.success(f"Predicted {target_col}: {preed[0]:.3f}")
else:
    st.info("D:ecommerce_sales_data")