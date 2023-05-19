from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

print("Sample test case started")
driver = webdriver.Chrome("E:\SeleniumWithPython\browsers\chromedriver.exe")

driver.get("https://accounts.google.com/v3/signin/identifier?dsh=S67682124%3A1684096987852538&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ifkv=Af_xneGYKzFqtmRVSY8H4OqjjKCFCjECRaOo4uCUDW4F4AgJ5xEVLScVhLU6uUZXPxVf6k8Bz4BYjw&rip=1&sacu=1&service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin")

#Username login
emailBox = driver.find_element("name", "identifier")
emailBox.send_keys('*********') #email address goes here
usernameNextBox = driver.find_element("xpath",'//*[@id="identifierNext"]').click()

#To wait for passwordBox to load
time.sleep(3)

#Password login
passwordBox = driver.find_element("name", "Passwd")
passwordBox.send_keys('*********') #password goes here
passwordNextBox = driver.find_element("xpath",'//*[@id="passwordNext"]').click()

time.sleep(10)

driver.close()
print("TS_GM_Login_001 completed")