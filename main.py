from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
chrome_driver_location = "E:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_location)
driver.get("https://tinder.com/app/recs")
base_window = driver.window_handles[0]
login = driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/button')
login.click()

time.sleep(5)
google = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[1]/div/button')
google.click()
time.sleep(5)
google_login_window = driver.window_handles[1]
driver.switch_to.window(google_login_window)
google_email = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input')
google_email.send_keys("cybertest0508@gmail.com")
next_button_username = driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button')
next_button_username.click()
time.sleep(5)

google_password = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
google_password.send_keys("1501@Broadway")
next_button_password = driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button')
next_button_password.click()

time.sleep(5)
driver.switch_to.window(base_window)
allow_location_button = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
allow_location_button.click()

not_interested = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
not_interested.click()

cookies = driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button')
cookies.click()
time.sleep(5)

body = driver.find_element_by_xpath('//*[@id="Tinder"]/body')

for i in range(0, 101):
    time.sleep(5)
    body.send_keys(Keys.ARROW_RIGHT)


