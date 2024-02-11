import sys
from collections import deque, defaultdict

products_count, handleable_weight = map(int,sys.stdin.readline().split())
dp_table = [[0] * (handleable_weight+1) for _ in range(products_count+1)]

for step in range(1,products_count+1):
    product_weight, product_value = map(int,sys.stdin.readline().split())
    
    # print(product_weight, product_value)
    
    for j in range(handleable_weight+1):
        if j - product_weight < 0: dp_table[step][j] = dp_table[step-1][j]
        else: dp_table[step][j] = max(dp_table[step-1][j], dp_table[step-1][j-product_weight] + product_value)

print(dp_table[-1][-1])