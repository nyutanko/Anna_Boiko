from selenium import webdriver
from src.pages.homepage import Homepage


def test_browserstack():
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/")

    homepage = Homepage(driver)
    sign_in_page = SignInPage(driver)

    homepage.click_sign_in()

    sign_in_page.select_username()
    sign_in_page.select_password()
    sign_in_page.click_login()
    homepage.get_username()
    driver.quit()
