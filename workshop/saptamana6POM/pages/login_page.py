from selenium.webdriver.common.by import By

from saptamana6POM.pages.base_page import BasePage


class LoginPage(BasePage):
    MAIN_URL = "https://www.saucedemo.com/"
    TEXT_STANDARD_USER = "standard_user"
    TEXT_PASSWORD = "secret_sauce"
    INPUT_USERNAME = (By.ID, "user-name")
    INPUT_PASSWORD = (By.ID, "password")
    BUTTON_LOGIN = (By.ID, "login-button")
    H3_LOGIN_ERROR = (By.XPATH, "//h3[@data-test='error']")  # h3[data-test='error']

    def open(self):
        self.driver.get(self.MAIN_URL)

    def set_username(self, username):
        self.driver.find_element(*self.INPUT_USERNAME).send_keys(username)

    def set_password(self, password):
        self.driver.find_element(*self.INPUT_PASSWORD).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.BUTTON_LOGIN).click()

    def is_user_logged_in(self):
        return "inventory" in self.driver.current_url




