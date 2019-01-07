import requests, os
from lxml import etree

# 采集1页
# 采集所有页
url = "https://www.dy2018.com/html/gndy/dyzz/index.html"
content = requests.get(url).text
root = etree.HTML(content)
pages = root.xpath("//select/option/@value")
for page in pages:
    url = "https:www.dy2018.com" + page
    # print(url)
    content = requests.get(url)
    content.encoding = content.apparent_encoding
    content = content.text
    movie_titles = root.xpath("//b/a/@title")
    movie_hrefs = root.xpath("//b/a/@herf")
    for movie_title, movie_herf in zip(movie_titles, movie_hrefs):
        movie_href = "" + movie_href
        # 标题只保留尖括号< >里面的
        content = requests.get(movie_herf)
        content.encoding = content.apparent_encoding
        content = content.text
        root = etree.HTML(content)
        ### download_url = root.xpath("//anchor/a/text()")#在检查中anchor存在,但是在源码中anchor不存在 故写法不对
        download_url = root.xpath("//td[@bgcolor='#fdfddf']/a/text()")[0]  #一电影可能有多个下载地址,[0]表示只要第0个
        print(movie_title,download_url)