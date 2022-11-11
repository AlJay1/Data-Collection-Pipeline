from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def load_and_accept_cookies() -> webdriver.Chrome:
    driver = webdriver.Chrome() 
    URL = "https://www.zoopla.co.uk/new-homes/property/london/?q=London&results_sort=newest_listings&search_source=new-homes&page_size=25&pn=1&view_type=list"
    driver.get(URL)
    time.sleep(3)

    try:
        driver.switch_to.frame('gdpr-consent-notice') # This is the id of the frame
        accept_cookies_button = driver.find_element(by=By.XPATH, value='//*[@id="save"]')
        accept_cookies_button.click()

    except AttributeError:
        driver.switch_to.frame('gdpr-consent-notice') # This is the id of the frame
        accept_cookies_button = driver.find_element(by=By.XPATH, value='//*[@id="save"]')
        accept_cookies_button.click()

    except:
        pass
    return driver

driver = load_and_accept_cookies()


def get_links() -> list:
    '''
    Returns a list with all the links in the current page
    Parameters
    ----------
    driver: webdriver.Chrome
        The driver that contains information about the current page
    
    Returns
    -------
    link_list: list
        A list with all the links in the page
    '''

    prop_container = driver.find_element(by=By.XPATH, value='//div[@class="css-1kk52wv etglsof6"]')
    prop_list = prop_container.find_elements(by=By.XPATH, value='./div')
    link_list = []

    for house_property in prop_list:
        a_tag = house_property.find_element(by=By.TAG_NAME, value='a')
        link = a_tag.get_attribute('href')
        link_list.append(link)

    print(f"There are {len(link_list)} properties on this page")
    print(link_list)   

big_list = []

def get_properties(link):
    dict_properties={'price':[],'Address':[],'bedrooms':[]}
    for link in big_list:
        driver.get(link)
        price=driver.find_element(By.XPATH, "//p[@data-testid='price']").text
        dict_properties['price'].append(price)
        address=driver.find_element(By.XPATH, '//address[@data-testid="address-label"]').text
        dict_properties['Address'].append(address)
        bedrooms=driver.find_element(By.XPATH, '//div[@class="c-PJLV c-PJLV-kQvhQW-centered-true c-PJLV-iPJLV-css"]').text
        dict_properties['Bedrooms'].append(bedrooms)
    return dict_properties


def pages(page_link):

    for i in range(5): # The first 5 pages only
        big_list.extend(get_links(driver)) # Call the function we just created and extend the big list with the returned list
        link= page_link[i]
        next_page = driver.find_element(by=By.XPATH, value='//li[@class="css-qhg1xn-PaginationItemPreviousAndNext-PaginationItemNext eaoxhri2"]')
        next_page.click()
        get_properties(link)
        

driver = load_and_accept_cookies
get_links()

driver.quit() # Close the browser when you finish

 

