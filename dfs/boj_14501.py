N = int(input())
list = []
for _ in range(N):
    T, P = map(int, input().split())
    list.append((T, P))

max_profit = 0

def dfs(day, total_profit):
    global max_profit
    if day > N:
        return
    if day == N:
        max_profit = max(max_profit, total_profit)
        return
    if day + list[day][0] <= N:
        dfs(day + list[day][0], total_profit + list[day][1])
    dfs(day+1, total_profit)

dfs(0, 0)
print(max_profit)