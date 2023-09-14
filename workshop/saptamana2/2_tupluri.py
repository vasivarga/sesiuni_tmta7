
#1. Declarati un tuplu
tuplu = ("Ana", 25, "Consultant", "Ana")

#2. Declarati un tuplu gol

# Varianta 1
tuplu_gol_1 = ()

# Varianta 2
tuplu_gol_2 = tuple()

#3. Accesati orice element din tuplu pe baza de index
print(tuplu[0])

#4. Accesati pozitia unui element din lista pe baza functiei index()
print(tuplu.index("Ana"))

#5. Folositi functia count() pentru a numara de cate ori apare un element in tuplu
print(tuplu.count("Ana"))

#6. Folositi functia index() pentru a verifica pozitia la care se afla un anumit element in tuplu
assert tuplu.index("Ana") == 3

#7. Incercati sa modificati un element din tuplu si observati rezultatele
tuplu[0] = "X"
