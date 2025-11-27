from collections import deque
N, K = map(int, input().split())

q = deque()
result = []
cnt = 1

for i in range(N):
    q.append(i+1)

while len(q) != 0 :
    if cnt % K != 0:
        front = q.popleft()
        q.append(front)
    else :
        front = q.popleft()
        result.append(front)
    cnt += 1
print("<" + ", ".join(map(str, result)) + ">")