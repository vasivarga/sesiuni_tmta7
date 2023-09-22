from saptamana4.gradi.clase_gradinita import GradinitaPrivata, GradinitaPublica25, GradinitaPublica

gradi_privat = GradinitaPrivata()

elev_1 = {
    "Andrei": {
        "varsta": 7,
        "an_inscriere": 2022,
        "sport_preferat": "fotbal"
    }
}

elev_2 = {
    "Alexandra": {
        "varsta": 5,
        "an_inscriere": 2021,
        "activitate_preferata": "colorat",
    }
}

gradi_privat.adauga_elev(**elev_1)
gradi_privat.adauga_elev(**elev_2)

gradi_privat.afisare_informatii_elevi()


gradi_public = GradinitaPublica()
gradi_public.start_concurs()

gradi_25 = GradinitaPublica25()
gradi_25.concurenti = ["Florica", "George", "Mihai", "Ana"]
gradi_25.start_concurs()

# Am creat un al doilea obict de tip GradinitaPublica25
gradi_25_2 = GradinitaPublica25()

print(gradi_public.concurenti)
print(gradi_25_2.concurenti)


