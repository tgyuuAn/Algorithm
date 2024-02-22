from collections import defaultdict

N = int(input())
M = 1_000_000_007

def divide_and_conquer(table, n):
    if n==0: return 0
    if table[n] != 0: return table[n]
    else:
        if n%2==0:
            value = ((divide_and_conquer(table,n//2) % M) * (2 * (divide_and_conquer(table,n//2-1) % M) + (divide_and_conquer(table,n//2) % M))) % M
        
        else:
            value = (((divide_and_conquer(table,(n//2)+1) % M) ** 2 % M) + ((divide_and_conquer(table,n//2) % M) ** 2 % M)) % M
        table[n] = value
        return value
    
table = defaultdict(int)
table[0] = 0
table[1] = 1
answer = divide_and_conquer(table, N)
print(answer)