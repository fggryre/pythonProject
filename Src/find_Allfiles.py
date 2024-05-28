import os   # 递归遍历所有文件

file_path = '.\\filelist.txt'


def func(path):
    for i in os.listdir(path):
        path2 = os.path.join(path, i)  # 拼接绝对路径
        if os.path.isdir(path2):  # 判断如果是文件夹,调用本身
            func(path2)
        else:
            print(i)
            # 写入文件
            with open(file_path, 'a') as file:
                file.write(i)
                file.write('\n')


func(r'C:\Users\zhuwei\Desktop\国轩资料\学习资料\文件')
