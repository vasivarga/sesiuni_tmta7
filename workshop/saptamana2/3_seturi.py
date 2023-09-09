#1. Declarati un set
set_elemente = {"Ana", 25, True, 1, 6, 5.0}

#2. Declarati un set gol
set_gol = set()

# Observatie:
# set_gol_2 = {} ar crea un dictionar gol

#3. Adaugati un element nou in set folosind functia add()
set_elemente.add("X")
print(f"Setul dupa functia add(): {set_elemente}")

#4. Stergeti un element din set folosind functia pop() si respectiv functia remove(). Observati rezultatele

set_elemente.pop()
print(f"Setul dupa functia pop(): {set_elemente}")


set_elemente.remove("Ana")
print(f"Setul dupa functia remove(): {set_elemente}")


#5. Verificati daca un set este o subdiviziune a unui alt set (subset)

# Adaugam elementele Y si Z
set_elemente.add("Y")
set_elemente.add("Z")

# Definim un subset nou cu elementele Z si Y
set_mic = {"Z", "Y"}

# Verificam daca setul format din elementele {Z, Y} este un subset al setului mare
assert set_mic.issubset(set_elemente)

#6. Verificati daca un set contine toate elementele dintr-un alt set + alte elemente (superset)
assert set_elemente.issuperset(set_mic)

#7. Verificati care sunt elementele comune intre doua seturi (intersection)

# In set_mic adaugam elemente care nu se vor afla in set_elemente
set_mic.add("A")
set_mic.add("B")
set_mic.add("C")

# Afisam seturile inainte sa vedem elementele comune
print(f"Setul mare: {set_elemente}")
print(f"Setul mic: {set_mic}")

# Verificam elementele comune. Observam ca metoda poate fi apelata de pe oricare set
print(f"Intersectia celor doua seturi: {set_elemente.intersection(set_mic)}")
print(f"Intersectia celor doua seturi: {set_mic.intersection(set_elemente)}")

#8. Verificati diferenta intre doua seturi cu functia difference()
print(f"Elementele care se afla doar in set_elemente: {set_elemente.difference(set_mic)}")
print(f"Elementele care se afla doar in set_mic: {set_mic.difference(set_elemente)}")

#9. Stergeti toate elementele dintr-un set folosind functia clear()
set_elemente.clear()

print(set_elemente)
