class Book:
    _id_counter = 1

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        instance.id = cls._id_counter
        cls._id_counter += 1
        return instance


    def __init__(self, title, author):
        self.title = title
        self.author = author


    def __str__(self):
        return f"Book(ID={self.id}, title={self.title}, author = {self.author})"


b1 = Book('ОГОГОГО', 'Fedor')
print(b1)
b2 = Book('ASAS', 'Dima')
print(b2)
