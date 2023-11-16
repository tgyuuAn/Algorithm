from collections import defaultdict, deque

def solution(k, room_number):
    rooms = defaultdict(int)
    answer = []
    
    for number in room_number:
        if rooms[number] == 0:
            rooms[number] = number+1
            answer.append(number)
            
        else:
            temp_list = [number]
            temp_maxi = rooms[number]
            while rooms[temp_maxi] != 0:
                temp_list.append(temp_maxi)
                temp_maxi = rooms[temp_maxi]
            
            rooms[temp_maxi] = temp_maxi+1
            answer.append(temp_maxi)
        
            for temp_number in temp_list:
                rooms[temp_number] = temp_maxi   

    return answer