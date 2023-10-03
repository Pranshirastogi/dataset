import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px 

st.title('HR-EMPLOYEE-ATTRITION')
st.markdown('''**HR-EMPLOYEE-ATTRITION** is a web app to predict the attrition of an employee in an organization.
            This app shows the prediction of attrition of an employee based on the data provided by the user.
            And also understanding the employees behaviour and their performance in the organization.
            Also things affecting the attrition of an employee in the organization.
            ''')
df=pd.read_csv('HR-Employee-Attrition.csv')
df=df.drop(['EmployeeCount','EmployeeNumber','Over18','StandardHours'],axis=1)
st.subheader('Data Information:')
if st.sidebar.checkbox('Show Data'):
    st.subheader('Raw Data')
    st.write(df)
if st.sidebar.checkbox('Show Shape'):
    st.subheader('Data Shape:')
    st.write(df.shape)
if st.sidebar.checkbox('Show Columns'):
    st.subheader('Columns Names:')
    st.write(df.columns)  
if st.sidebar.checkbox('Attribute Information'):
    st.subheader('Attrition Count:')
    st.write(df['Attrition'].value_counts())
    st.subheader('Attrition Percentage:')
    st.write(df['Attrition'].value_counts()/df.shape[0]*100)
    st.bar_chart(df['Attrition'].value_counts())
st.sidebar.subheader('Visualization Selector')




