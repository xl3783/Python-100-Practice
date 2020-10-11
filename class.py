"""
但是，Python并没有从语法上严格保证私有属性或方法的私密性，
它只是给私有的属性和方法换了一个名字来妨碍对它们的访问，
事实上如果你知道更换名字的规则仍然可以访问到它们，
下面的代码就可以验证这一点。之所以这样设定，可以用这样一句名言加以解释，
就是"We are all consenting adults here"。
因为绝大多数程序员都认为开放比封闭要好，
而且程序员要自己为自己的行为负责。
"""

class Test:

    def __init__(self, foo):
        self.__foo = foo

    def __bar(self):
        print(self.__foo)
        print('__bar')


def test1():
    test = Test('hello')
    test._Test__bar()
    print(test._Test__foo)

"""
@property装饰器
"""
class Person(object):
    """
    __slots__魔法
    需要注意的是__slots__的限定只对当前类的对象生效，对子类并不起任何作用。
    """
    # 限定Person对象只能绑定_name, _age和_gender属性
    __slots__ = ('_name', '_age', '_gender')

    def __init__(self, name, age):
        self._name = name
        self._age = age

    # 访问器 - getter方法
    @property
    def name(self):
        return self._name

    # 访问器 - getter方法
    @property
    def age(self):
        return self._age

    # 修改器 - setter方法
    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print('%s正在玩飞行棋.' % self._name)
        else:
            print('%s正在玩斗地主.' % self._name)

def test2():
    person = Person('王大锤', 12)
    person.play()
    person.age = 22
    person.play()
    # person.name = '白远方' # AttributeError: can't set attribute

def test3():
    person = Person('王大锤', 22)
    person.play()
    person._gender = '男'
    # AttributeError: 'Person' object has no attribute '_is_gay'
    # person._is_gay = True

"""
静态方法
@staticmethod
"""
"""
类方法
@classmethod
"""
from time import time, localtime, sleep


class Clock(object):
    """数字时钟"""

    def __init__(self, hour=0, minute=0, second=0):
        self._hour = hour
        self._minute = minute
        self._second = second

    @classmethod
    def now(cls):
        ctime = localtime(time())
        return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)

    def run(self):
        """走字"""
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def show(self):
        """显示时间"""
        return '%02d:%02d:%02d' % \
               (self._hour, self._minute, self._second)


def test4():
    # 通过类方法创建对象并获取系统时间
    clock = Clock.now()
    while True:
        print(clock.show())
        sleep(1)
        clock.run()


from abc import ABCMeta, abstractmethod


class Pet(object, metaclass=ABCMeta):
    """宠物"""

    def __init__(self, nickname):
        self._nickname = nickname

    @abstractmethod
    def make_voice(self):
        """发出声音"""
        pass


class Dog(Pet):
    """狗"""

    def make_voice(self):
        print('%s: 汪汪汪...' % self._nickname)


class Cat(Pet):
    """猫"""

    def make_voice(self):
        print('%s: 喵...喵...' % self._nickname)


class OriginCat(Cat):
    """橘猫"""

    def make_voice(self):
        print('%s: 喵...' % self._nickname)


def test5():
    pets = [Dog('旺财'), Cat('凯蒂'), Dog('大黄'), OriginCat('小黄')]
    for pet in pets:
        pet.make_voice()



if __name__ == "__main__":
    # test1()
    # test2()
    # test3()
    # test4()
    test5()