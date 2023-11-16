def solution(players, callings):
    player_player = dict()
    rank_player = dict()

    for rank, player in enumerate(players):
        player_player[player] = rank
        rank_player[rank] = player

    for calling in callings:
        temp_rank = player_player[calling]
        player_player[calling] -= 1
        temp_player = rank_player[temp_rank-1]
        player_player[temp_player] += 1
        
        rank_player[temp_rank] = temp_player
        rank_player[temp_rank-1] = calling
    
    return list(rank_player.values())