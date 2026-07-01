import sys
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        b = list(map(int, input().split()))
        
        b.sort(reverse=True)

        x, y = b[0], b[1]
        if n == 2:
            print(x,y)
            continue
        mod = x % y
        
        permutable = True
        for i in range(2, n):
            if mod != b[i]:
                permutable = False
                break
            mod = b[i-1] % b[i]
        if permutable:
            print(x, y)
        else:
            print(-1)

if __name__ == "__main__":
    main()
