import sys
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        h = list(map(int, input().split()))
        w = [0] * n

        for i in range(n):
            cur = h[i]
            prev = h[i-1] 
            w[i] = 
        print(w)

        
                

if __name__ == "__main__":
    main()
