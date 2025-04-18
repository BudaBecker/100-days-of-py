from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options= chrome_options)
driver.get("https://python.org")

events = driver.find_elements(By.XPATH, value='//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li')
events_dict = {}

for i in range(len(events)):
    events_dict[i] = {
        'time': events[i].text.split("\n")[0],
        'name': events[i].text.split("\n")[1]
    }

print(events_dict)
driver.quit()