# Machine Learning App Deployment
Method to deploy ML App into production. <br>
This Repository contain example of how to deploy machine learning app in many ways, From Script, Desktop GUI, Flask Web API, Streamlit Web App to the fully functioning Website using Django Web Framework.

> Last updated: Dec 2020

___
## Python Script Deployment

Model Deployment using Console Script is the most easiest and common method to serve the functionality of the program.

Script usualy purposed to do automation or scheduling which doesn't need UI Interface.

Script usually taking arguments alogside the script when running, in this case, our **Iris Flower Prediction Script** may take argument as features to predict the Iris Flower class.

For Detail instruction go to [here](https://github.com/BenedictusAryo/ml_app_deployment/tree/master/1_Script)

<br>

## Python Desktop GUI Application using DearPyGUI

Model Deployment using Desktop GUI using python can become an options if we want to make a Desktop GUI Application so that user can interact with the application interface such as slider and button.

Dear PyGui is an **easy-to-use, flexible, powerful graphical user interface (GUI) framework for Python**. As an extended wrapping of Dear ImGui, Dear PyGui is highly performant. It is written primarily in C/C++ and uses your GPU for renderering. Features include traditional GUI elements to display text, images and various controls, such as buttons, radio buttons, and menus and various methods to create a functional and beautiful layout. Additionally, it offers incredibly dynamic charts, tables, drawings and tools for application development, such as built-in documentation, logging, and debugger.

As a GUI toolkit, it is equally suitable for creating simple user interfaces for wrapping a basic command line interface. It can also be used for science, engineering, games, data science and other applications that require fast and interactive interfaces.

For Detail instruction go to [here](https://github.com/BenedictusAryo/ml_app_deployment/tree/master/2_DearPyGUI)

<br>

## Flask API Deployment

In previous approach (Script and Desktop GUI), the computation of the model inference happened in the Client means the machine where we run the script or the GUI Application. In some cases we may need more powerfull hardware to do computation like predicting the object in image, etc which may be easier to be deployed using server.

To Solve those scenario, we can use API based Deployment. API is the acronym for **[Application Programming Interface](https://www.mulesoft.com/resources/api/what-is-an-api)**, which is a software intermediary that allows two applications to talk to each other. Each time you use an app like Facebook, send an instant message, or check the weather on your phone, you’re using an API.

We will use flask `pip install flask` to create web server to serve API so that external application can use the model by simply sending request to the server where we run our flask App.

For Detail instruction go to [here](https://github.com/BenedictusAryo/ml_app_deployment/tree/master/3_FlaskAPI)

<br>

## Streamlit Web Application

The use case is similar with the Flask Web API Server, we want to serve the Prediction application in the server as a web application so that it will be accessible through the network/internet.

The key differences is with **[Streamlit](https://www.streamlit.io/)** we can data scripts into sharable fully web apps in minutes. All components can be developed in python,so no front-end experience required.

For Detail instruction go to [here](https://github.com/BenedictusAryo/ml_app_deployment/tree/master/4_Streamlit)

<br>

## Django Web Framework for Machine Learning Deployment

**[Django](https://www.djangoproject.com/)** is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of Web development, so you can focus on writing your app without needing to reinvent the wheel. It’s free and open source.

One of the advantages of Django is their **[Documentation](https://docs.djangoproject.com/)**. <br>
With Django, we can built fully functional website with **Database Integration as easy as making a class in python** or we call it **[Django models](https://docs.djangoproject.com/en/3.1/topics/db/models/)**. The default database is [SQLite3](https://www.sqlite.org/index.html) but we can integrate the to [other databases](https://docs.djangoproject.com/en/3.1/ref/databases/).

For Detail instruction go to [here](https://github.com/BenedictusAryo/ml_app_deployment/tree/master/5_Django_WebApp)