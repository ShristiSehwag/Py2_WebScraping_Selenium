# import selenium
from selenium import webdriver
import time
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
  

def clean_text(text):
  """Extract only the temperature from text"""
  # gives list of text, convert to float
  output = float(text.split(": ")[1])
  return output



def staticEle():
  """to extract static data"""
  
  driver = get_driver()
  element = driver.find_element(by='xpath',value ='/html/body/div[1]/div/h1[1]')
  return element.text



def dynamicEle():
  """to extract dynmaic data (frequently changing)"""
  driverD = get_driver()
  time.sleep(2) # stay on page for 2 seconds and then extract 
  elementD = driverD.find_element(by='xpath',value ='/html/body/div[1]/div/h1[2]')
  return clean_text(elementD.text)

print("Static code : " + staticEle())

print()

print("Dynamic code : " + str(dynamicEle()))




  