import re #regex正则表达式
# 匹配字符串中的数字
content = "欢迎来到2019年01月07日"
# 一个一个数字匹配
# pattern = re.compile(r"\d")
# 匹配连续的4个数字
# pattern = re.compile(r"\d{4}")
# 匹配连续的数字，至少1个，至多4个
# pattern = re.compile(r"\d{1,4}")
# 匹配至少1个数字,最多不确定
pattern = re.compile(r"\d{1,}")
result = pattern.findall(content)
print(result)
# 匹配< >中的内容
content = "2019年最新电影<大黄蜂>正在上映"
pattern = re.compile(r"<(.*?)>")
result = pattern.findall(content)
print(result)
