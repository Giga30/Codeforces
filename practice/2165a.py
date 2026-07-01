import sys
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        cost = 0
        i = 0
        operations = 0
        while operations < n-1:
            ahead = a[(i+1)%n]
            current = a[i%n]
            behind = a[(i-1)%n]

            if ahead > behind:
                cost += max(current, behind)
                a[(i-1)%n] = max(current, behind)
                i += 1
            else:
                cost += max(current, ahead)
                a[i%n] = max(current, ahead)
                i += 2
            operations += 1
        print(cost)
if __name__ == "__main__":
    main()
