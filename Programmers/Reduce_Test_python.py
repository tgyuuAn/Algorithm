from functools import reduce

def reduceTest(x,y):
    return x*y

def solution(num):
    
    return sum(num) if len(num) >= 11 else reduce(reduceTest,num)