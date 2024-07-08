# 2. Web Scraping Using Selenium 

Selenium is a robust tool for automating web browsers through programming. It supports all major browsers and operating systems, with script languages like Python, Java, and C#. Mastering Selenium enables automation of daily tasks such as tweeting, messaging on WhatsApp, and web browsing, all within 15-30 lines of Python code. Automation possibilities with Selenium are limitless.

## Code :

1. Importing Selenium:
The code begins by importing the `webdriver` module from the Selenium package. This module provides tools to automate web browser interaction.

3. Setting Chrome Options:
 Within the `get_driver` function, Chrome options are configured using `webdriver.ChromeOptions()`. These options include disabling info bars, maximizing the browser window (`start-maximized`), and enhancing security by disabling shared memory usage and sandboxing.

5. Creating the WebDriver:
A Chrome WebDriver instance is created using `webdriver.Chrome()` with the specified options. This WebDriver allows programmatic control over a Chrome browser session.

7. Navigating to a URL:
The WebDriver navigates to the URL `https://automated.pythonanywhere.com` using `driver.get()`. This demonstrates how Selenium can automate browsing to specific web pages.

9. Finding and Retrieving Element Text:
In the `staticEle/dynamicEle` function, the WebDriver finds a specific HTML element using its XPath (`/html/body/div[1]/div/h1[1]`) with `driver.find_element()`. It then retrieves the text content of this element using `element.text` and returns it.

Overall, we set up a Selenium WebDriver for Chrome, navigate to a webpage, and extract text from a specific element using XPath.
