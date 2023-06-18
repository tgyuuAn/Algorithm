def solution(num_list):
    odd_sum = ""
    even_sum = ""
    for num in num_list:
        if num%2!=0:
            odd_sum += str(num)
        else:
            even_sum += str(num)
    return int(odd_sum) + int(even_sum)