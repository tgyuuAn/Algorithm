N = int(input())

dp_table = [[[0]*4 for _ in range(10)] for _ in range(N+1)]

for i in range(10):
    dp_table[1][i][0] = 1

for step in range(2,N+1):
    for num in range(10):
        if num != 0 and num != 9:
            for count in range(2):
                if step == 2:
                    if num == 0: continue
                    
                    if count != 0:
                        dp_table[step][num-1][count] = dp_table[step-1][num-1][count]

                    elif count == 0:
                        dp_table[step][num][count] = dp_table[step-1][num+1][count]

                else:
                    if count != 0:
                        dp_table[step][num][count] = dp_table[step-1][num-1][count-1]

                    elif count == 0:
                        dp_table[step][num][count] = sum(dp_table[step-1][num-1][2:4])

            for count in range(2,4):
                if count != 2:
                    dp_table[step][num][count] = dp_table[step-1][num+1][count-1]

                elif count == 2:
                    dp_table[step][num][count] = sum(dp_table[step-1][num+1][:2])

        elif num == 0:
            for count in range(2,4):
                if count != 2:
                    dp_table[step][num][count] = dp_table[step-1][num+1][count-1]

                elif count == 2:
                    dp_table[step][num][count] = sum(dp_table[step-1][num+1][:2])

        elif num == 9:
            if step == 2:
                dp_table[step][num][0] = dp_table[step-1][num-1][0]
                continue

            for count in range(2):
                if count != 0:
                    dp_table[step][num][count] = dp_table[step-1][num-1][count-1]

                elif count == 0:
                    dp_table[step][num][count] = sum(dp_table[step-1][num-1][2:4])

print(dp_table[-1])

answer = 0
for num in range(10):
    for count in range(4):
        answer += dp_table[-1][num][count]

print(answer)

# [[1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0]]

