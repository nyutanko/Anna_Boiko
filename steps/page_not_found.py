from behave import *


@when("add to url non-existent {subdomain}")
def step_impl(context, subdomain):
    pass


@then('page "Error 404" will be loaded')
def step_impl(context):
    pass
