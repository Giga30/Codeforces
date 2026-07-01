import sys
import math
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        n, x = map(int, input().split())
        a = list(map(int, input().split()))
        print(max(max(a), math.ceil(sum(a)/x)))
if __name__ == "__main__":
    main()
