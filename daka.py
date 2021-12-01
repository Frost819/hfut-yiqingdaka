import time
import argparse
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

#命令参数
parser = argparse.ArgumentParser(description='定时自动打卡')
parser.add_argument('--username', help='学号')
parser.add_argument('--password', help='密码')
parser.add_argument('--once', help='是否无视打卡时间，立即进行一次打卡并结束', action='store_true')
args = parser.parse_args()

#浏览器选项
chrome_options = Options()  
chrome_options.add_argument("--headless")
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')

#打卡时间
hour = 15
minute = 0

#主循环
while True:
    now_time = datetime.now()
    print(' 当前时间：', now_time, '\n', '设定打卡时间：', hour,':',minute)
    if now_time.hour == hour and now_time.minute == minute or args.once:
        url="http://stu.hfut.edu.cn/xsfw/sys/xggzptapp/*default/index.do?min=1#/gzzm"
        browser=webdriver.Chrome(executable_path="./chromedriver", chrome_options=chrome_options)
        #进入首页
        browser.get(url)
        wait = WebDriverWait(browser, 5, 0.5)
        wait.until(lambda browser: browser.find_element(By.XPATH, '//*[@id="page"]/div/div/div/div/button[1]'))
        button = browser.find_element(By.XPATH, '//*[@id="page"]/div/div/div/div/button[1]')
        #进入登录界面
        button.click()
        #输入框
        input_username = browser.find_element(By.XPATH, '//*[@id="username"]')
        input_username.send_keys(args.username)
        input_password = browser.find_element(By.XPATH, '//*[@id="pwd"]')
        input_password.send_keys(args.password)
        input_password.send_keys(Keys.ENTER)
        #登录成功
        if 'cas.hfut.edu.cn' not in browser.current_url:
            #转到疫情信息收集页面
            browser.switch_to.new_window('tab')
            browser.get('http://stu.hfut.edu.cn/xsfw/sys/xsyqxxsjapp/*default/index.do#/mrbpa')
            wait = WebDriverWait(browser, 5, 0.5)
            try:
                wait.until(lambda browser: browser.find_element(By.XPATH, '//*[@id="save"]'))
            except Exception:
                print('Error:打卡失败，请确认是否已打过卡')
            else:
                submit_button = browser.find_element(By.XPATH, '//*[@id="save"]')
                #点击提交按钮
                submit_button.click()
                print('打卡成功!')
            #args.once为True则立即结束程序
            if args.once : break
            #关闭浏览器
            browser.close()
        else:
            print('登录失败！请检查用户名和密码是否正确')
            break
    #每30秒查询一次时间
    time.sleep(30)