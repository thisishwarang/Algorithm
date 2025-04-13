N = int(input())
numbers = list(map(int, input().split()))
operators = list(map(int, input().split()))  # +, -, *, //

mx = -int(1e9)
mn = int(1e9)

def dfs(n, temp):
    global mx, mn
    if n == N - 1:
        mx = max(mx, temp)
        mn = min(mn, temp)
        return

    if operators[0]:
        operators[0] -= 1
        dfs(n + 1, temp + numbers[n + 1])
        operators[0] += 1
    if operators[1]:
        operators[1] -= 1
        dfs(n + 1, temp - numbers[n + 1])
        operators[1] += 1
    if operators[2]:
        operators[2] -= 1
        dfs(n + 1, temp * numbers[n + 1])
        operators[2] += 1
    if operators[3]:
        operators[3] -= 1
        if temp < 0:
            dfs(n + 1, -(-temp // numbers[n + 1]))
        else:
            dfs(n + 1, temp // numbers[n + 1])
        operators[3] += 1

dfs(0, numbers[0])
print(mx)
print(mn)
