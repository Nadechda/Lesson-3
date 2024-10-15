class Product:
    def __init__(self, name, weight, category):
        self.name = str(name)
        self.weight = float(weight)
        self.category = str(category)

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop():
    __file_name = 'products.txt'

    def get_products(self):
        f = open(self.__file_name, 'r')
        s = f.read()
        f.close()
        return s

    def add(self, *products):
        for i in products:
            if self.get_products().find(f'{i.name}') != -1:
                print(f'Продукт {i} уже есть в магазине')
            else:
                f = open(self.__file_name, 'a')
                f.write(f'{i}\n')
                f.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
