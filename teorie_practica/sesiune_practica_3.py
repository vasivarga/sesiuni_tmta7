# OOP sau POO
# clasa cu constructor implicit
class Catel:
    atribut_1 = 'mamifer' # atribute sau proprietati
    blana = True # atribute sau proprietati
    picioare = 4 # atribute sau proprietati

    def latra(self): # metode sau comportament
        print('ham, ham')

    def se_joaca(self): # metode sau comportament
        print('Catelul se joaca.')

    def mananca(self): # metode sau comportament
        print('Catelul mananca pedigree.')

    def numar_picioare(self):
        print(f'Catelul are {self.picioare} picioare.')

catel_1 = Catel()# obiect instantiat din clasa Catel
catel_1.latra()
catel_1.se_joaca()
catel_1.mananca()
catel_1.numar_picioare()

print(catel_1.blana)

# Clasa cu constructor explicit
class Masina:
    def __init__(self,marca,model,numar_roti):
        self.marca = marca
        self.model = model
        self.numar_roti = numar_roti
        self.viteza = 0

    def claxoneaza(self):
        print('bit, bit')

    def accelereaza(self,kmh):
        print(f'Masina accelereaza cu {kmh}')
        self.viteza = self.viteza + kmh
        print(f'Masina are viteza {self.viteza}')

    def informatii(self):
        print(f'Marca este {self.marca}')
        print(f'Model este {self.model}')
        print(f'Numar roti este {self.numar_roti}')

masina_1 = Masina('Honda','civic', 4)# am instantiat 2 obiecte
masina_2 = Masina('Ford','focus', 5)
masina_1.informatii()
masina_2.informatii()

masina_1.accelereaza(10)
masina_1.accelereaza(30)
masina_2.claxoneaza()
masina_1.claxoneaza()

print(masina_1.marca)
print(masina_2.model)



