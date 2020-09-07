# Uses python3
import sys

def optimal_summands(n):
    summands = list()
    balance = n
    for i in range(n):
        current_val = i + 1
        next_val = current_val+1
        balance = balance - current_val
        if next_val > balance and balance <= current_val:
            summands.append(balance+current_val)
            break
        else:
            summands.append(current_val)

    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
