from flask import Flask, request, jsonify
import irisModel
model = irisModel.loadIris()

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello world!"

# Using Jsonify as Input
@app.route("/iris_predict", methods=['POST', 'GET'])
def iris_predict():
    # Get values using Json dictionary style
    input_data = request.get_json(force=True)
    prediction = model.predict([input_data['X']])

    # data = {
    #           "X":[sepLen, sepWid, petLen, petWid]
    #         }

    output = prediction
    return jsonify(status=200,
                   result=output)


if __name__ == '__main__':
    app.run()


# Usage:
# curl -H "Content-Type: application/json" -X POST http://localhost:5000/iris_predict -d "{""X"":[1.2,1.2,1.2,1.2]}"
# Cara manggil :
# curl  -H "Content-Type: application/json" 127.0.0.1:5000/iris_predict -d @json_test.txt
