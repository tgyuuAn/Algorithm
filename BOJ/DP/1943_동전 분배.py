import sys

def input(): return sys.stdin.readline().rstrip()

N = input()
while N != "":
    try:
        DP = [False for _ in range(50_001)]
        DP[0] = True
        accumulate = 0
        
        for _ in range(int(N)):
            coin, count = map(int, input().split())
            accumulate += (coin * count)
            
            for now_idx in range(50_000, -1, -1):
                for use_count in range(count,0,-1):
                    if (coin * use_count) > now_idx: continue
                
                    if DP[now_idx - (coin * use_count)]:
                        for true_idx in range(now_idx - (coin * use_count), now_idx+1, coin):
                            DP[true_idx] = True
                        break

        if accumulate%2 == 1:
            print(0)
            continue
        
        if DP[accumulate//2]: print(1)
        else: print(0)
        
        N = ""
        N = input()
    except: break