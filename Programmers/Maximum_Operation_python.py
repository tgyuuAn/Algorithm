def solution(expression):
    operations = [('+', '-', '*'),('+', '*', '-'),('-', '+', '*'),('-', '*', '+'),('*', '+', '-'),('*', '-', '+')]
    answer = []
    for op in operations:
        a = op[0]
        b = op[1]
        temp_list = []
        for e in expression.split(a):
            temp = [f"({i})" for i in e.split(b)]
            print(temp)
            temp_list.append(f'({b.join(temp)})')
            print(temp_list)
        answer.append(abs(eval(a.join(temp_list))))
    return max(answer)
