import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger


class Main_page(Base):

    url = 'https://www.onlinetrade.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    catalog_button = "//div[@class='header__menuLink__icon']"
    smartphone_button = "// a[ @ href = '/catalogue/smartfony-c13/']"


    # Getters
    def get_catalog_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.catalog_button)))
    def get_smartphone_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.smartphone_button)))


    # Action
    def click_catalog_button(self):
        self.get_catalog_button().click()
        print("click catalog_button")

    def click_smartphone_button(self):
        self.get_smartphone_button().click()
        print("click smartphone_button")

    # Methods
    def start_buy(self):
        with allure.step("start buy"):
            Logger.add_start_step(method="start_buy")
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.click_catalog_button()
            self.click_smartphone_button()
            Logger.add_end_step(url=self.driver.current_url, method="start_buy")

        time.sleep(2)