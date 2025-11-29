import sys
N, M = map(int, sys.stdin.readline().split())

heard = set()
for _ in range(N):
    heard.add(sys.stdin.readline().strip())

result = []

for _ in range(M):
    name = sys.stdin.readline().strip()
    if name in heard:
        result.append(name)
result.sort()

print(len(result))
if result:
    print("\n".join(result))

