from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Selenium init
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options= chrome_options)
driver.get("https://orteil.dashnet.org/cookieclicker/")

# Select lang
time.sleep(3)
select_lang = driver.find_element(By.ID, value= 'langSelect-PT-BR')
select_lang.click()

# Main Game
time.sleep(1)
click_cookie = driver.find_element(By.ID, value= 'bigCookie')
while True:
    click_cookie.click()