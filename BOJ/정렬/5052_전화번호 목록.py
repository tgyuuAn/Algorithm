import sys

def input(): return sys.stdin.readline().rstrip()

T = int(sys.stdin.readline())


for _ in range(T):
    N = int(input())
    
    phone_book = sorted([input() for _ in range(N)])
    is_consistency = True
    
    prev = phone_book[0]
    for number in phone_book[1:]:
        if number[:len(prev)] == prev:
            is_consistency = False
            break
        
        prev = number

    print("YES" if is_consistency else "NO")