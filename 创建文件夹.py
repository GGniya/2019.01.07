import os
# make 创建文件夹
# dir = directory=文件夹
# dirs =一堆文件夹
# 参数1 path 文件夹路径
# 参数2 mode 文件夹权限/模式
# 参数3 exist_ok:是否存在,默认False 也就是说不改,运行第二是会报错
os.makedirs('a',exist_ok=True)
os.makedirs('1/2/3',exist_ok=True)
