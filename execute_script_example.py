from selenium import webdriver

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()

#driver = webdriver.Chrome()
#driver.get("https://SunInJuly.github.io/execute_script.html")

#try:
    #button = driver.find_element_by_tag_name("button")
    #_ = button.location_once_scrolled_into_view

   #button.click()
    #assert True
#finally:
    #driver.quit()