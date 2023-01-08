from behave import *


@when("clicked on {tab}")
def step_impl(context, tab):
    pass


@then('"https://www.epam.com/{tab}" will be loaded')
def step_impl(context, tab):
    pass
