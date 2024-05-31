msg = "today is a good day"

# title()字符串首字母大写
print(msg.title())

# upper()字符串全大写
print(msg.upper())

# 字符串全小写
print(msg.lower())

# pycharm多行绿字注释可以前后三个单引号括起来表示
'''
'''

# 在字符串中使用变量：f字符串
first_name = "zhu"
last_name = "wei"
print(f"my name is {first_name} {last_name}")
print(f"my name is {first_name} {last_name}".title())

# 使用制表符和空格可以控制输出字符串格式，更加美观
new_msg = "Program_Language:\n\tpython\n\tC++\n\tJava"
print(new_msg)


# variable.lstrip()   清除变量左侧的空格
# variable.rstrip()   清除变量右侧空格
# variable.strip()    清除变量两侧空格

# 练习

def msg_generater(name):
    msg = f'{name} once said, “A person who never made a mistake never tried anything new.”'
    return msg

famous_person = "Albert Einstein"
print(msg_generater(famous_person))
famous_person = "\tAlbert Einstein\n"
print(msg_generater(famous_person))
famous_person = (famous_person.lstrip())
print(msg_generater(famous_person))
famous_person = "\tAlbert Einstein\n".rstrip()
print(msg_generater(famous_person))
famous_person = "\tAlbert Einstein\n".strip()
print(msg_generater(famous_person))



