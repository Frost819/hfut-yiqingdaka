import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

chrome_options = Options()  
chrome_options.add_argument("--headless")
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')

#定时打卡时间
hour = 15
minute = 0
while True:
    now_time = datetime.now()
    print(' 定时打卡中，当前时间：', now_time, '\n', '设定打卡时间：', hour,':',minute)
    if now_time.hour == hour and now_time.minute == minute:
        url="http://stu.hfut.edu.cn/xsfw/sys/xggzptapp/*default/index.do?min=1#/gzzm"
        browser=webdriver.Chrome(executable_path="./chromedriver", chrome_options=chrome_options)
        #进入首页
        browser.get(url)
        button = browser.find_element(By.XPATH, '//*[@id="page"]/div/div/div/div/button[1]')
        #进入登录界面
        button.click()
        #输入框
        input_username = browser.find_element(By.XPATH, '//*[@id="username"]')
        input_username.send_keys('2020170422')
        input_password = browser.find_element(By.XPATH, '//*[@id="pwd"]')
        input_password.send_keys('WOshi0819')
        input_password.send_keys(Keys.ENTER)
        #转到疫情信息收集页面
        browser.switch_to.new_window('tab')
        browser.get('http://stu.hfut.edu.cn/xsfw/sys/xsyqxxsjapp/*default/index.do#/mrbpa')
        wait = WebDriverWait(browser, 5, 0.5)
        wait.until(lambda browser: browser.find_element(By.XPATH, '//*[@id="save"]'))
        submit_button = browser.find_element(By.XPATH, '//*[@id="save"]')
        #点击提交按钮
        submit_button.click()
        #关闭浏览器
        print('打卡成功')
        browser.close()
    time.sleep(30)