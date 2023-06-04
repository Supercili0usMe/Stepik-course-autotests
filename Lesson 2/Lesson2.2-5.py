import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

with webdriver.Chrome() as browser:
    # Открываем страницу
    browser.get('https://suninjuly.github.io/execute_script.html')
    sleep(1)

    # Ищем результат функции
    x = browser.find_element(By.XPATH, "//*[@id='input_value']").text
    y = calc(x)

    # Отправляем полученное значение
    browser.find_element(By.XPATH, '//*[@id="answer"]').send_keys(y)

    # Двигаем страницу на 100 пикселей вниз
    browser.execute_script("window.scrollBy(0, 100);")

    # Тыкаем кнопочки
    browser.find_element(By.XPATH, '//*[@id="robotCheckbox"]').click()
    browser.find_element(By.XPATH, '//*[@id="robotsRule"]').click()
    browser.find_element(By.XPATH, "//button").click()
    sleep(5)