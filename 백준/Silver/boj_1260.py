from collections import deque
N, M, V = map(int, input().split())
m_dict = {}

for i in range(N):
    m_dict[i+1] = set()

for i in range(M):
    v1, v2 = map(int, input().split())
    m_dict[v1].add(v2)
    m_dict[v2].add(v1)

dfs_visited = set()
dfs_result = []

def dfs(v):
    dfs_visited.add(v)
    dfs_result.append(v)

    for next_v in sorted(m_dict[v]):
        if next_v not in dfs_visited:
            dfs(next_v)

dfs(V)
print(" ".join(map(str, dfs_result)))

bfs_visited = set()
bfs_result = []

def bfs(start):
    queue = deque([start])
    bfs_visited.add(start)

    while queue:
        v = queue.popleft()
        bfs_result.append(v)

        for next_v in sorted(m_dict[v]):
            if next_v not in bfs_visited:
                bfs_visited.add(next_v)
                queue.append(next_v)

bfs(V)
print(" ".join(map(str, bfs_result)))