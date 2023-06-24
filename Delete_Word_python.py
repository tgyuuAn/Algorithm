def solution(my_string, indices):
    answer = ''
    my_string = list(my_string)
    for indice in sorted(indices, reverse=True):
        my_string.pop(indice)
    return "".join(my_string)