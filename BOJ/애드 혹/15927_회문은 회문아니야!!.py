string = input()

if string != string[::-1]:
    print(len(string))

elif string[1:] == string[:0:-1]:
    print(-1)

else: print(len(string)-1)