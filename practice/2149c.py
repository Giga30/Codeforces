import sys
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        z = a.count(k)
        b = set(a)
        c = k - len(set(range(k)) & b)
        print(max(c, z))
if __name__ == "__main__":
    main()
