import os
import pickle

model_name = 'iris_decTree.pkl'
script_folder = os.path.dirname(os.path.abspath(__file__))
model_used = os.path.join(script_folder, model_name)


class loadIris:
    def __init__(self):
        self.model = None
        self.load_model()

    def load_model(self):
        self.model = pickle.load(open(model_used, 'rb'))

    def predict(self, X):
        return self.model.predict(X)[0]


if __name__ == '__main__':
    model = loadIris()
    test_case = [[5.1, 3.5, 1.4, 0.2]]
    prediction = model.predict(test_case)
    print("Test case: ", test_case[0])
    print("Result: ", prediction)
