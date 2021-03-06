import time
import argparse
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

#等待按钮出现并点击
def wait_and_click(Xpath):
    wait = WebDriverWait(browser, 5, 0.5)
    wait.until(lambda browser: browser.find_element(By.XPATH, Xpath))
    browser.find_element(By.XPATH, Xpath).click()

#命令参数
parser = argparse.ArgumentParser(description='定时自动打卡')
parser.add_argument('--username', help='学号')
parser.add_argument('--password', help='密码')
parser.add_argument('--once', help='是否无视打卡时间，立即进行一次打卡并结束', action='store_true')
parser.add_argument('--time', help='设定打卡时间', default='15:30')
args = parser.parse_args()

#浏览器选项
chrome_options = Options()  
chrome_options.add_argument("--headless")
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('blink-settings=imagesEnabled=false')

#打卡时间
hour = int(args.time.split(':')[0])
minute = int(args.time.split(':')[1])

#主循环
while True:
    now_time = datetime.now()
    print(' 当前时间：', now_time, '\n', '设定打卡时间：', hour,':',minute)
    if now_time.hour == hour and now_time.minute == minute or args.once:
        print('开始打卡')
        url="http://stu.hfut.edu.cn/xsfw/sys/emapfunauth/pages/welcome.do?service=http%3A%2F%2Fstu.hfut.edu.cn%2Fxsfw%2Fsys%2Fxggzptapp%2F*default%2Findex.do%3Fmin%3D1#/"
        browser=webdriver.Chrome(executable_path="./chromedriver")
        #进入首页
        browser.get(url)
        #进入登录界面
        wait_and_click('//*[@id="page"]/div/div/div/div/button[1]')
        #输入框
        input_username = browser.find_element(By.XPATH, '//*[@id="username"]')
        input_username.send_keys(args.username)
        input_password = browser.find_element(By.XPATH, '//*[@id="pwd"]')
        input_password.send_keys(args.password)
        input_password.send_keys(Keys.ENTER)
        #登录成功
        if 'cas.hfut.edu.cn' not in browser.current_url:
            #转到疫情信息收集页面
            browser.get('http://stu.hfut.edu.cn/xsfw/sys/swmxsyqxxsjapp/*default/index.do#/add')
            try:
                #点击提交按钮
                wait_and_click('//*[@id="app"]/div[1]/div/div[6]/div/button')
            except Exception:
                print('Error:打卡失败!')
                browser.quit()
            else:
                #点击返回转到index页面
                wait_and_click('//*[@id="app"]/div[1]/div/div[2]/button')
                wait = WebDriverWait(browser, 5, 0.5)
                wait.until(lambda browser: browser.find_element(By.XPATH, '//*[@id="scroll_container"]/div[1]/div[1]/div[1]/div'))
                #获取最新一次打卡日期
                text = browser.find_element(By.XPATH, '//*[@id="scroll_container"]/div[1]/div[1]/div[1]/div').get_attribute('textContent')
                if str(now_time.month)+'-'+str(now_time.day) in text:
                    print('Success:打卡成功!')
                browser.quit()
            #args.once为True则立即结束程序
            if args.once : break
        else:
            print('登录失败！请检查用户名和密码是否正确')
            browser.quit()
            break
    #每60秒查询一次时间
    time.sleep(60)