import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from time import sleep

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

with webdriver.Chrome() as browser:
    # Открываем страницу
    browser.get('http://suninjuly.github.io/explicit_wait2.html')

    # Создаём задержку и кликаем на кнопку
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    browser.find_element(By.ID, 'book').click()

    # Прокручиваем страницу вниз до конца
    browser.execute_script("window.scrollBy(0, 400);")

    # Ищем результат функции
    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)

    # Отправляем полученное значение
    browser.find_element(By.ID, 'answer').send_keys(y)
    
    # Тыкаем кнопочку
    browser.find_element(By.ID, "solve").click()
    sleep(5)