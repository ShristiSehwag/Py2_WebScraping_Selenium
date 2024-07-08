# import selenium
from selenium import webdriver
## for local IDE
# from selenium.webdriver.chrome.service import Service
# service = Service(executable_path="C:\chromedriver.exe")

def get_driver():
  
  #set options for easier browsing
  options = webdriver.ChromeOptions()
  options.add_argument('disaable-infobars')
  options.add_argument('start-maximized ')
  options.add_argument('disable-dev-shm-usage')
  options.add_argument('no-sandbox') #gain more privilage
  options.add_experimental_option('excludeSwitches', ['enable-automation'])
  options.add_argument('disable-blink-features=AutomationControlled')
  
  driver = webdriver.Chrome(options)
  driver.get('https://automated.pythonanywhere.com')
  
  return driver 

def main():
  driver = get_driver()
  # we use the xpath to find the element
  element = driver.find_element(by='xpath',value ='/html/body/div[1]/div/h1[1]')
  return element.text

print(main())
  