def solution(numbers):
    answer = []

    for number in numbers:
        nowBin = bin(number)[2:]

        while len(nowBin)<=50:
            nowBin = "0" + nowBin
        
        nowBin = list(nowBin)
        
        mock = nowBin.copy()
        count = len(mock)

        while mock:
            count -= 1
            temp = mock.pop()
            if temp == "0":
                break

        nowBin[count] = "1"

        if count != len(nowBin)-1:
            nowBin[count+1] = "0"

        nowBin = "".join(nowBin)
        answer.append(int(nowBin,2))

    return answer

numbers = [2,7]
solution(numbers)