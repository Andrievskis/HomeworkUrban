class Product:
    def __init__(self, name, weight, category):
        self.name = str(name)
        self.weight = float(weight)
        self.category = str(category)

    def __str__(self):
        a = str(f'{self.name}, {self.weight}, {self.category}.')
        return a


class Shop:

    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        b = file.read()
        file.close()
        return b

    def add(self, *products):
        for product in products:
            if str(product) not in self.get_products():
                file = open(self.__file_name, 'a')
                file.write(f'\n{str(product)}')
                file.close()
            else:
                print(f'Продукт {product.name} уже есть в магазине.')


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vagetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vagetables')
print(p2)
s1.add(p1, p2, p3)
print(s1.get_products())
