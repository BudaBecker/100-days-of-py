from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options= chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")

# event = driver.find_element(By.XPATH, value='//*[@id="mw-content-text"]/div[1]/div[1]/div/div[1]/table/tbody/tr/td[2]/div/p/b[1]')
# print(event.text)
# driver.quit()

# event = driver.find_element(By.LINK_TEXT, value= "artigos")
# event.click()

event = driver.find_element(By.NAME, value= "fName")
event.send_keys("Gabriel")
event = driver.find_element(By.NAME, value= "lName")
event.send_keys("Becker")
event = driver.find_element(By.NAME, value= "email")
event.send_keys("becker@gmail.com")

time.sleep(1)

event.find_element(By.CSS_SELECTOR, value= 'form button')
event.click()