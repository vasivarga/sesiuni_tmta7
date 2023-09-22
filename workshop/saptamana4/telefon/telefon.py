from abc import ABC, abstractmethod


class Telefon(ABC):
    culoare = ''
    brand = ''
    dimensiune_ecran = ''

    # def __init__(self):
    #     print('S-a initializat o variabila tip telefon')

    @abstractmethod
    def suna(self):
        pass

    @abstractmethod
    def porneste(self):
        pass

    @abstractmethod
    def opreste(self):
        pass


class Iphone(Telefon):
    airplay = False

    def suna(self):
        print(f'{self.brand} suna cu ring tone de iphone')

    def porneste(self):
        print('Iphone-ul porneste')

    def opreste(self):
        print('Iphone-ul se opreste')


class AndroidPhone(Telefon):

    def __init__(self, brand, culoare, dimensiune):
        self.brand = brand
        self.culoare = culoare
        self.dimensiune_ecran = dimensiune

        # super().__init__()
        print('S-a initializat o variabila tip AndroidPhone')

    def suna(self):
        print(f'{self.brand} suna cu ring tone de android')

    def porneste(self):
        print('Android-ul porneste')

    def opreste(self):
        print('Android-ul se opreste')


samsung = AndroidPhone('Samsung Note 20', 'negru', '16')
numar = 5
print(type(numar))
print(type(samsung))
samsung.suna()

iphone_13 = Iphone()
print(type(iphone_13))
iphone_13.suna()
iphone_13.brand = 'Iphone 13'
iphone_13.suna()
iphone_13.airplay = True
print(iphone_13.airplay)

samsung.culoare = 'verde'
samsung.brand = 'Samsung Note 20'
samsung.dimensiune_ecran = 13
samsung.suna()

nokia = AndroidPhone('nokia g11', 'negru', '10')
nokia.culoare = 'negru'
nokia.brand = 'nokia G 11'
nokia.suna()
