def solution(numbers, hand):
    keypad = [["1","4","7","*"],
               ["2","5","8","0"],
               ["3","6","9","#"]]
    ans = ""
    l_last = [3,0]
    r_last = [3,2]
    l_len = 0
    r_len = 0

    for i in numbers:
        i=str(i)
        if i in ["1","4","7","*"]:
            ans+="L"
            l_last = [keypad[0].index(i),0]

        elif i in ["3","6","9","*"]:
            ans+="R"
            r_last = [keypad[2].index(i),2]

        elif i in ["2","5","8","0"]:
            idx = [keypad[1].index(i),1]
            l_len = abs((l_last[0]-idx[0]))+abs((l_last[1]-idx[1]))
            r_len = abs((r_last[0]-idx[0]))+abs((r_last[1]-idx[1]))

            if l_len<r_len:
                ans+="L"
                l_last = idx

            elif l_len>r_len:
                ans+="R"
                r_last = idx

            else:
                if hand == "right":
                    ans+="R"
                    r_last = idx

                else :
                    ans+="L"
                    l_last = idx
    return ans