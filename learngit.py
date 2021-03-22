from selenium import webdriver
import argparse
import os
import time
parser = argparse.ArgumentParser(description='Nothing')
parser.add_argument('names', type=str, help='string to name git repo')
args = parser.parse_args()
chromedriver = "/home/zekousek/chromedriver"
browser = webdriver.Chrome(chromedriver)
browser.get("https://github.com/new")
login = browser.find_element_by_xpath("//*[@id='login_field']")
login.click()
login.send_keys('') # enter your username
password = browser.find_element_by_xpath("//*[@id='password']")
password.click()
password.send_keys('')# enter your password
kk = browser.find_elements_by_name('commit')
kk[0].click()
repo = browser.find_elements_by_xpath("//*[@id='repository_name']")
repo[0].click()
repo[0].send_keys(args.names)
cr_button = browser.find_element_by_xpath("//*[@id='new_repository']/div[4]/button")
time.sleep(1)
cr_button.click()
browser.execute_script("window.open('https://stackoverflow.com/users/login?ssrc=head&returnurl=https%3a%2f%2fstackoverflow.com%2f', 'new window')")
windows = browser.window_handles
browser.switch_to.window(windows[1])
loginstack = browser.find_element_by_name("email")
loginstack.click()
loginstack.send_keys('')# enter your login
passwordstack = browser.find_element_by_xpath("//*[@id='password']")
passwordstack.click()
passwordstack.send_keys('')# enter your password 
python_button = browser.find_element_by_xpath("//*[@id='submit-button']")
python_button.click()

