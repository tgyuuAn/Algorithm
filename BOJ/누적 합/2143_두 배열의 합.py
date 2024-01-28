from collections import defaultdict

target_number = int(input())

total_a_numbers_count = int(input())
a_numbers = list(map(int,input().split()))
a_dic = defaultdict(int)
a_temp = [0]

total_b_numbers_count = int(input())
b_numbers = list(map(int,input().split()))
b_dic = defaultdict(int)
b_temp = [0]

a_accumulate = 0
for a_number in a_numbers:
    a_accumulate += a_number
    a_temp.append(a_accumulate)

for start in range(0,len(a_numbers)+1):
    for end in range(start+1,len(a_numbers)+1):
        _sum = a_temp[end] - a_temp[start]
        a_dic[_sum] += 1

b_accumulate = 0
for b_number in b_numbers:
    b_accumulate += b_number
    b_temp.append(b_accumulate)

for start in range(0,len(b_numbers)+1):
    for end in range(start+1,len(b_numbers)+1):
        _sum = b_temp[end] - b_temp[start]
        b_dic[_sum] += 1

answer = 0

for a_key in a_dic.keys():
    if b_dic[target_number - a_key] != 0:
        answer += a_dic[a_key] * b_dic[target_number - a_key]

print(answer)