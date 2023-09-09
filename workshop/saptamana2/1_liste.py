#1. Declarati o lista cu elemente multi type
lista_multi_type = ["Andreea", 28, True, 65.5, 28, "Andreea"]

#2. Declarati o lista goala

# varianta 1
lista_goala_1 = []

# varianta 1
lista_goala_2 = list()

print(lista_goala_1)
print(lista_goala_2)

#3. Accesati orice element din lista pe baza de index
print(lista_multi_type[0])

#4. Accesati pozitia unui element din lista pe baza functiei index()
print(lista_multi_type.index("Andreea"))

# Varianta de mai jos ar returna eroare, deoarece "Andrei" n use afla in lista
# print(lista_multi_type.index("Andrei"))


#5. Adaugati elemente in lista atat cu functia append() cat si cu functia insert(). Observati rezultatele
lista_multi_type.append("Alex")
print(lista_multi_type)

lista_multi_type.insert(0, 30)
print(lista_multi_type)


#6. Stergeti elemente din lista atat cu functia pop() cat si cu functia remove(). Observati rezultatele

# pop() fara index
lista_multi_type.pop()
print(lista_multi_type)


# pop() cu index
lista_multi_type.pop(3)
print(lista_multi_type)


# remove()
lista_multi_type.remove("Andreea")
print(lista_multi_type)


#7. Numarati elementele dintr-o lista folosind functia len()
print(f"Lista are {len(lista_multi_type)} elemente")


#8. Numarati de cate ori apare un anumit element in lista folosind functia count()
print(lista_multi_type.count(28))


#9. Uniti doua liste folosind functia extend()
lista_1 = ["X", "Y", "Z"]
lista_2 = ["A", "B", "C"]

lista_1.extend(lista_2)

print(lista_1)

#10. Sortati lista folosind functia sort()
lista_1.sort()
print(lista_1)

#11. Inversati continutul listei folosind functia reverse()
lista_1.reverse()
print(lista_1)

#12. Stergeti toate elementele din lista folosind functia clear()
lista_1.clear()
print(lista_1)

#13. Parcurgeați o lista si printati toate elementele din aceasta folosind pe rand for, while si foreach
lista = ["X", 2, 3, True, 4.5]

# VARIANTA CU FOR
for i in range(len(lista)):
    print(lista[i])


# VARIANTA CU FOR EACH
for element in lista:
    print(element)

# VARIANTA CU WHILE
i = 0
while i < 0:
    print(lista[i])
