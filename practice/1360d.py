import sys
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        ans = n
        for i in range(1, int(n**0.5)+1):
            if n % i == 0:
                if i <= k:
                    ans = min(ans, n // i)
                if n//i <= k:
                    ans = min(ans, i)
        print(ans)
if __name__ == "__main__":
    main()
