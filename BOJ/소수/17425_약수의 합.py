def generate_factors_sum(number):
    temp = 0
    for i in range(1,int(number**0.5)+1):
        if number%i==0:
            temp += i
            if i != number//i:
                temp += number//i
    return temp

total_test_case = int(input())
dp_table = [None for _ in range(1_000_001)]
for number in range(1,1_000_001):
    dp_table[number] = generate_factors_sum(number)

for _ in range(total_test_case):
    max_number = int(input())

    temp = 0
    for number in range(1,max_number+1):
        temp += dp_table[number]
    print(temp)

# 시간 제한 1초 -> 2천만 연산
# N은 최대 100만 까지 가능. 한 번 약수들을 구하기 위해 log(n)번의 연산 필요.
# 즉, 100만 X log(100만) 이 되야함.
# log(100만) = log(1000) + log(1000) -> 20
# 2천만 딱 맞네.
# 여기에서 시간 초과가 난다면 dp를 이용해서 저장하면 더 깎을 수 있음.
# 근데 테스트 케이스 총 개수가 10만개네
# 
