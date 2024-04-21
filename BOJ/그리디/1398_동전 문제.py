import sys
from collections import deque

def input(): return sys.stdin.readline().rstrip()

T = int(input())
for _ in range(T):
    target = deque(map(int,input()))
    count = 0

    while target:
        # 만약 길이가 짝수라면,
        if len(target)%2 == 0:
            if target[0] >= 5:
                target[0] = target[0] - 2
                target[1] = target[1] - 5

                if target[1] < 0:
                    target[0] -= 1
                    target[1] += 10

                count += 1

            elif target[0] >= 2:
                # 만약 일의 자리가 5보다 크다면,
                if target[1] >= 5:

                    target[0] = target[0] - 2
                    target[1] = target[1] - 5
                    count += 1
                
                else:
                    target[0] = target[0] - 1
                    count += 1

            else:
                target[0] = target[0] - 1
                count += 1

        # 만약 길이가 홀수라면,
        else:
            if target[0] > 0:
                target[0] = target[0] - 1
                count += 1

        while target and target[0] == 0: 
            target.popleft()

    print(count)