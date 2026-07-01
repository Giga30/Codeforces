import sys
input = sys.stdin.readline

def main():
    t = int(input())
    count = 0
    for _ in range(t):
        a = list(map(int, input().split()))
        count += 1 if a.count(1) > 1 else 0
    print(count)

if __name__ == "__main__":
    main()
