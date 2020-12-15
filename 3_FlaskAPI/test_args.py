# Script to test the Flask App of basicFlaskApp_args.py
import requests

# Location of Deployed server, basic = localhost
server = 'http://127.0.0.1'
port = '5000'
flask_route = '/iris_predict_args'

# Params sends to test the request
sepal_length = 5.9
sepal_width = 3.0
petal_length = 5.1
petal_width = 1.8

# Full API Contructor
api_constructor = f"{server}:{port}{flask_route}?sepal_length={sepal_length}&sepal_width={sepal_width}&petal_length={petal_length}&petal_width={petal_width}"

# Initialization
print("Test Api Iris Prediction", end='\n\n')
print(f"""
Iris Test Data: 
Sepal Length: {sepal_length}
Sepal Width: {sepal_width}
Petal Length: {petal_width}
Petal Width: {petal_width}

""")

# Use Request to test
test = requests.post(api_constructor)
result = test.text

print(test)
print("Prediction Result: ", result)
