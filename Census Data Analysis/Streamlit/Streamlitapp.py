import streamlit as st
import pandas as pd

Query01 = pd.read_csv('Query01_result.csv')
Query02 = pd.read_csv('Query02_result.csv')
Query03 = pd.read_csv('Query03_result.csv')
Query04 = pd.read_csv('Query04_result.csv')
Query05 = pd.read_csv('Query05_result.csv')
Query06 = pd.read_csv('Query06_result.csv')
Query07 = pd.read_csv('Query07_result.csv')
Query08 = pd.read_csv('Query08_result.csv')
Query09 = pd.read_csv('Query09_result.csv')
Query10 = pd.read_csv('Query10_result.csv')
Query11 = pd.read_csv('Query11_result.csv')
Query12 = pd.read_csv('Query12_result.csv')
Query13 = pd.read_csv('Query13_result.csv')
Query14 = pd.read_csv('Query14_result.csv')
Query15 = pd.read_csv('Query15_result.csv')
Query16 = pd.read_csv('Query16_result.csv')
Query17 = pd.read_csv('Query17_result.csv')
Query18 = pd.read_csv('Query18_result.csv')
Query19 = pd.read_csv('Query19_result.csv')
Query20 = pd.read_csv('Query20_result.csv')

# Display the DataFrame
st.write("01) What is the total population of each district?")
st.dataframe(Query01)

st.write("02) How many literate males and females are there in each district?")
st.dataframe(Query02)

st.write("03) What is the percentage of workers (both male and female) in each district?")
st.dataframe(Query03)

st.write("04) How many households have access to LPG or CNG as a cooking fuel in each district?")
st.dataframe(Query04)

st.write("05) What is the religious composition (Hindus, Muslims, Christians, etc.) of each district?")
st.dataframe(Query05)

st.write("06) How many households have internet access in each district?")
st.dataframe(Query06)

st.write("07 What is the educational attainment distribution (below primary, primary, middle, secondary, etc.) in each district?")
st.dataframe(Query07)

st.write("08) How many households have access to various modes of transportation (bicycle, car, radio, television, etc.) in each district?")
st.dataframe(Query08)

st.write("09) What is the condition of occupied census houses(dilapidated, with separate kitchen, bathing facility, latrine facility) in each district?")
st.dataframe(Query09)

st.write("10) How is the household size distributed (1 person, 2 persons, 3-5 persons, etc.) in each district?")
st.dataframe(Query10)

st.write("11) What is the total number of households in each state?")
st.dataframe(Query11)

st.write("12) How many households have a latrine facility within the premises in each state?")
st.dataframe(Query12)

st.write("13) What is the average household size in each state?")
st.dataframe(Query13)

st.write("14) How many households are owned versus rented in each state?")
st.dataframe(Query14)

st.write("15) What is the distribution of different types of latrine facilities (pit latrine, flush latrine, etc.) in each state?")
st.dataframe(Query15)

st.write("16) How many households have access to drinking water sources near the premises in each state?")
st.dataframe(Query16)

st.write("17) What is the average household income distribution in each state based on the power parity categories?")
st.dataframe(Query17)

st.write("18) What is the percentage of married couples with different household sizes in each state?")
st.dataframe(Query18)

st.write("19) How many households fall below the poverty line in each state based on the power parity categories?")
st.dataframe(Query19)

st.write("20) What is the overall literacy rate (percentage of literate population) in each state?")
st.dataframe(Query20)
