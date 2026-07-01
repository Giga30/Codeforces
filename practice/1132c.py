import sys
from collections import defaultdict
input = sys.stdin.readline

def main():
    n, q = list(map(int, input().split()))
    intervals = []
    for i in range(q):
        l, r = map(int, input().split())
        intervals.append((l-1, r-1))
    diff = [0] * (n+1)
    for l, r in intervals:
        diff[l] += 1
        diff[r+1] -= 1
    sm = 0
    c = [0] * n
    d = [0] * n
    for i in range(n):
        sm += diff[i]
        c[i] = sm
        if c[i] == 1:
            d[i] = 1
    active = 0
    p = []
    for i in range(n):
        active += d[i]
        p.append(active)
    min_answer = float('inf')
    for x in range(q):
        pass
    print(min_answer)
if __name__ == "__main__":
    main()
