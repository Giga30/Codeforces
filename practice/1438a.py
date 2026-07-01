import sys
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(*[1]*n)

if __name__ == "__main__":
    main()
