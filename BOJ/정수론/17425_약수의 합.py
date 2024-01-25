import sys

MAX_NUM = 1_000_000

factor_numbers_sum = [0 for x in range(MAX_NUM+1)]
accumulate_factor_numbers_sum = [0 for x in range(MAX_NUM+1)]

for number in range(1,MAX_NUM+1):
    temp = 1
    while number*temp <= MAX_NUM:
        factor_numbers_sum[temp*temp]+=number

    accumulate_factor_numbers_sum[number] = accumulate_factor_numbers_sum[number-1] + factor_numbers_sum[number]

total_test_case = int(sys.stdin.readline())

for _ in range(total_test_case):
    target_number = int(input())
    print(accumulate_factor_numbers_sum[target_number])