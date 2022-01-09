from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# browser exposes an executable file
# Through Selenium test we need to invoke the executable file which will then invoke actual browser
s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/#/index")  # get method to hit url on browser

print(driver.title)
print(driver.current_url)
driver.get("https://courses.rahulshettyacademy.com/courses")
driver.minimize_window()
driver.back()
driver.refresh()
driver.close()
