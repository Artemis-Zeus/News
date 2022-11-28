import re
import requests  # 读取主页面
import csv

urls = ['https://news.cctv.com/2019/07/gaiban/cmsdatainterface/page/china_%s.jsonp?cb=china','https://news.cctv.com/2019/07/gaiban/cmsdatainterface/page/world_%s.jsonp?cb=world','https://news.cctv.com/2019/07/gaiban/cmsdatainterface/page/society_%s.jsonp?cb=society']
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.56'}
title=['国内新闻','国际新闻','社会新闻']

for i in range(3):
    csv_file = open(title[i] + '.csv', 'w', newline='', encoding='gbk')
    writer = csv.writer(csv_file)

    for j in range(5):
        t = urls[i] % str(j+1)
        res = requests.get(t)
        temp = res.content.decode()
        news_list = re.findall(r'"title":"(.*?)","focus', temp)
        news_list2 = re.findall(r'"url":"(.*?).shtml"', temp)
        for k in range(len(news_list)):
            writer.writerow([news_list[k], news_list2[k]])
    print(title[i]+"已输出")
