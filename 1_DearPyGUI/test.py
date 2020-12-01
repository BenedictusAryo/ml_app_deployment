# from dearpygui.core import *
# from dearpygui.simple import *

# def directory_picker(sender, data):
#     select_directory_dialog(callback=apply_selected_directory)

# def apply_selected_directory(sender, data):
#     log_debug(data)  # so we can see what is inside of data
#     directory = data[0]
#     folder = data[1]
#     set_value("directory", directory)
#     set_value("folder", folder)
#     set_value("folder_path", f"{directory}\\{folder}")

# show_logger()

# with window("Tutorial"):
#     add_button("Directory Selector", callback=directory_picker)
#     add_text("Directory Path: ")
#     add_same_line()
#     add_label_text("##dir", source="directory", color=[255, 0, 0])
#     add_text("Folder: ")
#     add_same_line()
#     add_label_text("##folder", source="folder", color=[255, 0, 0])
#     add_text("Folder Path: ")
#     add_same_line()
#     add_label_text("##folderpath", source="folder_path", color=[255, 0, 0])

# start_dearpygui()

# from dearpygui.core import *
# from dearpygui.simple import *

# def button_callback(sender, data):
#     log_debug(f"sender is: {sender}")
#     log_debug(f"data is: {data}")

# show_logger()  # we're going to use the logger here to show the result

# with window("Tutorial"):
#     add_input_text("Input Text", default_value="Hello World!")
#     add_button("Apply", callback=button_callback, callback_data=get_value("Input Text"))
#     add_button("Apply##2", tip="callback was set after item was created")
#     set_item_callback("Apply##2", callback=button_callback, callback_data=get_value("Input Text"))

# start_dearpygui() 

from dearpygui.core import *
from dearpygui.simple import *

def add_buttons(sender, data):
    add_button("New Button")
    add_button("New Button 2", parent="Secondary Window")

def delete_buttons(sender, data):
    delete_item("New Button")
    delete_item("New Button 2")

show_debug()

with window("Tutorial"):
    add_button("Add Buttons", callback=add_buttons)
    add_button("Delete Buttons", callback=delete_buttons)

with window("Secondary Window"):
    pass

start_dearpygui() 