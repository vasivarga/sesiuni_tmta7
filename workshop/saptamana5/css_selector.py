import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# ################ CSS SELECTOR
"""
simbolul * - selecteaza toate elementele
sintaxa #idElement  - selecteaza elementul cu id-ul "idElement"
.button - selecteaza elementele care au clasa "button"
.button.primary - selecteaza elementele care au atat clasa "button" cat si clasa "primary"
input  - selecteaza toate elementele de tip input
div input -  selecteaza toate elementele de tip input care se afla intr-un div (div-ul nu e neaparat parinte)
div > input - selecteaza toate elementele de tip input unde parintele e un div
div + input - selecteaza primul element input care urmeaza dupa un element div (pe acelasi nivel - adica sunt frati)
"""

driver = webdriver.Chrome()

driver.get("https://formy-project.herokuapp.com/form")

# ##### Acelasi element cu CSS-uri diferite

# CSS doar cu ID
first_name_cu_id_css = driver.find_element(By.CSS_SELECTOR, "#first-name")

# CSS cu tag si ID
first_name_cu_tag_si_id = driver.find_element(By.CSS_SELECTOR, "input#first-name")

# tag si ID, de data asta ca id-ul e mentionat la fel ca orice alt atribut si fara #
first_name_cu_tag_si_atribut = driver.find_element(By.CSS_SELECTOR, "input[id='first-name']")

# selector_element_inexistent = driver.find_element(By.CSS_SELECTOR, "input[id='inexistent']")


# tag si atributul placeholder
first_name_cu_tag_si_atribut_placeholder_css = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Enter first name"]')

# tag cu clasa si atributul id
first_name_cu_tag_clasa_si_id = driver.find_element(By.CSS_SELECTOR, 'input.form-control[id="first-name"]')

# element cu tag-ul input si atributul type = radio
radio_cu_atribut_type_radio = driver.find_element(By.CSS_SELECTOR, "input[type='radio']")

time.sleep(3)


driver.quit()



