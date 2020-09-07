#Uses python3
import re
import sys


def is_greater_or_equal(digit, max_num):
    return int(str(digit) + str(max_num)) >= int(str(max_num) + str(digit))


def largest_number(a):
    res = ""
    new_list = []

    while a!=[]:
        max_num = 0
        for digit in a:
            if is_greater_or_equal(digit, max_num):
                max_num = digit
        new_list.append(max_num)
        a.remove(max_num)

    for num in new_list:
        res += num

    return res


if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))