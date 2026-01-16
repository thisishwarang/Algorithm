N, M = map(int, input().split())

path = []

def dfs():
    if len(path) == M:
        print(" ".join(map(str, path)))
        return

    for i in range(1, N + 1):
        path.append(i)
        dfs()
        path.pop()

dfs()