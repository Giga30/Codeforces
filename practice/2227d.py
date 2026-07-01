import sys
import math
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        
        x, y = None, None

        for i in range(n*2):
            if a[i] == 0:
                if x is None:
                    x = i
                else:
                    y = i

        max_mex = 0
        x_palin = expand(n*2, a, x, x)
        y_palin = expand(n*2, a, y, y)
        max_mex = max(max_mex, mex(a[x_palin[0]:x_palin[1]+1]))
        max_mex = max(max_mex, mex(a[y_palin[0]:y_palin[1]+1]))
        center = x + (y-x)/2
        if center.is_integer():
            center = int(center)
            center_palin = expand(n*2, a, center, center)
        else:
            center = math.floor(center)
            center_palin = expand(n*2, a, center, center+1)
        max_mex = max(max_mex, mex(a[center_palin[0]:center_palin[1]+1]))
        print(max_mex)


def expand(n, arr, l, r):
    while l >= 0 and r < n and arr[l] == arr[r]:
        l-=1
        r+=1
    return l+1, r-1

def mex(arr):
    num_set = set(arr)
    mex = 0
    while mex in num_set:
        mex += 1
    return mex

if __name__ == "__main__":
    main()
