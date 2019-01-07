a = ['a', 'b', 'c', 'd']
b = [20, 30, 40, 50]
# # 1 通过索引遍历 (不推荐)
# for i in range(len(a)):
#     name=a[i]
#     print(name)
# #  2通过in 遍历
# for i in a:     #   a为列表名字
#     print(i)
#   同时遍历多个列表
# zip压缩
#  前提: 列表长度需要保持一致 不一致会按照长度最短的遍历(会导致数据丢失)
for i, j in zip(a, b):
    print(i, j)
