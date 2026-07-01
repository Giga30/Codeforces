import sys
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        grid = []
        for _ in range(n):
            row = list(map(int, input().split()))
            grid.append(row)
        result = 0
        temp_result = 0
        for i in range(n):
            for j in range(n):
                if grid[j][i] < 0:
                    diag_i = i
                    diag_j = j
                    while diag_i < n and diag_j < n:
                        grid[diag_j][diag_i] = 0
                        diag_i += 1
                        diag_j += 1
                    temp_result += 1
        result += temp_result
        while temp_result != 0:
            temp_result = 0
            for i in range(n):
                for j in range(n):
                    if grid[j][i] < 0:
                        diag_i = i
                        diag_j = j
                        while diag_i < n and diag_j < n:
                            grid[diag_j][diag_i] = 0
                            diag_i += 1
                            diag_j += 1
                        temp_result += 1
            result += temp_result
        print("answer: " + str(result))

                    
if __name__ == "__main__":
    main()
