from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import json

captcha_url = "https://linkedin.com"
cookies_file = 'cookies.json'



def getsession(driver):
    img_path = None
    try:
        driver.get(captcha_url)

        with open('cookies.json', 'r') as file:
            cookies = json.load(file)
            print(cookies)

        for cookie in cookies:
            # Selenium expects expiry as an integer, ensure it's correct
            if 'expiry' in cookie:
                cookie['expiry'] = int(cookie['expiry'])
            # Add the cookie to the current domain
            driver.add_cookie(cookie)

        # Refresh the page to apply the cookies
        driver.refresh()
        input()
        
        return driver.title

    except Exception as e:
        print(e)
        return img_path

