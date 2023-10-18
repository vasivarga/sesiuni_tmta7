from browser import Browser


class BasePage(Browser):
    def navigate_to_login_page(self):
        self.driver.get('https://the-internet.herokuapp.com/login')