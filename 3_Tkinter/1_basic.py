import tkinter
import cv2
from PIL import Image, ImageTk
import os

# Callback for the "Blur" button


def blur_image():
    global photo
    global cv_img

    cv_img = cv2.blur(cv_img, (3, 3))
    photo = ImageTk.PhotoImage(image=Image.fromarray(cv_img[..., ::-1]))
    canvas.create_image(0, 0, image=photo, anchor=tkinter.NW)


# Create a window
window = tkinter.Tk()

# Load an image using OpenCV
cv_img = cv2.imread(
    os.path.dirname(__file__)+"/background.jpg")

# Get the image dimensions
height, width, channels = cv_img.shape

# Create a canvas that can fit the above image
canvas = tkinter.Canvas(window, width=width, height=height)
canvas.pack()

# Use PIL to convert numpy to PhotoImage
photo = ImageTk.PhotoImage(image=Image.fromarray(cv_img[..., ::-1]))

# Add a PhotoImage to the canvas
canvas.create_image(0, 0, image=photo, anchor=tkinter.NW)

# Button that lets the user blur the image
btn_blur = tkinter.Button(window, text="Blur", width=50,
                          height=1, command=blur_image)
btn_blur.pack(anchor=tkinter.CENTER, expand=True)

# Run the window loop
window.mainloop()
