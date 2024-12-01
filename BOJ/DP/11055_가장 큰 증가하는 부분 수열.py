N = int(input())
A = list(map(int,input().split()))

DP = [0 for _ in range(len(A))]
answer = 0

for idx in range(len(A)):
    temp_bigger = 0
    for prev_idx in range(idx):
        if A[prev_idx] < A[idx]:
            temp_bigger = max(temp_bigger, DP[prev_idx])
            
    DP[idx] = temp_bigger + A[idx]
    answer = max(answer, DP[idx])

print(answer)