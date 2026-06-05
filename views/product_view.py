import tkinter as tk

class ProductView:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller

        self.name_var = tk.StringVar()
        self.price_var = tk.StringVar()

        self.build_ui()

    def build_ui(self):
        tk.Label(self.root, text="Product Name").pack()
        tk.Entry(self.root, textvariable=self.name_var).pack()

        tk.Label(self.root, text="Price").pack()
        tk.Entry(self.root, textvariable=self.price_var).pack()

        tk.Button(self.root, text="Add Product", command=self.add_product).pack(pady=5)
        tk.Button(self.root, text="Load Products", command=self.load_products).pack()

        self.listbox = tk.Listbox(self.root, width=40)
        self.listbox.pack(pady=10)

        tk.Button(self.root, text="Delete Selected", command=self.delete_product).pack()

    def add_product(self):
        name = self.name_var.get()
        price = self.price_var.get()

        if name and price:
            self.controller.add_product(name, float(price))
            self.load_products()

    def load_products(self):
        self.listbox.delete(0, tk.END)
        products = self.controller.get_all_products()

        for p in products:
            self.listbox.insert(tk.END, f"{p['id']} | {p['name']} - ${p['price']}")

    def delete_product(self):
        selected = self.listbox.get(tk.ACTIVE)

        if selected:
            product_id = int(selected.split("|")[0])
            self.controller.delete_product(product_id)
            self.load_products()