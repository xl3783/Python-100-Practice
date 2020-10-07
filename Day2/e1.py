def string_test():
    # 前面加上字母   r  表示不转义
    print(r'\'hello, world!\'')
    # 使用*运算符来重复一个字符串的内容
    print('hello\n' * 3)
    # 用[]和[:]运算符从字符串取出某个字符或某些字符（切片运算）
    s1 = '0123456789'
    print('s1[2])', s1[2])
    print('s1[3:7]', s1[3:7])
    print('s1[:5]', s1[:5])
    print('s1[-5:]', s1[-5:])
    print('s1[-3:-1]', s1[-3:-1])
    print('s1[::2]', s1[::2])
    print('s1[::-1]', s1[::-1])

    # 内置库处理
    str1 = 'hello, world!'
    # 通过内置函数len计算字符串的长度
    print(len(str1))  # 13
    # 获得字符串首字母大写的拷贝
    print(str1.capitalize())  # Hello, world!
    # 获得字符串每个单词首字母大写的拷贝
    print(str1.title())  # Hello, World!
    # 获得字符串变大写后的拷贝
    print(str1.upper())  # HELLO, WORLD!
    # 从字符串中查找子串所在位置
    print(str1.find('or'))  # 8
    print(str1.find('shit'))  # -1
    # 与find类似但找不到子串时会引发异常
    # print(str1.index('or'))
    # print(str1.index('shit'))
    # 检查字符串是否以指定的字符串开头
    print(str1.startswith('He'))  # False
    print(str1.startswith('hel'))  # True
    print(str1.endswith('!'))  # True
    # 将字符串以指定的宽度居中并在两侧填充指定的字符
    print(str1.center(20, '*'))
    # 将字符串以指定的宽度靠右放置左侧填充指定的字符
    print(str1.rjust(50, ' '))
    str2 = 'abc123456'
    # 检查字符串是否由数字构成
    print(str2.isdigit())  # False
    # 检查字符串是否以字母构成
    print(str2.isalpha())  # False
    # 检查字符串是否以数字和字母构成
    str1.isalnum()
    print(str2.isalnum())  # True
    str3 = '  jackfrued@126.com '
    print(str3)
    # 获得字符串修剪左右两侧空格之后的拷贝
    print(str3.strip())
    # 在字符串前加上字母  f  ，我们可以使用下面的语法糖来简化上面的代码
    # 需要使用{ 时， 需要使用{{
    a, b = 5, 10
    print(f'{{a}} * {b} = {a * b}')
    # 可使用for循环进行遍历
    for i in str1:
        print(i)


def list_test():
    list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
    list2 = sorted(list1)
    # sorted函数返回列表排序后的拷贝不会修改传入的列表
    # 函数的设计就应该像sorted函数一样尽可能不产生副作用
    list3 = sorted(list1, reverse=True)
    # 通过key关键字参数指定根据字符串长度进行排序而不是默认的字母表顺序
    list4 = sorted(list1, key=len)
    list5 = sorted(list1, key=lambda l: l[2])
    print(list1)
    print(list2)
    print(list3)
    print(list4)
    print(list5)
    # 给列表对象发出排序消息直接在列表对象上进行排序
    list1.sort(reverse=True)
    print(list1)


def list_test2():
    f = [x for x in range(1, 10)]
    print(f)
    f = [x + y for x in 'abcde' for y in '12345677']
    print(f)
    # 把一个列表中所有的字符串转换成小写，非字符串元素原样保留
    L = ['TOM', 'Peter', 10, 'Jerry']
    # 用列表生成式实现
    print([x.lower() if isinstance(x, str) else x for x in L])
    # 把一个列表中所有的字符串转换成小写，非字符串元素移除
    L = ['TOM', 'Peter', 10, 'Jerry']
    # 用列表生成式实现
    print([x.lower() for x in L if isinstance(x, str)])


if __name__ == '__main__':
    list_test2()
