import streamlit as st
import os
from PIL import Image
import pickle

################  Model File and Folder Location  ###################
MODEL_FILE = 'iris_model.pkl'
MODEL_PATH = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir, MODEL_FILE))


####################  Model Class  #############################
class IrisModel:
    def __init__(self, model_path):
        self.model = pickle.load(open(model_path, 'rb'))

    def predict(self, features):
        return self.model.predict(features)[0]

model = IrisModel(MODEL_PATH)  


####################  StreamLit App  #############################

app_title = 'Iris Flower Classifier'
app_desc = '''
This app, predicted Iris Flower based on **Sepal Width**, **Sepal Length**, **Petal Width**, and **Petal Length**.
'''
usage = '''
Slide below slider on each Iris Flower Features (_sepal length_, _sepal width_, _petal length_, _petal width_)

Then Press the button below the slider to predict the Iris Flower Class result.
'''
IMG_FILENAME = 'iris_image.png'
IMG_PATH = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir, 'static', IMG_FILENAME))
# script_folder = os.path.dirname(os.path.abspath(__file__))
# img_loc = os.path.join(script_folder, 'iris_image.png')
# image = Image.open(img_loc)
image = Image.open(IMG_PATH)

st.title(app_title)
st.markdown(app_desc)
st.image(image, caption='Iris Flower and it\'s features', use_column_width=True)
st.markdown(usage)

# Get values using browser arguments
sepLen = st.slider('Sepal Length', min_value=4.30, max_value=7.90)
sepWid = st.slider('Sepal Width', min_value=2.00, max_value=4.40)
petLen = st.slider('Petal Length', min_value=1.00, max_value=6.90)
petWid = st.slider('Petal Width', min_value=0.10, max_value=2.50)

# Concate the Input Data
# input_data =
# st.write(sepLen, sepWid, petLen, petWid)


if st.button('Press here to Predict'):
    output = model.predict([[sepLen, sepWid, petLen, petWid]])
else:
    output = 'Press the button above to predict the result'

st.subheader('Result:')
st.write(f'{output}'.capitalize())


# How to use
# streamlit run streamlit_app.py
