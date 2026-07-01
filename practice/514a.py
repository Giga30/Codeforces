import sys
input = sys.stdin.readline

def main():
    x = input().strip()

    result = ""
    for i in range(len(x)):
        if (i == 0 and x[i] == '9') or int(x[i]) < 5:
            result += x[i]
            continue
        if int(x[i]) > 4:
            result += str(9-int(x[i]))
    print(int(result))

if __name__ == "__main__":
    main()
