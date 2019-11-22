from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json
from time import sleep
import sys
import datetime, time, schedule

chrome_option = Options()
chrome_option.add_experimental_option("detach", True)
driver = webdriver.Chrome()
base_url="https://pttblc-uat.dockeruat.23perspective.com"
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
    #driver.set_window_size(desktop['1366'], desktop['764'])

def Privilege():
    driver.get("https://pttblc-uat.dockeruat.23perspective.com/th/redeem/privilege")
    driver.implicitly_wait(30)
    driver.save_screenshot("privilege.png")
    cur_url = driver.current_url
    print(cur_url)

def dothing():
    dateSTR = datetime.datetime.now().strftime("%H:%M:%S" )
    print(dateSTR)
    setUp()
    Privilege()
    driver.close()
    sys.exit()
   



schedule.every().day.at("15:19").do(dothing)
while True: 
  
    # Checks whether a scheduled task  
    # is pending to run or not 
    schedule.run_pending() 
    currentTime = datetime.datetime.now().strftime("%H:%M:%S" )

    print(currentTime)
    time.sleep(1) 