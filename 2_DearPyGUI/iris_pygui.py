from dearpygui import core, simple
import os
import pickle

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


####################  DearPyGUI  #############################
def GetData(sender, data):
    sepLength = core.get_value("Sepal Length")
    sepWidth = core.get_value("Sepal Width")
    petLength = core.get_value("Petal Length")
    petWidth = core.get_value("Petal Width")
    core.set_value("sepLength", sepLength)
    core.set_value("sepWidth", sepWidth)
    core.set_value("petLength", petLength)
    core.set_value("petWidth", petWidth)

def predict_button(sender, data):
    sepLength = core.get_value("Sepal Length")
    sepWidth = core.get_value("Sepal Width")
    petLength = core.get_value("Petal Length")
    petWidth = core.get_value("Petal Width")
    features = [[float(sepLength), float(sepWidth), float(petLength), float(petWidth)]]
    result = model.predict(features)
    core.set_value("rs", result.title())


with simple.window("Iris Flower Prediction",
    width=300, height=300,
    x_pos=0,y_pos=0,
    no_close=True, menubar=True):
    # Component to input value
    core.add_text("Iris Flower Classification")
    core.add_slider_float("Sepal Length", default_value=4.30, min_value=4.30, max_value=7.90, callback=GetData)
    core.add_slider_float("Sepal Width", default_value=2.00, min_value=2.00, max_value=4.40, callback=GetData)
    core.add_slider_float("Petal Length", default_value=1.00, min_value=1.00, max_value=6.90, callback=GetData)
    core.add_slider_float("Petal Width", default_value=0.10, min_value=0.10, max_value=2.50, callback=GetData)
    # Predict callback
    core.add_button("Predict", callback=predict_button)
    core.add_text('\n\n')
    core.add_text('Result: ')
    core.add_same_line()
    core.add_label_text("\n##res", source="rs")

# Start DearPyGUI
core.start_dearpygui()#primary_window="Iris Flower Prediction")