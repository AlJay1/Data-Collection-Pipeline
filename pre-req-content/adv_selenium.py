from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time

def cookies():
    driver = webdriver.Chrome()

    URL = "https://www.zoopla.co.uk/new-homes/property/london/?q=London&results_sort=newest_listings&search_source=new-homes&page_size=25&pn=1&view_type=list"
    driver.get(URL)
    delay = 10

    try:
        WebDriverWait(driver, delay).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="gdpr-consent-notice"]')))
        print("Frame Ready")
        driver.switch_to.frame('gdpr-consent-notice')
        accept_cookies = WebDriverWait(driver, delay).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="save"]')))
        print("accept cookies ready")
        accept_cookies.click()
        time.sleep(1)

    except TimeoutException:
        print("loading took too long")

    return driver

cookies()