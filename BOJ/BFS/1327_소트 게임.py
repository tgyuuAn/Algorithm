from collections import deque 

N, K = map(int,input().split())
sequence = list((input().split()))
target = sorted(sequence)
visited = set()

deq = deque()
deq.append([sequence,0])
visited.add("".join(sequence))

while deq:
    now_sequence, now_count = deq.popleft()

    if now_sequence == target:
        print(now_count)
        break

    for idx in range(len(now_sequence)-K+1):
        rarr = now_sequence[idx:idx+K]
        rarr.reverse()
        new_sequence = now_sequence[:idx] + rarr + now_sequence[idx+K:]

        if "".join(new_sequence) not in visited:
            deq.append([new_sequence, now_count+1])
            visited.add("".join(new_sequence))

else: print(-1)