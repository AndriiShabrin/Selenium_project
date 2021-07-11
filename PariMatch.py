from selenium import webdriver
import time

from selenium.webdriver.chrome.webdriver import WebDriver

link = "https://air2.parimatch.com/ru/slots/"
browser:WebDriver = webdriver.Chrome()
browser.get(link)
time.sleep(4)

find_image = browser.find_element_by_css_selector('#assets-based-service-pm-casino > main > section > div > '
                                                  'div:nth-child(3) > div:nth-child(1) > '
                                                  'div.GamesSlider_slider__2rI4c > ul > li:nth-child(1) > a > div > '
                                                  'img')
search_alt = find_image.get_attribute("alt")
print(search_alt)

time.sleep(2)
browser.quit()
