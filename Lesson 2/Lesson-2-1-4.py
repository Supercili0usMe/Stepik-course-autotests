import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

with webdriver.Chrome() as browser:
    browser.get('https://suninjuly.github.io/math.html')
    sleep(1)
    # Поиск числа
    x_element = browser.find_element(By.XPATH, "//*[@id='input_value']")
    x = x_element.text
    print(x)
    y = calc(x)
    
    # Отправка полученного значения
    set_y = browser.find_element(By.XPATH, '//*[@id="answer"]')
    set_y.send_keys(y)

    # Работа с чек-боксами
    browser.find_element(By.XPATH, '//*[@id="robotCheckbox"]').click()
    browser.find_element(By.XPATH, '//*[@id="robotsRule"]').click()

    # Нажимаем кнопочку
    browser.find_element(By.XPATH, "//button").click()
    sleep(5)