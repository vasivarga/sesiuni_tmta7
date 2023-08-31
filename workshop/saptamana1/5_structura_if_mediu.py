"""
1 - Calculare pret discount

Dacă un client are peste 65 de ani, atunci i se va oferi o reducere de 15%.
În caz contrar, dacă clientul nu are peste 65 de ani, dacă persoana călătorește cu cel puțin un copil va avea o reducere de 10%
Atat pentru seniori cat si pentru non- seniori se va aplica o reducere suplimentara de 10% daca vor calatori in timpul iernii.
De asemenea, atât pentru seniori, cât și pentru non seniori se va aplica o taxă de lux de 3% dacă vor călători în clasa I (în orice sezon) sau 1% taxă de gestiune în caz contrar.
"""

varsta_client = 66
discount = 0
copii = False
sezon = "iarna"
clasa = "2"
pret = 100

if varsta_client > 65:
    discount = 0.15
elif copii == True:
    discount = 0.1
if sezon == "iarna":
    discount += 0.1  # discount = discount + 0.1
if clasa == "1":
    tax = 0.03
else:
    tax = 0.01
pret_calatorie = pret - (pret*discount) + (pret*tax)
print(f'Pretul excursiei este: {pret_calatorie}')


"""
2 - Calculare discount seller

Compania X vinde mărfuri la punctele de vânzare cu ridicata și cu amănuntul. 
Clienții angro primesc o reducere de două procente la toate comenzile. 
De asemenea, compania încurajează atât clienții angro, cât și clienții cu amănuntul
să plătească ramburs la livrare, oferind o reducere de două procente pentru această 
metodă de plată. Încă o reducere de două procente este acordată pentru comenzile de 
50 sau mai multe unități. 

"""
client_angro = True  # False
reducere = 0
cantitate = 50
ramburs = True  # False
pret = 100
if client_angro:
    reducere = 0.02
if ramburs:
    reducere += 0.02
if cantitate >= 50:
    reducere += 0.02
pret_final = pret - (pret*reducere)
print(f'Pretul total al comenzii este {pret_final}')

"""
3 - Introduceti un nume de film de la tastatura si evaluati daca numele acelui film este 
numele filmului vostru preferat. Daca da, atunci printati pe ecran: 
“Acesta este filmul meu preferat”. In caz contrar printati pe ecran: 
“Din pacate nu este filmul meu preferat”
"""
film = "Terminator"   # input("Introduceti filmul: ")
film_preferat = "Titanic"
if film == film_preferat:
    print("Acesta este filmul meu preferat")
else:
    print("Din pacate nu este filmul meu preferat")

"""
4 - Aveti la dispozitie urmatorul database url: 
jdbc:mysql://mysql.db.server:3306/my_database?useSSL=false&serverTimezone=UTC
Extrageti din acest text numele bazei de date: mysql.db.server
Folositi un if statement pentru a evalua daca numele bazei de date este cel corect (presupunand ca extrageti url-ul dintr-un sistem extern si nu stiti care este acesta)

"""

url = "jdbc:mysql://mysql.db.server:3306/my_database?useSSL=false&serverTimezone=UTC"

pozitie_start = url.index("//")+2
pozitie_stop = url.index(":3306")

nume_bd_asteptat = "mysql.db.server"
nume_bd_actual = url[pozitie_start:pozitie_stop]

assert nume_bd_asteptat == nume_bd_actual