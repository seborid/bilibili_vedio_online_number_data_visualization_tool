import time

from retrying import retry
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# 请求网站
driver.get("https://www.bilibili.com/video/BV13A411M73y?spm_id_from=333.851.b_7265636f6d6d656e64.4")
title = driver.find_element(By.XPATH, "//div/h1/span[@class='tit']").text
# 最大化窗口
driver.maximize_window()
# 获取当前访问的url
url = driver.current_url
print('现在的网址是:', url)
print("标题为：", title)
# 显示网页源码
html = driver.page_source
# 将源码保存以便观察
with open('html.html', 'w', encoding='utf-8') as f:
    f.write(html)
# 获取cookie
# cookie = driver.get_cookies()
# cookie = {i['name']:i['value'] for i in cookie}
# print('获取到的cookie：\n', cookie)
time.sleep(5)


@retry()
def get_number():
    numbers = driver.find_element(By.XPATH, '//div/span[@class="bilibili-player-video-info-people-number"]').text
    return numbers


while True:
    # 用selenium自带的定位功能获取信息
    number = get_number()
    data = time.strftime("%Y-%m-%d %H:%M:%S")
    if number != "1":
        print("现在的时间是：{}，当前的观看人数是：{}".format(data, number))
    driver.refresh()
    time.sleep(3)
