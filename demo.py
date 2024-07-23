
import requests
import re
import time
import datetime
import traceback
import json

def get_page_source(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "failed"

def getViewInfo(url, fpath):

    html = get_page_source(url)


    try:
        # soup = BeautifulSoup(html, 'html.parser')
        # viewInfo = soup.find_all('div', attrs={'class': 'online'})[0]
        # viewInfo = soup.find_all('div', attrs={'class':'ebox'})[0]
        # title = viewInfo.p.string
        # print(title)

        # numberStr = viewInfo.a.string
        # number = numberStr.split('：')[1]
        #print(number)

        #使用python来解析json

        json_data = json.loads(html)
        number = (json_data['data']['web_online'])

        #保存文件
        with open(fpath, 'a', encoding='utf-8') as f:
            nowTime = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M'))
            f.write(nowTime + "     " + str(number) + '\n')



    except:
        traceback.print_exc()



def main():
    count = 0
    while 1:
        url = "https://api.bilibili.com/x/web-interface/online"
        #文件路径
        output_path = "G://bilibiliInfo.txt"

        getViewInfo(url, output_path)
        #打印进度
        count = count + 1
        print(count)
        #延时一分钟
        time.sleep(60)


if __name__=="__main__":
    main()

