import sys
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = [1]

        for _ in range(n-1):
            a.append(a[-1]+2)
        print(*a)

if __name__ == "__main__":
    main()
