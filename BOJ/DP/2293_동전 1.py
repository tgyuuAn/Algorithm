coins_type, target = map(int,input().split())

coins = []
for _ in range(coins_type): coins.append(int(input()))

dp_table = [0 for _ in range(target+1)]
dp_table[0] = 1

for row, coin in enumerate(coins):
    for column in range(coin,target+1):
        dp_table[column] = dp_table[column] + dp_table[column-coin]

    print(dp_table)

print(dp_table[-1])