from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")


button = WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.XPATH, '//*[@id="price"]'), "100")
)
button_book = browser.find_element_by_xpath('//*[@id="book"]').click()

x_element = browser.find_element_by_id("input_value")
print(x_element.text)
x = x_element.text
y = calc(x)
print(y)

field_answer = browser.find_element_by_id("answer")
field_answer.send_keys(y)

submit_button = browser.find_element_by_xpath('//*[@id="solve"]').click()
time.sleep(2)
browser.quit()

