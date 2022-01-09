from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
Validateoption = "option3"
driver.find_element(By.ID, 'name').send_keys(Validateoption)
driver.find_element(By.ID, 'alertbtn').click()
alert = driver.switch_to.alert
print(alert.text)
alerttext = alert.text
assert Validateoption in alerttext
alert.accept()
