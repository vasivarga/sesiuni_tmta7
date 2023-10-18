from behave import *


@given(u'I am on login page')
def step_impl(context):
    print(u'STEP: Given I am on login page')
    context.base_page.navigate_to_login_page()


@when(u'I send a valid username')
def step_impl(context):
    print(u'STEP: When I send a valid username')
    context.login_page.send_valid_username()


@when(u'I send a valid password')
def step_impl(context):
    print(u'STEP: When I send a valid password')
    context.login_page.send_valid_password()


@when(u'I click on Login button')
def step_impl(context):
    print(u'STEP: When I click on Login button')
    context.login_page.click_login_button()


@then(u'A success message will be displayed on the screen')
def step_impl(context):
    print(u'STEP: Then A success message will be displayed on the screen')
    context.login_page.check_success_message()


@then(u'An error message will be displayed on the screen')
def step_impl(context):
    print(u'STEP: Then An error message will be displayed on the screen')
    context.login_page.check_error_message()


@when(u'I use an invalid "{username}" or "{password}"')
def step_impl(context, username, password):
    print(u'STEP: When I use an invalid "{username}" or "{password}"')
    context.login_page.send_invalid_username_or_password(username, password)
