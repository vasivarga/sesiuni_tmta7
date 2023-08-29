print("Hello world")

person_name = "John"
print(person_name)

person_name = 1
print(person_name)

# un comentariu pe o singura linie
"""
comentarii pe mai multe linii
"""

x, y, z = 1, 2, 3
# la fel cu a declara
# x=1
# y=2
# z=3
print(x, y, z)

has_type = type(person_name)
print(has_type)

print(type(person_name))
print(type(y))

person_name = "Popescu"
# converted_person_name = int(person_name)
# print(int(person_name))

a = "2"
b = "3"
print(a + b)  # concatenare
print(int(a) + int(b))  # adunare

a = int(a)
b = int(b)
print(a + b)
print(str(a) + str(b))

# printare prin concatenare si type casting pt int
print(person_name + " " + str(x) + " un text aleatoriu")

# printare cu formatare
print(f"{person_name} un text aleatoriu")

assert 1 + 2 == 3
# assert 1 + 2 == 4, f"Expected {1 + 2}; Actual: 4"

user = input("Please introduce username: ")
print(user)

number = input("Please introduce number: ")
print(int(number) + 3)
assert int(number) + 3 > 0
