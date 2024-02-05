def generate_prime_numbers(max_num):
    prime_numbers = set(x for x in range(2,max_num+1))

    for i in range(2,int(max_num**0.5)+1):
        for j in range(2*i,max_num+1,i):
            prime_numbers.discard(j)

    return sorted(list(prime_numbers))

_input = int(input())

# 8 이상은 모두 표현 가능
if _input <= 7: print("-1")

else:
    answer = []
    # 짝수일 경우,
    if _input%2==0:
        answer.extend([2,2])
        _input -= 4

    # 홀수일 경우,
    else:
        answer.extend([2,3])
        _input -= 5

    prime_numbers = generate_prime_numbers(_input)
    left = 0
    right = len(prime_numbers)-1

    while left <= right:
        now = prime_numbers[left] + prime_numbers[right]
        print(now)
        if now < _input: left += 1
        elif now > _input: right -= 1
        else: 
            answer.extend([prime_numbers[left], prime_numbers[right]])
            break
        
    print(*sorted(answer))