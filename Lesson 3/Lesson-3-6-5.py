import time
import math
import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

final = ''

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()
    print(final)

email = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
password = "XXXXXXXXXXXXXXXXXXX"
links = [
         'https://stepik.org/lesson/236895/step/1',
         'https://stepik.org/lesson/236896/step/1',
         'https://stepik.org/lesson/236897/step/1',
         'https://stepik.org/lesson/236898/step/1',
         'https://stepik.org/lesson/236899/step/1',
         'https://stepik.org/lesson/236903/step/1',
         'https://stepik.org/lesson/236904/step/1',
         'https://stepik.org/lesson/236905/step/1'
         ]

@pytest.mark.parametrize('link', links)
def test_choice_link(browser, link):
    browser.get(link)

    # Ждем пока прогрузиться кнопка "Войти"
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, 'ember33')))
    browser.find_element(By.ID, 'ember33').click()

    # Вставляем свои данные и нажимаем кнопочку "Войти"
    browser.find_element(By.ID, 'id_login_email').send_keys(email)
    browser.find_element(By.ID, 'id_login_password').send_keys(password)
    browser.find_element(By.XPATH, '//*[@id="login_form"]/button').click()
    sleep(4)

    # Вставляем данные в поле ввода
    browser.find_element(By.TAG_NAME, 'textarea').send_keys(f'{math.log(int(time.time()))}')
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.attempt__actions button')))
    browser.find_element(By.CSS_SELECTOR, '.attempt__actions button').click()
        
    # Получаем текст из выходного сообщения
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.smart-hints > p')))
    text = browser.find_element(By.CSS_SELECTOR, '.smart-hints > p').text

    try:
        assert text == "Correct!"
    except AssertionError:
        final += text
