class Product:
    def __init__(self,id,name,description,price,size):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.size = size

    def Product_Function(self):
        product  = f''' 
        id:{self.id}
        name:{self.name}
        description:{self.description}
        price:{self.price}
        size:{self.size}
        '''
        return product




