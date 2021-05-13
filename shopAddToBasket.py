# 10. Shop-Add to Basket-View Basket Functionality

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
chrome_driver_path = "D:\KTPM\ChromeDriver Set-up\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)

driver.get("http://practice.automationtesting.in/")
shopBtn = driver.find_element_by_id("menu-item-40")
shopBtn.click()

addToBasket = driver.find_element_by_xpath('//*[@id="content"]/ul/li[1]/a[2]')
addToBasket.click()
time.sleep(2)

viewBasket = driver.find_element_by_xpath('//*[@id="content"]/ul/li[1]/a[3]')
viewBasket.click()

proceedToCheckoutBtn = driver.find_element_by_class_name("checkout-button")
proceedToCheckoutBtn.click()

firstName = driver.find_element_by_id("billing_first_name")
firstName.send_keys("Tran")

lastName = driver.find_element_by_id("billing_last_name")
lastName.send_keys("Anh")

email = driver.find_element_by_id("billing_email")
email.send_keys("tranngocanh45@gmail.com")

phone = driver.find_element_by_id("billing_phone")
phone.send_keys("0969732701")

address = driver.find_element_by_id("billing_address_1")
address.send_keys("Ngu Hanh Son")

city = driver.find_element_by_id("billing_city")
city.send_keys("Da Nang")

payment = driver.find_element_by_id("payment_method_bacs")
payment.click()

payment = driver.find_element_by_id("place_order")
payment.click()

# driver.close()