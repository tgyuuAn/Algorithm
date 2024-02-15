target = int(input())

dp_table = [0 for _ in range(3)]
dp_table[0] = 0
dp_table[1] = 1

for idx in range(2,target+1):
    idx %= 3
    dp_table[idx] = dp_table[idx-1] + dp_table[idx-2]

print(dp_table[target%3])