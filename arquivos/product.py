class Product:
    def __init__(self, name, description, price, size):
        self.name = name
        self.description = description
        self.price = price
        self.size = size

    def get_product(self):
        product_info = f''' 
        name: {self.name}
        description: {self.description}
        price: {self.price}
        size: {self.size}
        '''
        return product_info
