import sys

def input(): return sys.stdin.readline().rstrip()

N, M, L, K = map(int, input().split())

xs = []
ys = []
stars = []
for _ in range(K):
    x, y = map(int, input().split())
    xs.append(x)
    ys.append(y)
    stars.append((x, y))
    
answer = 0
for start_x in xs:
    for start_y in ys:
        end_x, end_y = start_x+L, start_y+L

        temp = 0
        for star in stars:
            if start_x <= star[0] <= end_x and start_y <= star[1] <= end_y:
                temp += 1
    
        answer = max(answer, temp)
print(K-answer)