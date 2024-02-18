number = int(input())

answer = {x:0 for x in range(10)}

def make_number_beautiful(answer, number, place_idx):
    while number % 10 != 9:
        number += 1
        for digit in str(number):
            answer[int(digit)] -= 10 ** place_idx
    return number

for place_idx in range(len(str(number))):
    number = make_number_beautiful(answer, number, place_idx)
    number //= 10
    
    for digit in range(10):
        answer[digit] += (number+1) * (10 ** place_idx)

    answer[0] -= 10 ** place_idx
    place_idx += 1

print(*answer.values())