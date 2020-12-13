#shebang
import os
import sys
import pickle
import argparse

################  Model File and Folder Location  ###################
MODEL_FILE = 'iris_model.pkl'
MODEL_PATH = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir, MODEL_FILE))


#####################  Argument Parser  #############################
parser = argparse.ArgumentParser(description="Iris Flower Prediction")
required_args = parser.add_argument_group('required named arguments')
required_args.add_argument("-sl", "--sepal_length", required=True,
                    help="Sepal Length of Iris Flower", type=float)
required_args.add_argument("-sw", "--sepal_width", required=True,
                    help="Sepal Width of Iris Flower", type=float)
required_args.add_argument("-pl", "--petal_length", required=True,
                    help="Petal Length of Iris Flower", type=float)
required_args.add_argument("-pw", "--petal_width", required=True,
                    help="Petal Width of Iris Flower", type=float)

try:
    args = parser.parse_args()
except:
    parser.print_help()
    sys.exit(0)

#####################  Model Class  #############################
class IrisModel:
    def __init__(self, model_path):
        self.model = pickle.load(open(model_path, 'rb'))

    def predict(self, features):
        return self.model.predict(features)[0]


if __name__ == '__main__':
    model = IrisModel(MODEL_PATH)
    features = [[args.sepal_length, args.sepal_width, args.petal_length, args.petal_width]]
    prediction = model.predict(features)
    print("\nIris Flower Prediction\n")
    print("Input Features: ", features[0])
    print("Result: ", prediction.title())