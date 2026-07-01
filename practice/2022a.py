import sys
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        n, r = map(int, input().split())
        a = list(map(int, input().split()))
        happy = 0
        for family in a:
            if family % 2 == 0:
                happy += family
                r -= happy//2
            elif r >= (family+1)//2:
                happy += family


if __name__ == "__main__":
    main()
