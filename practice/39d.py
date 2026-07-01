import sys
input = sys.stdin.readline

def main():
    f1 = list(map(int, input().split()))
    f2 = list(map(int, input().split()))

    if f1 == [num^1 for num in f2]:
        print("NO")
    else:
        print("YES")

if __name__ == "__main__":
    main()
