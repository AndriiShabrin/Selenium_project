from selenium import webdriver
from selenium.webdriver.common.by import By
import time
link = "https://auth.qiwa.tech/sign-in"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(3)

    input1 = browser.find_element_by_id('login_username')
    input1.send_keys("1858568574")
    input2 = browser.find_element_by_id('login_password')
    input2.send_keys("123456789aA@")
    button = browser.find_element_by_id('continue_button')
    button.click()
    time.sleep(2)
    input3 = browser.find_element_by_id('code')
    input3.send_keys("0000")
    time.sleep(2)
    button = browser.find_element_by_id('sign_in_button').click()
    time.sleep(6)
    choose_workspace_root = browser.find_element_by_xpath('//p[text()="LMI Admin"]').click()
    time.sleep(3)


finally:
    time.sleep(2)

    browser.quit()