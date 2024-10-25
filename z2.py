class Person:
    def __setattr__(self, key, value):
        if key == 'name':
            if not(value and value[0].isupper() and value.isalpha()):
                raise ValueError('Не корректно введено имя!!!')
        elif key == 'age':
            if not(isinstance(value, int) and 0 <= value <= 120):
                raise ValueError('Не корректно введен возраст')
        elif key == 'email':
            if not(isinstance(value, str) and '@' in value):
                raise ValueError('Не корректно введен емайл')
        super().__setattr__(key, value)

    def __str__(self):
        return f"Person(name={self.name}, age={self.age}, email = {self.email})"


p = Person()
p.name = 'Иван'
p.age = 44
p.email = 'sdm@yandex.ru'
print(p)