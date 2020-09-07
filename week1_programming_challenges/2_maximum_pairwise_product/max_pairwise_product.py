# python3


def max_pairwise_product(numbers):

    n = len(numbers)
    numbers.sort(reverse = True)
    max_num = numbers[0]
    second_max_num = numbers[1]
    max_product = max_num*second_max_num

    return max_product

if __name__ == '__main__':

    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
