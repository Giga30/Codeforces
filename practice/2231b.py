import sys
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        diffs = [0]
        for index, num in enumerate(a):
            if index < n-1:
                diffs.append(num-a[index+1])
        k = max(diffs)
        sorted = True
        for index, num in enumerate(a):
            if index < n-1:
                if num > a[index+1]:
                    a[index+1] += k
                if num > a[index+1]:
                    sorted = False
        print("Yes" if sorted else "No")
        

if __name__ == "__main__":
    main()
