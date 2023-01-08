from behave import *

use_step_matcher("re")


@given('"https://www.epam.com/" is opened')
def step_impl(context):
    pass


@when("press F5 key")
def step_impl(context):
    pass


@then('"https://www.epam.com/" will be reloaded')
def step_impl(context):
    pass
