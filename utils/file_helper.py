import json
import os

FILE_PATH = "data/products.json"

def load_products():
    if not os.path.exists(FILE_PATH):
        return []

    with open(FILE_PATH, "r") as f:
        return json.load(f)

def save_products(products):
    with open(FILE_PATH, "w") as f:
        json.dump(products, f, indent=4)