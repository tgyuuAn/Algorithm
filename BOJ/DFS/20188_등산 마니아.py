from itertools import permutations
import sys

def input(): return sys.stdin.readline().rstrip()

tree = [[] for _ in range(N)]
N = int(input())
for _ in range(N-1):
    node1, node2 = map(int, input().split())
    tree[node1].append(node2)
    tree[node2].append(node1)

for x, y in permutations(range(N), 2):
    print(x, y)
    