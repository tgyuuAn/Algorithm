from heapq import *

card_count = int(input())
cards = []

for _ in range(card_count):
    heappush(cards,int(input()))

answer = 0
while len(cards)>1:
    one, two = heappop(cards), heappop(cards)
    answer += (one+two)
    heappush(cards,one+two)

print(answer)