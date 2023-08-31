# # # Ex_1 Citește de la tastatură un string de dimensiune impară și afișează caracterul din mijloc.
cuvant = input("Introduceti un string de dimensiune impara: ")

"""
cuvant:    a  l  a  b  a  l  a
index:     0  1  2  3  4  5  6
"""

lungime = len(cuvant)  # pentru cuvantul alabala avem lungimea = 7
pozitie_caracter_mijloc_v1 = round(lungime/2)-1  # cu round se va rotunji in sus, deci trebuie sa scadem 1
pozitie_caracter_mijloc_v2 = lungime // 2  # cu floor division vom avea catul care reprezinta exact indexul cautat

print(cuvant[pozitie_caracter_mijloc_v1])
print(cuvant[pozitie_caracter_mijloc_v2])


# # Ex_2 Folosind assert, verifică dacă un string este palindrom.
# # palindrom = un șir de caractere care citit de la stânga la dreapta sau de la dreapta la stânga rămâne neschimbat

string_palindrom = "sa nu iei un as"

assert string_palindrom[::-1] == string_palindrom

# PT URMATORUL SIR AR DA EROARE:
# string_nepalindrom = "ele fac cafele"
# assert string_nepalindrom[::-1] == string_nepalindrom

# Ex_3 - Citește un string de la tastatură (ex: 'alabala portocala') asupra caruia sa efectuezi urmatoarele:
# - salvează fiecare cuvânt într-o variabilă;
# - printează ambele variabile pentru verificare.

text_citit = input("Introdu un text format din doua cuvinte: ")
cuvant1, cuvant2 = text_citit.split()

print(cuvant1)
print(cuvant2)

# Ex_4 - Citește un string de la tastatură (ex: alabala portocala) asupra caruia sa efectuezi urmatoarele:

# salvează primul caracter într-o variabilă
# capitalizează caracterul a peste tot, mai puțin pentru primul și ultimul index => alAbAlA portocAla.

prima_litera = text_citit[0]
ultima_litera = text_citit[-1]

cuvant_final = prima_litera + text_citit[1:-1].replace("a", "A") + ultima_litera

print(cuvant_final)

# Ex_5 - citeste un user de la tastatura, citeste o parola. Afiseaza: 'Parola pt user x este ***** si are x caractere
username = input("Username: ")
password = input("Parola: ")

lungime_parola = len(password)
parola_mascata = "*" * lungime_parola

print(f"Parola pentru userul {username} este {parola_mascata} si are {lungime_parola} caractere")