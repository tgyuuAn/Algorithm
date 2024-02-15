N = int(input())

dp_table = [[0 for _ in range(10)] for _ in range(N+1)]

for i in range(1,10):
    dp_table[1][i] = 1

for step in range(2,N+1):
    for num in range(10):
        if num != 0 and num != 9:
            dp_table[step][num] = dp_table[step-1][num-1] + dp_table[step-1][num+1]
          
        elif num == 0:
            dp_table[step][num] = dp_table[step-1][num+1]

        elif num == 9:
            dp_table[step][num] = dp_table[step-1][num-1]

print(sum(dp_table[-1])%1_000_000_000)