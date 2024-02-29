import sys

def input(): return sys.stdin.readline()

while True:
    N = input()
    if N == "": break
    N = int(N)
    
    share_price = list(map(int,input().split()))
    new_share_price = [share_price[0]]

    def check(element, number):
        if element <= number: return True
        else: return False

    def add_share_price(element, new_share_price):
        if element > new_share_price[-1]:
            new_share_price.append(element)

        else:
            left = -1
            right = len(new_share_price)
            answer = right-1

            while left+1<right:
                mid = (left+right)//2

                if check(element, new_share_price[mid]):
                    right = mid
                    answer = mid

                else: left = mid

            new_share_price[answer] = element

    for i in share_price[1:]:
        add_share_price(i, new_share_price)

    print(len(new_share_price))