import sys

total_test_case = int(input())

for _ in range(total_test_case):
    coins_type = int(sys.stdin.readline())
    coins = list(map(int,sys.stdin.readline().split()))
    target = int(sys.stdin.readline())
    
    dp_table = [0 for _ in range(target+1)]
    dp_table[0] = 1

    for coin in coins:
        for column in range(coin,target+1):
            dp_table[column] = dp_table[column] + dp_table[column-coin]
    
    print(dp_table[-1])