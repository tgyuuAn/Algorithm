from collections import defaultdict
import sys

def input(): return sys.stdin.readline().rstrip()

dic = defaultdict(int)

for num in input():
    num = int(num)
    dic[num] += 1

answer = 0
for num in range(9):
    if num == 6: answer = max(answer, (dic[num] + dic[9] +1)//2)
    else: answer = max(answer, dic[num])

print(answer)