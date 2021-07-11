import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
browser = webdriver.Chrome()

link = "http://suninjuly.github.io/selects1.html"
link1 = "http://suninjuly.github.io/selects2.html"
try:
    browser.find_element_by_id("num1")