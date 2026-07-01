import sys
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        x = int(input())
        n = len(str(x))
        print(10 if n != 1 and x % (9**(n-1)) == 0 else 0)

if __name__ == "__main__":
    main()
