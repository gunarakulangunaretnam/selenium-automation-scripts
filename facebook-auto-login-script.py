import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('./chromedriver')
driver.get("https://www.google.com")
print(driver.title)
search_bar = driver.find_element_by_name("q")
search_bar.clear()
search_bar.send_keys("facebook")
search_bar.send_keys(Keys.RETURN)
driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div/div/div/div/div[1]/a/h3').click()

time.sleep(2)
driver.find_element_by_id("email").send_keys("testing_email@fake.com")
driver.find_element_by_id("pass").send_keys("12345678909876543")



