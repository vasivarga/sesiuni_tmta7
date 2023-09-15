import random

"""
# ### Important de retinut este faptul ca o clasa reprezinta O RETETA / UN PLAN / O REGULA 
dupa care se construiesc obiectele (variabilele).

cinema_1 = Cinema(nume_c1, nr_c1, adresa_c1)
cinema_2 = Cinema(nume_c2, nr_c2, adresa_c2)

- cinema_1 si cinema_2 sunt doua obiecte (variabile) diferite!
- cinema_1 este o instanta a clasei Cinema / un obiect al clasei Cinema
- cinema_2 este o alta instanta a clasei Cinema / un alt obiect al clasei Cinema
- cinema_1 si cinema_2 sunt salvate in memorie la adrese diferite
- fiecare obiect are proprietatile proprii
- tot ceea ce facem in constructor se reflecta pe toate obiectele (cinema_1/cinema_2/etc)
- modificaile pe care le facem pe cinema_1 nu se reflecta pe cinema_2!
"""

class Cinema:
    nume_cinema = str()
    nr_locuri = int()
    adresa = str()
    lista_filme = list()
    rezervari = dict()

    # Declaram constructorul pentru clasa Cinema
    # Fiecare obiect din clasa cinema va avea:
    # - nume primit la declarare
    # - nr_locuri primit la declarare
    # - adresa primit la declarare
    # EX: cinema_1 = Cinema("Cinema City Iasi", 450, "Incinta Iulius Mall")
    def __init__(self, nume, nr_locuri, adresa):
        print(f"Se initializeaza cinematograful {nume}")
        self.lista_filme = []
        self.nume_cinema = nume
        self.nr_locuri = nr_locuri
        self.adresa = adresa
        # daca as apela metoda de mai jos in constructor, as popula orice cinematograf creat cu filmele din functia respectiva
        # self.populeaza_lista_cu_filme()

    def populeaza_lista_cu_filme(self):
        film1 = {
            "titlu": "The Godfather",
            "durata": 175
        }

        film2 = {
            "titlu": "Forrest Gump",
            "durata": 144
        }

        film3 = {
            "titlu": "Inception",
            "durata": 148
        }

        self.lista_filme.append(film1)
        self.lista_filme.append(film2)
        self.lista_filme.append(film3)

    def afisare_detalii(self):
        print("------------Afsare detalii cinema------------")
        print(f"Nume cinematograf: {self.nume_cinema}")
        print(f"Numar locuri: {self.nr_locuri}")
        print(f"Adresa: {self.adresa}")
        print(f"Lista filmelor care ruleaza: {self.lista_filme}")
        print(f"Rezervarile: {self.rezervari}")

    def afiseaza_filme_disponibile(self):
        print(f"------------Afsare filme {self.nume_cinema}------------")

        for i in range(len(self.lista_filme)):
            film = self.lista_filme[i]
            titlu_film = film['titlu']
            durata_film = film['durata']
            print(f"Titlu: {titlu_film}")
            print(f"Durata: {durata_film}")
            print("----------------------------")

    # Adaugare film fara parametri (se citesc valorile de la tastatura)
    def adaugare_film(self):
        print("------------Adaugare film nou------------")

        titlu_film = input("Introduceti titlul filmului nou: ")
        durata_film = int(input("Introduceti durata filmului nou: "))

        film = {
            "titlu": titlu_film,
            "durata": durata_film
        }

        self.lista_filme.append(film)

    # Adaugare film cu parametri (se specifica titlu si durata cand apelam functia cu parametru)
    # Aici suprascriem metoda adaugare_film() initiala de mai sus, adica ea n-o sa mai fie valida
    def adaugare_film(self, titlu, durata):
        print("------------Adaugare film nou------------")

        film = {
            "titlu": titlu,
            "durata": durata
        }
        self.lista_filme.append(film)

    def rezervare_film(self):
        print("------------Adaugare rezervare noua------------")
        print("Avem urmatoarele filme disponibile: ")

        for i in range(len(self.lista_filme)):
            film = self.lista_filme[i]
            titlu_film = film['titlu']
            print(f"{i + 1} - {titlu_film}")

        index_film = int(input("Introduceti numarul filmului: ")) - 1
        locuri = int(input("Introduceti numarul de locuri: "))
        nume = input("Introduceti numele dvs: ")
        pret = 10 * locuri
        titlu_film_rezervat = self.lista_filme[index_film]['titlu']

        detalii_rezervare = {
            "titlu_film": titlu_film_rezervat,
            "nume": nume,
            "locuri": locuri,
            "pret": pret
        }

        nr_rezervare = self.genereaza_numar_random()

        self.rezervari.update({nr_rezervare: detalii_rezervare})

        self.printeaza_bilet(detalii_rezervare)


    def genereaza_numar_random(self):
        nr = random.randint(99999999, 99999999999999999)
        while nr in self.rezervari.keys():
            nr = random.randint(99999999, 99999999999999999)
        return nr


    def printeaza_bilet(self, rezervare):
        titlu_film = rezervare['titlu_film']
        nume = rezervare['nume']
        locuri = rezervare['locuri']
        pret = rezervare['pret']

        print("___________________________________")
        print("_______________BILET_______________")
        print(f"Film: {titlu_film}")
        print(f"Nume: {nume}")
        print(f"Locuri rezervate: {locuri}")
        print(f"PRET TOTAL: {pret} LEI")
        print("___________________________________")

    def afisare_rezervari(self):
        print("---- Rezervari efectuate ----")
        for key, value in self.rezervari.items():
            print(f"Rezervarea cu nr {key}: {value}")

cinema_1 = Cinema("Cinema City Iasi", 450, "Incinta Iulius Mall")
cinema_1.afisare_detalii()

cinema_2 = Cinema("Cinema City Cluj", 350, "Incinta Vivo Mall")
cinema_3 = Cinema("Cinema City Bucuresti", 600, "Centru")

cinema_2.afisare_detalii()
cinema_3.afisare_detalii()

cinema_1.afiseaza_filme_disponibile()

# Metoda prin care adaugam un film cu date introdue de la tastatura
# cinema_1.adaugare_film()

cinema_1.adaugare_film("Avatar", 235)
cinema_2.adaugare_film("Barbie", 160)

cinema_1.afiseaza_filme_disponibile()
cinema_2.afiseaza_filme_disponibile()
cinema_1.populeaza_lista_cu_filme()


cinema_1.afiseaza_filme_disponibile()
cinema_2.afiseaza_filme_disponibile()


cinema_1.rezervare_film()
cinema_1.rezervare_film()

cinema_1.afisare_rezervari()

