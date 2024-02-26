N = int(input())
solution = list(map(int,input().split()))
solution.sort()

def check(x, mid, solution):
    if solution[x] + solution[mid] > 0: return True
    return False

min_cost = int(1e10)
answer = []
for x in range(N-1):
    left = x
    right = N

    while left+1<right:
        mid = (left+right)//2

        if check(x,mid,solution): right = mid
        else: left = mid

    if x != left and abs(solution[x] + solution[left]) < min_cost:
        min_cost = abs(solution[x] + solution[left])
        answer = [solution[x], solution[left]]

    if right<N and abs(solution[x] + solution[right]) < min_cost:
        min_cost = abs(solution[x] + solution[right])
        answer = [solution[x], solution[right]]

print(*answer)