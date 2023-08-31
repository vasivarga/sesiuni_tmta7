varsta = 20
nume = "Andrei"
greutate = 75.5
casatorit = False

#Ex_1 - Folosește funcția print() și printează în consola 4 propoziții folosind cele 4 variabile. Rezolvă nepotrivirile de tip pe rand prin toate modalitatile cunoscute
print("Numele meu este " + nume)
print("Varsta mea este " + str(varsta))
print(f"Andrei are greutatea {greutate}")
print("Andrei este casatorit? {}".format(casatorit))
print("Numele meu este {} si am {} ani".format(nume, varsta))

#Ex_2 - Citește de la tastatură numele și prenumele unei persoane și salveaza-le in cate o variabila. Afișează pe ecran următoarea propoziție: 'Numele complet are x caractere'.
nume = "Petre"
prenume = "Popescu"

print(len(nume))
print(len(prenume))

nr_caractere = len(nume) + len(prenume)
print(f"Numele complet are {nr_caractere} caractere")


#Ex_3 - Citește de la tastatură lungimea și lățimea unui dreptunghi și salveaza-le in cate o variabila. Afișează pe ecran următoarea propoziție: 'Aria dreptunghiului este x'.
lungime = 5
latime = 3
arie = lungime*latime

print(f"Aria dreptunghiului este {arie}")

#Ex_4 - Având stringul: 'Coral is either the stupidest animal or the smartest rock' afișează de câte ori apare cuvântul 'the' în acest string
propozitie = "Coral is either the stupidest animal or the smartest rock"
print(propozitie.count("the"))

#EX_5 Folosindu-te de string-ul de la exercițiul 4, inlocuieste “the” cu “THE” peste tot (inclusiv in cuvantul “either”) si afișează pe ecran rezultatul
print(propozitie.replace("the", "THE"))

#Ex_6 Folosindu-te de string-ul de la exercițiul 4 foloseste un assert ca să verifici dacă acest string conține doar numere.
assert False == propozitie.isnumeric()

# OBSERVATIE:
# Cand atribuim o valoare unei variabile folosim =
# Cand verificam daca doua variabile/date sunt egale, folosim ==

