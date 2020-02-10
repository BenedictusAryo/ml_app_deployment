import os
import tkinter
import cv2
from PIL import Image, ImageTk
imgpath = os.path.dirname(__file__)+"/background.jpg"


class App:
    def __init__(self, window, window_title, image_path=imgpath):
        self.window = window
        self.window.title(window_title)

        # Load image using OpenCV
        self.cv_img = cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_BGR2RGB)
        # Get Image Dimension
        self.height, self.width, _ = self.cv_img.shape

        # Create a canvas that can fit the above image
        self.canvas = tkinter.Canvas(
            window, width=self.width, height=self.height)
        self.canvas.pack()
        # Use PIL to convert to a PhotoImage
        self.photo = ImageTk.PhotoImage(image=Image.fromarray(self.cv_img))
        self.canvas.create_image(0, 0, image=self.photo, anchor=tkinter.NW)

        # Create Blur Button
        self.btn_blur = tkinter.Button(
            window, text="Blur", width=50, command=self.blur_image)
        self.btn_blur.pack(anchor=tkinter.CENTER, expand=True)

        self.window.mainloop()

    # Callback for the "Blur" Button
    def blur_image(self):
        self.cv_img = cv2.blur(self.cv_img, (3, 3))
        self.photo = ImageTk.PhotoImage(image=Image.fromarray(self.cv_img))
        self.canvas.create_image(0, 0, image=self.photo, anchor=tkinter.NW)


# Create a window and pass it to the Application object
App(tkinter.Tk(), "OpenCV ImageBlur")
