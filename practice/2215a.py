import sys
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        n, k, p, q = map(int, input().split())
        a = list(map(int, input().split()))

        answer = 0
        l = 0
        min_inter_sum = min(
            sum(b % p for b in a[:k]),
            sum((c % q) % p for c in a[:k])
        )

        for i in range(n-k+1):
            inter = a[i:k+i]
            inter_sum = min(
                sum(b % p for b in inter),
                sum((c % q) % p for c in inter)
            )
            if inter_sum < min_inter_sum:
                min_inter_sum = inter_sum
                l = i
        answer += min_inter_sum

        for num in a[:l]+a[l+k:]:
            answer += min(num % p, (num % q) % p)

        print(l, answer)
if __name__ == "__main__":
    main()

