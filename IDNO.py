import streamlit as st
import pandas as pd


df = pd.read_csv('IDNO.csv')


st.table(df)
