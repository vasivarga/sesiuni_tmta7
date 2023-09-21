class Car:
    def __init__(self, brand):
        self.__brand = brand
    @property
    def brand(self):
        pass
    @brand.getter
    def brand(self):
        return self.__brand
    @brand.setter
    def brand(self, new_brand):
        self.__brand = new_brand
    @brand.deleter
    def brand(self):
        del self.__brand

mycar = Car('Volvo')
print(mycar.brand) # Am accesat atributul privat "brand" cu metoda "getter".

mycar.brand = 'VW' # Am schimbat atributul privat cu metoda "setter".
print(mycar.brand)

del mycar.brand
#print(mycar.brand)

mycar.brand = 'VW'
print(mycar.brand)


