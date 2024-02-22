import sys

plumb_counts = int(sys.stdin.readline())
plumbs = list(map(int,sys.stdin.readline().split()))
marble_counts = int(sys.stdin.readline())
marble_weights = list(map(int,sys.stdin.readline().split()))

sum_plubs_weight = sum(plumbs)

# 가운데는 0, 가운데 부터 왼쪽은 -, 오른쪽은 +
dp_table = [False for _ in range((sum_plubs_weight*2)+1)]

# 0은 가능하므로 True로 바꿈
dp_table[sum_plubs_weight] = True

for plumb in plumbs:
    # 더하기 (구슬의 반대 편에 추를 올림)
    for idx in range(len(dp_table)-1,plumb-1,-1):
        if dp_table[idx-plumb]: dp_table[idx] = True

    # 빼기 (구슬의 저울 쪽에 추를 올림)
    for idx in range(len(dp_table)-plumb):
        if dp_table[plumb+idx]: dp_table[idx] = True

answer = []

for marble in marble_weights:
    if marble > sum_plubs_weight: answer.append("N")
    elif dp_table[sum_plubs_weight+marble]: answer.append("Y")
    else: answer.append("N")

print(*answer)