str = input()
answer = ""
for x in str:
    if x.islower():
        answer+=x.upper()
    else:
        answer+=x.lower()
print(answer)