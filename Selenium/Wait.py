# Implicit wait  -
# Explicit Wait
# pause the test for few seconds using Time class
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.implicitly_wait(5)

# wait until 5 seconds if object is not displayed
# Global wait
# 1.5 second to reach next page- execution will resume in 1.5 seconds
# if object do not show up at all, then max time your test waits for 5 seconds

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR, 'input.search-keyword').send_keys("Ber")
time.sleep(4)
print(len(driver.find_elements(By.XPATH, "//div[@class='products']/div")))
products = driver.find_elements(By.XPATH, "//div[@class='product-action']/button")
print(len(driver.find_elements(By.XPATH, "//div[@class='product-action']/button")))
for product in products:
    product.click()

driver.find_element(By.XPATH, "//a[@class='cart-icon']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element(By.CSS_SELECTOR, "input.promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, "button.promoBtn").click()
time.sleep(6)
print(driver.find_element(By.CSS_SELECTOR, "button.promoBtn").text)



