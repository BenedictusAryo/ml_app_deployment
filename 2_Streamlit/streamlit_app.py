import streamlit as st
import irisModel
model = irisModel.loadIris()


app_title = 'Iris Flower Classifier'
app_desc = '''
This app, predicted Iris Flower based on Sepal Width, Sepal Length, Petal Width, and Petal Length
'''
st.title(app_title)
st.write(app_desc)
