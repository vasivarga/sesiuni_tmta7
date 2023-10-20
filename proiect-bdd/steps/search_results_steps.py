from behave import *


@given('I am on the home page')
def step_impl(context):
    context.home_page.open()


@when('I type "{product_name}" in the search box')
def step_impl(context, product_name):
    context.home_page.type_on_search_box(product_name)


@when('I click on the search button')
def step_impl(context):
    context.home_page.click_search_button()


@then('I should see at least "{x}" results')
def step_impl(context, x):
    assert context.search_results_page.is_products_list_size_at_least(x), "Search results size smaller than expected"