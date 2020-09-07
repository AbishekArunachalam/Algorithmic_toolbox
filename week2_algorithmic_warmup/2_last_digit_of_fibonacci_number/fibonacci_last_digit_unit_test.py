import time
import unittest
from fibonacci_last_digit import get_fibonacci_last_digit_naive, get_fibonacci_last_digit_fast

class TestFibonacciLastDigit(unittest.TestCase):

    def testExtremeCase(self):
        n = int(input())
        start_time = time.time()
        result1 = get_fibonacci_last_digit_naive(n)
        print(result1)
        print("Naive %s seconds ---" % (time.time() - start_time))
        start_time = time.time()
        result2 = get_fibonacci_last_digit_fast(n)
        print(result2)
        print("Naive %s seconds ---" % (time.time() - start_time))
        self.assertEqual(result1, result2)

    def testLowestCase(self):
        n = int(input())
        start_time = time.time()
        result1 = get_fibonacci_last_digit_naive(n)
        print(result1)
        print("Naive %s seconds ---" % (time.time() - start_time))
        start_time = time.time()
        result2 = get_fibonacci_last_digit_fast(n)
        print(result2)
        print("Naive %s seconds ---" % (time.time() - start_time))
        self.assertEqual(result1, result2)

if __name__ == '__main__':
    unittest.main()
