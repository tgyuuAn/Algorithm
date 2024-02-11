first_string = input()
second_string = input()

dp_table= [[0 for _ in range(len(second_string))] for _ in range(len(first_string))]

for first_idx in range(len(first_string)):
    for second_idx in range(len(second_string)):
        if first_string[first_idx] == second_string[second_idx]:
            dp_table[first_idx][second_idx] = min(first_idx+1, second_idx+1 ,dp_table[max(0,first_idx-1)][max(0,second_idx-1)]+1)
        else: 
            dp_table[first_idx][second_idx] = min(first_idx+1, second_idx+1 ,max(dp_table[first_idx][max(0,second_idx-1)],dp_table[max(0,first_idx-1)][second_idx]))

print(dp_table[-1][-1])