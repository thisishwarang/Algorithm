# T = int(input())
# nums = []

# nums_count = 0

# for _ in range(T):
#     n = int(input())
#     nums.append(n)

# def dfs(n, path):
#     global nums_count
#     if sum(path) > n:
#         return
#     if sum(path) == n:
#         nums_count += 1
#         return
#     for i in range(1, 4):
#         path.append(i)
#         dfs(n, path)
#         path.pop()

# for n in nums:
#     dfs(n, [])
#     print(nums_count)
#     nums_count = 0


T = int(input())

dp = [0] * 11

dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, 11):
    dp[i] = dp[i-3] + dp[i-2] + dp[i-1]

for _ in range(T):
    n = int(input())
    print(dp[n])