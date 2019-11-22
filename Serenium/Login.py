from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json
from time import sleep
import sys
import datetime, time, schedule
chrome_option = Options()
chrome_option.add_experimental_option("detach", True)
driver = webdriver.Chrome()
base_url="https://admin-scgfamily-loyalty.dockeruat.23perspective.com"
logindetail = "userlogin.json"
count=0
with open(logindetail, 'r') as f:
    user = json.load(f)
email = user["email"]
password = user["pwd"]


def setUp():
    driver.maximize_window()
    driver.get(base_url)
    driver.implicitly_wait(30)

def Login():
    driver.find_element_by_xpath("//*[@id='username-input']").click()
    sleep(1)
    username = driver.find_element_by_xpath("//*[@id='username-input']")
    username.send_keys(email)
    pwd = driver.find_element_by_xpath("//*[@id='password-input']")
    pwd.send_keys(password)
    driver.find_element_by_xpath("//*[@id='__layout']/div/div/div[1]/div/div[2]/div/button").click()
    sleep(2)
    driver.implicitly_wait(50)
    cur_url=driver.current_url
    ###print(cur_url)

def dothing():
    dateSTR = datetime.datetime.now().strftime("%H:%M:%S" )
    print("good to go")
    setUp()
    Login()   



schedule.every().day.at("18:22").do(dothing)
while True: 
  
    # Checks whether a scheduled task  
    # is pending to run or not 
    schedule.run_pending() 
    time.sleep(1) 

 