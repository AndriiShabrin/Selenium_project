from selenium import webdriver
import time
import math
from math import log, sin
from selenium.webdriver.chrome.webdriver import WebDriver

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/execute_script.html"
browser: WebDriver = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element_by_xpath('//*[@id="input_value"]')
print(x_element.text)
x = x_element.text
y = calc(x)
print(y)
time.sleep(3)

field_answer = browser.find_element_by_id("answer")
browser.execute_script("return arguments[0].scrollIntoView(true);", field_answer)
field_answer.send_keys(y)

time.sleep(2)

browser.find_element_by_xpath("//*[@type='checkbox']").click()
browser.find_element_by_xpath("//*[@id='robotsRule']").click()
browser.find_element_by_xpath("/html/body/div/form/button").click()



time.sleep(3)
browser.quit()


