import time


import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.logger import Logger
from base.base_class import Base


class Cart_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    button_select_city = "//div[@id='basket_pickup__ID']//a[@data-handlermode='cityselectnew']"
    select_balashika_city = "//a[@title='Балашиха' and @class='js__cityselectclickdesc ']"
    select_pickup_point_galion = "//label[@for='shipmentradio103']"
    select_payment_method_cash = "//label[@for='paymentradio1']"
    button_checkout = "//input[@type='submit' and @name='submit']"

    # Getters
    def get_button_select_city(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.button_select_city)))

    def get_select_balashika_city(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.select_balashika_city)))

    def get_select_pickup_point_galion(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.select_pickup_point_galion)))

    def get_select_payment_method_cash(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.select_payment_method_cash)))

    def get_button_checkout(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.button_checkout)))

    # Action
    """Выбираем опции по городу, доставке, оплате"""
    def click_button_select_city(self):
        self.get_button_select_city().click()
        print("click button_select_city")

    def click_select_balashika_city(self):
        self.get_select_balashika_city().click()
        print("click select_balashika_city")

    def click_select_pickup_point_galion(self):
        self.get_select_pickup_point_galion().click()
        print("click select_pickup_point_galion")

    def click_select_payment_method_cash(self):
        self.get_select_payment_method_cash().click()
        print("click select_payment_method_cash")

    def click_button_checkout(self):
        self.get_button_checkout().click()
        print("click button_checkout")


    # Methods
    def option_buy_and_checkout(self):
        with allure.step("option buy and checkout"):
            Logger.add_start_step(method="option_buy_and_checkout")
            self.click_button_select_city()
            self.click_select_balashika_city()
            self.click_select_pickup_point_galion()
            self.click_select_payment_method_cash()
            #self.click_button_checkout() #выключено, чтобы не создавать тестовый заказ
            Logger.add_end_step(url=self.driver.current_url, method="option_buy_and_checkout")
