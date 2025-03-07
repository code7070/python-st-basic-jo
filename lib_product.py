import pandas as pd

class Product:
    def __init__(self, name:str, price, id:str):
        self.name = name
        self.price = price
        self.id = id
        self.is_active = True

    def __str__(self):
        return f"{self.name}, Harga: {self.price}, ID: {self.id}"
    
    def __repr__(self):
        return f"{self.name}, Harga: {self.price}, ID: {self.id}"
    
    def name(self):
        return self.name
    
    def price(self):
        return self.price
    
    def id(self):
        return self.id
    
    def activate(self):
        self.is_active = True
    
    def deactivate(self):
        self.is_active = False
    

class ProductList:
    def __init__(self, name:str):
        self.name = name
        self.products = []
    
    def add_product(self, product:Product):
        self.products.append(product)
    
    def get_active_products(self):
        active_products = []
        for product in self.products:
            if product.is_active:
                active_products.append(product)
        return active_products
    
    def get_all_products(self):
        return self.products
    
    def load_products_from_csv(self, filepath):
        df = pd.read_csv(filepath)
        for index, row in df.iterrows():
            product = Product(name=row['product_name'], price=row['price'], id=row['ID'])
            self.add_product(product)