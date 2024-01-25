total_numbers_count = int(input())
numbers = list(map(int,input().split()))

answer = [-1 for _ in range(total_numbers_count)]
temp = []

for idx, i in enumerate(range(len(numbers))):
    now = numbers[i]

    while temp:
        if temp[-1][1] < now:
            temp2 = temp.pop()
            answer[temp2[0]] = now
        else:
            break

    temp.append([idx,now])
        
print(*answer)