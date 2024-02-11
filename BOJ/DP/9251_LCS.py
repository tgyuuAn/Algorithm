first_string = input()
second_string = input()

dp_table= [0 for _ in range(len(first_string)) for _ in range(len(second_string))]

for first_idx in range(1,len(first_string)):
    for second_idx in range(1,len(second_string)):
        if first_string[first_idx] == second_string[second_idx]:
            dp_table[first_idx][second_idx] = dp_table[first_idx][second_idx-1]+1

print(*dp_table)