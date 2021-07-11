import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)

button_click = browser.find_element_by_xpath("/html/body/form/div/div/button").click()

confirm = browser.switch_to.alert
confirm.accept()

x_element = browser.find_element_by_id("input_value")
print(x_element.text)
x = x_element.text
y = calc(x)
print(y)

answer_field = browser.find_element_by_xpath('//*[@id="answer"]').send_keys(y)

submit_button = browser.find_element_by_xpath('/html/body/form/div/div/button').click()

time.sleep(2)
browser.quit()





