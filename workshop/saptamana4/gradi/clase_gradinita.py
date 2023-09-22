# Mini proiect "Gradinita"
import operator
import random
from abc import ABC, abstractmethod

class Gradinita(ABC):

    @abstractmethod
    def activitate_practica(self):
        pass

    @abstractmethod
    def ora_de_somn(self):
        raise NotImplementedError


class GradinitaPublica(Gradinita):

    concurenti = list()

    def __init__(self):
        self.concurenti = []

    def activitate_practica(self):
        print('Copiii invata sa deseneze!')

    def ora_de_somn(self):
        print('Copiii trebuie sa doarma la ora cinci!')

    def start_concurs(self):
        print("A inceput concursul...")


class GradinitaPrivata(Gradinita):

    @property
    def elevi(self):
        return self.__elevi

    @elevi.setter
    def elevi(self, valoare):
        self.__elevi = valoare

    def __init__(self):
        self.__elevi = {}

    def adauga_elev(self, **kwargs):
        self.__elevi.update(kwargs)

    def afisare_informatii_elevi(self):

        for key, value in self.__elevi.items():
            print("------------------------------------------")
            print(f"Elev: {key}")
            for key_int, value_int in value.items():
                print(f"{key_int} - {value_int}")
            print("------------------------------------------")

    def activitate_practica(self):
        print('Copiii invata sa modeleze cu plastilina!')

    def ora_de_somn(self):
        print('Este timpul pentru un somn dulce!')


class GradinitaPublica25(GradinitaPublica):

    def start_concurs(self):
        print("A inceput concursul in Gradinita nr. 25")

        rezultate = {}

        for concurent in self.concurenti:
            puncte = random.uniform(5.0, 15.0)
            rezultate[concurent] = round(puncte, 2)

        rezultate_sortate = dict(sorted(rezultate.items(), key=operator.itemgetter(1), reverse=True))

        print("Rezultatele concursului:")
        print("------------------------")
        for key, value in rezultate_sortate.items():
            print(f"{key} - {value}")

