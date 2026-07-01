import sys
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        s = input().strip()
        result = True
        for i in range(n):
            if i < n-k and s[i] != s[i+k]:
                result = False
            if i >= n-k and i < n-1 and s[i] == 1:
                result = False
            print(i >= n-k, i < n-1, s[i] == 1, i >= n-k and i < n-1 and s[i] == 1)
            print('\n')

if __name__ == "__main__":
    main()
