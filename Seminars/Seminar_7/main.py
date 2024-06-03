from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = Options()
options.add_argument('start-maximized')

driver = webdriver.Chrome(options=options)

driver.get('https://www.wildberries.ru/')

# input = driver.find_element(By.XPATH, "//input[]@id='searchInput'")

time.sleep(2)
input = driver.find_element(By.ID, "searchInput")
input.send_keys("телевизор")
input.send_keys(Keys.ENTER)

print()
