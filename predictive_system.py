# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pickle

loaded_model=pickle.load(open("C:/Users/R NITHAN/Downloads/Diabetes_Model_creation/trained_model.sav",'rb'))

input_data=(3,126,88,41,235,39.3,0.704,27)
input_data_as_numpy=np.asarray(input_data)
input_data_reshaped=input_data_as_numpy.reshape(1,-1)
prediction=loaded_model.predict(input_data_reshaped)
print(prediction)

if(prediction[0]==0):
    print("You are not Diabetic")
else:
    print("You are Diabetic")