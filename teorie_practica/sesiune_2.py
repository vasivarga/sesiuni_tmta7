word = "ITFACTORY"
print(word[0:3])
print(word[0:8])
print(word[0:9])
print(word[:])  # la fel cu print(word[::])
print(word[1:9:2])
print(word[::])
print(word[::-1])  # parcurgere in sens invers
second_word = word[:]  # cream o copie
print(second_word)

x = 50.17
y = 30.13
a = str(x)
b = str(y)
print(int(a[0:2]) + int(b[0:2]))  # adunarea partilor intregi ale numerelor
print(int(a[:2]) + int(b[:2]))

# type casting de la float la int
c = int(x)
d = int(y)
print(c + d)

name = "Popescup"
print(name.replace('p', 'a'))
print(name.replace('p', 'a', 1))  # prima aparitie a lui p o sa fie inlocuita

print(name.upper())
print(name.lower())
print(name.upper().replace('P', 'A').lower())  # inlocuirea tuturor caracterelor 'p' cu 'a'

phrase = "Ana are mere, pere si prune."
print(phrase.split('a'))

print(phrase.index('a'))

print(phrase.islower())
print(phrase.isupper())

other_name = "andreea"
print(other_name.capitalize())

print(other_name.count('a'))
print(len(other_name))

# is decimal verifica daca stringul contine doar caractere de la 0-9
telephone = "0096376853124987659"
print(telephone.isdecimal())

telephone = "1234ab"
print(telephone.isdecimal())

# is digit = verifica daca stringul contine doar caractere de la 0-9
# plus daca contine unicode numeric
print("x\u00b2")
print("x\u2082")
telephone = "12345\u2082"
print(telephone.isdigit())
print(telephone.isdecimal())

# isNumeric = verifica ce verifica isDigit + fractii sau numere exponentiale
print("¾2²1234\u2082".isnumeric())

suma = 0
salariu = 100
suma = salariu + 100
print(suma)
print(salariu % 8)  # returneaza restul impartirii la 8
print(2 ** 3)  # ridicare la putere
print(7 / 2)  # returneaza rezultatul impartirii (cu tot cu partea zecimala)
print(int(7 / 2))
print(7 // 2)  # imparte si returneaza rezultatul fara zecimala

salariu = salariu + 20
salariu += 20  # la fel cu salariu = salariu + 20
print(salariu)

# NOT > AND > OR
print(not 1 == 2 or 1 + 1 == 2 and 1 + 2 == 4)
# True or True and False = True or False => True

print((not 1 == 2 or 1 + 1 == 2) and 1 + 2 == 4)
# (True or True) and False = True and False => False

numar = -2
if numar > 0:
    print("Numarul este mai mare ca 0")
    print("Am intrat in if")
elif numar == 0:
    print("Numarul este egal cu 0")
elif numar == 1:
    print("Numarul este egal cu 1")
else:
    print("Numarul este minunat")

if numar < 0:
    print("Numarul este negativ")
    if numar == -2:
        print("Numarul este -2")

# if -else
# if
# if - elif - ... - elif - else
