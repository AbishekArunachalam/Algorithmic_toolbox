import unittest
import random
from car_fueling import compute_min_refills


class TestCarFuelling(unittest.TestCase):

    def test_car_fueling(self):

        distance = random.randint(1, 10^5)
        tank = random.randint(1, 400)
        num_stops = random.randint(1, 300)
        stops = list()
        for stop in range(num_stops):
            refil_stop = random.randint(1, 400)
            stops.append(refil_stop)
        print(f'Dist: {distance}')
        print(f'Tank: {tank}')
        print(f'Stops: {stops}')
        num_stops = compute_min_refills(distance, tank, stops)
        print(num_stops)

if __name__ == '__main__':
    unittest.main()

