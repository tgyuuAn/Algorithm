target = int(input())

def dfs(max_length, now):
    global target

    if len(now) == max_length:
        target -= 1
        if target == 0: return now
        return None
    
    if len(now) < max_length:
        if len(now) == 0:
            for num in range(10):
                result = dfs(max_length, str(num))
                if result is not None:
                    return result
        else:
            if int(now) != 0:
                for num in range(int(now[-1])):
                    result = dfs(max_length, now+str(num))
                    if result is not None:
                        return result

max_length = 1
while True:
    result = dfs(max_length, "")

    if target == 0: 
        print(result)
        break

    max_length += 1

    if max_length >= 11:
        print(-1)
        break