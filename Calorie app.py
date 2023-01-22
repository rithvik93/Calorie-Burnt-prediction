
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 19:08:13 2023
@author: RITHVIK
"""
import pickle
import streamlit as st
import numpy as np
import database as db
loaded_model = pickle.load(open('calorie_model.sav', 'rb'))
st.title("CALORIE BURNT PREDICTION")
def prediction(age,gender,height,weight,duration,heart_rate,temparature ):   
# Pre-processing user input   
    if gender=='male':
        gender=1
    else:
        gender=0  
    #temparature=int(float(temparature))
    input_data = (age,gender,height,weight,duration,heart_rate,temparature)

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)
    
    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    return loaded_model.predict(input_data_reshaped)                 
gender=st.radio("Select Gender: ", ('male', 'female'))
age=st.selectbox ("Age",range(1,101,1))
height=st.selectbox("Select Height(in cms)",range(1,300,1))
weight=st.selectbox('Enter Weight',range(1,300,1))
duration=st.selectbox('Select Duration in Mins',range(1,300,1))
heart_rate=st.selectbox('Enter Heart Rate',range(1,300,1))
temparature=st.number_input('Enter body temparature')
prediction(age, gender, height, weight, duration, heart_rate, temparature)
if st.button('Result'):
     pred = prediction(age,gender,height,weight,duration,heart_rate,temparature)
     db.insert_data(age, gender, height, weight, duration, heart_rate, temparature, pred[0])
     st.success(pred[0])
