from collections import defaultdict

def solution(N, number):
    dic = defaultdict(set)

    for count in range(1,9):

        dic[count].add(int(str(N)*count))
        
        for x in range(1,count):
            y = count -x
            
            for temX in dic[x]:
                for temY in dic[y]:
                    dic[count].update([temX+temY,temX-temY,temX*temY])
                    
                    if temY != 0 :
                        dic[count].add(temX//temY)

        if number in dic[count]:
            return count

    return -1