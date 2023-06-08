from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from links import *

# Глобальные переменные
LESSON_TEXT = (By.CSS_SELECTOR, ".step-inner  span")
LESSON_NAME = (By.CSS_SELECTOR, "div.top-tools__lesson-name")
LOGIN_BUTTON = (By.CSS_SELECTOR, ".navbar__auth_login")
EMAIL = "XXXXXXXXXXXXXXXXXXXXXXXXXXX"
PASSWORD = "XXXXXXXXXXXXXXX"

# Список теории из курса
LINKS_1 = [FirstTheory.links_1, FirstTheory.links_2, FirstTheory.links_3,
            FirstTheory.links_4, FirstTheory.links_6]
LINKS_2 = [SecondTheory.links_1, SecondTheory.links_2, SecondTheory.links_3, SecondTheory.links_4]
LINKS_3 = [ThirdTheory.links_1, ThirdTheory.links_2, ThirdTheory.links_3, ThirdTheory.links_4,
           ThirdTheory.links_5, ThirdTheory.links_6, ThirdTheory.links_8]
LINKS_4 = [ForthTheory.links_5, ForthTheory.links_3, ForthTheory.links_4, ForthTheory.links_5]

for links in LINKS_4:
    for steps in links.keys():
        with webdriver.Chrome() as browser:
            # Открываем браузер
            browser.get(links[steps])

            # Ждем пока можно будет войти
            WebDriverWait(browser, 20).until(EC.element_to_be_clickable(LOGIN_BUTTON))
            browser.find_element(By.CSS_SELECTOR, ".navbar__auth_login").click()

            # Вставляем свои данные и нажимаем кнопочку "Войти"
            browser.find_element(By.CSS_SELECTOR, '#id_login_email').send_keys(EMAIL)
            browser.find_element(By.CSS_SELECTOR, '#id_login_password').send_keys(PASSWORD)
            browser.find_element(By.XPATH, '//*[@id="login_form"]/button').click()
            sleep(10)

            # Переходим к уроку
            browser.get(links[steps])

            # Забираем только текст из урока + создаем название txt файла
            WebDriverWait(browser, 20).until(EC.presence_of_element_located(LESSON_TEXT))
            page_text = browser.find_element(*LESSON_TEXT).text
            page_name = browser.find_element(*LESSON_NAME).text
            if page_name.endswith("?"):
                page_name = page_name.removesuffix("?")
            text_file_name = f"{page_name}.txt"
            print(text_file_name)

            # Забираем внутренности текстового документа + создаём название md файла
            md_file_name = f'{page_name[0:3]}-{steps}.md'
            print(md_file_name)
            spans = browser.find_element(*LESSON_TEXT)
            inner = spans.get_attribute('innerHTML')

            with open(md_file_name, "+a", encoding="utf-8") as markdown, open(text_file_name , "+a", encoding="utf-8") as txt:
                markdown.write(inner)
                txt.write(f'{page_text}\n\n\n')
