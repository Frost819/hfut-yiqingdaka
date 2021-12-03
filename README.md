# 合工大疫情信息收集自动打卡

基于selenium网页自动化工具，进入学工系统疫情信息收集模块，自动填写并提交表单。

## 依赖

- Linux or Windows
- Python 3
- Selenium
- Chrome浏览器

## 如何开始

### 安装

- Clone this repo:

```bash
git clone https://github.com/Frost819/hfut-yiqingdaka.git
```

- 安装selenium:

```python
pip install selenium
```

- 安装webdriver:
  - 先查看chrome版本，在**https://npm.taobao.org/mirrors/chromedriver/**选择相应版本的chromedriver。将下载的chromedriver 解压至repo根目录下。

### 运行

```python
python daka.py --username xuehao --password mima --time hour:minute --once 
```

-  `--username` 为学号， `--password`为[综合信息门户 (hfut.edu.cn)](https://one.hfut.edu.cn/)的登录密码，请先确认密码正确。`--time`为设定的自动打卡时间，默认为15:30，第一次运行建议设为当前时间。`--once`用于一次性运行打卡程序，会无视打卡时间、立即进行一次打卡并退出程序，如果希望定时打卡则无需输入。

## windows脚本

repo内三个.bat脚本运行前均需要右键编辑，修改USERNAME和PASSWORD为你的学号和密码。

1. start.bat为定时打卡脚本，每到设定打卡时间进行打卡。

2. start_once.bat为一次性打卡脚本，立即进行一次打卡并退出。

3. start_silent.bat与1功能相同，但会隐藏命令行窗口，如需关闭请在任务管理器-后台进程中关闭`Windows命令处理程序`和`Python`
