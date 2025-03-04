import sys

def input(): return sys.stdin.readline().rstrip()

N, K = map(int, input().split())
DP = [[] for _ in range(12)]

DP[1] = ["1"]
DP[2] = ["1+1", "2"]
DP[3] = ["1+2", "1+1+1", "2+1", "3"]

for idx in range(4,N+1):
    for gap in range(3,0,-1):
        for previous in DP[idx-gap]:
            DP[idx].append(f"{previous}+{str(gap)}")
            
if len(DP[N]) < K: 
    print(-1)
else:
    answer = sorted(DP[N])
    print(answer[K-1])