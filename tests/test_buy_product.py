import allure
from selenium import webdriver

from pages.cart_page import Cart_page
from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.smartphone_page import Smartphone_page


@allure.description("Test buy product 1 online trade")
def test_buy_product1():
    driver = webdriver.Chrome(executable_path='D:\\Юра\\Тестировщик\\resource\\chromedriver.exe')
    print("Start test 1")

    mp = Main_page(driver)
    mp.start_buy()

    sp = Smartphone_page(driver)
    sp.filter_product()

    lp = Login_page(driver)
    lp.move_to_cart()

    cp = Cart_page(driver)
    cp.option_buy_and_checkout()


