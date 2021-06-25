from numpy.core.fromnumeric import size
import streamlit as st
import pandas as pd
import pickle

st.title("Cardio Disease Detection")
model = pickle.load(open("ResourcesAndCode\HeartDiseaseDetectModel.pickle", 'rb'))


def predictIt(dat): 
    return model.predict([dat])
hide_streamlit_style = """
             <style>
             #MainMenu {visibility: hidden;}
             footer {visibility: hidden;}
             </style>
             """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
df = pd.read_csv("ResourcesAndCode\CHDdata.csv")

st.dataframe(data = df.head(), width = 500, height = 500)

def get_user_input(): 
    sbp = st.slider("Stystolic Blood Pressure", min_value=0, max_value=300)
    tobacco = st.slider("Yearly Tobacco Usage in Kilograms", min_value = 0, max_value = 75)
    ldl = st.slider("Low Density Lipoprotein", min_value = 0, max_value=35)
    adiposity = st.slider("Adiposity", min_value=0, max_value=100) 
    bmi = st.slider("BMI (Body Mass Index)", min_value = 0, max_value = 200)
    alcohol = st.slider("Alcohol Usage Yearly (Liters)", min_value = 0, max_value = 250)
    age = st.number_input("Age (Years)", value= 0)
    return [sbp, tobacco, ldl, adiposity, bmi, alcohol, age]

users_input = get_user_input()

if (st.button("Predict whether or not this person is diseased")): 
    prediction = predictIt(users_input)
    if (prediction[0] == 1): 
        print("diseased")
        st.write("This person unfortunatly has Coronary Heart Disease")
    elif (prediction[0] == 0):
        print("healthy")
        st.write("Congrats! This person is healthy!")