from browser import Browser
from pages.base_page import BasePage
from pages.login_page import LoginPage


def before_all(context):
    context.browser = Browser()
    context.base_page = BasePage()
    context.login_page = LoginPage()



def after_all(context):
    context.browser.close()
