import json
import re
import time
import warnings

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def find_word_and_output_numbers(html_bilibili):
    '''输入视频的html格式的json文件，输出正在观看人数'''
    # 使用正则表达式查找<pre>标签中的JSON字符串
    json_str = re.search(r'<pre>(.*?)</pre>', html_bilibili, re.DOTALL).group(1)
    json_data = json.loads(json_str)
    # 现在您可以在Python中处理json_data了
    number = json_data['data']['total']
    print(number)
    number = str(number)
    number = number.rstrip('+')
    if '万' in number:
        number = number.rstrip('万')
        number = int(float(number) * 10000)
    else:
        number = int(number)
    return number


def query_the_online_people_number(urls):
    '''输入一个urls列表，输出一个格式为月，日，小时，分钟，观看人数1，观看人数2，，，的数字列表(同时在显示器上输出时间信息）'''
    numbers = []
    now = time.time()
    local_time = time.localtime(now)
    hour = local_time.tm_hour
    minute = local_time.tm_min
    month = local_time.tm_mon
    day = local_time.tm_mday
    sec1 = local_time.tm_sec
    print(f'现在时间是2024年{month}月{day}日{hour}时{minute}分{sec1}秒')
    numbers.append(f'{month:02d}')
    numbers.append(f'{day:02d}')
    numbers.append(f'{hour:02d}')
    numbers.append(f'{minute:02d}')  # 实现补0功能，时间信息以字符串存储
    for url in urls:
        warnings.simplefilter('ignore', ResourceWarning)
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(url)
        html_bilibili = driver.page_source
        driver.close()
        number = find_word_and_output_numbers(html_bilibili)
        numbers.append(number)
    print(numbers)
    now = time.time()
    local_time = time.localtime(now)
    hour = local_time.tm_hour
    minute = local_time.tm_min
    month = local_time.tm_mon
    day = local_time.tm_mday
    sec2 = local_time.tm_sec
    print(f'现在时间是2024年{month}月{day}日{hour}时{minute}分{sec2}秒')
    print(f'获取数据用时{((sec2 - sec1) + 60) % 60}秒')
    return numbers
