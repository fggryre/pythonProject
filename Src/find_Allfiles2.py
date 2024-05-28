import os

file_path = 'C:\\Users\\zhuwei\\Desktop\\国轩资料\\学习资料\\文件'


# for a, b, c in os.walk(r'D:\爬虫'):
for a, b, c in os.walk(file_path):  # a代表所在根目录;b代表根目录下所有文件夹(以列表形式存在);c代表根目录下所有文件
    for i in c:
        print(i)  # 结果与方法一相同

print(os.getcwd())  # 获取当前文件绝对地址。
gen = os.walk(os.getcwd())
print(type(gen))

for a, b, c in os.walk(os.getcwd()):  # a代表所在根目录;b代表根目录下所有文件夹(以列表形式存在);c代表根目录下所有文件
    for i in c:
        print(i)
