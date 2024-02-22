N = int(input())
A = list(map(int,input().split()))

DP = [[1 for _ in range(2)] for _ in range(len(A))]
answer = 1

for idx in range(1,len(A)):

    temp_bigger = 0
    temp_smaller = 0
    for prev_idx in range(idx):
        print(idx, prev_idx)

        if A[prev_idx] < A[idx]:
            temp_bigger = max(temp_bigger, DP[prev_idx][0])

        if A[prev_idx] > A[idx]:
            temp_smaller = max(temp_smaller, DP[prev_idx][0], DP[prev_idx][1])
    
    DP[idx][0] = temp_bigger + 1
    DP[idx][1] = temp_smaller + 1
    print(DP)
    answer = max(answer, max(DP[idx]))

print(DP)
print(answer)