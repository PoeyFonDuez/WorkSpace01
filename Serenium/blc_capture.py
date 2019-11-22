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

def Privilege():
    driver.get("https://pttblc-uat.dockeruat.23perspective.com/th/redeem/privilege")
    driver.implicitly_wait(30)
    total_width = driver.execute_script("return document.body.offsetWidth")
    total_height = driver.execute_script("return document.body.scrollHeight")
    driver.set_window_size(total_width, total_height)
    dateSTR = datetime.datetime.now().strftime("%H:%M:%S" )
    filename = "privilege " + dateSTR + ".png"
    driver.save_screenshot(filename)
    cur_url = driver.current_url
    print(cur_url)
    print("Resulution ",total_height," X ",total_width)

def dothing():
    print("- - Program is running - -")
    setUp()
    Privilege()
    driver.close()
    print("- - END - -")
    sys.exit()#break
   
dothing()

'''schedule.every().day.at("15:57").do(dothing)
while True: 
    # Checks whether a scheduled task  
    # is pending to run or not 
    schedule.run_pending() 
    currentTime = datetime.datetime.now().strftime("%H:%M:%S" )
    print(currentTime)
    time.sleep(1) '''