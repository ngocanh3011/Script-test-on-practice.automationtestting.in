# 3. Shop-Default Sorting Fuction 

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
chrome_driver_path = "D:\KTPM\ChromeDriver Set-up\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)

driver.get("http://practice.automationtesting.in/")
shopBtn = driver.find_element_by_id("menu-item-40")
shopBtn.click()

sortByPopularity = driver.find_element_by_xpath('//*[@id="content"]/form/select/option[2]')
sortByPopularity.click()

# driver.close()