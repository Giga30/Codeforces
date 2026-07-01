import sys
from collections import defaultdict
input = sys.stdin.readline

def main():
    n = int(input())
    connections = defaultdict(int)
    for _ in range(n-1):
        u, v = map(int, input().split())
        connections[u] += 1
        connections[v] += 1
    print(list(connections.values()).count(1))

if __name__ == "__main__":
    main()
