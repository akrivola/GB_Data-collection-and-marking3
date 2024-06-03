from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

options = Options()
options.add_argument('start-maximized')

driver = webdriver.Chrome(options=options)

driver.get('https://mirsud.spb.ru/cases/?type=civil&id=&full_name=Криволапов')

court = 106  # номер судебного участка
# находим поле для ввода номера участка мирового судьи
input = driver.find_element(By.ID, "id_court_number")

# и вводим его
input.send_keys(court)

# находим кнопку "ИСКАТЬ" и нажимаем ее
button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
button.click()

# wait = WebDriverWait(driver, 30)
# case = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//table[@class='rwd-table']")))
time.sleep(30)
# TODO: Вместо ожидания полминуты нужно реализовать нормальное ожидание по появлению данных

# выводим на экран данные по судебным делам в виде текста
case = driver.find_element(By.XPATH, "//table[@class='rwd-table']").text
print(case)
# TODO: Нужно реализовать сбор данных в виде таблицы с номерами дел, датами, статусами, участниками и сделать листание по страницам
# TODO и остановку, если ничего не нашлось. Но не успеваю


