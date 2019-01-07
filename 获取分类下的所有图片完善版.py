import requests,os   # 获取网页源码
from lxml import etree  # 解析网页源码

# import urllib.request     导入
# urllib.request.urlretrieve()  用
from  urllib.request import urlretrieve  # 与上面的导入作用相同引用时写法不一样
# urlretrieve()
url = "http://www.ivsky.com/tupian/"
content = requests.get(url).text
root = etree.HTML(content)
big_category = root.xpath("//ul[@class='tpmenu']/li/a/text()")  # //.../@标签   或者   //...@text() -标签之间的文字
bog_category_url = root.xpath("//ul[@class='tpmenu']/li/a/@href")
for name, url in zip(big_category, bog_category_url):
    # os.makedirs(name, exist_ok=True)
    url = 'http://www.ivsky.com' + url
    content = requests.get(url).text
    root = etree.HTML(content)
    small_Category = root.xpath("//div[@class='sline']/div/a/text()")
    small_Category_url = root.xpath("//div[@class='sline']/div/a/@href")
    for name2,url in zip(small_Category,small_Category_url ):
        os.makedirs(name + '/' + name2, exist_ok=True)
        page = 1
        while True:
            new_url = 'http://www.ivsky.com' + url+f'/index_{page}.html'
            content = requests.get(new_url).text
            root = etree.HTML(content)
            img_src= root.xpath("//img/@src")   #图片地址
            if img_src:    #如果列表不为空
                for src in img_src:
                    # split :切割,分割
                    img_name = src.split('/')[-1]    #将字符串以"/"开割形成一个字符串数组，然后再通过索引[-1]取出所得数组中的倒数第1个元素的值。
                    print(img_name)
                    # 图片路径 = 文件夹路径 + / + 图片名字.jpg
                    urlretrieve(src, name + '/' + name2 + '/' + img_name)
                print(f"下载{name}{name2}第{page}页")
                page+=1
            else:
                print(f"{name}{name2}到达最后一页了")
                break