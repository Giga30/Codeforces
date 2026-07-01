import sys
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))

        print("YES" if a.count(67) > 0 else "NO")

if __name__ == "__main__":
    main()
