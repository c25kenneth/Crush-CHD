#import libraries 
import streamlit as st
import pandas as pd
import pickle
from PIL import Image

# description of project
st.title("Crush CHD")
st.write("Coronary heart disease (CHD) is an extremely serious disease. The disease occurs when the arteries clog up from plaque and cannot deliver enough blood to the heart. It is now one of the most leading causes of death worldwide, even in developed countries. About 3.8 million men and 3.4 million women die every year from this disease. Luckily, Crush CHD can help. In a matter of seconds, without having to go to a doctor, an AI/Machine Learning model will help determine whether or not you have Coronary Heart Disease. Not only is this method non-invasive, it is also reliably accurate, having accuracy rates that are higher than standard methods. Standard methods hover around the low 70 percent mark, while Crush CHD has an accuracy rate of almost 80%.")
#image = Image.open("C:/Users/assist/Desktop/MachineLearningProjects/AppDevLeaugeHackathonGithubProject/ResourcesAndCode/Heart-Picture.jpg")
st.image("data:image/jpeg;base64,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", width = 290)
model = pickle.load(open("ResourcesAndCode/HeartDiseaseDetectModel.pickle", 'rb'))

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

    