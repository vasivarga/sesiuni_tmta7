import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
LINK = "https://formy-project.herokuapp.com/form"

driver.get(LINK)
time.sleep(1)

driver.maximize_window()


# ################# XPATH-uri cu "axis navigation" sau "rudenii" intre elemente #################

"""
Sintaxa generala:
//<elementul_din_care_pornim>/<axis_sau_rudenia_dintre_elemente>::<elementul_cautat>
"""

# ancestor	        - selecteaza toti stramosii elementului din care pornim (parinti, parintii parintilor, etc) - IN SUS
# parent	        - selecteaza STRICT parintele elementului din care pornim - IN SUS
# descendant	    - selecteaza toti descendentii (copiii, copiii copiilor) elementului din care pornim - IN JOS
# child	            - selecteaza toti copii nodului (elementului) din care pornim - IN JOS
# following-sibling	- selecteaza "fratii" urmatori ai elementului din care pornim - ACELASI NIVEL
# preceding-sibling	- selecteaza "fratii" precedenti ai elementului din care pornim - ACELASI NIVEL


# EXEMPLE:

# ############################## ancestor

# Stramosii <strong> al elementului <label> cu textul ='First name'
driver.find_element(By.XPATH, "//label[@for='first-name']/ancestor::strong")

# TOTI stramosii elementului <label> cu textul ='First name' (caracterul * selecteaza tot)
driver.find_element(By.XPATH, "//label[text()='First name']/ancestor::*")

#  ############################## parent

# Parintele elementului <label> cu textul ='First name' (cu sau fara tag specificiat)
driver.find_element(By.XPATH, "//label[text()='First name']/parent::strong")
driver.find_element(By.XPATH, "//label[text()='First name']/parent::*")

#  ############################## descendant

# Toti descendentii elementului <div> avand clasa 'input-group', indiferent de tip
driver.find_element(By.XPATH, "//div[@class='input-group']/descendant::*")

# Toti descendentii elementului <div> avand clasa 'input-group' care unt de tip <input>
driver.find_element(By.XPATH, "//div[@class='input-group']/descendant::input")

# Toti copiii elementului <div> cu clasa 'input-group' care sunt si ei de tipul <div>
driver.find_element(By.XPATH, "//div[@class='input-group']/child::div")

#  ############################## following-sibling

# cauta toti fratii de dupa elementul //option[2] care sunt de tipul <option>
print(len(driver.find_elements(By.XPATH, "//option[2]/following-sibling::option")))

#  ############################## preceding-sibling

# cauta toti fratii dinaintea elementul //option[2] care sunt de tipul <option>
print(len(driver.find_elements(By.XPATH, "//option[2]/following-sibling::option")))