N = int(input())
numbers = list(map(str,input().split()))
numbers.sort(reverse=True, key = lambda x:x*9)

print(int("".join(numbers)))