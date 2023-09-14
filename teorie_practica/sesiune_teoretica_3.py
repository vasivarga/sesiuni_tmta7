# Functie simpla, fara parametri
def function_1():
    print('Am intrat in functia 1.')


function_1()

def function_2():
    return 2

print(function_2())  # alta metoda, vezi liniile 12 + 13

value_function_2 = function_2()
print(value_function_2)


# Functie cu parametru explicit

def function_3(number):
    print(number * 5)


function_3(4)


def function_3_1(elev):
    print(f'Bine ai venit {elev}!')

function_3_1('Elena')
# function_3_1()


# Functie cu parametru implicit

def function_4(username = 'default_user'):
    print(f'My username is {username}')


function_4()
function_4('Mihai')


def function_5(number = 0):
    return number * 3


print(function_5())
print(function_5(1.3))


# Numar indefinit de parametri

def diferenta_numere(*args):
    diferenta = 0
    for i in args:
        diferenta -= i
    return diferenta

print(diferenta_numere())
print(diferenta_numere(17, 3))


def diferenta_numere(*args):
    diferenta = args[0]
    for i in range(1, len(args)):
        diferenta -= args[i] # diferenta = diferenta - args[i}
    return diferenta


print(diferenta_numere(17, 3))
print(diferenta_numere(17, 3, 1, 2, 3))

def diferenta_numere(*args):
    diferenta = args[0]
    for i in range(2, len(args)):
        diferenta -= args[i] # diferenta = diferenta - args[i}
    return diferenta

print(diferenta_numere( 3, 17, 1, 2, 3))


def diferenta_numere(*args):
    if len(args) == 0:
        return 0
    else:
        diferenta = args[0]
        i = 1
        while i < len(args):
            diferenta -= args[i] # diferenta = diferenta - args[i}
            i = i + 1
        return diferenta


print(diferenta_numere( 3, 17, 1, 2, 3))
print(diferenta_numere( 150, 17, 1, 2, 3))
print(diferenta_numere())

# Functie cu nr. indefinit de paramatri (kwargs)

def suma_numere(**kwargs):
    suma = 0
    for i in kwargs.values():
        suma = suma + int(i)
    print(suma)

suma_numere(cheie1=5, cheie2=20, cheie3=12)
suma_numere()
suma_numere(**{'cheie1':5, 'cheie2':20, 'cheie3':12})

numere = {'cheie1':5, 'cheie2':20, 'cheie3':12}
suma_numere(**numere)

# Exceptii
# Ex. 1
try:
    my_list = [23, 14, 55, 102, 30]
    print(my_list[5])
except:
    print('Nu avem suficiente valori in lista.')

# Ex. 2
try:
    my_list = [23, 14, 55, 102, 30]
    print(10/0)
    print(my_list[5])
except IndexError:
    print('Nu avem suficiente valori in lista.')
except ZeroDivisionError:
    print('Impartirea la zero nu e posibila.')

# Ex. 3
try:
    my_list = [23, 14, 55, 102, 30]
    print(my_list[4])
except:
    print('Nu avem suficiente valori in lista.')
else:
    print('Am gasit elementul.')

#Ex. 4
try:
    my_list = [23, 14, 55, 102, 30]
    print(my_list[2])
except:
    print('Nu avem suficiente valori in lista.')
else:
    print('Am gasit elementul.')
finally:
    print('Am terminat executia.')

#Ex. 5
if -1 < 0:
    raise Exception('Conditia nu e valida.')



