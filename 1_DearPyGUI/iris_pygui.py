from dearpygui import core, simple
import irisModel
model = irisModel.loadIris()



def save_callback(sender, data):
    print("Save Clicked")

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
    core.set_value("rs", result)

# core.show_logger()

# core.set_main_window_size(400,400)
with simple.window("Example Window",
    width=400, height=400,
    x_pos=0,y_pos=0,
    no_close=True, menubar=True):
    core.add_text("Iris Flower Classification")
    core.add_slider_float("Sepal Length", default_value=4.30, min_value=4.30, max_value=7.90, callback=GetData)
    core.add_slider_float("Sepal Width", default_value=2.00, min_value=2.00, max_value=4.40, callback=GetData)
    core.add_slider_float("Petal Length", default_value=1.00, min_value=1.00, max_value=6.90, callback=GetData)
    core.add_slider_float("Petal Width", default_value=0.10, min_value=0.10, max_value=2.50, callback=GetData)
    # core.add_text("Parameters:")
    # core.add_text('Sepal Length: ')
    # core.add_same_line()
    # core.add_label_text("##sp", source="sepLength")
    # core.add_text('Sepal Width: ')
    # core.add_same_line()
    # core.add_label_text("##sw", source="sepWidth")
    core.add_button("Predict", callback=predict_button)
    core.add_text('\n\n')
    core.add_text('Result: ')
    core.add_same_line()
    core.add_label_text("\n##res", source="rs")

# print(sepLen)
core.start_dearpygui(primary_window="Example Window")