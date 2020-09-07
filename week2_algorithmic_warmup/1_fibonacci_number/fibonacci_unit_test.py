import unittest
import time
import random
from fibonacci import calc_fib_naive
from fibonacci import calc_fib_fast

class TestFibonacciMethods(unittest.TestCase):

    def test_simple_series(self):
        n = int(input())
        start_time = time.time()
        val1 = calc_fib_naive(n)
        print("Naive %s seconds ---" % (time.time() - start_time))
        start_time = time.time()
        val2 = calc_fib_fast(n)
        print("Fast %s seconds ---" % (time.time() - start_time))
        print(f'Val1: {val1}')
        print(f'Val2: {val2}')
        self.assertEquals(val1, val2)

if __name__ == '__main__':
    unittest.main()