# Trebuie sa calculam pretul unei facturi la curent
# Daca persoana care plateste are peste 65 de ani, primeste reducere de 10%
# Daca anotimpul curent este iarna, se aplica o reducere de 10%
# Valoarea facturii se calculeaza cu formula [putere_consumata * 1.5]

# pret_factura = 0
# puterea_consumata = 110
# avem_peste_65_de_ani = True
# este_iarna = False
#
# pret_factura = 110 * 1.5
#
# if avem_peste_65_de_ani:
#     pret_factura = pret_factura - (pret_factura * 0.1)
#
# if este_iarna:
#     pret_factura = pret_factura - (pret_factura * 0.1)
#
# print(pret_factura)

def calculeaza_pret_factura(puterea_consumata, avem_peste_65_de_ani, este_iarna):
    pret_factura = puterea_consumata * 1.5

    if avem_peste_65_de_ani:
        pret_factura = pret_factura - (pret_factura * 0.1)

    if este_iarna:
        pret_factura = pret_factura - (pret_factura * 0.1)

    return pret_factura

pret_factura_1 = calculeaza_pret_factura(220, True, True)
print(pret_factura_1)

pret_factura_2 = calculeaza_pret_factura(110, False, False)
print(pret_factura_2)

pret_factura_3 = calculeaza_pret_factura(59, True, False)
print(pret_factura_3)

print(calculeaza_pret_factura(59, True, False))




