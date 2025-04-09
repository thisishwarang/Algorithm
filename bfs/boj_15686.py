from itertools import combinations
N, M = map(int, input().split())

city = []
for i in range(N):
    city.append(list(map(int, input().split())))

chicken = []
house = []

for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            house.append((i, j))
        if city[i][j] == 2:
            chicken.append((i, j))

combs = list(combinations(chicken, M))
print(combs)

answer = int(1e9)

for comb in combs:
    city_dist = 0
    for x, y in house:
        min_dist = int(1e9)
        for i, j in comb:
            dist = abs(i - x) + abs(j - y)
            min_dist = min(min_dist, dist)
        city_dist += min_dist
    answer = min(answer, city_dist)

print(answer)