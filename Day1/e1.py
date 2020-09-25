from random import randint
import math


def print_star():
    row = 4
    for i in range(row):
        for _ in range(i + 1):
            print("*", end="")
        print()
    print()
    for i in range(row):
        for j in range(row):
            if j < row - i - 1:
                print(" ", end="")
            else:
                print("*", end="")
        print()
    print()


def find_narcissistic_number():
    for num in range(100, 1000):
        low = num % 10
        mid = num // 10 % 10
        high = num // 100
        if num == low ** 3 + mid ** 3 + high ** 3:
            print(num)


def num_reverse(num):
    reverse = 0
    while num > 0:
        reverse = reverse * 10 + num % 10
        num //= 10
    print(reverse)


def hundred_chicken():
    for x in range(0, 20):
        for y in range(0, 33):
            z = 100 - x - y
            if 5 * x + 3 * y + z / 3 == 100:
                print("公鸡：%d, 母鸡：%d，小鸡：%d" % (x, y, z))


"""斐波那契数列"""
def fibonacci_sequence(num):
    sequence = [1, 1]
    for index in range(2, num):
        sequence.append(sequence[index - 1] + sequence[index - 2])
    for fibonacci in sequence:
        print(fibonacci)


"""
完美数
"""
def find_perfect():
    for num in range(2, 10000):
        factor_sum = 0
        for factor in range(1, int(math.sqrt(num)) + 1):
            if num % factor == 0:
                factor_sum += factor
                if factor > 1 and num // factor != factor:
                    factor_sum += num // factor
                if factor_sum > num:
                    break
        if factor_sum == num:
            print(num)



"""素数"""
def find_prime_number():
    for num in range(2, 100):
        is_prime = True
        for factor in range(2, int(math.sqrt(num)) + 1):
            if num % factor == 0:
                is_prime = False
                break
        if is_prime:
            print(num)


# 在参数名前面的*表示args是一个可变参数
def add(*args):
    total = 0
    for val in args:
        total += val
    return total


# 最大公约数
def gcd(x, y):
    (x, y) = (x, y) if x > y else (y, x)
    for num in range(y, 0, -1):
        if x % num == 0 and y % num == 0:
            return num


# 最小公倍数
def lcm(x, y):
    return x * y // gcd(x, y)


def main():
    # print_star()
    # find_narcissistic_number()
    # num_reverse(123)
    # hundred_chicken()
    # fibonacci_sequence(100)
    # find_perfect()
    find_prime_number()


# __name__是Python中一个隐含的变量它代表了模块的名字
# 只有被Python解释器直接执行的模块的名字才是__main__
if __name__ == '__main__':
    main()


