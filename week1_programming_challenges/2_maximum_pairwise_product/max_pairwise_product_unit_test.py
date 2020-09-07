import unittest
import random
from max_pairwise_product import max_pairwise_product, max_pairwise_product_fast

class TestMaxPairwiseProduct(unittest.TestCase):

    def testMaxPairwiseProductRepeatedElements(self):
        num = 5
        numbers_list = [10, 10, 20, 40, 60]
        product1 = max_pairwise_product(numbers_list)
        product2 = max_pairwise_product_fast(numbers_list)
        self.assertEquals(product1, product2)

    # def testMaxPairwiseBorderElements(self):
    #     num = random.randint(2, 2*(10^5))
    #     numbers_list = random.sample(range(0, 2*(10^5)), num)
    #     product1 = max_pairwise_product(numbers_list)
    #     product2 = max_pairwise_product_fast(numbers_list)
    #     self.assertEquals(product1, product2)
    #
    # def testMaxPairwiseProduct(self):
    #     num = random.randint(2, 2*(10^5))
    #     numbers_list = random.sample(range(0, 2*(10^5)), num)
    #     product1 = max_pairwise_product(numbers_list)
    #     product2 = max_pairwise_product_fast(numbers_list)
    #     self.assertEquals(product1, product2)

if __name__ == '__main__':
        unittest.main()
