from selenium import webdriver

import time

import math

from selenium.webdriver.chrome.webdriver import WebDriver


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"
browser: WebDriver = webdriver.Chrome()
browser.get(link)

chest_treasure=browser.find_element_by_id("treasure")
print(chest_treasure)

treasure_num = chest_treasure.get_attribute("valuex")
print("Value of the valuex attribute is:", treasure_num)
x = treasure_num
y = calc(x)
print(y)

field_answer = browser.find_element_by_id("answer")
field_answer.send_keys(y)

browser.find_element_by_css_selector("div input[type='checkbox']").click()
browser.find_element_by_css_selector("div input[value=robots]").click()
browser.find_element_by_css_selector("div button[type=submit]").click()
time.sleep(3)
browser.quit()
