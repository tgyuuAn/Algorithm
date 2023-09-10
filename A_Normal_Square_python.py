def gcd(num1,num2):
    num1, num2 = max(num1,num2), min(num1,num2)
    while num2!=0:
        mod = num1%num2
        num1, num2 = num2, mod
    return num1

def solution(w,h):
    if w==h:
        return w*w-w
    
    else:
        
        gcd_wh = gcd(w,h)
        w_rate, h_rate = w/gcd_wh, h/gcd_wh
        tot_block_count = h/h_rate
        trash = (w_rate+h_rate-1) * tot_block_count
        
        return w*h-trash