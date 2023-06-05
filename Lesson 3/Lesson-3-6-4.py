from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "https://stepik.org/lesson/236895/step/1"
email = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
password = "XXXXXXXXXXXXXXXXXXX"

def test_guest_login(browser):
    # Открываем ссылку
    browser.get(link)
    
    # Ждем пока прогрузиться кнопка "Войти"
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, 'ember33')))
    browser.find_element(By.ID, 'ember33').click()

    # Вставляем свои данные и нажимаем кнопочку "Войти"
    browser.find_element(By.ID, 'id_login_email').send_keys(email)
    browser.find_element(By.ID, 'id_login_password').send_keys(password)
    browser.find_element(By.XPATH, '//*[@id="login_form"]/button').click()

