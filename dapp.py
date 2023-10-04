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
if st.sidebar.subheader('Visualization Selector:'):
    if st.sidebar.checkbox('Types of Job Roles'):
        fig1 = px.pie(df, names='JobRole', title='Job Role') 
        st.plotly_chart(fig1)
        st.subheader('Data Analysis:')
        st.write('**Sales Executive** has the highest number of employees in the organization.Followed by **Research Scientist** and **Laboratory Technician**.')
    if st.sidebar.checkbox('Business Travel'):
        fig2 = px.bar(df,x='JobRole', y='BusinessTravel',facet_col='BusinessTravel',color='JobRole', title='Business Travel by Job Role',height=600,width=800)
        st.plotly_chart(fig2)
        st.subheader('Data Analysis:')
        st.write('**Sales Executives** travels the most rarely in the organisation.And by the visualisation of data we can see employees prefer traveling rarely or frequently. ')
    if st.sidebar.checkbox('Monthly Income by Gender division'):
        fig3 = px.violin(df, x='JobRole', y='MonthlyIncome', color='JobRole',facet_col='Gender', title='Monthly Income by Job Role')
        st.plotly_chart(fig3)
        st.subheader('Data Analysis:')
        st.write('There is slight difference between montly incomes of males and females in the organisation irrespective of their job roles. ')
    if st.sidebar.checkbox('Monthly Income by Age'):
        fig4 = px.scatter(df, x='MonthlyIncome', y='Age', color='JobRole', title='Monthly Income by Age')
        st.plotly_chart(fig4)
        st.subheader('Data Analysis:')
        st.write('Employees with age between 30 to 40 have the highest monthly income in the organisation.')
    if st.sidebar.checkbox('Job Satisfaction by Job Role'):
        fig5 = px.histogram(df, x='JobRole', y='JobSatisfaction',facet_col='Attrition', color='JobRole', title='Job Satisfaction by Job Role')
        st.plotly_chart(fig5)
        st.subheader('Data Analysis:')
        st.write('Employees with job role **Sales Executive** and **Research Scientist** have the highest job satisfaction in the organisation.')
    if st.sidebar.checkbox('Marital Status'):
        fig6 = px.bar(df,x='Age',y='MaritalStatus',facet_col='Gender',color='Attrition',title='Marital Status by Age')
        st.plotly_chart(fig6)
        st.subheader('Data Analysis:')
        st.write('Employees with age between 30 to 40 are married and have the highest attrition rate in the organisation.')
    if st.sidebar.checkbox('Job Satisfaction by Age'):
        fig7 = px.histogram(df,x='Age',y='JobSatisfaction',color='Gender',title='Job Satisfaction by Age')
        st.plotly_chart(fig7)
        st.subheader('Data Analysis:')
        st.write('Employees with age between 30 to 40 have the highest job satisfaction in the organisation.')
    if st.sidebar.checkbox('Years worked at company'):
        fig8 = px.scatter(df,x='Age',y='YearsAtCompany',facet_col='Attrition',title='Years at Company by Age')
        st.plotly_chart(fig8)
        st.subheader('Data Analysis:')
        st.write('Employees with no attrition have worked for more than 10 years in the organisation than the employees with attrition.')
    if st.sidebar.checkbox('Years worked in current role'):
        fig9 = px.bar(df,x='JobRole',y='YearsInCurrentRole',facet_col='Attrition',title='Years in Current Role by Age')
        st.plotly_chart(fig9)
        st.subheader('Data Analysis:')
        st.write('Employees with no attrition have worked for more than 10 years in the organisation than the employees with attrition in the current roles.')
    if st.sidebar.checkbox('Years worked with current manager'):
        fig10 = px.box(df,x='JobRole',y='YearsWithCurrManager',facet_col='Attrition',color='JobRole',title='Years with Current Manager by Age')
        st.plotly_chart(fig10)
        st.subheader('Data Analysis:')
        st.write('**Research Directors**have worked for more than 10 years with current manager than the employees with attrition than the employees of other roles.')
    if st.sidebar.checkbox('Percent salary hike'):
        fig11 = px.histogram(df,x='MonthlyIncome',y='PercentSalaryHike',facet_col='Gender',color='JobRole',title='Percent Salary Hike by Monthly Income') 
        st.plotly_chart(fig11)
        st.subheader('Data Analysis:')
        st.write('Employees with monthly income between 5000 to 10000 have the highest percent salary hike in the organisation.**Human resource** employees have the greatest percent salary hike in the organisation.')
    if st.sidebar.checkbox('Performance rating'):
        fig12 = px.bar(df,x='JobRole',y='PerformanceRating',facet_col='Attrition',color='JobRole',title='Performance Rating by Job Role')
        st.plotly_chart(fig12)
        st.subheader('Data Analysis:')
        st.write('Employees with no attrition have the highest performance rating in the organisation.And **Sales Executive** has the highest performance rating in the organisation.')
    if st.sidebar.checkbox('Work life balance'):
        fig13 = px.funnel(df,x='JobRole',y='WorkLifeBalance',color='JobRole',title='Work Life Balance by Job Role')
        st.plotly_chart(fig13)
        st.subheader('Data Analysis:')
        st.write('Employees with job role **Sales Executive** have the highest work life balance in the organisation.')
    if st.sidebar.checkbox('Show tree map'):
        fig14 = px.treemap(df,path=['JobRole','OverTime','JobSatisfaction'],values='MonthlyIncome',title='Job Satisfaction by Job Role and Overtime')
        st.plotly_chart(fig14)
        st.subheader('Data Analysis:')
        st.write('Employees with job role **Sales Executive** have the highest job satisfaction and highest pay with over time in the organisation.')
        fig15 = px.treemap(df,path=['EducationField','Department','JobRole'],values='MonthlyRate',title='Montly rate by educational field and department')
        st.plotly_chart(fig15)
        st.subheader('Data Analysis:')
        st.write('Employees with job role **Sales Executive** have the highest montly rate in the organisation after calculating their education field depatment and job role.')