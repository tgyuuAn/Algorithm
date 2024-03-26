import sys
from collections import defaultdict, deque

MOD = 1_000_000_007
pow_cache = defaultdict(int)

def input(): return sys.stdin.readline().rstrip()

def rabin_karp(text, previous_char = None, previous_hash = None):
    # 만약 처음 해쉬 값을 구하는 텍스트일 경우
    if previous_char is None or previous_hash is None:
        hash = 0
        for idx, char in enumerate(text):
            if (len(text)-1-idx) in pow_cache:
                hash += ord(char) * pow_cache[(len(text)-1-idx)]
            else:
                hash += ord(char) * pow(2, len(text)-1-idx, MOD)
            hash %= MOD

        return hash

    if (len(text)-1) in pow_cache:
        previous_hash -= (ord(previous_char) * pow_cache[len(text)-1]) % MOD
    else:
        previous_hash -= (ord(previous_char) * pow(2, len(text)-1, MOD)) % MOD
        
    # 그리고 모든 해쉬를 *2해서 한 칸씩 밀어줌
    previous_hash *= 2
    previous_hash %= MOD
    previous_hash += ord(text[-1])
    previous_hash %= MOD

    return previous_hash

def check(text, mid):
    dic = defaultdict(int)
    hash = 0
    previous_hash = None
    previous_text = None
    for start_idx in range(len(text)-mid+1):
        if start_idx == 0:
            hash = rabin_karp(text[start_idx:start_idx+mid])
            dic[hash] = start_idx

            previous_text = deque(text[start_idx:start_idx+mid])
            previous_hash = hash
            continue

        # 앞 문자 떼고 뒷 문자를 붙여서 새로운 텍스트로 갱신
        previous_text.popleft()
        previous_text.append(text[start_idx+mid-1])

        hash = rabin_karp(previous_text, text[start_idx-1], previous_hash)
        previous_hash = hash
        if hash in dic:
            origin_text = text[dic[hash]:dic[hash]+mid]
            now_text = text[start_idx:start_idx+mid]
            for origin_char, now_char in zip(origin_text, now_text):
                if origin_char != now_char: break
            else: return True

        else: dic[hash] = start_idx
    return False

L = int(input())
text = input()
left = 0
right = L+1
while left+1 < right:
    mid = (left+right)//2
    # 만약 mid 길이만큼 중복되는 부분 문자열이 존재할 경우,
    if check(text, mid): left = mid
    else: right = mid

print(left)