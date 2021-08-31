import os
import platform
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from aes_crypt import *


def is_connected():
    cmd = ''
    sysstr = platform.system()
    if sysstr == 'Windows':
        print("windows system")
        cmd = 'ping baidu.com -n 4'
    elif sysstr == "Linux":
        print("Linux system")
        cmd = 'ping baidu.com -c 4'
    result = os.system(cmd)
    if result == 0:
        return True;
    else:
        print("Network connection error!")
        return False


def autoLogin(username, password):
    key = ""
    iv = ""
    method = ""
    username = decrypt(key=key, iv=iv, method=method,payload=username)
    password = decrypt(key=key, iv=iv, method=method, payload=password)

    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    browser = webdriver.Chrome(executable_path="./chromedriver.exe", options=chrome_options)
    browser.get("http://124.16.81.61/")
    time.sleep(3)
    browser.refresh()

    browser.find_element_by_id("username").send_keys(username)
    browser.find_element_by_id("password").send_keys(password)
    browser.find_element_by_id("login-account").click()

    browser.quit()


if __name__ == '__main__':

    with open("./config.txt", 'r') as f:
        data = f.readlines()
    username = data[0]
    password = data[1]

    while True:
        if not is_connected():
            autoLogin(username, password)
        time.sleep(20)

