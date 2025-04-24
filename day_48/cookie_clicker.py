import time as t
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, ElementClickInterceptedException, ElementNotInteractableException

# Selenium init
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

t.sleep(2)

try:
    cookie_button = driver.find_element(By.ID, 'cookie')
    button_locators = {
        "Cursor": (By.ID, "buyCursor"), 
        "Grandma": (By.ID, "buyGrandma"),
        "Factory": (By.ID, "buyFactory"),
        "Mine": (By.ID, "buyMine"),
        "Shipment": (By.ID, "buyShipment"),
        "Alchemy lab": (By.ID, "buyAlchemy lab"),
        "Portal": (By.ID, "buyPortal"),
        "Time machine": (By.ID, "buyTime machine")
    }

    price_locators = {
        "Cursor": (By.XPATH, '//*[@id="buyCursor"]/b'),
        "Grandma": (By.XPATH, '//*[@id="buyGrandma"]/b'),
        "Factory": (By.XPATH, '//*[@id="buyFactory"]/b'),
        "Mine": (By.XPATH, '//*[@id="buyMine"]/b'),
        "Shipment": (By.XPATH, '//*[@id="buyShipment"]/b'),
        "Alchemy lab": (By.XPATH, '//*[@id="buyAlchemy lab"]/b'),
        "Portal": (By.XPATH, '//*[@id="buyPortal"]/b'),
        "Time machine": (By.XPATH, '//*[@id="buyTime machine"]/b')
    }
    money_locator = (By.ID, 'money')
    driver.find_element(*money_locator)
    for name, locator in price_locators.items():
        driver.find_element(*locator)
    for name, locator in button_locators.items():
        driver.find_element(*locator)

except NoSuchElementException as error:
    print(f"Fatal Error: Could not find essential elements on page load. Check IDs/XPaths. Error: {error}")
    driver.quit()
    exit()

def get_current_cookies():
    try:
        money_element = driver.find_element(*money_locator)
        total_cookies_text = money_element.text if money_element.text else "0"
        return int(total_cookies_text.replace(',', ''))
    
    except (NoSuchElementException, ValueError) as e:
        print(f"Error reading cookie count: {e}")
        return 0

def get_upgrade_prices():
    upgrades = {}
    for name, locator in price_locators.items():
        try:
            price_element = driver.find_element(*locator)
            price_text = price_element.text.split("-")[-1].strip()
            upgrades[name] = int(price_text.replace(',', ''))
        
        except (NoSuchElementException, IndexError, ValueError) as error:
            print(f"Warning: Could not parse price for {name}. Error: {error}")
            upgrades[name] = float('inf')
        
        except StaleElementReferenceException:
             print(f"Warning: Stale element reference when getting price for {name}. Retrying next cycle.")
             upgrades[name] = float('inf')
    return upgrades


def find_best_affordable_upgrade(current_cookies, upgrade_prices):
    affordable_upgrades = {}
    for name, price in upgrade_prices.items():
        if current_cookies >= price:
            affordable_upgrades[name] = price

    if affordable_upgrades:
        best_item = max(affordable_upgrades, key=affordable_upgrades.get)
        print(f"Highest affordable item: {best_item} at cost {affordable_upgrades[best_item]} with {current_cookies} cookies.")
        return best_item
    else:
        print(f"Cannot afford any upgrades with {current_cookies} cookies.")
        return None

check_interval = 5
last_check_time = t.time()

while True:
    try:
        cookie_button.click()
    except (StaleElementReferenceException, ElementClickInterceptedException, ElementNotInteractableException) as e:
         print(f"Warning: Error clicking cookie: {e}. Trying to re-find cookie element.")
         try:
             cookie_button = driver.find_element(By.ID, 'cookie')
         except NoSuchElementException:
             print("Fatal Error: Cookie button not found anymore!")
             break

    current_time = t.time()
    if (current_time - last_check_time) >= check_interval:
        print("\n--- Checking for Upgrades ---")
        try:
            cookies = get_current_cookies()
            prices = get_upgrade_prices()
            item_to_buy = find_best_affordable_upgrade(cookies, prices)

            if item_to_buy and item_to_buy in button_locators:
                target_locator = button_locators[item_to_buy]
                try:
                    print(f"Finding button for {item_to_buy}...")
                    target_button = driver.find_element(*target_locator)
                    print(f"Checking if button {item_to_buy} is enabled...")
                    if target_button.is_enabled():
                        print(f"Attempting to buy: {item_to_buy}")
                        target_button.click()
                        print(f"Successfully clicked {item_to_buy}.")
                        t.sleep(0.1)
                    else:
                        print(f"Warning: Button for {item_to_buy} is not enabled (greyed out).")

                except NoSuchElementException:
                    print(f"Error: Could not find button for {item_to_buy} even though it was affordable.")
                except (ElementClickInterceptedException, ElementNotInteractableException):
                    print(f"Warning: Click for {item_to_buy} was intercepted or element not interactable.")
                except StaleElementReferenceException:
                    print(f"Warning: Button for {item_to_buy} became stale before/during interaction.")
                except Exception as e:
                     print(f"An unexpected error occurred when trying to buy {item_to_buy}: {e}")
            last_check_time = current_time
            
        except StaleElementReferenceException as error:
            print(f"Stale Element Error occurred during check/buy cycle (outer catch): {error}")
            last_check_time = current_time
        except Exception as error:
            print(f"An error occurred during the check/buy cycle: {error}")
            last_check_time = current_time 

    t.sleep(0.01)
driver.quit()