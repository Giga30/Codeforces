import sys
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        n, s, x = map(int, input().split())
        a = list(map(int, input().split()))
        if s-sum(a) % x == 0:
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    main()
