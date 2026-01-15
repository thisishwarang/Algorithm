# import sys
# N, M = map(int, sys.stdin.readline().split())

# nums = [n for n in range(1, N + 1)]
# visited = [False] * N
# results = []

# def dfs(path):
#     if len(path) == M:
#         results.append(path[:])
#         return
    
#     for i in range(N):
#             if len(path) == 0:
#                 if not visited[i]:
#                     visited[i] = True
#                     path.append(nums[i])
#                     dfs(path)
#                     path.pop()
#                     visited[i] = False
#             else :
#                  if not visited[i] and i + 1 > path[-1]:
#                     visited[i] = True
#                     path.append(nums[i])
#                     dfs(path)
#                     path.pop()
#                     visited[i] = False      
            
# dfs([])

# for result in results:
#     print(" ".join(map(str, result)))

import sys
N, M = map(int, sys.stdin.readline().split())

path = []

def dfs(start):
    if len(path) == M:
        print(" ".join(map(str, path)))
        return
    
    for i in range(start, N + 1):
        path.append(i)
        dfs(i + 1)
        path.pop()

dfs(1)
