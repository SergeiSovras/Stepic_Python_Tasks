import time
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    link = "https://onliner.by"
    browser = webdriver.Chrome()
    # говорим WebDriver искать каждый элемент в течение 5 секунд
    browser.implicitly_wait(5)
    time.sleep(2)
    browser.get(link)
    time.sleep(2)
    user_icon = browser.find_element(By.CSS_SELECTOR, ".header-style__underlay")
    user_icon.click()
    time.sleep(2)
finally:
    browser.quit()