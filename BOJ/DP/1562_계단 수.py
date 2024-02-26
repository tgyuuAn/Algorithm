N = int(input())
MOD = 1_000_000_000

# 숫자 152가 사용되면 비트 마스크로 0000100110 로 표현한다.

# DP[i][j][k] = i자리 숫자 중에서 j로 끝나는 숫자 중 k비트가 사용된 숫자.
DP = [[[0 for _ in range(1<<10)] for _ in range(10)] for _ in range(N+1)]

# 초기 세팅 (0을 제외한 1의 자리를 만들 수 있음)
for i in range(1,10):
    DP[1][i][1<<i] = 1

for i in range(1,N):
    for j in range(10):
        for k in range(1<<10):
            # 마지막 숫자가 0보다 큰 경우
            if j>0:
                next_minus_bit = k | (1 << j-1)
                DP[i+1][j-1][next_minus_bit] = (DP[i][j][k] % MOD + DP[i+1][j-1][next_minus_bit] % MOD) % MOD

            if j<9:
                next_plus_bit = k | (1 << j+1)
                DP[i+1][j+1][next_plus_bit] = (DP[i][j][k] % MOD) + (DP[i+1][j+1][next_plus_bit] % MOD) % MOD
                
answer = 0
for j in range(10):
    answer = ((DP[-1][j][-1] % MOD) + (answer % MOD)) % MOD

print(answer)