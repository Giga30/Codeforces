import sys
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        if n == 10:
            print(-1)
        else:
            r = n % 12
            a = 0
            if r <= 9:
                a = r
            elif r == 10:
                a = 22
            else:
                a = 11
            print(a, n-a)

if __name__ == "__main__":
    main()
