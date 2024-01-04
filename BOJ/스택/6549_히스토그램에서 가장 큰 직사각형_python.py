from collections import deque

while True:
    _input = input()

    if _input == "0":
        break
    
    _input_list = list(map(int,_input.split()))
    heights = [0]
    heights.extend(_input_list[1:])
    heights.append(0)


    max_width = -1
    stack = deque([0])
    for idx, height in enumerate(heights):
        if idx == 0:
            continue
        print(stack, idx, max_width)

        if height >= heights[stack[-1]]:
            stack.append(idx)

        else:
            while True:
                top = heights[stack[-1]]
                
                if top <= height:
                    break
                
                top_idx = stack.pop()
                top = heights[top_idx]
                max_width = max(max_width, top*(idx-stack[-1]-1))

            stack.append(idx)
    print(stack, idx, max_width)
    
    while True:
         top = heights[stack[-1]]
         
         if top <= height:
             break
         
         top_idx = stack.pop()
         top = heights[top_idx]
         max_width = max(max_width, top*(idx-stack[-1]-1))
    
    if max_width > -1: print(max_width)
    else: print(0)