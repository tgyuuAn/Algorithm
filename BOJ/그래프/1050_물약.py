import sys
from collections import defaultdict

def input(): return sys.stdin.readline().rstrip()

N, M = map(int, input().split())

cost = defaultdict(lambda : int(1e9))
receipes = defaultdict(list)
for _ in range(N):
    ingredient, ingredient_cost = input().split()
    cost[ingredient] = int(ingredient_cost)

for _ in range(M):
    result, receipe = input().split("=")
    ingredients = receipe.split("+")
    
    receipes[result].append(list((int(ingredient[0]), ingredient[1:]) for ingredient in ingredients))

def update_price(target, receipes, cost):
    loop_flag = False
    
    for receipe in receipes:
        
        accumulate = 0
        for (count, ingredient) in receipe:

            if ingredient not in cost: break
            
            accumulate += (count * cost[ingredient])
        
        else:
            if target not in cost or accumulate < cost[target]:
                loop_flag = True
                cost[target] = accumulate

    return loop_flag

loop_flag = True

while loop_flag:
    loop_flag = False
    
    for target in receipes:
        loop_flag |= update_price(target, receipes[target], cost)

print(min(1000000001,cost["LOVE"])) if "LOVE" in cost else print("-1")