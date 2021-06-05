#import libraries
import matplotlib.pyplot as plt 
import pandas as pd
import streamlit as st
import numpy as np
import matplotlib
from matplotlib import style
#matplotlib.use('Agg')
import seaborn as sns
#Remove Warnings
st.balloons()
st.set_option('deprecation.showPyplotGlobalUse', False)
st.title("COVID-19 Globally Recovered Dataset")
#import dataset
df = pd.read_csv('covid19_recovered.csv')
#First ten rows
cdata = df.head(10)
#Display the table
st.table(cdata)
###################################
#bar plot
st.subheader("Bar Plot")
cdata.plot(kind='bar')
st.pyplot()
###################################
#Heat Map
st.subheader("Heat Map")
sns.heatmap(cdata.corr())
st.pyplot()
###################################
#Joint Plot
st.subheader("Joint Plot")
sns.jointplot(x='Country', y='6/3/21', data=cdata)
st.pyplot()
###################################