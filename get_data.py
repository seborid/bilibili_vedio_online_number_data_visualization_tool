import json
import time

from find_number import query_the_online_people_number


def get_time_in_sen():
    '''获得当前的秒值，用于计数'''
    timestamp = time.time()
    local_time = time.localtime(timestamp)
    sen = local_time.tm_sec
    return sen


def get_data_in_json(urls, key):
    '''输入urls，获取从现在开始的数据，并以json文件存储'''
    sen = get_time_in_sen()
    i = 0
    numbers = []
#4种不同的数据获取模式对应4个不同名字的json文件，都是在数据获取完后，一次性写入json文件
    if key == 1:
        while i < 10:
            if sen == get_time_in_sen():
                print(f'现在是第{i + 1}次获取数据')
                numbers_current = query_the_online_people_number(urls)
                numbers.append(numbers_current)
                i += 1
            else:
                time.sleep(1)
        with open('data1.json', 'w') as f:
            json.dump(numbers, f)

    elif key == 2:
        while i < 60:
            if sen == get_time_in_sen():
                print(f'现在是第{i + 1}次获取数据')
                numbers_current = query_the_online_people_number(urls)
                numbers.append(numbers_current)
                i += 1
            else:
                time.sleep(1)
        with open('data2.json', 'w') as f:
            json.dump(numbers, f)

    elif key==3:
        while i < 180:
            if sen == get_time_in_sen():
                print(f'现在是第{i + 1}次获取数据')
                numbers_current = query_the_online_people_number(urls)
                numbers.append(numbers_current)
                i += 1
            else:
                time.sleep(1)
        with open('data3.json', 'w') as f:
            json.dump(numbers, f)

    elif key==4:
        while i < 1440:
            if sen == get_time_in_sen():
                print(f'现在是第{i + 1}次获取数据')
                numbers_current = query_the_online_people_number(urls)
                numbers.append(numbers_current)
                i += 1
            else:
                time.sleep(1)
        with open('data4.json', 'w') as f:
            json.dump(numbers, f)