import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

first_name_field = browser.find_element_by_xpath("/html/body/div/form/div/input[1]").send_keys("Vasya")
last_name_field = browser.find_element_by_xpath("/html/body/div/form/div/input[2]").send_keys("Poopkin")
email_field = browser.find_element_by_xpath("/html/body/div/form/div/input[3]").send_keys("blah.mail.com")
current_dir = os.path.abspath(os.path.dirname(__file__))
file_name = "file_example.txt"
file_path = os.path.join(current_dir, file_name)
element = browser.find_element_by_css_selector("[type='file']")
element.send_keys(file_path)

submit_button = browser.find_element_by_xpath("/html/body/div/form/button").click()

time.sleep(5)
browser.quit()
