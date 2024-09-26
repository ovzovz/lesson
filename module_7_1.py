class Product():
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return self.name + ', ' + str(self.weight) + ', ' + self.category

class Shop():
    __file_name = 'products.txt'

    def get_products(self):
        # если файла нет, пусть создастся, поэтому а+
        file = open(self.__file_name, 'a+')
        file.close()
        file = open(self.__file_name, 'r')
        str=file.read()
        file.close()
        return str

    def add(self, *products):
    #    product = type(Product)
        for product in products:
            if str(product) in self.get_products():
                print ( f'Продукт {product} уже есть в магазине')
            else:
                file = open(self.__file_name, 'a+')
                file.write(str(product) + '\n')
                file.close()

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
