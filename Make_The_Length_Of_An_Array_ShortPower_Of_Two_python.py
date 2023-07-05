def solution(arr):
    table = [2**x for x in range(11)]
    length = len(arr)
    for idx,level in enumerate(table):
        if length <= level:
            for x in range(table[idx]-length):
                arr.append(0)
            break
    return arr