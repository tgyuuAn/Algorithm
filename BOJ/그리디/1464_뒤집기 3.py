string = input()

for idx in range(len(string)-1):
    if string[idx] < string[idx+1]:
        string = string[idx+1]+string[:idx+1]+string[idx+2:]

print(string[::-1])