def BFS(list,list_xy,now_x,now_y,direction,value,flag):
    now_x = int(now_x)
    now_y = int(now_y)
    value = int(value)

    if direction=="U":
        for temp_y in range(now_y+1,now_y+value+1):
            print([now_x,temp_y])
            if [now_x,temp_y] in list_xy:
                if flag[list_xy.index([now_x,temp_y])+1] == True:
                    flag[list_xy.index([now_x,temp_y])+1] = False
                    now_y = temp_y
                    return BFS(list,list_xy,now_x,now_y,list[list_xy.index([now_x,temp_y])][2],list[list_xy.index([now_x,temp_y])][3],flag)

                else: return -1
            now_y = temp_y

        return [now_x,now_y]
        
    elif direction=="D":
        for temp_y in range(now_y-1,now_y-value-1,-1):
            print([now_x,temp_y])
            if [now_x,temp_y] in list_xy:
                if flag[list_xy.index([now_x,temp_y])+1] == True:
                    flag[list_xy.index([now_x,temp_y])+1] = False
                    now_y = temp_y
                    return BFS(list,list_xy,now_x,now_y,list[list_xy.index([now_x,temp_y])][2],list[list_xy.index([now_x,temp_y])][3],flag)

                else: return -1
            now_y = temp_y

        else:
            return [now_x,now_y]

    elif direction=="R":
        for temp_x in range(now_x+1,now_x+value+1):
            print([temp_x,now_y])
            if [temp_x,now_y] in list_xy:
                if flag[list_xy.index([temp_x,now_y])+1] == True:
                    flag[list_xy.index([temp_x,now_y])+1] = False
                    now_x = temp_x
                    return BFS(list,list_xy,now_x,now_y,list[list_xy.index([temp_x,now_y])][2],list[list_xy.index([temp_x,now_y])][3],flag)

                else: return -1
            now_x = temp_x
        return [now_x,now_y]

    elif direction=="L":
        for temp_x in range(now_x-1,now_x-value-1,-1):
            print([temp_x,now_y])
            if [temp_x,now_y] in list_xy:
                if flag[list_xy.index([temp_x,now_y])+1] == True:
                    flag[list_xy.index([temp_x,now_y])+1] = False
                    now_x = temp_x
                    return BFS(list,list_xy,now_x,now_y,list[list_xy.index([temp_x,now_y])][2],list[list_xy.index([temp_x,now_y])][3],flag)

                else: return -1
            now_x = temp_x
        return [now_x,now_y]


example1 = "6\n0 0 R 3\n2 0 D 6\n2 -4 D 4\n2 -5 L 2\n1 4 U 5\n 0 -5 U 3"
#출력 0 0
example2 = "3\n0 0 R 7\n4 0 U 6\n4 5 D 7"
#출력 -1

list1 = example2.split("\n")
list2 = []
list_xy = []
for element in list1:
    if len(element)==1:
        continue
    else:
        temp = element.split()
        list2.append(temp)
        list_xy.append(list(map(int,temp[:2])))

now_x=int(list2[0][0])
now_y=int(list2[0][0])
flag = {x+1 : True for x in range(len(list_xy))}
flag[1] = False
print(list2)
print(BFS(list2,list_xy,now_x,now_y,list2[0][2],list2[0][3],flag))
