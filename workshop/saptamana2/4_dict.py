# 1. Declarati un dictionar

dictionar = {
    "Prenume": "Ana",
    "Nume": "Popescu",
    "Varsta": 25,
    "Inaltime": 1.60
}

# 2. Declarati un dictionar gol

# Varianta 1
dict_gol_1 = {}

# Varianta 2
dict_gol_2 = dict()

# 3. Adaugati un element nou in dictionar folosind functia update() si respectiv pe baza de cheie
dictionar.update({"Nota": 10})
print(dictionar)

dictionar["Media"] = 9.50
print(dictionar)

# 4. Extrageti un element din dictionar folosind metoda get() si respectiv pe baza de cheie
print(f"Nume: {dictionar.get('Nume')}")
print(f"Prenume: {dictionar['Prenume']}")

# 5. Stergeti un element din dictionar folosind functia pop() si respectiv functia popitem(). Observati rezultatele
dictionar.pop("Media")
print(dictionar)

dictionar.popitem()
print(dictionar)

# 6. Extrageti pe rand toate cheile, apoi toate valorile, si apoi toate item-urile din dictionar
print(dictionar.keys())
print(dictionar.values())
print(dictionar.items())

# 7. Stergeti toate valorile din dictionar folosind metoda clear()
dictionar.clear()
print(dictionar)

