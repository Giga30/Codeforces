import sys
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        a = list(map(int, input().split()))
        max_streak = 0
        streak = 0
        for i in range(1, len(a)):
            if a[i] == a[i-1]:
                streak += 1
            else:
                streak = 0
            max_streak = max(max_streak, streak)
        print("YES" if max_streak+1 < m else "NO")
if __name__ == "__main__":
    main()
