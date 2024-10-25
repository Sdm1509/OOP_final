class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


    def __setattr__(self, key, value):
        if key == 'price':
            if not(isinstance(value, (int, float)) and value > 0):
                raise ValueError('Цена должна быть положительным числом')
        elif key == 'quantity':
            if not(isinstance(value, int) and value >= 0):
                raise ValueError('Кол-во должно быть неотрицательным числом')
        super().__setattr__(key, value)


    def __str__(self):
        return f'Product(name={self.name}, price={self.price}, quantity={self.quantity})'


p1 = Product('яблоко', 120, 25)
print(p1)
