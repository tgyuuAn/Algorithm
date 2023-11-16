def solution(n, control):
    for key in list(control):
        if key == "w":
            n+=1
        elif key =="s":
            n-=1
        elif key =="a":
            n-=10
        else:
            n+=10
    return n