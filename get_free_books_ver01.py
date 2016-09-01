import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import getpass

user_id = input('ID를 입력하세요: ')
user_pwd = getpass.getpass('PWD를 입력하세요: ')

free_url = 'https://www.packtpub.com/packt/offers/free-learning'

driver = webdriver.Chrome('C:/Users/hufs/Downloads/download/lawjmc/chromedriver.exe')
driver.get(free_url)

btn_claim = driver.find_element_by_xpath("//input[@class='form-submit']")
ActionChains(driver).click(btn_claim).perform()

time.sleep(2)

btn_login_form = driver.find_element_by_xpath("//div[@class='respoLogin']")
ActionChains(driver).click(btn_login_form).perform()

input_id = driver.find_element_by_xpath("//input[@id='email']")
input_pwd = driver.find_element_by_xpath("//input[@id='password']")

input_id.send_keys(user_id)
input_pwd.send_keys(user_pwd)

btn_login = driver.find_element_by_xpath("//input[@id='edit-submit-1']")
ActionChains(driver).click(btn_login).perform()

time.sleep(4)

btn_claim = driver.find_element_by_xpath("//input[@class='form-submit'][@value='Claim Your Free eBook']")
ActionChains(driver).click(btn_claim).perform()

driver.quit()
