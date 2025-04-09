## combinations를 활용한 풀이법

# from itertools import combinations
# N, M = map(int, input().split())

# city = []
# for i in range(N):
#     city.append(list(map(int, input().split())))

# chicken = []
# house = []

# for i in range(N):
#     for j in range(N):
#         if city[i][j] == 1:
#             house.append((i, j))
#         if city[i][j] == 2:
#             chicken.append((i, j))

# combs = list(combinations(chicken, M))
# print(combs)

# answer = int(1e9)

# for comb in combs:
#     city_dist = 0
#     for x, y in house:
#         min_dist = int(1e9)
#         for i, j in comb:
#             dist = abs(i - x) + abs(j - y)
#             min_dist = min(min_dist, dist)
#         city_dist += min_dist
#     answer = min(answer, city_dist)

# print(answer)


## 백트래킹을 활용한 풀이법
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

city = []

for _ in range(N):
    city.append(list(map(int, input().split())))

house = []
chicken = []

for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            house.append((i, j))
        elif city[i][j] == 2:
            chicken.append((i, j))

min_result = int(1e9)
selected = []

def calc_dist():
    total = 0
    for x, y in house:
        dist = int(1e9)
        for cx, cy in selected:
            dist = min(dist, abs(cx-x) + abs(cy-y))
        total += dist
    return total

def dfs(idx, selected_chicken):
    global min_result
    if selected_chicken == M:
        min_result = min(min_result, calc_dist())
        return
    for i in range(idx, len(chicken)):
        selected.append(chicken[i])
        dfs(idx + 1, selected_chicken + 1)
        selected.pop()

dfs(0, 0)
print(min_result)