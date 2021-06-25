from numpy.core.fromnumeric import size
import streamlit as st
import pandas as pd
import pickle
#print("streamlit loaded successfully")
st.title("Cardio Disease Detection")
model = pickle.load(open("ResourcesAndCode\HeartDiseaseDetectModel.pickle", 'rb'))
def predict_disease(sbp, tobacco, ldl, adiposity, bmi, alcohol, age):
    prediction = model.predict([ [sbp, tobacco, ldl, adiposity, bmi, alcohol, age] ])
    if (prediction[0] == 0): 
        st.write("You are healthy!")
    else: 
        st.write("diseased!")
if (st.button("Predict!")): 
    predict_disease(sbp=90, tobacco=30, ldl=80, adiposity=80, bmi=500, alcohol=6000, age=100)

hide_streamlit_style = """
             <style>
             #MainMenu {visibility: hidden;}
             footer {visibility: hidden;}
             </style>
             """

