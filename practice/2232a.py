import sys
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))

        a.sort()

        mid = n//2

        distant_l = 0
        distant_r = 0
        for i in range(n):
            if i < mid and a[i] != a[mid]:
                distant_l += 1
            elif i > mid and a[i] != a[mid]:
                distant_r += 1
        print(max(distant_l, distant_r))


if __name__ == "__main__":
    main()
