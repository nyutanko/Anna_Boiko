from behave import *
from ..main import OrangeHRMScraper


@given('started the driver')
def init_driver(context):
    OrangeHRMScraper.__init__()


@when('we loginned')
def login(context):
    OrangeHRMScraper.login()


@when('new job added')
def add_new_job(context):
    OrangeHRMScraper.add_new_job()


@then('job removed')
def remove_job(context):
    OrangeHRMScraper.remove_job()

