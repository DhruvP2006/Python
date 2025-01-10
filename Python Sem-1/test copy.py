from selenium import webdriver
from selenium.webdriver.chrome.service import Service

CHROME_DRIVER_PATH = "C:\chromedriver_win32\chromedriver.exe"

# Initialize WebDriver
service = Service(CHROME_DRIVER_PATH)
driver = webdriver.Chrome(service=service)

# Open a website
driver.get("https://www.google.com")
print("Google opened successfully.")
driver.quit()
