import streamlit as st
import pandas as pd
import pickle
#print("streamlit loaded successfully")

#st.title("Cardio Disease Detection")
model = pickle.load(open("HeartDiseaseDetectModel.pickle", 'rb'))
predict = model.predict([ [20, 4, 6, 5, 3, 3, 7] ])
print("Model loaded successfully")
print(predict)
if (predict[0] == 0): 
    print("Healthy!")
else: 
    print("Dseased")
#def predict_disease(sbp, tobacco, ldl, adiposity, bmi, alcohol, age):
 #   print(sbp)

# hide_streamlit_style = """
#             <style>
#             #MainMenu {visibility: hidden;}
#             footer {visibility: hidden;}
#             </style>
#             """
# st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# sl = st.slider(label= "Glucose", min_value = 0, max_value= 35)
# st.write(sl)
# st.selectbox("Chose age", ("1", "2", "3", "4", "5", "6", "7"))