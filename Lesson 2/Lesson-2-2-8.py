from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import os 

# Создаём путь к файлу
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')

with webdriver.Chrome() as browser:
    # Открываем страницу
    browser.get('http://suninjuly.github.io/file_input.html')
    sleep(1)

    # Вводим обязательные данные
    browser.find_element(By.NAME, 'firstname').send_keys('Стас')
    browser.find_element(By.NAME, 'lastname').send_keys('Барецкий')
    browser.find_element(By.NAME, 'email').send_keys('stasbareckyi@ya.ru')

    # Загрузка файла
    browser.find_element(By.NAME, 'file').send_keys(file_path)

    # Тыкаем кнопочку
    browser.find_element(By.XPATH, "//button").click()
    sleep(5)
