from collections import deque

n = int(input())
grid = []

for _ in range(n):
    row = list(map(int, input().split()))
    grid.append(row)

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 아기상어 시작 위치 찾기
for i in range(n):
    for j in range(n):
        if grid[i][j] == 9:
            x, y = i, j
            grid[i][j] = 0  # 상어 위치 초기화
            break

size = 2
eat = 0
time = 0

def bfs(sx, sy, size):
    visited = [[-1]*n for _ in range(n)]
    q = deque()
    q.append((sx, sy))
    visited[sx][sy] = 0
    fishes = []

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1:
                if grid[nx][ny] <= size:  # 지나갈 수 있는 조건
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))

                    if 0 < grid[nx][ny] < size:  # 먹을 수 있는 물고기면
                        fishes.append((visited[nx][ny], nx, ny))

    # 거리, 위, 왼 순으로 정렬
    fishes.sort()
    return fishes[0] if fishes else None

while True:
    result = bfs(x, y, size)

    if result is None:
        break  # 더 이상 먹을 수 있는 물고기가 없음

    dist, nx, ny = result
    time += dist
    x, y = nx, ny
    grid[x][y] = 0
    eat += 1

    if eat == size:
        size += 1
        eat = 0

print(time)
