import sys
input = sys.stdin.readline

def main():
    x_sum = 0
    y_sum = 0
    z_sum = 0
    n = int(input())
    for _ in range(n):
        x, y, z = map(int, input().split())
        x_sum += x
        y_sum += y
        z_sum += z

    print("YES" if x_sum == 0 and y_sum == 0 and z_sum == 0 else "NO")


if __name__ == "__main__":
    main()
