import argparse
import os
import platform
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


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

    parser = argparse.ArgumentParser(description='UCAS Campus Network Auto Login by sjc')
    parser.add_argument('-username', dest='username', type=str, required=True, help='账号(必填参数)')
    parser.add_argument('-password', dest='password', type=str, required=True, help='密码(必填参数)')
    args = parser.parse_args()

    while True:
        if not is_connected():
            autoLogin(args.username, args.password)
        time.sleep(20)

