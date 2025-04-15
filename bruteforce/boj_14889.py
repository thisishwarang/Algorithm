from itertools import combinations
N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
player = list(range(1, N+1))

def calc_S(member):
    score = 0
    for a, b in combinations(member, 2):
        score += (S[a-1][b-1] + S[b-1][a-1])
    return score

team = list(combinations(player, N//2))

min_diff = float('inf')

for i in range(len(team)//2):
    team1 = team[i]
    team2 = team[-(i+1)]
    diff = abs(calc_S(team1) - calc_S(team2))
    min_diff = min(diff, min_diff)

print(min_diff)