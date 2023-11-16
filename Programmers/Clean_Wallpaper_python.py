def solution(wallpaper):
    answer = []
    minX,minY,maxX,maxY = int(1e9),int(1e9),-1,-1
    for index, x in enumerate(wallpaper):
        if "#" in x:
            index2 = len(x)
            minX = min(minX,x.index("#"))
            
            x = list(x)
            while x:
                index2 -= 1
                now = x.pop()
                if now == "#":
                    break
                
            maxX = max(maxX,index2+1)
            minY = min(minY,index)
            maxY = max(maxY,index+1)

    return [minY,minX,maxY,maxX]