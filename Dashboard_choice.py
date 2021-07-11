import time

from Tools.scripts.serve import app
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

link = "https://auth.qiwa.tech/workspaces"

browser = webdriver.Chrome()
browser.get(link)
time.sleep(2)

dashboard_choice = browser.find_element_by_class_name("workspaces__list-info").click()

