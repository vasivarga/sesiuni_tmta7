# SUGESTII EXERCITII


# - Test 1:
# Intrati pe site-ul https://www.elefant.ro/
# - Test 2:
# cautati un produs la alegere (iphone 14) si verificati ca s-au returnat cel putin 10 rezultate ([class="product-title"])
# - Test 3: E
# xtrageti din lista produsul cu pretul cel mai mic [class="current-price "] (puteti sa va folositi de find_elements)
# - Test 4:
# Extrageti titlul paginii si verificati ca este corect
# - Test 5:
# Intrati pe site, accesati butonul cont si click pe conectare.
# Identificati elementele de tip user si parola si inserati valori incorecte
# (valori incorecte inseamna oricare valori care nu sunt recunoscute drept cont valid)
# - Dati click pe butonul "conectare" si verificati urmatoarele:
#              1. Faptul ca nu s-a facut logarea in cont
#             2. Faptul ca se returneaza eroarea corecta
# - Test 6:
# Stergeti valoarea de pe campul email si introduceti o valoare invalida
# (adica fara caracterul "@") si verificati faptul ca butonul "conectare" este dezactivat
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class ElefantTests(unittest.TestCase):
    cookie_button = (By.ID, 'CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll')


    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.elefant.ro/')
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_access_site(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located((By.ID, 'CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll')))
        self.driver.find_element(*self.cookie_button).click()
        # assert self.driver.find_element()