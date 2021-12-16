import time
import argparse
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait


print('开始打卡')
url="http://stu.hfut.edu.cn/xsfw/sys/emapfunauth/pages/welcome.do?service=http%3A%2F%2Fstu.hfut.edu.cn%2Fxsfw%2Fsys%2Fxggzptapp%2F*default%2Findex.do%3Fmin%3D1#/"
browser=webdriver.Chrome(executable_path="./chromedriver")
#进入首页
browser.get(url)
wait = WebDriverWait(browser, 5, 0.5)
wait.until(lambda browser: browser.find_element(By.XPATH, '//*[@id="page"]/div/div/div/div/button[1]'))
button = browser.find_element(By.XPATH, '//*[@id="page"]/div/div/div/div/button[1]')
#进入登录界面
button.click()
#输入框
input_username = browser.find_element(By.XPATH, '//*[@id="username"]')
input_username.send_keys('2020170421')
input_password = browser.find_element(By.XPATH, '//*[@id="pwd"]')
input_password.send_keys('498152Zsr.')
input_password.send_keys(Keys.ENTER)
#登录成功
if 'cas.hfut.edu.cn' not in browser.current_url:
    #转到疫情信息收集页面
    browser.get('http://stu.hfut.edu.cn/xsfw/sys/swmxsyqxxsjapp/*default/index.do#/')
    wait = WebDriverWait(browser, 5, 0.5)
    try:
        wait.until(lambda browser: browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[6]/div/button'))
    except Exception:
        print('Error:打卡失败，请确认是否已打过卡')
        browser.quit()
    else:
        submit_button = browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[6]/div/button')
        #点击提交按钮
        submit_button.click()
        print('打卡成功!')
        # browser.quit()
else:
    print('登录失败！请检查用户名和密码是否正确')
    browser.quit()