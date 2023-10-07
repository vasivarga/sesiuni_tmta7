import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

# Vedem din ce tip de data are variabila driver
# type() combinat cu __name__ ne va da exact clasa
print(type(driver).__name__)

LINK = "https://formy-project.herokuapp.com/form"

# Navigam la link-ul dorit
driver.get(LINK)

# Asteptam 1 secunda sa se incarce pagina
time.sleep(1)

# Maximizam fereastra
driver.maximize_window()

# ######## INTERACTIUNEA CU DROPDOWNURI ########

# ### Dropdownuri uzuale, vechi/clasice, cu tag-ul <select> ###

"""
Orice dropdown care are tag-ul HTML <select> este un dropdown clasic.
Pentru a putea interactiona cu un dropdown clasic, este nevoie sa folosim clasa Select din Selenium:

Pasul 1 - Gasim selectorul dropdownului in pagina HTML. 
FOARTE IMPORTANT: trebuie sa fie elementul cu tag-ul <select>
ex: 
- "//select[@id='select-menu']" -xpath 
- "select#select-menu" - css
- etc..

Pasul 2 - Initializam o variabila (obiect) din clasa Select
Pasul 3 - In constructorul clasei Select, punem WebElement-ul cu tag-ul <select>
Pasul 4 - Apelam una din metodele specifice dropdownului (select_by_visible_text, select_by_index, select_by_value)
"""

# Pasul 1 - am identificat un dropdown cu id-ul "select-menu" si il salvam in variabila dropdown_element,
# care va fi un WebElement
dropdown_element = driver.find_element(By.ID, "select-menu")
print(type(dropdown_element).__name__)

# Pasul 2: initializam obiectul years_of_experience din clasa Select
# Pasul 3: Select primeste in constructor WebElementul care reprezinta dropdownul nostru
years_of_experience = Select(dropdown_element)

# Pasul 4: Apelam pe rand fiecare metoda de selectare de pe dropdown

# Dupa text
years_of_experience.select_by_visible_text("2-4")
time.sleep(2)

# Dupa index
years_of_experience.select_by_index(0)
time.sleep(2)

# Dupa atributul "value" din HTML
years_of_experience.select_by_value("4")
time.sleep(2)

# ### Dropdownuri moderne care nu au tag-ul HTML ###
"""
Dropdownurile care nu au tagul HTML <select>, sunt mai moderne si apartin de frameworkuri avansate de design web.
De obicei o aplicatie foloseste acelasi tip de dropdown in toate paginile sale.
In functie de aplicatia pe care o testam, e nevoie sa identificam elementele principale a dropdownului, la modul general,
apoi putem sa facem o funtie generica care se poate aplica oricarui dropdown
"""

# Navigam la o pagina cu un dropdown atipic
driver.get("https://formy-project.herokuapp.com/dropdown")
time.sleep(1)

"""
Orice dropdown se deschide daca facem click pe el, deci functia pe care o construim va primi ca parametru 
un WebElement care reprezinta dropdownul de pe care vrem sa selectam.

Apoi ne uitam in HTML la modul in care sunt construite optiunile dropdownului pe care le putem selecta.

Observam ca fiecare optiune poate fi reprezentata printr-un locator de forma:
    
    //div[@class ='dropdown-menu show']//a[contains(text(), 'TEXTUL_OPTIUNII_DORITE')]

Deci functia noastra primeste ca al doilea parametru textul optiunii pe care dorim sa o selectam.

Initializam un WebElement cu locatorul generalizat.
Elementul va fi construit folosind doilea parametru a functiei, ca sa identifice optiunea dupa textul dat.
"""


# Incepem sa construim functia
# la primul parametru am specificat ca este WebElement ca sa putem accesa functiile acestuia
def select_dropdown_option_by_text(element_dropdown: WebElement, text):
    # facem click pe elementul care reprezinta dropdownul:
    element_dropdown.click()
    time.sleep(1)
    # construim locatorul otpiunii pe baza textului primit ca parametru:
    option = driver.find_element(By.XPATH, f"//div[@class ='dropdown-menu show']//a[contains(text(), '{text}')]")
    # facem click pe optiune:
    option.click()



# De fiecare data cand selectam ceva pe dropdown suntem mutati pe o alta pagina
# La revenirea pe pagina anterioara, dropdownu se va reincarca, deci este nevoie sa-l construim iarasi
# Altfel programul ne va da eroare
dropdown_modern_1 = driver.find_element(By.ID, "dropdownMenuButton")

select_dropdown_option_by_text(dropdown_modern_1, "File Upload")
time.sleep(2)
driver.back()

dropdown_modern_2 = driver.find_element(By.ID, "dropdownMenuButton")
select_dropdown_option_by_text(dropdown_modern_2, "Buttons")
time.sleep(2)
driver.back()

dropdown_modern_3 = driver.find_element(By.ID, "dropdownMenuButton")
select_dropdown_option_by_text(dropdown_modern_3, "Drag and Drop")
time.sleep(2)
driver.back()
time.sleep(2)
