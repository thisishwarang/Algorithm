import sys
N, M = map(int, sys.stdin.readline().split())

nums = [n for n in range(1, N+1)]
visited = [False] * N
results = []

def dfs(path):
    if len(path) == M:
        results.append(path[:])
        return
    
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            path.append(nums[i])
            dfs(path)
            path.pop()
            visited[i] = False
dfs([])

for result in results:
    print(" ".join(map(str, result)))