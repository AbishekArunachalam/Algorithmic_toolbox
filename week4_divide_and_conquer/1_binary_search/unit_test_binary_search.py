import unittest
import random
from binary_search import binary_search

class TestBinarySearch(unittest.TestCase):

    def test_lower_border_case(self):
        x = random.sample(range(1, 500), 100)
        a = random.sample(range(1, 500), 200)
        for num in x:
            print(f'x : {num}, index : {binary_search(a, num)}')

    def test_higher_border_case(self):
        start = 1
        stop = (10**9)+1
        limit = (10**5)+1
        x = [random.randint(start, stop) for i in range(limit)]
        a = [random.randint(start, stop) for i in range((3*(10**4))+1)]
        for num in x:
            print(f'x : {num}, index : {binary_search(a, num)}')




if __name__ == "__main__":
    unittest.main()