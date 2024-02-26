import sys

N = int(sys.stdin.readline())
prices = list(map(int,sys.stdin.readline().split()))
money = int(sys.stdin.readline())

DP = ["0" for _ in range(money+1)]

for idx, price in enumerate(prices[::-1]):
    idx = N - idx -1

    for _ in range(money//price):
        for now_money in range(money, price-1, -1):

            if DP[now_money] == "0": 
                DP[now_money] = str(idx)

            now_room_number = DP[now_money]
            new_room_number = DP[now_money-price] + str(idx)

            DP[now_money] = str(max(int(now_room_number), int(new_room_number)))

print(DP[-1])
