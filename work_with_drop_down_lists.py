import time

from select import select
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver


import math

def calc(x,y):
    return str(int(x) + int(y))

link = "http://suninjuly.github.io/selects1.html"
browser: WebDriver = webdriver.Chrome()
browser.get(link)
x = browser.find_element_by_css_selector("#num1")
y = browser.find_element_by_css_selector("#num2")
print(x.text)
print(y.text)
x = x.text
y = y.text

z = calc(x,y)
print(z)

from selenium.webdriver.support.ui import Select
select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value(z)
browser.find_element_by_xpath("/html/body/div/form/button").click()
time.sleep(3)
browser.quit()