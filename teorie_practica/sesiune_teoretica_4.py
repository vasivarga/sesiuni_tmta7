# Abstractizare
from abc import ABC, abstractmethod


class CarModel(ABC):

    @abstractmethod
    def roti(self):
        pass
    @abstractmethod
    def volan(self):
        raise NotImplemented
    def sistem_audio(self):
        print('Se aude muzica.')

class OldCar(CarModel):
    def __scaune(self): # metoda private
        print('Masina are 4 scaune.')
    def _decapotabila(self): # metoda protected
        print('Masina este decapotabila.')

    def volan(self):
        print('Masina are volan pe stanga.')

    def roti(self):
        print('Masina are 4 roti.')

    def motor(self):
        print('Masina are motor Diesel.')

class ModernCar(OldCar):
    def airbag(self):
        print('Masina are airbag.')
    def trusa_medicala(self):
        print('Masina are trusa medicala.')
    def roti(self): # polimorfism
        print('Masina are 5 roti.')
    def extraoptiuni(self):
        self._decapotabila()
        #self.__scaune() # Metodele private nu pot fi apelate in clasa copil.


dacia = OldCar()
dacia.roti()
dacia.volan()
dacia.motor()
dacia.sistem_audio()
# dacia.__scaune() # Nu se poate accesa o metoda de tip private in afara clasei, doar in interior.
dacia._decapotabila() # Metoda de tip protected se poate accesa in afara clasei, intr-un obiect instantiat.

print('----------')
renault = ModernCar()
renault.motor()
renault.volan()
renault.roti()
renault.sistem_audio()
renault.airbag()
renault.extraoptiuni()
renault.trusa_medicala()


