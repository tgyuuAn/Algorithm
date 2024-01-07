from collections import defaultdict

sequence_length = int(input())

sequence = []
dic = defaultdict(int)
visited = [False for _ in range(sequence_length+1)]
visited[0] = True

for _ in range(sequence_length):
    element = int(input())

    if visited[element] == False:
        if visited[element-1] == False:
            dic[element-1] = element
            dic[element] = element-1
            visited[element] = True
            visited[element-1] = True

        else:
            dic[element] = element
            visited[element] = True

    sequence.append(element)

new_sequence = []
for idx, element in enumerate(sequence):
    new_sequence.append(dic[element])

for element in new_sequence:
    print(element)