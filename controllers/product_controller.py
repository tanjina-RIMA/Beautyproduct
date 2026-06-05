from utils.file_helper import load_products, save_products

class ProductController:
    def get_all_products(self):
        return load_products()

    def add_product(self, name, price):
        products = load_products()

        new_id = 1
        if products:
            new_id = products[-1]["id"] + 1

        products.append({
            "id": new_id,
            "name": name,
            "price": price
        })

        save_products(products)

    def delete_product(self, product_id):
        products = load_products()

        products = [p for p in products if p["id"] != product_id]

        save_products(products)