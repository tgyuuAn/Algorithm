from itertools import combinations, product

def get_dice_sum_list(dice, idxes):
    sum_list = []
    
    for sum_idxes in product(range(6), repeat=len(idxes)):
        accumulate = 0

        for pick_dice_idx, sum_idx in zip(idxes,sum_idxes):
            accumulate += dice[pick_dice_idx][sum_idx]

        sum_list.append(accumulate)
    return sorted(sum_list)

def get_a_win_count(a_dice_sum_list, b_dice_sum_list):
    total_win_count = 0

    for a_element in a_dice_sum_list:
        left, right = 0, len(a_dice_sum_list)
        win_count = 0

        while left+1 < right:
            mid = (left+right)//2
            if check(a_element, b_dice_sum_list[mid]):
                left = mid
                win_count = mid

            else: right = mid

        total_win_count += win_count+1

    return total_win_count

def check(a,b):
    if a>b: return True
    return False

def solution(dice):
    n = len(dice)

    max_win_count = -1
    max_win_indexes = []
    for a_dice_idxes in combinations(range(n),n//2):
        b_dice_idxes = []
        for b_dice_idx in range(n):
            if b_dice_idx in a_dice_idxes: continue

            b_dice_idxes.append(b_dice_idx)


        a_dice_sum_list = get_dice_sum_list(dice, a_dice_idxes)
        b_dice_sum_list = get_dice_sum_list(dice, b_dice_idxes)

        win_count = get_a_win_count(a_dice_sum_list, b_dice_sum_list)

        if win_count > max_win_count: 
            max_win_count = win_count
            max_win_indexes = a_dice_idxes

    return list(map(lambda x : x+1,max_win_indexes))

dice = [[1, 2, 3, 4, 5, 6], [3, 3, 3, 3, 4, 4], [1, 3, 3, 4, 4, 4], [1, 1, 4, 4, 5, 5]]
print(solution(dice))