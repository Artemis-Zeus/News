import re
import requests  # 读取主页面
import csv

# 传入三个目标网页 %s是为了后续的添加页码值进行修改，起始值为1
urls = ['https://news.cctv.com/2019/07/gaiban/cmsdatainterface/page/china_%s.jsonp?cb=china',
        'https://news.cctv.com/2019/07/gaiban/cmsdatainterface/page/world_%s.jsonp?cb=world',
        'https://news.cctv.com/2019/07/gaiban/cmsdatainterface/page/society_%s.jsonp?cb=society']

# 插入头
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.56'}

# 存储格式为csv，title为csv文件名/新闻分类
title = ['国内新闻', '国际新闻', '社会新闻']

# 分别对三个网址进行爬虫，并存储到对应文件（文件不存在直接创建）
# newline目的是为了防止存储csv文件时出现空行，encoding='gbk' 中文utf-8会出现乱码
for i in range(3):
    csv_file = open(title[i] + '.csv', 'w', newline='', encoding='gbk')
    writer = csv.writer(csv_file)
    # 修改对应网页的页数，并且将对应标题和url写入文件
    for j in range(5):
        t = urls[i] % str(j + 1)
        res = requests.get(t)
        temp = res.content.decode()

        # 检索对应标题名和url
        news_list = re.findall(r'"title":"(.*?)","focus', temp)
        news_list2 = re.findall(r'"url":"(.*?).shtml"', temp)
        # 写入文件
        for k in range(len(news_list)):
            writer.writerow([news_list[k], news_list2[k]])
    print(title[i] + "已输出")


# SCNU 黄晓楠
