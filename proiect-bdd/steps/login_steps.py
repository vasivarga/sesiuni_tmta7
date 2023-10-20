from behave import *


@given('I am on the Login Page')
def step_impl(context):
    context.login_page.open()


@when('I enter an unregistered email')
def step_impl(context):
    context.login_page.set_email("tmta7@itfactory.ro")


@when('I click on the login button')
def step_impl(context):
    context.login_page.click_login_button()


@then('I should see "{message}" main error message')
def step_impl(context, message):
    assert context.login_page.is_main_error_message_displayed(), "The main error message is not displayed"
    assert message in context.login_page.get_main_error_message_text(), "The main error message does not contain the expected text"


@then('I should see "{message}" email error message')
def step_impl(context, message):
    assert context.login_page.is_email_error_message_displayed(), "The email error message is not displayed"
    assert message in context.login_page.get_email_error_message_text(), ("The email error message does not contain the expected text")


@when('I enter "{email_text}" as email')
def step_impl(context, email_text):
    context.login_page.set_email(email_text)


@then('The URL of the page is "{url}"')
def step_impl(context, url):
    context.login_page.is_url_correct(url), "The login page url is incorrect."