answer = []

def check(query, word):
    diff = 0
    for i in range(len(query)):
        if query[i] != word[i]:
            diff +=1
    return diff==1

def solution(begin, target, words):
    global answer
    dfs(begin,target,words, 0)
    return 0 if target not in words else min(answer)

def dfs(begin,target,words,depth):
    global answer

    for idx, word in enumerate(words):
        if check(begin, word):
            
            if word==target:
                answer.append(depth+1)
                return
            
            words_2 = words.copy()
            words_2.remove(word)
            dfs(word,target,words_2,depth+1)