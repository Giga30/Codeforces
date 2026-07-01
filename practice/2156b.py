import sys
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        n, q = map(int, input().split())
        s = input().strip()
        a = list(map(int, input().split()))
        has_b = 'B' in s
        for i in range(q):
            if not has_b:
                print(a[i])
            else:
                j = 0
                while a[i] != 0: 
                    if s[j%n] == 'A':
                        a[i] -= 1
                    else:
                        a[i] //= 2
                    j += 1
                print(j)


if __name__ == "__main__":
    main()
