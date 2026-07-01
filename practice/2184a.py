import sys
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(n if n<=3 else n % 2)

if __name__ == "__main__":
    main()
