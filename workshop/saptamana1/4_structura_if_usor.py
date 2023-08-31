"""
Exista 4 tipare de if

1) if simplu - daca expresia din if e adevarata, executam setul de instructiuni din if, iar daca nu, trecem mai departe
    if true:
        executam_codul_de_aici
-----------------------------------------------------------------------------------------------------------------------

2) if else - daca expresia din if e adevarata, executam setul de instructiuni din if, iar daca nu,
            executam setul de instructiuni din else

    if true:
        executam_codul_din_if
    else:
        executam_codul_din_else
-----------------------------------------------------------------------------------------------------------------------

3) if elif - aici verificam mai multe expresii si executam codul unde gasim prima expresie care se evalueaza la True
            IMPORTANT DE STIUT: putem avea oricate elif-uri

    if <expresie de evaluat>:
        executam_codul_din_if

    elif <alta expresie de evaluat>:
        executam_codul_din_acest_elif

    elif <alta expresie de evaluat>:
        executam_codul_din_acest_elif

    elif <alta expresie de evaluat>:
        executam_codul_din_acest_elif
-----------------------------------------------------------------------------------------------------------------------

4) if elif else = aici verificam toate posibilitatile de care stim, iar daca niciuna din ele nu este adevarata, putem

    if <expresie de evaluat>:
        executam_codul_din_if

    elif <alta expresie de evaluat>:
        executam_codul_din_acest_elif

    elif <alta expresie de evaluat>:
        executam_codul_din_acest_elif

    else:
        executam_codul_din_else

-----------------------------------------------------------------------------------------------------------------------
"""

#Ex_1 Explica cu cuvintele tale in cadrul unui comentariu cum functioneaza un if else
# Un if-else evalueaza o expresie logica, iar in functie de rezultat (True sau False) executa anumite instructiuni

# Ex_2 Verifica si afiseaza daca x este numar natural sau nu (un numar se considera natural daca este numar intreg
# mai mare ca 0)
x = 7

if x > 0 and type(x) == int:
    print(f'{x} este numar natural')
else:
    print(f'Numarul {x} nu este numar natural')

#Ex_3 Verifica si afiseaza daca x este numar pozitiv, negativ sau neutru
if int(x) > 0:
    print("numar pozitiv")
elif int(x) < 0:
    print("numar negativ")
else:
    print("neutru")


#Ex_4 Verifica si afiseaza daca x este intre -2 si 13 (incluzand captele de interval).
# [-2, -1, 0 , 1, 2, 3, 4 ,5 ,6 ,7, 8 ,9, 10 , 11, 12, 13]
if -2 <= x <= 13:
    print("numarul este inclus in intervalul -2 13")
else:
    print("nu este inclus in interval -2 13")

#Ex_5 Verifica daca x NU este intre 5 si 27, excluzand capetele de interval. (a se folosi ‘not’)
x = 7

if not 5 < x < 27:   # if not(x>5)  and not(x<27)
    print("numarul nu este in interval")
else:
    print("numarul este in interval")

# Ex_6 Declara o noua variabila y de tip int si apoi verifica si afiseaza daca x si y sunt egale, daca nu,
# afiseaza care din ele este mai mare
x = 8
y = 8
if x > y:
    print(f'{x} este mai mare ca {y}')
elif y > x:
    print(f'{y} este mai mare ca {x}')
else:
    print("numerele sunt egale")


# Ex_7 Presupunand ca x, y, z (toate de tip int) reprezinta laturile unui triunghi, afiseaza daca triunghiul este
# isoscel (doua laturi sunt egale), echilateral (toate laturile sunt egale) sau oarecare (nicio latura nu e egala).

x = 3
y = 6
z = 9
if x == y and y == z:
    print("triunghi echilateral")
elif x == y or x == z or y == z:
    print("triunghi isoscel")
else:
    print("triunghi oarecare")


# Ex_8 Citeste o litera de la tastatura apoi verifica si afiseaza daca este vocala sau nu. Atentie! Trebuie sa
# evaluati si cazurile uppercase si cazurile lowercase.

"""
# Operatorul de apartenenta <in>

Evalueaza daca operandul din stanga se afla in componenta operandului din dreapta. 
Returneaza True sau False
- Putem verifca daca un cuvant este intr-o litera
- Putem verifica daca un element se afla intr-o lista
- Putem verifica daca un numar se afla intrun interval

"""

print("a" in "plan")

print("ana" in ["ana", "are", "mere"])

x = 5
print(x in range(1, 6))

litera = "E"  #input(str("introduceti litera = "))

# VARIANTA 1
if litera.lower() == "a" or litera.lower() == "e" or litera.lower() == "i" or litera.lower() == "o" or litera.lower() == "u":
    print("litera este vocala")
elif litera.isdigit():
    print("caracterul introdus nu este litera")
else:
    print("litera este consoana")

# VARIANTA 2
vocale = "aeiou"
if litera.lower() in vocale:
    print("litera este vocala")
else:
    print("litera este consoana")