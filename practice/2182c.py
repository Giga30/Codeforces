import sys
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        c = list(map(int, input().split()))

        seen = set([])
        
        a1 = a
        b1 = b
        c1 = c
        added = True
        while added:
            min_head = []
            for index, num in enumerate(a1):
                if not min_head:
                    min_head = (index, num)
                elif min_head[1] > num:
                    min_head = (index, num)
            torso_candidates = []
            for k in range(len(b1)):
                torso = b1[k]
                if torso > min_head[1]:
                    torso_candidates.append(torso)
            min_torso = []
            for index, num in enumerate(b1):
                if not min_torso:
                    min_torso = (index, num)
                elif min_torso[1] > num:
                    min_torso = (index, num)
            leg_candidates = []
            for j in range(len(c1)):
                legs = c1[j]
                if legs > min_torso[1]:
                    leg_candidates.append(legs)
            min_legs = []
            for index, num in enumerate(c1):
                if not min_legs:
                    min_legs = (index, num)
                elif min_legs[1] > num:
                    min_legs = (index, num)
            added = False
            print(min_head, min_torso, min_legs)
            
            

                
        print(seen)
if __name__ == "__main__":
    main()
