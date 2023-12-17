import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO
import random

def on_no_button(question_label, image_label, no_button, root, window_width):
    question_label.config(text="I will ask you again, did you like my project?! do not make me angry.")
    root.configure(bg="white")

    # Load and display the GIF image for "No"
    gif_url = "https://i.pinimg.com/originals/fc/83/aa/fc83aaf30f5253bf82818e960a8fcd19.gif"
    load_and_display_gif(image_label, gif_url, window_width)

    move_no_button_randomly(no_button, root, window_width)

def load_and_display_gif(image_label, gif_url, window_width):
    response = requests.get(gif_url)
    gif_image = Image.open(BytesIO(response.content))

    image_width = int(window_width * 0.4)
    image_height = int((image_width / gif_image.width) * gif_image.height)
    resized_gif = gif_image.resize((image_width, image_height))
    photo = ImageTk.PhotoImage(resized_gif)
    image_label.config(image=photo)
    image_label.image = photo
    image_label.update_idletasks()

def move_no_button_randomly(no_button, root, window_width):
    new_x = random.randint(10, window_width - 100)
    new_y = random.randint(10, root.winfo_screenheight() - 30)
    no_button.place(x=new_x, y=new_y)

# Example of how to use the code in a Tkinter application
root = tk.Tk()

question_label = tk.Label(root, text="Do you like Kodi?")
question_label.pack()

image_label = tk.Label(root)
image_label.pack()

no_button = tk.Button(root, text="💔No💔", command=lambda: on_no_button(question_label, image_label, no_button, root, root.winfo_width()))
no_button.pack(side=tk.RIGHT, padx=10)

root.mainloop()
