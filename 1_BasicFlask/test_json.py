import requests


url = 'http://localhost:5000/iris_predict'
json_test = {'X': [1.2, 1.2, 1.2, 1.2]}

print("Testing data: ", json_test)
req = requests.post(url=url, json=json_test)
print('========================================================', '\n',)
print(req)
print(req.json())
