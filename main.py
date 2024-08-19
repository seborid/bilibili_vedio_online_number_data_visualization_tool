import json

from build_data_icon import build_icon
from get_data import get_data_in_json

#整个程序用于实现一个小想法，获取b站视频的正在观看人数，并给出可视化分析图像
def save_data_in_json(titles, urls):
    '''以json格式存储标题和网址数据'''
    filename_urls = 'urls.json'
    with open(filename_urls, 'w', encoding='utf-8') as f:
        json.dump(urls, f, ensure_ascii=False)
    filename_titles = 'titles.json'
    with open(filename_titles, 'w', encoding='utf-8') as f:
        json.dump(titles, f, ensure_ascii=False)


def read_data_in_json():
    ''''以json格式读取标题和网址数据'''
    filename_urls = 'urls.json'
    filename_titles = 'titles.json'
    with open(filename_titles, 'r', encoding='utf-8') as f:
        titles = json.load(f)
    with open(filename_urls, 'r', encoding='utf-8') as f:
        urls = json.load(f)
    return titles, urls


titles, urls = read_data_in_json()
choice = []
while choice != '5':
    choice = input('获取数据请输入1，绘制图标请输入2,修改视频地址请输入3,查看视频列表请输入4,退出程序请输入5\n')
    #没经过完整测试，可能有bug
    if choice == '1':
        if len(titles) == 0:
            print('没有视频，请输入视频后再获取数据\n')
        else:
            key=input('输入1获取10分钟数据，输入2获取1小时数据，输入3获取3小时数据，输入4获取24小时数据，输入5获取不限时数据\n'
                      '(不同时长的数据独立存储互不干扰，但是相同时长数据会被新获取的数据覆盖)\n')#五种获取数据的模式（4,5是直接写入json文件`
            get_data_in_json(urls,int(key))#图像一旦开始获取是不能中断的，中断会丢失所有数据（懒的改了

    elif choice == '2':
        key = input('输入1获取10分钟数据图像，输入2获取1小时数据图像，输入3获取3小时数据图像，输入4获取24小时数据图像,输入5获取不限时图像\n')
        build_icon(titles,int(key))#四种数据模式，两种方法

    elif choice == '3':
        print('视频列表：\n')
        i = 0
        while i < len(titles):
            print(f'第{i + 1}个视频')
            print(f'标题：{titles[i]}')
            print(f'url：{urls[i]}')
            print('')
            i += 1
        key = input('输入1增加视频，输入2删除视频\n')

        if key == '1':
            print('视频数量上限为10个')
            print('输入stop保存输入结果并退出')
            while True:
                api_bilibili = input('请输入视频的api的url\n')#api的url获取方式，在对应视频界面按F12，进行元素搜索："total"="(这里就会是正在观看的人数)"，也可以直接搜索人数
                                                           #这个正在观看人数是用js动态加载的，用get请求会遇到cookie问题，好在数据量不大，selenium的无头模式足够了
                if 'api.bilibili.com' in api_bilibili:
                    urls.append(api_bilibili)
                elif api_bilibili == 'stop':
                    break
                else:
                    print('网址输入有误，请重新输入')
                    continue
                while True:
                    title_bilibili = input('请输入视频标题\n')
                    if title_bilibili == 'stop':
                        print('还未输入标题，请输入完标题再保存')
                    else:
                        titles.append(title_bilibili)
                        break
            save_data_in_json(urls=urls, titles=titles)
            print('已退出视频输入\n')

        elif key == '2':
            while True:
                vedio_willing_delete = input('请输入要删除第几个视频（输入-1删除全部，输入0退出删除）\n')
                try:
                    vedio_willing_delete = int(vedio_willing_delete) - 1
                    if vedio_willing_delete == -1:
                        break
                    elif vedio_willing_delete == -2:
                        urls = []
                        titles = []
                        print('已删除全部视频')
                        break
                except Exception:
                    print('请输入正确数字')
                if vedio_willing_delete > len(titles):
                    print('输入数字大于总视频数，请重新输入')
                else:
                    print(f'被删除的视频的标题为:{titles.pop(vedio_willing_delete)}')
                    print(f'被删除的视频的网址为:{urls.pop(vedio_willing_delete)}')
            save_data_in_json(titles=titles, urls=urls)
            print('已退出视频删除\n')

        else:
            print('无效输入，请重新选择')

    elif choice == '4':
        i = 0
        while i < len(titles):
            print(f'第{i + 1}个视频')
            print(f'标题：{titles[i]}')
            print(f'url：{urls[i]}')
            print('')
            i += 1
        if i == 0:
            print('未存储视频\n')

    elif choice == '5':
        break
    else:
        print('无效输入，请重新选择')
print('程序退出')
