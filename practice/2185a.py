import sys
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())

        print(*[i+1 for i in range(n)])

if __name__ == "__main__":
    main()
