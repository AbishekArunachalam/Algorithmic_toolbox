# python3
import sys


def compute_min_refills(distance, tank, stops):
    # write your code here
    stops.insert(0, 0)
    stops.insert(len(stops), distance)

    if tank >= distance:
        return 0

    if stops[1] <= tank:
        first_stop = [stop for stop in stops if stop <= tank][-1]
        stop_idx = stops.index(first_stop)
        stops = stops[stop_idx+1:]
        last_refuel_stop = first_stop
        num_stations = 1

        for ind, current_stop in enumerate(stops):
            if ind == (len(stops) - 1):
                destination = stops[ind]
                if destination - last_refuel_stop > tank:
                    return -1
                else:
                    return num_stations
            if (current_stop - last_refuel_stop) > tank:
                return -1
            elif (stops[ind+1]-last_refuel_stop) <= tank:
                continue
            else:
                last_refuel_stop = current_stop
                num_stations = num_stations+1
    return -1


if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    num_stops = compute_min_refills(d, m, stops)
    print(num_stops)