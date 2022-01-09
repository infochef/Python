import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("http://www.phptravels.net/login")
driver.find_element(By.XPATH, "//*[@placeholder='Email']").send_keys("user@phptravels.com")
driver.find_element(By.XPATH, "//*[@placeholder='Password']").send_keys("demouser")
driver.find_element(By.XPATH, "//*[@type='submit']").click()

my_list = driver.find_elements(By.XPATH, "//*[@class='main-menu-content']/nav/ul/li/a")
for link in my_list:
    print(link.text)
    a = driver.find_element(By.LINK_TEXT, "Flights")
    if link == a:
        a.click()
        break
    else:
        print("WebDriver didn't found Text 'Flights' ")
driver.find_element(By.NAME, 'from').send_keys("Del")
Countries = driver.find_elements(By.CSS_SELECTOR, "div[class = 'autocomplete-wrapper _1 row_1'] div b")
for country in Countries:
    print(country.text)
    if (country.text == 'DEL'):
        country.click()
        break
print(driver.find_element(By.NAME, 'from').text)
assert driver.find_element(By.NAME, 'from').get_attribute('value') == 'DEL - Indira Gandhi Intl - Delhi'
time.sleep(10)
