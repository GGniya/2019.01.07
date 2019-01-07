import requests
#encode 编码
# 在网页编码转换出现乱码时,使用
url = "https://www.dy2018.com/html/gndy/dyzz/index.html"
content = requests.get(url)
content.encoding=content.apparent_encoding
content = content.text
print(content)