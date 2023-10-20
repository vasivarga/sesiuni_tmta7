from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from browser import Browser


class BasePage(Browser):
    _INPUT_SEARCH = (By.ID, "small-searchterms")
    _BUTTON_SEARCH = (By.CLASS_NAME, "search-box-button")

    # #### METODE AJUTATOARE CARE TIN DE INTERACTIUNEA CU TOATE ELEMENTELE ####

    # Functie care cauta si returneaza un Web Element dupa un locator dat
    def find(self, locator):
        return self.driver.find_element(*locator)

    # Functie care cauta si returneaza o lista cu Web Elements dupa un locator dat (sub forma de tuplu)
    # Daca nu gaseste nimic, va returna o lista goala
    def find_all(self, locator):
        return self.driver.find_elements(*locator)

    # Functie care face click pe un Web Element
    def click(self, locator):
        # self.driver.find_element(*locator).click()
        self.find(locator).click()

    # Functie care scrie pe un Web Element
    # Primeste 2 parametri:
    # locator - locatorul elementului pe care se va scrie (sub forma de tuplu)
    # text - textul care urmeaza a fi scris
    def type(self, locator, text):
        self.find(locator).send_keys(text)

    # Functie care returneaza textul de pe un Web Element
    # Primeste 1 parametru:
    # locator - locatorul elementului de pe care va returna textul
    def get_text(self, locator):
        return self.find(locator).text

    # va returna True daca URL-ul paginii curente este egal cu
    # URL-ul paginii din care apelam metoda
    def is_url_correct(self, url):
        return self.driver.current_url == url

    # Functie care selecteaza o optiune de pe un dropdown dupa textul dat.
    # Functia are 2 parametri:
    # locator - locatorul dropdown-ului (sub forma de tuplu)
    # text - textul optiunii pe care vrem sa o selectam
    def select_dropdown_option_by_text(self, locator, text):
        dropdown_element = self.find(locator)
        select = Select(dropdown_element)
        select.select_by_visible_text(text)

    # Functie care selecteaza (bifeaza) un checkbox
    def check_checkbox(self, locator):
        checkbox = self.find(locator)

        # daca checkbox-ul NU este selectat (bifat), va da click pe el
        if not checkbox.is_selected():
            self.click(checkbox)

    # Functie care deselecteaza (debifeaza) un checkbox
    def uncheck_checkbox(self, locator):
        checkbox = self.find(locator)

        # daca checkbox-ul este selectat (bifat), va da click pe el
        if checkbox.is_selected():
            self.click(checkbox)

    # #### METODE DE INTERACTIUNE CU ELEMENTELE COMUNE (CARE APAR PE TOATE PAGINILE) ####
    def type_on_search_box(self, text):
        self.type(self._INPUT_SEARCH, text)

    def click_search_button(self):
        self.click(self._BUTTON_SEARCH)
