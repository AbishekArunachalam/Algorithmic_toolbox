import time
import unittest
from gcd import gcd_naive, gcd_fast

class TestGCD(unittest.TestCase):

	def test_GCD_boundaries(self):
		values = input()
		a,b = map(int, values.split())
		start_time= time.time()
		result1 = gcd_naive(a, b)
		print(f"Runtime Naive:{time.time() - start_time}")
		start_time = time.time()
		result2 = gcd_fast(a, b)
		print(f"Runtime Fast:{time.time() - start_time}")
		self.assertEqual(result1, result2)


if __name__ == '__main__':
	unittest.main()