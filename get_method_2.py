import time

from selenium import webdriver

driver = webdriver.Chrome()

time.sleep(5)

driver.get("file:///C:/Users/Samurai/Downloads/2021-02-24_andrij_shabrin.pdf")
time.sleep(10)

driver.quit()