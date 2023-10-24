from collections import defaultdict
from collections import deque


def solution(enroll, referral, seller, amount):
    dic = defaultdict(int)
    person_mapper = dict()

    for e, r in zip(enroll,referral):
        person_mapper[e] = r

    for s, a in zip(seller,amount):
        dic[s] += a*100
        deq = deque()
        deq.append([s,a*100])

        while deq:
            now = deq.popleft()
            now_person, now_money = now[0], now[1]

            parent_person = person_mapper[now_person]
            
            parent_money = int(now_money/10)
            
            if parent_money == 0:
                continue
                
            dic[parent_person] += parent_money
            dic[now_person] -= parent_money

            if parent_person != "-":
                deq.append([parent_person, parent_money])

    return [dic[x] for x in enroll]