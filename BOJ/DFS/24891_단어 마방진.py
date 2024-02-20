import sys

word_length, word_count = map(int,sys.stdin.readline().split())

word_list = []
for _ in range(word_count):
    word_list.append(sys.stdin.readline().split())

def is_magic_square(idx_bundle):
    for col in range(idx_bundle):
        for row in range(idx_bundle):
            print(col, row)
            print(row, col)
            if word_list[col][row] != word_list[row][col]: return False
    return True

def dfs(idx_bundle, visited, last_idx, word_count, word_length):
    if len(idx_bundle) == word_length:
        print(idx_bundle)
        is_magic_square(idx_bundle)
        return

    for idx in range(last_idx,word_count):
        if idx in visited: continue

        visited.add(idx)
        idx_bundle.append(idx)
        dfs(idx_bundle, visited, idx+1, word_count, word_length)
        visited.discard(idx)
        idx_bundle.pop()

    return

dfs(list(),set(), 0, word_count, word_length)