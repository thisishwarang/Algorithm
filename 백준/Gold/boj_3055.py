from collections import deque
R, C = map(int, input().split())

grid = [list(map(str, input())) for _ in range(R)]

s_queue = deque()
w_queue = deque()

s_visited = [[False] * C for _ in range(R)]
w_visited = [[False] * C for _ in range(R)]

for i in range(R):
    for j in range(C):
        if grid[i][j] == 'S':
            s_queue.append((i, j, 0))
            s_visited[i][j] = True
        elif grid[i][j] == '*':
            w_queue.append((i, j))
            w_visited[i][j] = True

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while s_queue:
    # 1. 물 부터 이동
    for _ in range(len(w_queue)):
        x, y = w_queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < R and 0 <= ny < C and grid[nx][ny] == '.' and not w_visited[nx][ny]:
                w_visited[nx][ny] = True
                grid[nx][ny] = '*'
                w_queue.append((nx, ny))
    # 2. 고슴도치 이동
    for _ in range(len(s_queue)):
        x, y, time = s_queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < R and 0 <= ny < C:
                if grid[nx][ny] == 'D':
                    print(time + 1)
                    exit()
                if grid[nx][ny] == '.' and not s_visited[nx][ny]:
                    s_visited[nx][ny] = True
                    s_queue.append((nx, ny, time + 1))
            
print('KAKTUS')
