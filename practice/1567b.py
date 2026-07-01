import sys
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        s = 0
        if (a-1)%4 == 0:
            s = a-1
        elif (a-1)%4 == 1:
            s = 1
        elif (a-1)%4 == 2:
            s = a
        else:
            s = 0
        need = s ^ b
        if need == 0:
            print(a)
        elif need != a:
            print(a+1)
        else:
            print(a+2)

if __name__ == "__main__":
    main()
