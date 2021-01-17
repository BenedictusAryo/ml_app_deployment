import os
import pickle
from flask import Flask, request, jsonify


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



####################  Flask Application  #############################

app = Flask(__name__)


@app.route('/')
def index():
    return """
    <h1>Tutorial</h1>
    Usage: "/iris_predict_args" for argument and "/iris_predict_json" for json POST
    """

# Using Arguments as Input
@app.route("/iris_predict_args", methods=['POST', 'GET'])
def iris_predict_args():
    # Get values using browser arguments
    sepLen = request.args['sepal_length']
    sepWid = request.args['sepal_width']
    petLen = request.args['petal_length']
    petWid = request.args['petal_width']

    # Set argument values as feature predictor and output the result as dictionary/JSON
    data = [[sepLen, sepWid, petLen, petWid]]
    output = model.predict(data)
    return jsonify(result=output.title(), status=200)


# Using Json data as Input
@app.route("/iris_predict_json", methods=['POST'])
def iris_predict_json():
    # Get values using Json dictionary style
    input_data = request.get_json(force=True)
    features = input_data.get('features')

    # If Json Data is invalid return HTTP 400 Error with note, else return 200 OK with Prediction Result
    if (features == None) | (not isinstance(features, list)):
        status = 400
        return_val = 'Json key should be "features" with array as values'
    elif len(features) != 4:
        status = 400
        return_val = 'Json values should be array with size 4 of [Sepal_Length, Sepal_Width, Petal_Length, Petal_Width]'
    else:
        prediction = model.predict([features])
        return_val = prediction.title()
        status = 200

    return jsonify(status=status,
                    result=return_val)



if __name__ == '__main__':
    app.run(host= '0.0.0.0')


# Usage:
# Arguments:
# http://127.0.0.1:5000/iris_predict_args?sepal_length=6.0&sepal_width=2.5&petal_length=5.5&petal_width=0
# Powershell: 
# Invoke-RestMethod 'http://127.0.0.1:5000/iris_predict_args?sepal_length=6.0&sepal_width=2.5&petal_length=5.5&petal_width=0'

# JSON
# CMD: 
# curl  -H "Content-Type: application/json" 127.0.0.1:5000/iris_predict_json -d @json_test.txt
# curl -H "Content-Type: application/json" -X POST http://localhost:5000/iris_predict_json -d "{""features"":[1.2,1.2,1.2,1.2]}"