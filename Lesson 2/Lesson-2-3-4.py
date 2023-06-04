import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

with webdriver.Chrome() as browser:
    # Открываем страницу
    browser.get('http://suninjuly.github.io/alert_accept.html')
    sleep(1)

    # Нажимаем кнопочку
    browser.find_element(By.XPATH, '//button').click()

    # Соглашаемся с alert
    browser.switch_to.alert.accept()

    # Ищем результат функции
    x = browser.find_element(By.XPATH, "//*[@id='input_value']").text
    y = calc(x)

    # Отправляем полученное значение
    browser.find_element(By.XPATH, '//*[@id="answer"]').send_keys(y)
    
    # Тыкаем кнопочку
    browser.find_element(By.XPATH, "//button").click()
    sleep(5)