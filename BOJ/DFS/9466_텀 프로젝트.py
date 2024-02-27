import sys

T = int(sys.stdin.readline())

def dfs(start, idx, now, team, not_team, visited, S):
    next = S[idx]
 
    if next in not_team:
        visited.update(now)
        visited.add(idx)
        not_team.add(idx)
        return
    
    if next in team:
        visited.update(now)
        visited.add(idx)
        not_team.add(idx)
        return

    if idx == next:
        visited.add(idx)
        team.add(idx)
        now.discard(idx)
        not_team.update(now)
        return
    
    if start == next:
        team.update(now)
        visited.update(now)
        return

    if next in visited: return

    if next in now: return
    
    now.add(next)
    dfs(start, next, now, team, not_team, visited, S)

for _ in range(T):
    N = int(sys.stdin.readline())
    S = [0]
    S.extend(list(map(int,sys.stdin.readline().split())))

    visited = set()
    team = set()
    not_team = set()

    for idx in range(1,N+1):
        if idx in visited: continue
        
        now = {idx}
        visited.add(idx)

        dfs(idx, idx, now, team, not_team, visited, S)

    print(len(({x for x in range(1,N+1)} - team)))