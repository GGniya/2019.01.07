import requests  #获取网页源码
from lxml import etree   #解析网页源码
import os       #os=operation = 操作系统=查看CPU/硬盘/创建文件夹/.....
# 获取某个网页源码
url = "http://www.ivsky.com/tupian/"
content = requests.get(url).text
# print(content)
# 使用etree解析源码 ,使用xpath提取数据
root = etree.HTML(content)
big_category = root.xpath("//ul[@class='tpmenu']/li/a/text()")    #//.../@标签   或者   //...@text() -标签之间的文字
# print(big_category)       #列表格式输出
#         len = length 长度
#        创建文件夹
# for i in range(len(big_category)):
#     name = big_category[i]        #获取大分类,由于len相同,与下面的代码合并
#     os.makedirs(name,exist_ok=True)
# 获取大分类下的小分类
bog_category_url = root.xpath("//ul[@class='tpmenu']/li/a/@href")
for i in range(len(bog_category_url )):
    name = big_category[i]
    os.makedirs(name,exist_ok=True)
    url = bog_category_url[i]
    url = 'http://www.ivsky.com'+url
    # print(url)
    content=requests.get(url).text
    root = etree.HTML(content)
    small_Category = root.xpath("//div[@class='sline']/div/a/text()")
    # print(small_Category)
    for j in range (len(small_Category)):
        name2=small_Category[j]
        # /自然风光/自然风光
        os.makedirs(name+'/'+name2, exist_ok=True)