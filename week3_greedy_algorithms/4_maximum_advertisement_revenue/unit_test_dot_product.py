import unittest
import random
from dot_product import max_dot_product


class TestDotProduct(unittest.TestCase):

    def test_border_cases(self):
        n = random.randrange(1, (10 ^ 3) + 1)
        a = list()
        b = list()
        for i in range(0, n):
            a.append(random.randrange(-(10 ^ 5), 10 ^ 5))
            b.append(random.randrange(-(10 ^ 5), 10 ^ 5))
        print(a)
        print(b)
        print(max_dot_product(a, b))


if __name__ == '__main__':
    unittest.main()



