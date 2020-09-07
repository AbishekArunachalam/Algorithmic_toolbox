# Uses python3
import sys
import numpy as np


def calculate_val_per_item(values, weights):

    val_per_unit = list()
    for i in range(len(weights)):
        if weights[i] == 0:
            val_per_unit.append(0)
        else:
            val_per_unit.append(values[i]/weights[i])
    return val_per_unit


def get_optimal_value(capacity, values, weights):

    if len(values) == 1 and capacity > weights[0]:
        return values[0]

    val_per_unit = calculate_val_per_item(values, weights)
    sorted_index = np.argsort(val_per_unit)[::-1].tolist()
    max_value = sorted_index[0]
    sorted_index.pop(0)

    if capacity <= weights[max_value] or len(val_per_unit) == 1:
        total_value = capacity * val_per_unit[max_value]
        return total_value
    else:
        rem_capacity = capacity - weights[max_value]
        current_value = values[max_value]
    while rem_capacity > 0:

        for ind in sorted_index:
            if rem_capacity <= weights[ind]:
                total_value = current_value + (rem_capacity * val_per_unit[ind])
                return total_value
            else:
                rem_capacity = rem_capacity - weights[ind]
                current_value = current_value + values[ind]

        total_value = current_value

    return total_value



if __name__ == "__main__":
    data = list(map(int, input().split()))
    n, capacity = data[0:2]
    weights = list()
    values = list()
    for i in range(n):
        value, weight = map(int, input().split())
        values.append(value)
        weights.append(weight)
    opt_value = get_optimal_value(capacity, values, weights)
    print("{:.4f}".format(opt_value))
