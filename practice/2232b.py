import sys
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        prefix = []

        for i in range(n):
            prefix.append(a[:i+1])


if __name__ == "__main__":
    main()
