from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep

with webdriver.Chrome() as browser:
    # Открываем страницу
    browser.get("http://suninjuly.github.io/selects2.html")
    sleep(1)

    # Вычисляем сумму
    summ = int(browser.find_element(By.XPATH, '//*[@id="num1"]').text) + int(browser.find_element(By.XPATH, '//*[@id="num2"]').text)
    
    # Ищем строку с полученной суммой
    select = Select(browser.find_element(By.TAG_NAME, 'select'))
    select.select_by_value(f'{summ}')

    # Нажимаем кнопочку
    browser.find_element(By.XPATH, "//button").click()
    sleep(5)