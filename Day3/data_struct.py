def dict_use():
    # 创建字典的字面量语法
    scores = {'骆昊': 95, '白元芳': 78, '狄仁杰': 82}
    # 创建字典的构造器语法
    items1 = dict(one=1, two=2, three=3, four=4)
    # 通过zip函数将两个序列压成字典
    items2 = dict(zip(['a', 'b', 'c'], '123'))
    # 创建字典的推导式语法
    items3 = {num: num ** 2 for num in range(1, 10)}
    print(items1, items2, items3)
    # 对字典中所有键值对进行遍历
    for key in scores:
        print(f'{key}: {scores[key]}')
    if '武则天' in scores:
        print(scores['武则天'])
    print(scores.get('武则天'))
    print(scores.popitem())
    print(scores.pop('骆昊', 100))


# 练习1：在屏幕上显示跑马灯文字。
def excise1():
    import os
    import time
    content = '北京欢迎你为你开天辟地…………'
    while True:
        os.system('cls')
        print(content)
        time.sleep(0.2)
        content = content[1:] + content[0]


# 练习2：设计一个函数产生指定长度的验证码，验证码由大小写字母和数字构成
def excise2():
    import random
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    code = ''
    code_len = 4
    for _ in range(code_len):
        code += all_chars[random.randint(0, len(all_chars) - 1)]
    return code


# 练习3：设计一个函数返回给定文件名的后缀名。
def excise3(filename):
    return str.split(filename, '.')[-1]


# 练习4：设计一个函数返回传入的列表中最大和第二大的元素的值。
def excise4(data_list):
    if len(data_list) < 1:
        return None
    (max_v, second) = (data_list[0], data_list[0])
    for value in data_list:
        if value > max_v:
            second = max_v
            max_v = value
        elif value > second:
            second = value
    return max_v, second


if __name__ == '__main__':
    print(excise2())
    print(excise3('asdasd.ss.text'))
    print(excise4([1, 2, 3, 4, 5, 6, 7, 1231, 44, 21]))
