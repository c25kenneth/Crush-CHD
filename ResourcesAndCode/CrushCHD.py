#import libraries 
import streamlit as st
import pandas as pd
import pickle
from PIL import Image
import sklearn
# description of project
st.title("Crush CHD")
st.write("Coronary heart disease (CHD) is an extremely serious disease. The disease occurs when the arteries clog up from plaque and cannot deliver enough blood to the heart. It is now one of the most leading causes of death worldwide, even in developed countries. About 3.8 million men and 3.4 million women die every year from this disease. Luckily, Crush CHD can help. In a matter of seconds, without having to go to a doctor, an AI/Machine Learning model will help determine whether or not you have Coronary Heart Disease. Not only is this method non-invasive, it is also reliably accurate, having accuracy rates that are higher than standard methods. Standard methods hover around the low 70 percent mark, while Crush CHD has an accuracy rate of almost 80%.")
image = Image.open("C:/Users/assist/Desktop/Machine Learning Projects/AppDevLeaugeHackathonGithubProject/ResourcesAndCode/Heart-Picture.jpg")
st.image(image, width = 290)
model = pickle.load(open("ResourcesAndCode\HeartDiseaseDetectModel.pickle", 'rb'))

# predicts based of user data
def predictIt(dat): 
    return model.predict([dat])

# hides bottom tag
hide_streamlit_style = """
             <style>
             #MainMenu {visibility: hidden;}
             footer {visibility: hidden;}
             </style>
             """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

# Gets our csv data
df = pd.read_csv("ResourcesAndCode\CHDdata.csv")
# Fix Data
df = df.drop("famhist", axis = 1)
df = df.drop("typea", axis=1)

# Displays data of patients in the past
st.write("A few real life patients before you had these results. 0 represents healthy and 1 represents those who have the disease: ")
st.dataframe(data = df.head(10), width = 500, height = 500)

st.text("")
st.bar_chart(data=df.head(10))

st.text("")
st.text("")
st.text("")
st.text("")
st.text("")

st.write("Below is some data about other patients who correspond to possibly being diagnosed with Coronary Heart Disease. Data charts can be zoomed in and out. Charts can also be downloaded in SVG and PNG format.")

st.text("")

st.write("Overall: ")
chart = st.bar_chart(df)

# Display individual data

st.write("Adiposity rates among patients: ")
st.bar_chart(df['adiposity'])

st.write("Age among patients: ")
st.bar_chart(df['age'])

st.write("Alcohol usage among patients. (In liters): ")
st.bar_chart(df['alcohol'])

st.write("Low Density Lipoprotein (LDL) rates among patients: ")
st.bar_chart(df['ldl'])

st.write("Obesity/Body Mass Index (BMI) rates: ")
st.bar_chart(df['obesity'])

st.write("Stystolic Blood Pressure (SBP) among paitents: ")
st.bar_chart(df['sbp'])

st.write("Tobacco use (In Kilograms) among patients: ")
st.bar_chart(df['tobacco'])

st.sidebar.write("Directions: Enter in your data. Data fields include systolic blood pressure, yearly tobacco usage in kilograms, low density lipoprotein, adiposity, BMI, yearly alcohol usage, and age. All values are defaulted to zero. Either type the data in or use the + and - buttons.")
st.text("")
st.text("")
# Gets user input from number fields

def get_user_input_number_field(): 
    sbp = st.sidebar.number_input("Stystolic Blood Pressure", min_value=0, key="a")
    tobacco = st.sidebar.number_input("Yearly Tobacco Usage in Kilograms", min_value = 0, key="b")
    ldl = st.sidebar.number_input("Low Density Lipoprotein", min_value = 0, key="c")
    adiposity = st.sidebar.number_input("Adiposity", min_value=0, key="d") 
    bmi = st.sidebar.number_input("BMI (Body Mass Index)", min_value = 0, key="e")
    alcohol = st.sidebar.number_input("Alcohol Usage Yearly (Liters)", min_value = 0, key="f")
    age = st.sidebar.number_input("Age (Years)", value= 0, min_value = 0, key="f")
    return [sbp, tobacco, ldl, adiposity, bmi, alcohol, age]

users_input = get_user_input_number_field()

# Writes out the outcome
if (st.sidebar.button("Predict Results")): 
    prediction = predictIt(users_input)
    if (prediction[0] == 1): 
        st.sidebar.text("")
        st.sidebar.text("")
        st.sidebar.write("This person unfortunatly has Coronary Heart Disease. We recommend seeking out medical attention at a hospital soon. If symptoms are serious, we strongly advise calling emergency numbers right away.")
    elif (prediction[0] == 0):
        st.sidebar.text("")
        st.sidebar.text("")
        st.sidebar.text("") 
        st.sidebar.write("Congrats! This person is healthy!")

    