def make_new_lock(lock):
    new_lock = []

    for _ in range(len(lock)):
        new_lock.append([2 for _ in range(len(lock[0])*3)])

    for row_lock in lock:
        temp = []
        temp.extend([2 for _ in range(len(row_lock))])
        temp.extend(row_lock)
        temp.extend([2 for _ in range(len(row_lock))])
        new_lock.append(temp)

    for _ in range(len(lock)):
        new_lock.append([2 for _ in range(len(lock[0])*3)])

    return new_lock

def rotate_key(key):
    rotated_key = []

    for col in range(len(key[0])):
        
        temp = []
        for row in range(len(key)):
            temp.append(key[len(key)-row-1][col])

        rotated_key.append(temp)

    return rotated_key

def solution(key, lock):
    new_lock = make_new_lock(lock)

    hole_count = 0

    for row in range(len(new_lock)):
        for col in range(len(new_lock)):
            if new_lock[row][col] == 0:
                hole_count += 1

    for _ in range(4):
        
        for row in range(len(lock)-len(key), len(lock)*2+1):
            for col in range(len(lock)-len(key), len(lock)*2+1):
                temp = 0

                for inner_row in range(row, row+len(key)):
                    for inner_col in range(col, col+len(key)):
                        if key[inner_row-row][inner_col-col] == 1 and new_lock[inner_row][inner_col] == 0:
                            temp += 1
                            

                        elif key[inner_row-row][inner_col-col] == 1 and new_lock[inner_row][inner_col] == 1:
                            temp += int(1e9)

                if hole_count == temp: return True

        key = rotate_key(key)

    return False