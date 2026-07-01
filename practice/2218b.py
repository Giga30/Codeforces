import sys
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        a = list(map(int, input().split()))
        a.sort()
        result = 0
        for i in range(len(a)):
            if i == 6:
                result += a[i]
            else:
                result -= a[i]
        print(result)


if __name__ == "__main__":
    main()
