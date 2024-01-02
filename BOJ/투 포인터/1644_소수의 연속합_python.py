def generatePrime(maximum):
    if maximum <= 1:
        return None

    prime_numbers = []
    
    for number in range(2,maximum+1):
        for i in range(2,int(number**0.5)+1):
            if number%i ==0:
                break
        
        else:
            prime_numbers.append(number)

    return prime_numbers

target = int(input())

if target <= 1:
    print("0")

else:
    primeNumbers = generatePrime(target)

    #print(primeNumbers)

    left, right = 0,0
    temp = 2
    count = 0

    while left<=right:
        if temp < target:
            right += 1
            if right >= len(primeNumbers): break
            temp += primeNumbers[right]

        elif temp > target:
            temp -= primeNumbers[left]
            left += 1

        else:
            right += 1
            count += 1
            if right >= len(primeNumbers): break
            temp += primeNumbers[right]

    print(count)