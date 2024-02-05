total_numbers_count = int(input())
numbers = list(map(int,input().split()))

numbers.sort()
answer = 0

for idx, number in enumerate(numbers):
    left = 0
    right = len(numbers)-1

    if idx == left:
        left += 1

    if idx == right:
        right -= 1

    while left < right:
        now = numbers[left] + numbers[right]

        if now == number:
            answer += 1
            break

        elif now < number:
            if left + 1 == idx: left += 2
            else: left += 1

        elif now > number:
            if right - 1 == idx: right -= 2
            else: right -= 1

    print(left,right)

print(answer)