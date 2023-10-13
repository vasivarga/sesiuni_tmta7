import unittest

from saptamana6POM.pages.login_page import LoginPage


class LoginPageTest(unittest.TestCase):

    def setUp(self) -> None:
        self.login_page = LoginPage()
        self.login_page.open()

    def tearDown(self) -> None:
        self.login_page.driver.quit()

    def test_valid_login(self):
        self.login_page.set_username("standard_user")
        self.login_page.set_password("secret_sauce")
        self.login_page.click_login_button()
        assert self.login_page.is_user_logged_in(), "Error, bad login"


