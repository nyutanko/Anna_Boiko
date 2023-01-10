import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException

delay_to_load_page = 10
username = 'Admin'
password = 'admin123'
name = 'Anna Boiko'
description = 'A job description'
notes = 'Job notes'


class OrangeHRMScraper:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://opensource-demo.orangehrmlive.com/')
        print('Page loaded')

    def login(self):
        WebDriverWait(self.driver, delay_to_load_page).until(ec.presence_of_element_located(
            (By.XPATH, '//input[@name="username"]'))).send_keys(username)
        self.driver.find_element(By.XPATH, '//input[@name="password"]').send_keys(password)
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()

    def add_new_job(self):
        WebDriverWait(self.driver, delay_to_load_page).until(ec.presence_of_element_located(
            (By.XPATH, '//span[text()="Admin"]'))).click()

        WebDriverWait(self.driver, delay_to_load_page).until(ec.presence_of_element_located(
            (By.XPATH, '//span[contains(text(),"Job")]'))).click()
        self.driver.find_element(By.XPATH, '//a[contains(text(),"Job Titles")]').click()

        WebDriverWait(self.driver, delay_to_load_page).until(ec.presence_of_element_located(
            (By.XPATH, '//button[contains(.,"Add")]'))).click()

        WebDriverWait(self.driver, delay_to_load_page).until(ec.presence_of_element_located(
            (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/input'))).send_keys(name)
        self.driver.find_element(By.XPATH, "//textarea[@placeholder='Type description here']").send_keys(description)
        self.driver.find_element(By.XPATH, "//textarea[@placeholder='Add note']").send_keys(notes)
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()

    def remove_job(self):
        xpath_delete = f'//div[@role="row"][contains(.,"{name}")]//i[@class="oxd-icon bi-trash"]'
        WebDriverWait(self.driver, delay_to_load_page).until(ec.presence_of_element_located(
            (By.XPATH, '//div[@role="rowgroup"]')))
        self.driver.find_element(By.XPATH, xpath_delete).click()
        self.driver.find_element(By.XPATH, '//button[contains(.,"Yes, Delete")]').click()
        time.sleep(5)
        try:
            self.driver.find_element(By.XPATH, xpath_delete)
            assert 'Element not removed'
        except NoSuchElementException:
            print('Element removed')
            pass

        self.driver.close()


def main():
    scraper = OrangeHRMScraper()
    scraper.login()
    scraper.add_new_job()
    scraper.remove_job()


if __name__ == "__main__":
    main()
