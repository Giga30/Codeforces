import sys
input = sys.stdin.readline

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    boxes = 0
    remainder = float('inf')
    box_type = None
    for i in range(k):
        box = a[i]
        if n % box < remainder:
            remainder = n % box
            boxes = n // box
            box_type = i+1
    print(box_type, boxes)


if __name__ == "__main__":
    main()
