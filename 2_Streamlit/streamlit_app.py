import streamlit as st
import irisModel
model = irisModel.loadIris()


app_title = 'Iris Flower Classifier'
app_desc = '''
This app, predicted Iris Flower based on Sepal Width, Sepal Length, Petal Width, and Petal Length
'''
st.title(app_title)
st.write(app_desc)

# Get values using browser arguments
sepLen = st.slider('sepal_length', min_value=4.30, max_value=7.90)
sepWid = st.slider('sepal_width', min_value=2.00, max_value=4.40)
petLen = st.slider('petal_length', min_value=1.00, max_value=6.90)
petWid = st.slider('petal_width', min_value=0.10, max_value=2.50)

# Concate the Input Data
# input_data =
# st.write(sepLen, sepWid, petLen, petWid)


if st.button('Predict the Result'):
    output = model.predict([[sepLen, sepWid, petLen, petWid]])
else:
    output = 'Press the button to predict the result'

st.header('Result')
st.write(output)


# How to use
# streamlit run streamlit_app.py
