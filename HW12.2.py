# ДЗ 12.2. Корзина для покупок


class Item:

    def __init__(self, name, price, description, dimensions):
        self.price = price
        self.description = description
        self.dimensions = dimensions
        self.name = name


    def __str__(self):
        return f"{self.name} prise: {self.price}"
    

class User:

    def __init__(self, name, surname, numberphone):
        self.name = name
        self.surname = surname
        self.numberphone = numberphone


    def __str__(self):
        return f"{self.name} {self.surname}"
    

class Purchase:
    def __init__(self, user):
        self.products = {}
        self.user = user
        self.total = 0


    def add_item(self, item, cnt):
        self.products[item] = cnt


    def __str__(self):
        info = [f"User: {self.user}"]

        for key, value in self.products.items():
            info.append(f"{key}, {value} pcs.")

        return "\n".join(info)

    
    def get_total(self):
        total = 0
        
        for key, value in self.products.items():
            total += key.price * value

        self.total = total
        return self.total
        
        




lemon = Item('lemon', 5, "yellow", "small", )
apple = Item('apple', 2, "red", "middle", )
# banana = Item('banana', 7, "yellow", "middle", )
# print(apple)  # lemon, price: 5
# print(apple.description)


buyer = User("Ivan", "Ivanov", "02628162")
buyer_2 = User("Vlad", "Bondarenko", "323454")
# print(buyer_2)  # Ivan Ivanov


cart = Purchase(buyer)
cart.add_item(lemon, 4)
cart.add_item(apple, 20)
# print(cart)
"""
User: Ivan Ivanov
Items:
lemon: 4 pcs.
apple: 20 pcs.
"""

assert isinstance(cart.user, User) is True, 'Екземпляр класу User'
assert cart.get_total() == 60, "Всього 60"
assert cart.get_total() == 60, 'Повинно залишатися 60!'
cart.add_item(apple, 10)
print(cart)
"""
User: Ivan Ivanov
Items:
lemon: 4 pcs.
apple: 10 pcs.
"""

assert cart.get_total() == 40

print("0K")