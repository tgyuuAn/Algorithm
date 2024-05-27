import sys

def input(): return sys.stdin.readline().rstrip()

N = int(input())
eggs = []
is_broken = [False for _ in range(N)]
for _ in range(N):
    durability, weight = map(int, input().split())
    eggs.append([durability, weight])

answer = 0
def dfs(eggs, is_borken, depth):
    global answer
    
    if depth == len(eggs):
        answer = max(answer, sum(is_borken))
        return
    
    if is_borken[depth]:
        dfs(eggs, is_borken, depth+1)
        return
    
    can_hit = False

    now_egg = eggs[depth]
    now_durability, now_weight = now_egg[0], now_egg[1]

    for poor_idx in range(N):
        if poor_idx == depth: continue
        if is_borken[poor_idx]: continue
    
        can_hit = True
        
        poor_egg = eggs[poor_idx]
        poor_durability, poor_weight = poor_egg[0], poor_egg[1]

        new_now_durability = now_durability - poor_weight
        new_poor_durability = poor_durability - now_weight
        
        if new_now_durability <= 0: is_borken[depth] = True
        if new_poor_durability <= 0: is_borken[poor_idx] = True

        eggs[depth], eggs[poor_idx] = [new_now_durability, now_weight], [new_poor_durability, poor_weight]
        dfs(eggs, is_borken, depth+1)
        eggs[depth], eggs[poor_idx] = [now_durability, now_weight], [poor_durability, poor_weight]

        is_borken[depth] = False
        is_borken[poor_idx] = False
        
    if can_hit == False: answer = max(answer, sum(is_borken))
    return

dfs(eggs, is_broken, 0)
print(answer)