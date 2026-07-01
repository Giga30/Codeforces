import sys
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        s = input().strip()
        removed = 0
        splits = [(s[:i], s[i:]) for i in range(len(s)+1)]
        for prefix, suffix in splits:
            prefix_odd = sum([1 for x in range(len(prefix)) if int(prefix[x]) % 2 == 1])
            suffix_even = sum([1 for x in range(len(suffix)) if int(suffix[x]) % 2 == 0])
            print(prefix_odd, suffix_even, prefix_odd+suffix_even)
            removed = max(removed, prefix_odd + suffix_even)
        print(removed)

if __name__ == "__main__":
    main()
