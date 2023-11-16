from collections import deque

def solution(skill, skill_trees):
    answer = 0

    while skill_trees:
        skill2 = deque([x for x in skill])
        temp = deque(skill_trees.pop())
        flag = True

        while temp:
            now = temp.popleft()

            if now in skill2:
                check = skill2.popleft()

                if check != now:
                    flag = False
                    break

                else:
                    continue

        if flag:
            answer += 1

    return answer