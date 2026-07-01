import sys
from collections import defaultdict
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        sortable = True
        chains = defaultdict(list)

        for i in range(1, n+1):
            root = i
            while root % 2 == 0:
                root //= 2
            chains[root].append(i)

        for root, indices in chains.items():
            current_values = sorted([a[i-1] for i in indices])
            expected_values = sorted(indices)

            if current_values != expected_values:
                sortable = False
        print("YES" if sortable else "NO")


if __name__ == "__main__":
    main()
