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
sepLen = st.number_input('sepal_length', min_value=0.01, step=0.01)
sepWid = st.number_input('sepal_width', min_value=0.01, step=0.01)
petLen = st.number_input('petal_length', min_value=0.01, step=0.01)
petWid = st.number_input('petal_width', min_value=0.01, step=0.01)

# Concate the Input Data
# input_data =
# st.write(sepLen, sepWid, petLen, petWid)


output = model.predict([[sepLen, sepWid, petLen, petWid]])
st.header('Result')


st.write(output)


# How to use
# streamlit run streamlit_app.py
