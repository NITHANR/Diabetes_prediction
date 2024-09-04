# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 11:04:07 2023

@author: R NITHAN
"""

import numpy as np
import pickle
import streamlit as st

loaded_model=pickle.load(open("C:/Users/R NITHAN/Downloads/Diabetes_Model_creation/trained_model.sav",'rb'))

def diabetes_prediction(input_data):
  
    input_data_as_numpy=np.asarray(input_data)
    input_data_reshaped=input_data_as_numpy.reshape(1,-1)
    prediction=loaded_model.predict(input_data_reshaped)
    print(prediction)

    if(prediction[0]==0):
        return "You are not Diabetic"
    else:
        return "You are Diabetic"
    
    
def main():
    
    #giving a title
    st.title('DIABETES PREDICTION WEB APP')
    
    #getting input data from users
    
    pregencies=st.text_input('Number of Pregenies')
    gulcose=st.text_input('Gulcose level')
    bloodPressure=st.text_input('Blood Pressure Value')
    insulin=st.text_input('Insulin level')
    skinThickness=st.text_input('Skin Thickness Value')
    BMI=st.text_input('BMI Value')
    DiagetesPedegreFunction=st.text_input('Diabetes Pedegre Function')
    Age=st.text_input('Your Age ')

    #Code for Prediction
    
    diagnosis=""
    
    #Button for prediction
    
    if st.button('Test Results'):
        diagnosis=diabetes_prediction([pregencies,gulcose,bloodPressure,skinThickness,insulin,BMI,DiagetesPedegreFunction,Age])
    
    
    st.success(diagnosis)
    

if __name__=="__main__":
    main()
    
    
    
    