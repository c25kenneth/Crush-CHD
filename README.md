# Coronary-Heart-Disease-Web-App
An ADL (App Dev League) Hackathon Project! Crush CHD is a machine learning web app that is fully responsive and adapts to different screen resolutions. It uses a real machine learning/AI model to predict whether or not a person has Coronary Heart Disease. Users can easily input their data via the left-hand panel that opens up. After data is put in successfully, hit the "Predict Results" button and wait for results to show up! Data visualizations of real life patients can also be viewed if the patient scrolls down on the main panel. The data that is visualized can be scrolled in and out.  

Files: 
1. ```CHDdata.csv``` is the csv file for the data used in this project. 

2. ```webapp.py``` is the python file for the web app.

3. ```CHDMachineLearningModel.ipynb``` is the Jupyter Notebook that contains our machine learning model. 

4. ```HeartDiseaseDetectModel.pickle``` is the pickled file of our machine learning model. It is a binary file so it cannot be viewed by opening. It is simply the ```CHDMachineLearningModel.ipynb``` file but in another form. 

5. ```Heart-Picture.jpg``` is the image that is shown in our web app. 

Instructions (Running)

1. Clone github repository to your machine. 

2. Open a terminal window in the project directory.

3. Run ```streamlit run ResourcesAndCode/CrushCHD.py``` to run on localhost. 

4. If errors occur, you may need to install modules such as Streamlit via typing in the command line ```pip install streamlit```. Jupyter Notebooks may also be required to run     this project. 

5. After the web app runs successfully, navigate to ```localhost:8501``` and try it out!
