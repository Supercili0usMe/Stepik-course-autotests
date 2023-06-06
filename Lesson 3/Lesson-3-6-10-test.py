from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_add_to_basket_button(browser):
    # Открываем ссылку
    browser.get(link)   
    sleep(3)
    # Ищем кнопку добавления в корзину
    assert browser.find_elements(By.CSS_SELECTOR , '.btn-add-to-basket'), 'basket-button-not-found'
