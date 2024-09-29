def solution(alp, cop, problems):
    max_alp = max(problem[0] for problem in problems)
    max_cop = max(problem[1] for problem in problems)

    alp = min(alp, max_alp)
    cop = min(cop, max_cop)

    DP = [[float('inf')] * (max_cop + 1) for _ in range(max_alp + 1)]
    DP[alp][cop] = 0

    for i in range(alp, max_alp + 1):
        for j in range(cop, max_cop + 1):
            if i + 1 <= max_alp:
                DP[i + 1][j] = min(DP[i + 1][j], DP[i][j] + 1)
                
            if j + 1 <= max_cop:
                DP[i][j + 1] = min(DP[i][j + 1], DP[i][j] + 1)

            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if i >= alp_req and j >= cop_req:
                    new_alp = min(max_alp, i + alp_rwd)
                    new_cop = min(max_cop, j + cop_rwd)
                    DP[new_alp][new_cop] = min(DP[new_alp][new_cop], DP[i][j] + cost)

    return DP[max_alp][max_cop]