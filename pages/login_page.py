import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger


class Login_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    #button_continue_no_reg = "//a[text()='Продолжить без регистрации']"
    button_continue_no_reg = "//a[@href='/basket.html']"

    # Getters
    def get_button_continue_no_reg(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.button_continue_no_reg)))

    # Action
    def click_button_continue_no_reg(self):
        self.get_button_continue_no_reg().click()
        print("click button_continue_no_reg")


    # Methods
    def move_to_cart(self):
        with allure.step("move to cart"):
            Logger.add_start_step(method="move_to_cart")
            self.click_button_continue_no_reg()
            Logger.add_end_step(url=self.driver.current_url, method="move_to_cart")
