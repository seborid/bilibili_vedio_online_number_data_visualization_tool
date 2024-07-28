import json

import matplotlib.pyplot as plt
import plotly.graph_objs as go

plt.rcParams['font.sans-serif'] = 'SimHei'


def build_icon(titles, key):
    '''画出可视化图像'''
    try:
        with open(f'data{key}.json', 'r') as f:#提取对应模式的json文件
            number_data = json.load(f)
    except FileNotFoundError:
        print('未获取过数据，请先启动对应数据获取程序获取数据')
    else:  # 绘制图像，得到x轴，y轴信息
        print()
        x = []
        y = []
        i = 0
        while i < len(titles):
            y.append([])
            i += 1

        for number in number_data:
            x.append(f'{number[2]}\n时\n{number[3]}\n分')#适用于matplotlib的x轴，在下面plotly处会重写
            i = 0
            while i < len(titles):
                y[i].append(number[i + 4])
                i += 1

        while True:
            choice = input(
                '请选择制图方式,输入1为matplotlib折线图（png格式），输入2为Plotly折线图（html格式）,退出制图请输入3\n')
            if choice == '1':#matplotlib，不大好看，不推荐
                i = 0
                if key == 1:
                    length = 10
                elif key == 2:
                    length = 20
                elif key == 3:
                    length = 50
                else:
                    length = 20
                while i < len(titles):
                    plt.figure(figsize=(length, 6))
                    plt.plot(x, y[i], label=f'{titles[i]}', marker='o')
                    plt.title(f'{number_data[0][0]}月{number_data[0][1]}日"{titles[i]}"正在观看数据图像')
                    plt.xlabel('时间')
                    plt.ylabel('人数')
                    plt.legend()
                    plt.grid(True)
                    plt.savefig(f'数据模式{key}下的{titles[i]}正在观看数据图像.png')#以不同名字保存图像
                    plt.close()
                    i += 1

            elif choice == '2':
                x = []
                for number in number_data:#重写x轴，因为一些历史遗留问题，这里支持时间为int和str两种格式，历史遗留问题解决后可以只保存str格式
                    if type(number[0]) == int:
                        x.append(f'2024-{number[0]:02d}-{number[1]:02d} {number[2]:02d}:{number[3]:02d}')
                    else:
                        x.append(f'2024-{number[0]}-{number[1]} {number[2]}:{number[3]}')
                i = 0
                while i < len(titles):
                    data = go.Scatter(x=x, y=y[i], mode='lines+markers')
                    fig = go.Figure(data)
                    fig.add_trace(
                        go.Scatter(name=f'{number_data[0][0]}月{number_data[0][1]}日"{titles[i]}"正在观看数据图像'))
                    fig.update_layout(
                        title=f'{number_data[0][0]}月{number_data[0][1]}日"{titles[i]}"正在观看数据图像',
                        xaxis_title='时间',
                        yaxis_title='人数',
                        font=dict(
                            family="SimHei"
                        )
                    )
                    xaxis = dict(type='date')
                    if type(number[0][0]) == int:
                        fig.write_html(
                            f'data_of_{i}_in_{number_data[0][0]:02d}{number_data[0][1]:02d}_with_{key}form.html')
                    else:
                        fig.write_html(f'data_of_{i}_in_{number_data[0][0]}{number_data[0][1]}_with_{key}_form.html')#因为文件名不支持中文，所以用英文格式
                    i += 1

            elif choice == '3':
                print('退出制图')
                break

            else:
                print('无效输入，请重新输入')
                continue
