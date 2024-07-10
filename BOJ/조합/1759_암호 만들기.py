import sys
from itertools import combinations

def input(): return sys.stdin.readline().rstrip()

L, C = map(int, input().split())
word = list(input().split())
consonants = []
vowels = []

for char in sorted(word):
    if char in ("a", "e", "i", "o", "u"):
        consonants.append(char)
    else: vowels.append(char)

visited = set()

for vowels_count in range(2,min(L,len(vowels)+1)):
    consonants_count = L - vowels_count
    
    for temp_vowel in combinations(vowels, vowels_count):
        for temp_consonant in combinations(consonants, consonants_count):
            
            answer = []
            answer.extend(temp_vowel)
            answer.extend(temp_consonant)
            answer.sort()
            visited.add("".join(answer))
            
for ans in sorted(list(visited)):
    print(ans)