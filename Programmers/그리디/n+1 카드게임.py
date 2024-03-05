def solution(coin, cards):
    n = len(cards)
    now = set(cards[:n//3])
    now_can_make = set()
    keep = set()

    for element in now:
        if (n-element+1) in now and (n-element+1,element) not in now_can_make:
            now_can_make.add((element,n-element+1))

    for idx, start_idx in enumerate(range(n//3,n,2)):
        first = cards[start_idx]
        second = cards[start_idx+1]

        # 먼저 두 카드에 대한 구매 여부 결정
        if ((n-first+1) in now) and ((n-first+1, first) not in now_can_make) and (coin > 0):
            now_can_make.add((first,n-first+1))
            now.add(first)
            coin -= 1

        else: keep.add(first)

        if ((n-second+1) in now) and ((n-second+1, second) not in now_can_make) and (coin > 0):
            now_can_make.add((second,n-second+1))
            now.add(second)
            coin -= 1

        else: keep.add(second)


        # 다음 라운드 수명 연장을 위해서 카드 제출
        if now_can_make:
            for pair_1, pair_2 in now_can_make:
                now.discard(pair_1)
                now.discard(pair_2)
                
                now_can_make.discard((pair_1, pair_2))
                break

        # 제출할 카드가 없을 경우 keep 목록에서 탐색
        elif coin >= 2:
            for element in keep:
                if n-element+1 in keep:
                    keep.discard(element)
                    keep.discard(n-element+1)
                    coin -= 2
                    break
                    
            else: return idx+1

        # 만약 제출할 게 없으면 게임 종료
        else: return idx+1

    else: return idx+2