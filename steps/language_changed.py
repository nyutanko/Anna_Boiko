from behave import *


@when('press "Global (EN)" button')
def step_impl(context):
    pass


@step("select {language}")
def step_impl(context, language):
    pass


@then("page in {language} will be loaded")
def step_impl(context, language):
    pass
