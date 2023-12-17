import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO

def on_yes_button(question_label, image_label, root):
    question_label.config(text="Oh, how nice you are. I really thank you because you liked my project.❤️")

    gif_url = "https://i.pinimg.com/originals/11/e8/bc/11e8bc738505435ab02de410e6f848d0.gif"
    response = requests.get(gif_url)
    gif_image = Image.open(BytesIO(response.content))
    photo = ImageTk.PhotoImage(gif_image)
    image_label.config(image=photo)
    image_label.image = photo
    image_label.update_idletasks()

# مثال على كيفية استخدام الكود في تطبيق Tkinter
root = tk.Tk()

question_label = tk.Label(root, text="Do you like Kodi?")
question_label.pack()

image_label = tk.Label(root)
image_label.pack()

yes_button = tk.Button(root, text="Yes", command=lambda: on_yes_button(question_label, image_label, root))
yes_button.pack()

root.mainloop()


