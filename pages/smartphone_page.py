import time

import allure
from selenium.common import TimeoutException
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.logger import Logger
from base.base_class import Base


class Smartphone_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    button_choice_price = "//div[@data-spoiledcontent='price_active']"
    min_price_cell = "//input[@id='price1']"
    max_price_cell = "//input[@id='price2']"
    pick_up_button = "//a[@class='button button__blue js__filterResult_link']"
    #number_visible_goods = "//div[@class='percount']" #"показать" 15 30 45 позиций
    listing_item = "//select[@id='js__listingSort_ID']" #Сортировка по признаку
    buy_button_page_item = "//a[@class='button button__orange  js__ajaxExchange']"
    button_diagonal = "//div[@data-spoiledcontent='diagonal_active']"
    min_diagonal_slider = "//div[@id='diagonal_ID']/span[contains(@class,'ui-state-default')][1]"
    max_diagonal_slider = "//div[@id='diagonal_ID']/span[contains(@class,'ui-state-default')][2]"
    button_availability = "//div[@data-spoiledcontent='selling_active']"
    check_box_stock = "//label[@id='l5950a4a1de00bc24202c5f78a0a726be']"
    button_cart = "//span[@class='ic__set ic__set__multicartWhite']"
    button_buy_a33w = "//div[@class='indexGoods__item__dataCover']//a[@data-itemid='2327320']"



    # Getters
    def get_button_choice_price(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.button_choice_price)))

    def get_min_price_cell(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.min_price_cell)))

    def get_max_price_cell(self):
         return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.max_price_cell)))

    def get_pick_up_button(self):
         return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.pick_up_button)))

    # def get_number_visible_goods(self):
    #      return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.number_visible_goods)))

    def get_listing_item(self):
         return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.listing_item)))

    def get_buy_button_page_item(self):
         return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.buy_button_page_item)))

    def get_min_diagonal_slider(self):
         return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.min_diagonal_slider)))

    def get_max_diagonal_slider(self):
         return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.max_diagonal_slider)))

    def get_button_availability(self):
         return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.button_availability)))

    def get_check_box_stock(self):
         return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.check_box_stock)))

    def get_button_diagonal(self):
         return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.button_diagonal)))

    def get_button_cart(self):
         return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.button_cart)))

    def get_button_buy_a33w(self):
         return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.button_buy_a33w)))

    # Action
    '''ставим Фильтр по цене'''

    def input_min_price_cell(self, min_price):
        try:
            self.get_min_price_cell().click()
            time.sleep(1)
            self.get_min_price_cell().send_keys(Keys.CONTROL + "a")
            self.get_min_price_cell().send_keys(Keys.BACKSPACE)
            print("clear min price")
            self.get_min_price_cell().send_keys(min_price)
            print("input min price")
        except TimeoutException:
            self.get_button_choice_price().click() #Если фильтр по цене не активен, то нажимаем на него для активации
            print("Нажмаем кнопку Выбор по цене")
            self.get_min_price_cell().click()
            time.sleep(1)
            self.get_min_price_cell().send_keys(Keys.CONTROL + "a")
            self.get_min_price_cell().send_keys(Keys.BACKSPACE)
            print("clear min price")
            self.get_min_price_cell().send_keys(min_price)
            print("input min price")

    def input_max_price_cell(self, max_price):
        try:
            self.get_max_price_cell().click()
            time.sleep(1)
            self.get_max_price_cell().send_keys(Keys.CONTROL + "a")
            self.get_max_price_cell().send_keys(Keys.BACKSPACE)
            print("clear max price")
            self.get_max_price_cell().send_keys(max_price)
            print("input max price")
        except TimeoutException:
            self.get_button_choice_price().click() #Если фильтр по цене не активен, то нажимаем на него для активации
            print("Нажимаем кнопку Выбор по цене")
            self.get_max_price_cell().click()
            time.sleep(1)
            self.get_max_price_cell().send_keys(Keys.CONTROL + "a")
            self.get_max_price_cell().send_keys(Keys.BACKSPACE)
            print("clear max price")
            self.get_max_price_cell().send_keys(max_price)
            print("input max price")

    '''Ставим фильтр-слайдер по диагонале (размер экрана продукта)'''
    def move_min_diagonal_slider(self, x, y):
        try:
            ActionChains(self.driver).click_and_hold(self.get_min_diagonal_slider()).move_by_offset(x, y).release().perform()
            print("input min_diagonal")
        except TimeoutException:
            self.get_button_diagonal().click() #Если фильтр по диагонали не активен, то нажимаем на него для активации
            ActionChains(self.driver).click_and_hold(self.get_min_diagonal_slider()).move_by_offset(x, y).release().perform()
            print("input min_diagonal")

    def move_max_diagonal_slider(self, x, y):
        try:
            ActionChains(self.driver).click_and_hold(self.get_max_diagonal_slider()).move_by_offset(x, y).release().perform()
            print("input max_diagonal")
        except TimeoutException:
            self.get_button_diagonal().click() #Если фильтр по диагонале не активен, то нажимаем на него для активации
            ActionChains(self.driver).click_and_hold(self.get_max_diagonal_slider()).move_by_offset(x, y).release().perform()
            print("input max_diagonal")


    '''Ставим фильтр по наличию товара'''
    def click_check_box_stock(self):
        try:
            self.get_check_box_stock().click()
            print("click check_box")
        except TimeoutException:
            self.get_button_availability().click() #Если фильтр по наличию товара не активен, то нажимаем на него для активации
            print('click button availability')
            self.get_check_box_stock().click()
            print("click check_box")


    '''Приминяем выбраные фильтры'''
    def click_pick_up_button(self):
        self.get_pick_up_button().click()
        print("input pick up button")

    '''Кладем в корзину определенный товар'''
    def click_button_buy_a33w(self):
        self.get_button_buy_a33w().click()
        print("move in cart phone а33w")
        self.driver.refresh()
        print("refresh page")

    """Блок выбор первого товара в списке (если определенный товар не выпал в поиске)"""
    '''Выбираем первый смартфон (предмет) на экране'''
    def move_mouse_and_click_to_1_item(self, x, y):
        ActionChains(self.driver).send_keys(Keys.PAGE_UP).perform()
        ActionChains(self.driver).move_to_element(self.get_listing_item()).send_keys(Keys.PAGE_DOWN).move_by_offset(x, y).click().perform()
        print("click item (product) 1")


    '''Кликаем купить в сплывающем окне и сбрасывем (закрываем) его'''
    def click_buy_button_page_item(self):
        self.get_buy_button_page_item().click()
        print("move item (product) 1 to cart")
        self.driver.refresh()

    '''Переходим в корзину'''
    def click_button_cart(self):
        self.get_button_cart().click()
        print('click icon cart, move to login_page or to cart_page')


    # Methods
    def filter_product(self):
        with allure.step("filter product"):
            Logger.add_start_step(method="filter_product")
            self.input_min_price_cell('15000')
            self.input_max_price_cell('50000')
            self.move_min_diagonal_slider('20', '0')
            self.move_max_diagonal_slider('-40', '0')
            self.click_check_box_stock()
            time.sleep(2)
            self.click_pick_up_button()
            try:
                self.click_button_buy_a33w()
            except TimeoutException:
                self.move_mouse_and_click_to_1_item('0','-235')
                self.click_buy_button_page_item()
                self.driver.back()
                print('return_previous_page')
            time.sleep(1)
            self.click_button_cart() #переход на страницу Логин, если авторизация не пройдена
            Logger.add_end_step(url=self.driver.current_url, method="filter_product")



        time.sleep(10)
