from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest
from numpy.random import randint 

class Tests(unittest.TestCase):
    def test1(self):
        # Открываем сайт
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        
        # Заполняем строки
        inputs = browser.find_element(By.XPATH, "//div[@class='first_block']/div[contains(@class, 'first')]//input")
        inputs.send_keys(f"{randint(1, 100)}")
        inputs = browser.find_element(By.XPATH, "//div[@class='first_block']/div[contains(@class, 'second')]//input")
        inputs.send_keys(f"{randint(1, 100)}")
        inputs = browser.find_element(By.XPATH, "//div[@class='first_block']/div[contains(@class, 'third')]//input")
        inputs.send_keys(f"{randint(1, 100)}")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем результаты загрузки
        welcome_text = browser.find_element(By.TAG_NAME, "h1").text
        browser.quit()
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", 'First test failed')

    def test2(self):
        # Открываем сайт
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        
        # Заполняем строки
        inputs = browser.find_element(By.XPATH, "//div[@class='first_block']/div[contains(@class, 'first')]//input")
        inputs.send_keys(f"{randint(1, 100)}")
        inputs = browser.find_element(By.XPATH, "//div[@class='first_block']/div[contains(@class, 'second')]//input")
        inputs.send_keys(f"{randint(1, 100)}")
        inputs = browser.find_element(By.XPATH, "//div[@class='first_block']/div[contains(@class, 'third')]//input")
        inputs.send_keys(f"{randint(1, 100)}")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем результаты загрузки
        welcome_text = browser.find_element(By.TAG_NAME, "h1").text
        browser.quit()
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", 'First test failed')

if __name__ == "__main__":
    unittest.main()