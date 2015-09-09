from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://ww.python.org")
driver.close()