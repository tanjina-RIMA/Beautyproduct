import tkinter as tk
from controllers.product_controller import ProductController
from views.product_view import ProductView

class MainWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Product App (JSON)")
        self.root.geometry("400x500")

        controller = ProductController()
        self.view = ProductView(self.root, controller)

    def run(self):
        self.root.mainloop()