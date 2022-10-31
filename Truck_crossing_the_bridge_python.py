from collections import deque

def solution(bridge_length, weight, truck_weights):
    truck = deque(truck_weights)
    time = 1
    bridge_weight = 0
    dict = {}

    while True:
        time += 1
        if truck:
            if bridge_weight + truck[0] <= weight:
                temp = truck.popleft()
                dict[time] = [temp,0]
                bridge_weight += temp

        keys = list(dict.keys())
        for i in keys:
            dict[i][1] += 1
            if dict[i][1] == bridge_length:
                bridge_weight -= dict.pop(i)[0]

        if bridge_weight == 0 and not truck:
            break

    return time