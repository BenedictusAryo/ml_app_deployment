from flask import Flask, request, jsonify
import irisModel
model = irisModel.loadIris()

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello world!"

# Using Arguments as Input
@app.route("/iris_predict", methods=['POST', 'GET'])
def iris_predict():
    # Get values using browser arguments
    sepLen = request.args['sepal_length']
    sepWid = request.args['sepal_width']
    petLen = request.args['petal_length']
    petWid = request.args['petal_width']

    data = [[sepLen, sepWid, petLen, petWid]]
    output = model.predict(data)
    return output
    #jsonify(result=str(model.predict(X)), status=200)


if __name__ == '__main__':
    app.run()


# Usage:
# http://127.0.0.1:5000/iris_predict?sepal_length=6.0&sepal_width=2.5&petal_length=5.5&petal_width=0
