import sys
import math
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        x = math.ceil((max(a)-min(a))/2)
        print(x)


if __name__ == "__main__":
    main()
