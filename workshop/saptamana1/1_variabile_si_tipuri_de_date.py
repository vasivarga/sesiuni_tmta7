#Ex_1 - În cadrul unui comentariu, explică cu cuvintele tale ce este o variabilă.
# variabila = reprezinta o adresa de memorie la care se pot stoca anumite valori


#Ex_2 - Declară și inițializează câte o variabilă din fiecare din următoarele tipuri:int, string, float, boolean
varsta = 20
nume = "Andrei"
greutate = 75.5
casatorit = False


#Ex_3 - Utilizează funcția type pentru a verifica dacă variabilele declarate mai sus au tipul de date așteptat.
print(type(varsta))
print(type(nume))
print(type(greutate))
print(type(casatorit))


#Ex_4 - Rotunjește variabila ‘float’ folosind funcția round() și salvează această modificare în aceeași variabilă (suprascriere), apoi verifică din nou tipul de date al acesteia.
greutate = round(greutate)
print(type(greutate))

#Ex_5 - Incearca sa convertesti variabila string la int folosind type casting si observa rezultatele
# print(int(nume)) - va returna eroare in cazul in care nu se poate converti in int

lungime = "17"
print(int(lungime))

#Ex_6 - Incearca sa convertesti variabila boolean la int folosind type casting si observa rezultatele
print(int(casatorit))

#Ex_7 - Schimba valoarea variabilei boolean (din true in false sau din false in true) si repeta exercitiul anterior
casatorit = True
print(int(casatorit))

