# Considera urmatoarea lista:
lista = [3, 5, 4, 6, 2, 1]

"""
Metoda "Bubble Sort" (Sortarea bulelor) este un algoritm de sortare simplu, care funcționează prin compararea și 
schimbul repetat al elementelor adiacente (vecine) într-o listă până când lista este sortată complet.
Iată cum putem aplica Bubble Sort pe lista ta în Python:


1. Parcurgem lista folosind două bucle for imbricate. 
Prima buclă va parcurge lista pentru a face iterații pentru fiecare element din ea, 
iar a doua buclă va parcurge lista și va compara elementul curent cu următorul. 
Dacă elementul curent este mai mare decât următorul, le schimbăm locurile.

2. În fiecare iterație a primei bucle, cel mai mare element din listă va ajunge la finalul ei. 
De aceea, putem reduce numărul de comparații în fiecare iterație a doua bucle cu len(lista) - i - 1.

3. După ce terminăm toate iterațiile, lista va fi sortată în ordine crescătoare.
"""

print(f"Lista inainte de sortare: {lista}")

for i in range(len(lista)):
    for j in range(0, len(lista) - i - 1):
        if lista[j] > lista[j + 1]:
            lista[j], lista[j + 1] = lista[j + 1], lista[j]

print(f"Lista dupa sortare: {lista}")
