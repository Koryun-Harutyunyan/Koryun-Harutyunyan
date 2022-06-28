class Products:
    def __init__(self, name, price, quantity, dict_Price, dict_quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.dict_quantity = quantity
        self.dict_Price = dict_Price
        self.dict_Price = dict()
        self.dict_quantity = dict()
        self.dict_Price[self.name] = self.price
        self.dict_quantity[self.name] = self.dict_quantity


class Shop(Products):
    def __init__(self, address, shopName):
        self.address = address
        self.shopName = shopName

    def sell(self):
        self.prodName = input()
        self.prodQuantity = input()
        if self.prodName in self.dict_Price and self.dict_quantity[self.name] > self.prodQuantity:
            print(self.dict_quantity[self.name] * self.dict_Price[self.name])
        else:
            print('Sorry but, we can not serve you.')


apples = Products('apple', 10, 500, {}, {})
Smile = Shop('Knunyanc50', 'Smile')
Shop.sell()