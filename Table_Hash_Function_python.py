def solution(data, col, row_begin, row_end):
    answer = 0
    
    data = sorted(data,key = ((lambda x : (x[col - 1], -x[0]))))
    
    temp_list = []
    for i in range(row_begin,row_end+1):
        temp = 0
        for d in data[i-1]:
            temp+=d % i
        temp_list.append(temp)
    
    for j in temp_list:
        answer ^= j
    return answer


''' 
정렬할 때 여러개의 조건으로 key를 넣어주기 위해서 key = (조건1, 조건2) 로 넣어주면 된다.

위 조건에서는 2번째 항을 기준으로 오름차순으로 정렬하고 만약 동일할 경우 첫 번째 값을 기준으로 내림차순 하기 때문에,

lambda 안의 하나의 x로 해결 할 수 있었고, 오름차순과 내림차순을 동시에 구현하기 위해 뒤의 기준에 마이너스를 붙여서 오름차순으로 내림차순을 만들었다.

비트 연산

& = and
| = or
^ = xor
~ = not
<< = 비트 왼쪽 시프트
>> = 비트 오른쪽 시프트
'''