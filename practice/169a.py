import sys
input = sys.stdin.readline

def main():
    n, a, b = map(int, input().split())
    h = list(map(int, input().split()))

    h.sort()

    print(h[b] - h[b-1])
if __name__ == "__main__":
    main()
