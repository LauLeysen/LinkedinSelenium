from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


import json
import time

driver = webdriver.Chrome()  # Ensure chromedriver is in PATH or specify executable_path

try:
    driver.get('https://www.linkedin.com')
    
    time.sleep(2)

    with open('cookies.json', 'r') as file:
        cookies = json.load(file)

    for cookie in cookies:
        cookie_dict = {
            'name': cookie.get('name'),
            'value': cookie.get('value'),
            'domain': cookie.get('domain'),
            'path': cookie.get('path', '/'),
            'secure': cookie.get('secure', False),
            'httpOnly': cookie.get('httpOnly', False)
        }

        if not cookie.get('session', False) and 'expirationDate' in cookie:
            cookie_dict['expiry'] = int(cookie['expirationDate'])
        
        try:
            driver.add_cookie(cookie_dict)
            print(f"Added cookie: {cookie_dict['name']}")
        except Exception as e:
            print(f"Failed to add cookie: {cookie_dict['name']}. Error: {e}")

    driver.refresh()
    time.sleep(1)
    driver.get("https://www.linkedin.com/mynetwork/grow/?skipRedirect=true")
    time.sleep(2)
    element = driver.find_element(By.CSS_SELECTOR, "#root > div._16rb9d7.cnuthtw.cnuthtb4._1ptbkx6bs._1xoe5hd3._1ptbkx61eo > div._16rb9df.cnuthtb4._1ptbkx6bs > div > div > div > main > div > div.cnuthtao > div > div:nth-child(3) > section > div > div._1k2lxmeu8._1k2lxmey0._1k2lxme120._1k2lxme15s.cnuthtaw.cnuthte0.cnutht180.cnutht0.cnuthtgw.cnuthtio > button > span").click()
    
    input("enter when ready")
    
    actions = ActionChains(driver)

    sequence = [Keys.TAB, Keys.TAB, Keys.TAB, Keys.ENTER]

    repeat_count = 200

    for _ in range(repeat_count):
        print(_)
        for key in sequence:
            actions.send_keys(key)
        actions.perform()
        actions.reset_actions()
        time.sleep(0.3)
        

finally:
    driver.quit()
