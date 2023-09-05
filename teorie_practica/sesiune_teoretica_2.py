first_list = [1, 2, 8, 5, 10]
print(first_list[1])
print(first_list[3])
print(first_list[len(first_list)-1])  # pt. a afla ultimul element din lista

# Sort - pt. liste ce contin elem. de acelasi tip (numeric, float, string)
first_list.sort()  # ordonare crescatoare
print(first_list)

# Reverse
first_list.reverse()  # ordonare descrescatoare
print(first_list)

# Sum
print(sum(first_list))

# Remove - Delete an item
first_list.remove(1)
print(first_list)

# Pop - stergem un element la un index specific sau ultimul elem din lista
first_list.pop(1)
first_list.pop()
print(first_list)

# Insert - adaugam elem.
first_list.insert(1, "Ana")
print(first_list)
first_list.insert(len(first_list), True)  # adaugam elem. pe ultima pozitie
print(first_list)

# Append - adaugam elem. la finalul listei
first_list.append(15.5)
print(first_list)

# Count - cate aparitii are un elem. in lista
print(first_list.count(5))

# Pt. a copia o lista in alta lista
# second_list = first_list  # ASA NU
# second_list.insert(2, "Andrei")
# print(first_list)
# print(second_list)

third_list = first_list.copy()
print(third_list)
third_list[1] = "soare"
print(third_list, first_list)  # pt. a printa mai multe liste simultan


# Set

first_set = {"pepene", 15, True, "Maria", 203.62, "pepene"}
print(first_set)

# Remove - sterge un elem. specific
first_set.remove("pepene")
print(first_set)

# Add - pt. a adauga un elem.
first_set.add("pepene")
print(first_set)

# print(first_set[0])
# print(first_set)

duplicate_list = [1, 1, 1, 2, 2, 2, 3, 3]
print(set(duplicate_list))  # lista transformata in set
print(list(set(duplicate_list)))  # lista trans. in set, apoi transformat iarasi in lista

# Tuple
first_tuple = (False, 155, 2000.11, "Mari", "Marian", 155)
print(first_tuple) # accepta valori duplicate
print(first_tuple[2])
# first_tuple[2] = 45
# print(first_tuple)

# Dictionar
first_dict = {1:"mare", "cer":"albastru", True:"vara", 5.12:123}
print(first_dict)
print(first_dict[1])
print(first_dict["cer"])
print(first_dict[5.12])

# Modicam valoare
first_dict["cer"] = "inorat"
print(first_dict["cer"])
first_dict.update({"blabla":"da"})
print(first_dict)

# Pop - elimina val. aflata la cheia respectiva
first_dict.pop("blabla")
print(first_dict)

second_dict = {"user1":"admin",
               "user2":"Petru",
               "user3":{"name":"John", "email":"john@email.com"}}
print(second_dict["user3"])
print(second_dict["user3"]["name"])

third_dict = {"elev1":"Mihai",
              "elev2":"Georgiana",
              "elev3":["Ana", "Andrei", "Barbu"]}
print(third_dict["elev3"])
print(third_dict["elev3"][1])




