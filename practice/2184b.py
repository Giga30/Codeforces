import sys
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        s, k, m = map(int, input().split())

        if s > k:
            m = m % 2 * k
            print()
        else:
            m %= k
            print(k-m)

if __name__ == "__main__":
    main()
