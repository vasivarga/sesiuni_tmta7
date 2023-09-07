#  STRUCTURI REPETITIVE
# While
# Exemplul 1:
i = 1
while i <= 101:
    print(f'Dalmatianul curent este {i} .')
    i = i + 1

# Exemplul 2:
phrase = 'american'
i = 0
while i < len(phrase):
    print(f'{phrase[i]}')
    i += 1

# Exemplul 3:
list = [1, 5, 'are', 6, 8, 'adevarat']
i = 0
while i < len(list):
    print(list[i])
    i = i + 1

# vom afisa lista in ordine inversa
i = len(list) - 1
while i >= 0:
    print(f' Elementul in ordine inversa este: {list[i]}')
    i = i - 1

# Exemplul 4:
my_tuple = (3, 5, 'apple', 'orange')
i = 0
while i < len(my_tuple):
    print(my_tuple[i])
    i = i + 1

# STRUCTURA REPETITIVA: FOR
# Exemplul 1:
for i in range(1, 102, 2):
    print(f'Dalmatianul curent este {i}')

# Exemplul 2:
for i in range(6):
    print(i)

# Exemplul 3:
for i in range(10, -1, -1):
    print(i)

# Exemplul 4:
# list = [1, 5, 'are', 6, 8, 'adevarat']
print('Exemplul 4:')
for i in range(len(list)):
    print(list[i])

# STRUCTURA REPETITIVA FOR EACH:
# Exemplul 1:
print('Exemplul 5:')
# list = [1, 5, 'are', 6, 8, 'adevarat']
for i in list:
    print(i)

# Exemplul 2:
# my_tuple = (3, 5, 'apple', 'orange')
print('Exemplul 2:')
for i in my_tuple:
    print(i)

# Exemplul 3:
print('Exemplul 3:')
my_set = {'ana', 'ARE', 6, True, 8, 7}
for i in my_set:
    print(i)

# Exemplul 4:
print('Exemplul 4:')
my_dictionary = {'name': 'Popescu', 'age': 15, 'elev': True}
for i in my_dictionary:
    print(i, my_dictionary[i])

# o alta modalitate de a parcurge valorile dintr-un dictionar
print('Exemplul 4-1:')
for k, v in my_dictionary.items():
    print(k, v)

# Exemplul 5:
print('Exemplul 5:')
lista_fructe = ['mere', 'pere', 'kiwi', 'struguri']
for i in lista_fructe:
    if i == 'kiwi':
        break
    print(i)

# Exemplul 6:
print('Exemplul 6:')
lista_fructe = ['mere', 'pere', 'kiwi', 'struguri']
for i in lista_fructe:
    if i == 'kiwi':
        continue
    print(i)

# Exemplul 7:
print('Exemplul 7:')
date_plata_facturi = [1, 10, 15, 20, 25, 30]
data_plata_factura = 15

for i in range(len(date_plata_facturi)):
    if date_plata_facturi[i] == data_plata_factura:
        print(f"Factura a fost platita in ziua de {date_plata_facturi[i]}, nu mai mananci la lumanare.")
        break
    print(f"Data de astazi este: {date_plata_facturi[i]}, in continuare mananci la lumanare.")

print('Exemplul 7-1:')
for i in range(len(date_plata_facturi)):
    if date_plata_facturi[i] == data_plata_factura:
        print(f"Factura a fost platita in ziua de {date_plata_facturi[i]}, nu mai mananci la lumanare.")
        continue
    print(f"Data de astazi este: {date_plata_facturi[i]}, in continuare mananci la lumanare.")

print('Exemplul 7-2:')
for i in range(len(date_plata_facturi)):
    if date_plata_facturi[i] == data_plata_factura:
        continue
        print(f"Factura a fost platita in ziua de {date_plata_facturi[i]}, nu mai mananci la lumanare.")
    print(f"Data de astazi este: {date_plata_facturi[i]}, in continuare mananci la lumanare.")
