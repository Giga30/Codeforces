import sys
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        print("Sakurako" if n % 2 == 0 else "Kosuke")

if __name__ == "__main__":
    main()
