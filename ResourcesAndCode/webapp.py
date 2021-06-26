from numpy.core.fromnumeric import size
import streamlit as st
import pandas as pd
import pickle
from PIL import Image
st.title("Cardio Disease Detection")
image = Image.open("C:/Users/assist/Desktop/Machine Learning Projects/AppDevLeaugeHackathonGithubProject/ResourcesAndCode/robina-weermeijer-NIuGLCC7q54-unsplash.jpg")
st.image(image, width = 290)
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

df = df.drop("famhist", axis = 1)
df = df.drop("typea", axis=1)

st.write("Some people before you had these results: ")
st.dataframe(data = df.head(), width = 500, height = 500)

st.text("")
st.text("")
st.sidebar.write("Predict whether or not you have Coronary Heart Disease")
def get_user_input(): 
    sbp = st.sidebar.slider("Stystolic Blood Pressure", min_value=0, max_value=300)
    tobacco = st.sidebar.slider("Yearly Tobacco Usage in Kilograms", min_value = 0, max_value = 75)
    ldl = st.sidebar.slider("Low Density Lipoprotein", min_value = 0, max_value=35)
    adiposity = st.sidebar.slider("Adiposity", min_value=0, max_value=100) 
    bmi = st.sidebar.slider("BMI (Body Mass Index)", min_value = 0, max_value = 200)
    alcohol = st.sidebar.slider("Alcohol Usage Yearly (Liters)", min_value = 0, max_value = 250)
    age = st.sidebar.number_input("Age (Years)", value= 0)
    return [sbp, tobacco, ldl, adiposity, bmi, alcohol, age]

users_input = get_user_input()

if (st.sidebar.button("Predict whether or not this person is diseased")): 
    prediction = predictIt(users_input)
    if (prediction[0] == 1): 
        st.sidebar.text("")
        st.sidebar.text("")
        st.sidebar.text("")
        st.sidebar.write("This person unfortunatly has Coronary Heart Disease")
    elif (prediction[0] == 0):
        st.sidebar.text("")
        st.sidebar.text("")
        st.sidebar.text("") 
        st.sidebar.write("      Congrats! This person is healthy!")