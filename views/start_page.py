import tkinter as tk
from PIL import Image, ImageTk
from views.main_window import MainWindow

class StartPage:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Welcome")

        # Get screen size
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()

        # Make window full screen (optional but recommended)
        self.root.geometry(f"{self.screen_width}x{self.screen_height}")

        self.set_background()
        self.build_ui()

    def set_background(self):
        image = Image.open("images/bg.jpg")

        # Resize to screen size
        image = image.resize((self.screen_width, self.screen_height), Image.LANCZOS)

        self.bg = ImageTk.PhotoImage(image)

        self.bg_label = tk.Label(self.root, image=self.bg)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    def build_ui(self):
       tk.Button(
    self.root,
    text="ENTER",
    font=("Arial", 16, "bold"),  # bigger text
    bg="#A0522D",
    fg="white",
    width=12,   # button width
    height=2,   # button height
    command=self.open_app
).place(relx=0.5, rely=0.5, anchor="center")

    def open_app(self):
        self.root.destroy()
        app = MainWindow()
        app.run()

    def run(self):
        self.root.mainloop()