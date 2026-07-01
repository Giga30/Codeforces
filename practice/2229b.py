import sys
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        max_a = 0
        sum = 0
        for i in range(n):
            if a[i] > b[i]:
                a[i], b[i] = b[i], a[i]
            max_a = max(max_a, a[i])
            sum += b[i]
        print(max_a+sum)



if __name__ == "__main__":
    main()
