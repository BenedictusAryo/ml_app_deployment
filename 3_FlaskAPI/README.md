# Flask API Deployment

In previous approach (Script and Desktop GUI), the computation of the model inference happened in the Client means the machine where we run the script or the GUI Application. In some cases we may need more powerfull hardware to do computation like predicting the object in image, etc which may be easier to be deployed using server.

To Solve those scenario, we can use API based Deployment. API is the acronym for **[Application Programming Interface](https://www.mulesoft.com/resources/api/what-is-an-api)**, which is a software intermediary that allows two applications to talk to each other. Each time you use an app like Facebook, send an instant message, or check the weather on your phone, you’re using an API.

We will use flask `pip install flask` to create web server to serve API so that external application can use the model by simply sending request to the server where we run our flask App.

### Usage:
Run :
```python
python iris_flask_api.py
```

### Home Web Page
Go to http://127.0.0.1:500 and see the instructions


### Argument based Request
To make prediction we can use argument based request using web browser

```python
http://127.0.0.1:5000/iris_predict_args?sepal_length=6.0&sepal_width=2.5&petal_length=5.5&petal_width=0
```
Or using PowerShell:
```powershell
Invoke-RestMethod 'http://127.0.0.1:5000/iris_predict_args?sepal_length=6.0&sepal_width=2.5&petal_length=5.5&petal_width=0'
```

### JSON based Request
In some cases, we need complex queries to send data to web server, usually we can send the request using JSON format

Using command prompt:

```cmd
curl -H "Content-Type: application/json" -X POST http://localhost:5000/iris_predict_json -d "{""features"":[1.2,1.2,1.2,1.2]}"
```
json text separately:
```cmd
curl  -H "Content-Type: application/json" 127.0.0.1:5000/iris_predict_json -d @json_test.txt
```

---
### Python File for testing Request
* `test_args.py` for testing send request using argument format
* `test_json.py` for testing send request using json format