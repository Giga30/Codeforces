import sys
input = sys.stdin.readline

def main():
    grid = []
    coords = ()
    for i in range(5):
        row = list(map(int, input().split()))
        grid.append(row)
        for j in range(5):
            if row[j] == 1:
                coords = (i, j)

    print(abs(2-coords[0]) + abs(2-coords[1]))
if __name__ == "__main__":
    main()
