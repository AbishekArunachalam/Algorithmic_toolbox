import unittest
import random
import numpy as np

from sorting import randomized_quick_sort, partition3

class TestQuickSort(unittest.TestCase):

    def test_border_case_1(self):
        a = [5]
        n = len(a)
        print(randomized_quick_sort(a, 0, n - 1))

    def test_border_case_2(self):
        a = np.random.choice(range(1, 100000), 1000000000, replace = True)
        n = len(a)
        print(randomized_quick_sort(a, 0, n - 1))

if __name__ == "__main__":
    unittest.main()