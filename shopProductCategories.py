# 2. Shop-Product Categories Functionality

from selenium import webdriver
chrome_driver_path = "D:\KTPM\ChromeDriver Set-up\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)

driver.get("http://practice.automationtesting.in/")
shopBtn = driver.find_element_by_id("menu-item-40")
shopBtn.click()

productLink = driver.find_element_by_class_name("post-170")
productLink.click()

# driver.close()