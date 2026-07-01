import sys
import math
input = sys.stdin.readline

def main():
    n = int(input())
    friends = list(map(int, input().split()))

    fingers = sum(friends)
    overlaps = (n+1) / math.gcd(n+1, fingers)
    final_i = fingers%(n+1)

    
if __name__ == "__main__":
    main()
