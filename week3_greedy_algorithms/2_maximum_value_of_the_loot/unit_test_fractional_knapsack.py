import unittest
import random
from fractional_knapsack import calculate_val_per_item, get_optimal_value

class TestFractionalKnapsack(unittest.TestCase):

    def testBorderCases(self):
        n = random.randint(1, 10 ^ 3)
        print(f'n: {n}')
        capacity = random.randint(0, 2*(10 ^ 6))
        print(f'capacity: {capacity}')
        weights = list()
        values = list()
        for i in range(n):
            weight = random.randint(0, 2*(10 ^ 6))
            value = random.randint(1, 2*(10 ^ 6))
            weights.append(weight)
            values.append(value)
        opt_value = get_optimal_value(capacity, values, weights)
        print("{:.4f}".format(opt_value))
        self.testBorderCases()


if __name__ == '__main__':
    unittest.main()
