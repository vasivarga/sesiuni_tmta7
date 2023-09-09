fotbalisti_pe_echipe = {
    "Barcelona": {
        "Dica":
            {
                "Nume complet": "Nicolae Dica",
                "Varsta": 45,
                "Numar Tricou": 10
            },
        "Banel":
            {
                "Nume complet": "Banel Nicolita",
                "Varsta": 47,
                "Numar Tricou": 3
            },
        "Dukadam":
            {
                "Nume complet": "Helmut Dukadam",
                "Varsta": 65,
                "Numar Tricou": 7
            }
    }
}

# Pe baza acestui dictionar faceti urmatoarele exerciti:

"""
Explicație:

Aici întâlnim conceptul de dicționar în dicționar (dicționare îmbricate) 
- Dicționarul principal <fotbalisti_pe_echipe> conține o singură cheie: <Barcelona>
- Cheia <Barcelona> are ca valoare un alt dicționar, deci <Barcelona> poate fi considerat un dictionar interior/imbricat
- Dictionarul <Barcelona> contine 3 chei: <Dica>, <Banel> si <Dukadam>, si ele dictioare interioare
- <Dica>, <Banel> si <Dukadam> au cheile identice <Nume complet>, <Varsta> si <Numar Tricou>
"""

# 1. Printati pe ecran numarul de pe tricou al oricarui jucator doriti
print(fotbalisti_pe_echipe['Barcelona']['Dica']['Numar Tricou'])

# 2. Folositi functia pop pentru a scoate orice jucator din dictionar
fotbalisti_pe_echipe['Barcelona'].pop('Dica')
print(fotbalisti_pe_echipe)

# 3. Printati pe ecran detaliile despre fiecare jucator astfel incat sa obtineti urmatorul rezultat:


# ##### EXPLICATIE ACCESARE ELEMENTE DICTRIONAR PRIN FOR EACH:
# ### Consideram dictionarul simplu de mai jos:

dictionar = {
    "Prenume": "Ana",
    "Nume": "Popescu",
    "Varsta": 25,
    "Inaltime": 1.60
}

# Folosind un for each putem accesa fiecare cheie si valoare din dictionar

for cheie, valoare in dictionar.items():
    print(f'Cheia este {cheie}, iar valoarea este {valoare}')

# Inseamna ca in mod similar putem accesa cheile si valorile dictionarelor interioare
# cu for each in for each (for imbricat / in engleza: nested for)

for cheie, valoare in fotbalisti_pe_echipe.items():
    for cheie_interioara, valoare_interioara in valoare.items():
        for cheie_jucator, detalii_jucator in valoare_interioara.items():
            print('Detalii jucator', f'{cheie_jucator}:{detalii_jucator}', sep='-', end=', ')
        print('\n')

print('-------------------------------------------------------------------------------')

# ### <sep> si <end> sunt niste argumente ale functiei print() care ii pot schimba comportamentul
# <sep> specifica separatorul
# <end> specifica cum se termina linia printata.
# In mod normal, functia print() se termina cu un rand nou, dar poate fi schimbat

# ################### Exemplu cu <sep>

# print cu mai multe argumente de printat, simplu, fara separator specificat:
print('Hello', 'Hello', 'Hello')

# print cu mai multe argumente de printat, cu separatorul "-":
print('Hello', 'Hello', 'Hello', sep='-')
print('-------------------------------------------------------------------------------')

# ################### Exemplu cu <end>

# doua printuri consecutive, fara final de rand modificat (fiecare este afisat pe rand nou)
# deoarece in mod implicit se pune un rand nou la final de print:
print('Hello')
print('Hello')

# doua printuri consecutive, cu final de rand modificat:
# prin <end="### "> modificam comportamentul primului print: in loc sa puna rand nou la final, acesta va pune "### ",
# iar urmatorul print va fi afisat pe aceeasi linie
print('Hello', end="### ")
print('Hello')

