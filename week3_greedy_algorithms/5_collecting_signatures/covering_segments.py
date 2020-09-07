# Uses python3
import sys
import numpy
import collections

Segment = collections.namedtuple('Segment', 'start end')


def optimal_points(segments):

    points = []
    segments = sorted(segments, key=lambda s: s.end)
    r = -1
    for segment in segments:
        if r < segment.start:
            r = segment.end
            points.append(r)
    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
