from collections import deque

total_people, total_party = map(int,input().split())
who_knows_the_truth = deque(map(int,input().split()))
who_knows_the_truth.popleft()
who_knows_the_truth = set(who_knows_the_truth)
parties = []

for _ in range(total_party):
    party = deque(map(int,input().split()))
    party.popleft()
    party = set(party)
    parties.append(party)

    check = party - who_knows_the_truth
    if len(party) != len(check):
        who_knows_the_truth.update(party)

answer = 0
for party in parties:
    check = party - who_knows_the_truth
    if len(party) == len(check):
        answer += 1

print(answer)