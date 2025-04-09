from collections import deque
M, N = map(int, input().split())

box = []

for i in range(N):
    box.append(list(map(int, input().split())))

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque()

zero_count = 0
for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            queue.append((i, j))
        elif box[i][j] == 0:
            zero_count += 1
if zero_count == 0:
    print(0)
    exit()


while queue:
    n, m = queue.popleft()
    
    for i in range(4):
        nn = n + dx[i]
        mm = m + dy[i]    
        if 0 <= nn < N and 0 <= mm < M and box[nn][mm] == 0:
            box[nn][mm] = box[n][m] + 1
            queue.append((nn, mm))

result = 0
for i in range(N):
    for j in range(M):
        if box[i][j] == 0:
            print(-1)
            exit()
        result = max(result, box[i][j])

print(result-1)