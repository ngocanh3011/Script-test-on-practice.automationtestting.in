# 1. Shop-Filter By Price Functionality

from selenium import webdriver
chrome_driver_path = "D:\KTPM\ChromeDriver Set-up\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)

driver.get("http://practice.automationtesting.in/")
shopBtn = driver.find_element_by_id("menu-item-40")
shopBtn.click()

filterPrice = driver.find_element_by_xpath('//*[@id="woocommerce_price_filter-2"]/form/div/div[1]/span[2]')

filterBtn = driver.find_element_by_class_name("button")
filterBtn.click()

# driver.close()