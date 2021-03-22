from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import sys
import os

chromedriver = "/home/zekousek/chromedriver"
browser = webdriver.Chrome(chromedriver)
browser.maximize_window()
browser.get("https://github.com/new")
login = browser.find_element_by_xpath("//*[@id='login_field']")
login.click()
login.send_keys('zekosnb')
password = browser.find_element_by_xpath("//*[@id='password']")
password.click()
password.send_keys('MakoMako132')
kk = browser.find_elements_by_name('commit')
kk[0].click()
browser.execute_script("window.open('https://stackoverflow.com/users/login?ssrc=head&returnurl=https%3a%2f%2fstackoverflow.com%2f', 'new window')")
windows = browser.window_handles
browser.switch_to.window(windows[1])
loginstack = browser.find_element_by_name("email")
loginstack.click()
loginstack.send_keys('maros3845@gmail.com')
passwordstack = browser.find_element_by_xpath("//*[@id='password']")
passwordstack.click()
passwordstack.send_keys('MakoMako132') 
python_button = browser.find_element_by_xpath("//*[@id='submit-button']")
python_button.click()

