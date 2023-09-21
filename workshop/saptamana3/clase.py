class Pisica:
    nume = str()
    culoare = str()
    varsta = float()
    vaccinata = bool()

    def __init__(self, nume):
        self.nume = nume

    def vaccinare_pisica(self):
        if self.vaccinata:
            print(f"Pisica {self.nume} este deja vaccinata...")
        else:
            print(f"Pisica {self.nume} va fi vaccinata acum...")
            self.vaccinata = True


# Saptamana 1
garfield = Pisica("Garfield")
garfield.vaccinare_pisica()

# Saptamana 2
garfield.vaccinare_pisica()
minnie = Pisica("Minnie")
minnie.vaccinare_pisica()
minnie.vaccinare_pisica()

minnie.nume
minnie.culoare = "Portocaliu"

print(f"Pisica minnie are culoarea {minnie.culoare}")
print(f"Pisica garfield are culoarea {garfield.culoare}")

garfield.culoare = "Negru"
print(f"Pisica garfield are culoarea {garfield.culoare}")

# a = int(5)
# b = int(7)
#
# lista_mea = list([1, 2, 3])
# lista_ta = list([3, 4, 5])
#
# lista_mea.clear()