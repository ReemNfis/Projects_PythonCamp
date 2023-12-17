import tkinter as tk
from PIL import Image, ImageTk
from First_File import on_no_button
from Second_File import on_yes_button
import requests
from io import BytesIO

def main():
    root = tk.Tk()
    root.title("Interactive App")

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    window_width = int(screen_width * 0.6)
    window_height = int(screen_height * 0.6)
    root.geometry(f"{window_width}x{window_height}")

    question_label = tk.Label(root, text="Did you like my simple project?")
    question_label.pack()

    # Load and display the initial GIF image
    gif_url = "https://i.pinimg.com/originals/6d/f9/89/6df98931d9c90c86885ca8d280ef02c8.gif"
    response = requests.get(gif_url)
    gif_image = Image.open(BytesIO(response.content))
    initial_image = ImageTk.PhotoImage(gif_image)

    image_label = tk.Label(root, image=initial_image)
    image_label.pack()

    # Initialize buttons
    yes_button = tk.Button(root, text="❤️Yes ️❤️", command=lambda: on_yes_button(question_label, image_label, root))
    yes_button.pack(side=tk.LEFT, padx=10)

    no_button = tk.Button(root, text="💔No💔", command=lambda: on_no_button(question_label, image_label, no_button, root, window_width))
    no_button.pack(side=tk.RIGHT, padx=10)

    # Use after method to delay the closing of the window

    root.mainloop()

if __name__ == "__main__":
    main()
