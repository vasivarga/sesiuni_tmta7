"""
##### Can avem un for simplu, acesta are urmatoarea forma generala:

for <variabila_de_control> in range (<inceput>, <final>, <pas>):
    cod de executat

variabila_de_control isi va schimba valoarea la fiecare iteratie in functie de regula specificata in range()

de exemplu, daca avem urmatorul for:

for i in range (0, 10, 1), atunci:

 - i va incepe cu valoarea 0
 - i va merge pana la 9 - capatul de interval 10 nu este inclus, daca vrem sa mearga pana la 10, punem range(0, 11, 1)
 - i isi va mari valoarea cu 1 la fiecare iteratie, daca vrem sa mearga din 2 in 2 putem scrie range(0, 10, 2)
"""

# Exemplu 1
# Vrem ca i sa ia valoarea de la 0 la 9 si sa isi CREASCA valoarea cu 1 la fiecare iteratie

for i in range(0, 10, 1):
    print(f"La aceasta iteratie i este egal cu {i}")

print("-----------------------------------------------------------------------------------")

# Cand inceputul range-ului e 0, iar valoarea adaugata la i este 1, putem scrie exemplul de mai sus mai simplu:
for i in range(10):  # varianta asta este identica cu cea de mai sus
    print(f"La aceasta iteratie i este egal cu {i}")

print("-----------------------------------------------------------------------------------")

# Exemplu 2
# Vrem ca i sa ia valoarea de la 0 la 10 si sa isi CREASCA valoarea cu 2 la fiecare iteratie

for i in range(0, 11, 2):
    print(f"La aceasta iteratie i este egal cu {i}")

print("-----------------------------------------------------------------------------------")

# Exemplu 3
# Vrem ca i sa ia valoarea de la 10 la 1 si sa isi SCADA valoarea cu 1 la fiecare iteratie
# Aici folosim -1
for i in range(10, 0, -1):
    print(f"La aceasta iteratie i este egal cu {i}")

print("-----------------------------------------------------------------------------------")

# Exemplu 4
# Consideram ca avem o lista

lista = ["Ana", "mere", 28, "pere", True, "portocale"]
# index:   0      1     2     3      4         5

# Vrem sa afisam fiecare element din lista pe baza de index
# -Inseamna ca i trebuie sa mearga de la 0 pana la 5 pentru a acoperi toti indecsii si sa creasca cu 1 => range(0, 6, 1)
# -Deoarece inceputul e 0 si i creste din 1 in 1, putem scrie simplu => range(6)
# -De fapt 6 reprezinta lungimea listei, iar pentru a parcurge orice lista pana la capat, fara sa-i mai numaram
# toate elementele putem folosi len(lista)
# -Deci regula devine range(len(lista)) - valabila pentru orice lista indiferent de marime

for i in range(len(lista)):
    print(f"Variabila i este egala cu {i}")
    print(f"La indexul {i} avem elementul: {lista[i]}")
    print("")
