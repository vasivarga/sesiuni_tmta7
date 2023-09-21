# Mini proiect "Gradinita"
from abc import ABC, abstractmethod


class Gradinita(ABC):
    @abstractmethod
    def activitate_practica(self):
        pass

    @abstractmethod
    def ora_de_somn(self):
        raise NotImplementedError


class GradinitaPublica(Gradinita):
    def activitate_practica(self):
        print('Copiii invata sa deseneze!')

    def ora_de_somn(self):
        print('Copiii trebuie sa doarma la ora cinci!')


class GradinitaPrivata(Gradinita):
    def activitate_practica(self):
        print('Copiii invata sa modeleze cu plastilina!')

    def ora_de_somn(self):
        print('Este timpul pentru un somn dulce!')


class GradinitaPublica25(GradinitaPublica):
    atribut_public = 'atribut public'
    _atribut_protected = 'atribut protejat'
    __atribut_private = 'atribut privat'

    def activitate_practica(self):
        print('Copiii se joaca in curte pe balansoar!')

    def calcul_medie_buline_rosii(self):
        numar_copii = int(input('Introduceti numarul de copii: '))
        suma_buline_rosii = 0
        for i in range(numar_copii):
            buline_rosii = int(input(f'Introduceti numarul de buline rosii pentru copilul {i + 1}: '))
            suma_buline_rosii = suma_buline_rosii + buline_rosii
        medie_buline_rosii = suma_buline_rosii / numar_copii

        if medie_buline_rosii > 5:
            print('Elevii acestei gradinite sunt foarte neastamparati!')

    def afisare_informatii_elev(self):
        informatii_primite = eval(input('Introduceti informatiile elvului: '))
        for identificator_elev, date_elev in informatii_primite.items():
            for k, v in date_elev.items():
                print(f'{k} : {v}')
            print('----------------------------------')
    @property
    def afisare_atribut_privat(self):
        pass
    @afisare_atribut_privat.getter
    def afisare_atribut_privat(self):
        return self.__atribut_private

    @afisare_atribut_privat.setter
    def afisare_atribut_privat(self, noua_valoare):
        self.__atribut_private = noua_valoare

    @afisare_atribut_privat.deleter
    def afisare_atribut_privat(self):
        del self.__atribut_private


print('----------------------------------')
gradinita_publica1 = GradinitaPublica()
gradinita_publica1.activitate_practica()
print('----------------------------------')
gradinita_privata1 = GradinitaPrivata()
gradinita_privata1.ora_de_somn()

print('----------------------------------')
gradinita_publica_25 = GradinitaPublica25()
# gradinita_publica_25.activitate_practica()
# gradinita_publica_25.ora_de_somn()
# gradinita_publica_25.calcul_medie_buline_rosii()
print('----------------------------------')
# gradinita_publica_25.afisare_informatii_elev()
# {'elev1':{'nume_elev':'Matei Ionescu', 'nume_parinti':'Ana si Ion Ionescu','varsta_elev':4,'activitate_preferata':'pictura'}}
# {'elev1':{'nume_elev':'Matei Ionescu', 'nume_parinti':'Ana si Ion Ionescu','varsta_elev':4,'activitate_preferata':'pictura'},'elev2':{'nume_elev':'Cosmina Ionescu', 'nume_parinti':'Ana si Ion Ionescu','varsta_elev':2,'activitate_preferata':'balet'}}
print(gradinita_publica_25.atribut_public)
print(gradinita_publica_25._atribut_protected)
print(gradinita_publica_25.afisare_atribut_privat)
gradinita_publica_25.afisare_atribut_privat = 'noua valoare atribut privat'
print(gradinita_publica_25.afisare_atribut_privat)
del gradinita_publica_25.afisare_atribut_privat
print(gradinita_publica_25.afisare_atribut_privat)
