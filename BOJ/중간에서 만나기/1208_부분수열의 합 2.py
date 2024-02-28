import sys
from collections import Counter
from itertools import product

N, target = map(int,sys.stdin.readline().split())
numbers = list(map(int,sys.stdin.readline().split()))

# 홀수개 일 경우 ex) 9개면 0~4까지 A배열 5~8까지 B배열임.
# 짝수개 일 경우 ex) 10개면 0~4까지 A배열 5~9까지 B배열임.
# 그럼 N+1의 절반을 하면 되겠다.
A = numbers[:(N+1)//2] 
B = numbers[(N+1)//2:]

A_dedications = []
for idx in product(range(2), repeat=len(A)):
    temp = 0
    for i, value in enumerate(idx):
        if value == 1:
            temp += A[i]
            
    A_dedications.append(temp)

B_dedications = []
for idx in product(range(2), repeat=len(B)):
    temp = 0
    for i, value in enumerate(idx):
        if value == 1:
            temp += B[i]
            
    B_dedications.append(temp)
    
A_dedications = Counter(A_dedications)
B_dedications = Counter(B_dedications)

answer = 0
for dedication in B_dedications:
    B = B_dedications[dedication]
    
    if target - dedication in A_dedications:
        A = A_dedications[target - dedication]
        answer += B * A
        continue
        
if target == 0: answer -= 1
        
print(answer)