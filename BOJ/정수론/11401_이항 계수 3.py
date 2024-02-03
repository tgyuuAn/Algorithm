N, K = map(int,input().split())
    
p = 1_000_000_007
factorial = [1 for _ in range(N+1)]

temp = 1
for i in range(1,N+1):
    temp = (temp*i)%p
    factorial[i] = temp

def pow(bottom,top):
    if top == 0: return 1
    elif top == 1: return bottom
    else:
        temp = pow(bottom,top//2) % p

        if top%2==0: return (temp * temp) % p # 짝
        else: return ((bottom % p) * temp * temp % p) # 홀

A = factorial[N]
B = pow((factorial[N-K] * factorial[K]),p-2)
answer = (A % p) * (B % p) %p
print(answer)