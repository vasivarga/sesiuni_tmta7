import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

LINK = "https://formy-project.herokuapp.com/form"

driver.get(LINK)
time.sleep(1)
driver.maximize_window()

element = driver.find_element(By.ID, "first-name")
print(f"Tipul elementului gasit cu find_element este: {type(element).__name__}")

# find_elements()
element_list = driver.find_elements(By.TAG_NAME, "input")
print(f"Elementul gasit cu find_elements este: {type(element_list).__name__}")

print(len(element_list))

element_list[0].send_keys("Popescu")
element_list[1].send_keys("Ion")
element_list[2].send_keys("Automation Tester")
element_list[3].click()
element_list[4].click()
element_list[5].click()
element_list[6].click()
element_list[7].click()
element_list[8].click()
time.sleep(5)

lista_optiuni = driver.find_elements(By.TAG_NAME, "option")
print(f"Elementul gasit cu find_elements este: {type(lista_optiuni).__name__}")
print(len(lista_optiuni))

print("Optiunile de pe dropdown sunt:")

for optiune in lista_optiuni:
    print(f"Elementul curent este un {type(optiune).__name__}")
    print(f"Optiunea are textul {optiune.text}")

# Returneaza o eroare NoSuchElementException
# driver.find_element(By.ID, "ID_INEXISTENT")

lista = driver.find_elements(By.ID, "ID_INEXISTENT")
print(lista)

print(element_list[0].get_attribute("placeholder"))