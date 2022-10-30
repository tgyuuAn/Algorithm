import matplotlib.pyplot as plt
import math

length = int(input("n 값을 입력하세요 :"))
degrees = [(4/(math.pi*i)) if i%2==1 else 0 for i in range(1,length+1)]
plt.scatter(range(1,length+1), degrees)
plt.xlabel("bn if,k =1")
plt.ylabel("f(x)")
plt.ylim(0,1.5)
plt.show()